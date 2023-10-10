import math
import pygame

# Calculate the x and y coordinates of a point on a circle given an angle in degrees
def calculate_point_on_circle(radius, angle_degrees, center):
    # Calculate the x and y coordinates of a point on a circle given an angle in degrees
    x = radius * math.cos(math.radians(angle_degrees)) + center[0]
    y = radius * math.sin(math.radians(angle_degrees)) + center[1]
    return x, y

def rotate_point(x, y, angle, origin):
    radians = angle * (math.pi / 180.0)
    x_rotated = origin[0] + (x - origin[0]) * math.cos(radians) - (y - origin[1]) * math.sin(radians)
    y_rotated = origin[1] + (x - origin[0]) * math.sin(radians) + (y - origin[1]) * math.cos(radians)
    return x_rotated, y_rotated

# Function to check if a point is inside a triangle
def is_point_inside_triangle(x, y, triangle_sensor, eps=0.1):
    # Extract the coordinates of the triangle's vertices
    x1, y1 = triangle_sensor[0]
    x2, y2 = triangle_sensor[1]
    x3, y3 = triangle_sensor[2]

    # Calculate the area of the triangle
    area_triangle = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1-y2)) / 2.0)

    # Calculate the areas of three triangles made between the point and the vertices of the triangle
    area1 = abs((x1 * (y2 - y) + x2 * (y - y1) + x * (y1-y2)) / 2.0)
    area2 = abs((x1 * (y - y3) + x * (y3 - y1) + x3 * (y1-y)) / 2.0)
    area3 = abs((x * (y2 - y3) + x2 * (y3 - y) + x3 * (y-y2)) / 2.0)

    # Check if the sum of the three areas is equal to the area of the triangle
    if area1 + area2 + area3 - eps <= area_triangle <= area1 + area2 + area3 + eps:
        return True
    else:
        return False

def draw_triangle_robot(screen, x, y, rotation, ROBOT_SIZE, ROBOT_COLOR):
    # Calculate the height of the equilateral triangle based on its side length (ROBOT_SIZE)
    triangle_height = int((3 ** 0.5 / 2) * ROBOT_SIZE)

    # Define the vertices of the equilateral triangle relative to its center
    vertices = [
        (-ROBOT_SIZE / 2, triangle_height / 2),
        (0, -triangle_height),
        (ROBOT_SIZE / 2, triangle_height / 2)
    ]

    # Rotate the triangle by 'rotation' degrees
    radians = math.radians(rotation + 90)
    rotated_vertices = [(x + vertex[0] * math.cos(radians) - vertex[1] * math.sin(radians),
                         y + vertex[0] * math.sin(radians) + vertex[1] * math.cos(radians))
                        for vertex in vertices]

    # Draw the rotated triangle on the screen
    pygame.draw.polygon(screen, ROBOT_COLOR, rotated_vertices)