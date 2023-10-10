# Pygame Field of View (FOV) Obstacle Detection

This Python project uses the Pygame library to simulate a robot equipped with sensors for detecting obstacles within its field of view (FOV). The robot's FOV is represented as a triangle, and it can detect obstacles within this triangular area.

## Project Structure

The project consists of the following files:

1. `utils.py`: Contains utility functions used for geometry calculations and drawing.
2. `robot-360-detection.py`: Implements a robot with sensors for 360-degree FOV detection.
3. `robot-one-sensor.py`: Implements a robot with a single sensor for FOV detection.

## Getting Started

### Prerequisites

Before running the project, make sure you have Python and Pygame installed on your system.

You can install Pygame using pip:

```
pip install pygame
```

### Running the Simulation

To run the simulation, execute one of the following Python files:

1. For the 360-degree FOV detection robot:

```bash
python robot-360-detection.py
```

2. For the robot with a single sensor:

```bash
python robot-one-sensor.py
```

### Controls

- Use the arrow keys to control the robot's movement (left, right, up, down).
- Press the `SPACE` key to rotate the robot.

## Usage

The robot's FOV is visualized on the screen as a colored triangle. Obstacles within the FOV are detected and displayed in real-time. The detected obstacles' positions are shown on the screen, along with their coordinates.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```