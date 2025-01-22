# PENCIL SKETCH SIMULATOR

A Python project that simulates the process of drawing a pencil sketch from an input image. The program uses OpenCV to convert an image into a realistic pencil sketch and visually recreates the drawing process, mimicking human-like pencil strokes.

**FEATURES**

- Converts any image into a realistic pencil sketch.
- Displays a step-by-step drawing simulation of the pencil sketch creation.
- Adjustable pencil speed for fine-tuned performance.
- Supports grayscale and edge-based sketching.

**REQUIREMENTS**

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

$How$ $to$ $Run$

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pencil-sketch-simulator.git
   cd pencil-sketch-simulator
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python pencil_sketch_simulator.py
   ```

4. Enter the path to the image file when prompted.


Adjusting Simulation Speed

Modify the `time.sleep()` value in the script to control the speed of the drawing simulation. Lower values increase the speed, while higher values slow it down.
