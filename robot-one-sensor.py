import pygame
import sys
import random

from utils import calculate_point_on_circle, is_point_inside_triangle, draw_triangle_robot

def main():
    
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 600
    BACKGROUND_COLOR = (255, 255, 255)
    ROBOT_COLOR = (0, 0, 0)
    OBSTACLE_COLOR = (255, 0, 0)
    ROBOT_SIZE = 15
    TEXT_X, TEXT_Y = WIDTH // 20, HEIGHT // 20
    TEXT_COLOR = (0, 255, 0)
    font = pygame.font.SysFont("Arial", 20)

    eps_far = 100   # Distance of detection
    eps_rot = 15    # FOV divide by 2: eps_rot=15 <=> FOV = 30 degrees

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("FOV Detection")

    # Initial robot position and rotation
    x, y = WIDTH // 2, HEIGHT // 2
    rotation = 0

    # Generate random obstacles
    num_obstacles = 10
    obstacles = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(num_obstacles)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        triangle_sensor = [(x, y),
                           calculate_point_on_circle(eps_far, -eps_rot + rotation, (x, y)),
                           calculate_point_on_circle(eps_far, eps_rot + rotation, (x, y))]

        # Draw a transparent sector to visualize the sensor's field of view
        pygame.draw.polygon(screen, (0, 0, 255, 100), triangle_sensor, 0)

        # Draw obstacles
        for obstacle_x, obstacle_y in obstacles:
            pygame.draw.circle(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_y), 5)

        # Draw the robot
        draw_triangle_robot(screen, x, y, rotation, ROBOT_SIZE, ROBOT_COLOR)

        # Check for obstacles within the sensor's FOV
        obstacles_detected = [
            (obstacle_x, obstacle_y)
            for obstacle_x, obstacle_y in obstacles
            if is_point_inside_triangle(obstacle_x, obstacle_y, triangle_sensor)
        ]

        # Print obstacles detected in the sensor's FOV
        if obstacles_detected:
            text = f"Obstacles detected at: {obstacles_detected}"
            text_surface = font.render(text, True, TEXT_COLOR)
            screen.blit(text_surface, (TEXT_X, TEXT_Y))

        # Update the display
        pygame.display.flip()

        # Control the robot's movement and rotation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 1
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_UP]:
            y -= 1
        if keys[pygame.K_DOWN]:
            y += 1
        if keys[pygame.K_SPACE]:
            rotation = (rotation + 1) % 360

        pygame.time.delay(10)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
