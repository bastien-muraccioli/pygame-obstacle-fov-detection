import pygame
import sys
import random

from utils import calculate_point_on_circle, is_point_inside_triangle, draw_triangle_robot

# Function to create the sensors
def create_turn_arround_sensor(screen, x, y, eps_far, eps_rot, rotation):
    sensor = {"front":          [(x, y),
                                  calculate_point_on_circle(eps_far, -eps_rot + rotation, (x, y)),
                                  calculate_point_on_circle(eps_far, eps_rot + rotation, (x, y))],
              "behind":         [(x, y),
                                  calculate_point_on_circle(eps_far, rotation + 180 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation + 180 - eps_rot, (x, y))],
              "right":          [(x, y),
                                  calculate_point_on_circle(eps_far, rotation + 90 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation + 90 - eps_rot, (x, y))],
              "left":           [(x, y),
                                  calculate_point_on_circle(eps_far, rotation - 90 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation - 90 - eps_rot, (x, y))],
              "front right":    [(x, y),
                                  calculate_point_on_circle(eps_far, rotation + 45 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation + 45 - eps_rot, (x, y))],
              "front left":     [(x, y),
                                  calculate_point_on_circle(eps_far, rotation - 45 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation - 45 - eps_rot, (x, y))],
              "behind left":    [(x, y),
                                  calculate_point_on_circle(eps_far, rotation + 225 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation + 225 - eps_rot, (x, y))],
              "behind right":   [(x, y),
                                  calculate_point_on_circle(eps_far, rotation + 135 + eps_rot, (x, y)),
                                  calculate_point_on_circle(eps_far, rotation + 135 - eps_rot, (x, y))]}
    i = 0
    # Draw all sensors
    for key in sensor:
        i += 10
        pygame.draw.polygon(screen, (0, 255-i, 255, 50), sensor[key], 0)

    return sensor

# Function to check if a point is inside a sensor
def turn_arround_detection(obstacles, sensor):
    text = []
    for key in sensor:
        for obstacle_x, obstacle_y in obstacles:
            if is_point_inside_triangle(obstacle_x, obstacle_y, sensor[key]):
                text.append(f"Obstacle detected at {key}: {obstacle_x}, {obstacle_y}")
    return text


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
    FONT_SIZE = 20
    font = pygame.font.SysFont("Arial", FONT_SIZE)

    eps_far = 100   # Distance of detection
    eps_rot = 22.5  # FOV divide by 2: eps_rot=22.5 <=> FOV = 45 degrees Use for 360 degrees detection

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("360 Detection")

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

        # Create and draw the sensors
        sensor = create_turn_arround_sensor(screen, x, y, eps_far, eps_rot, rotation)

        # Draw obstacles
        for obstacle_x, obstacle_y in obstacles:
            pygame.draw.circle(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_y), 5)

        # Draw the robot
        draw_triangle_robot(screen, x, y, rotation, ROBOT_SIZE, ROBOT_COLOR)

        # Print obstacles detected in the sensor's FOV
        obstacle_detected = turn_arround_detection(obstacles, sensor)
        if obstacle_detected:
            for index, text in enumerate(obstacle_detected):
                text_surface = font.render(text, True, TEXT_COLOR)
                screen.blit(text_surface, (TEXT_X, TEXT_Y + index * FONT_SIZE))

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
            # print(f"rotation: {rotation}")

        pygame.time.delay(10)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
