import cv2
import numpy as np
import time

def sketch(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image file. Please check the file path.")
        return
    image = cv2.resize(image, (600, 400))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blurred = 255 - blurred
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    canvas = np.ones_like(pencil_sketch_image) * 255
    cv2.namedWindow("Pencil Sketch with Simulated Pencil", cv2.WINDOW_NORMAL)
    height, width = pencil_sketch_image.shape
    pencil_radius = 5
    step_size = 5
    for y in range(0, height, step_size):
        for x in range(0, width, step_size):
            canvas[y, x] = pencil_sketch_image[y, x]
            pencil_canvas = canvas.copy()
            cv2.circle(pencil_canvas, (x, y), pencil_radius, (0, 0, 0), -1)
            cv2.imshow("Pencil Sketch with Simulated Pencil", pencil_canvas)
            time.sleep(0.000000000000000000001)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.imshow("Pencil Sketch with Simulated Pencil", pencil_sketch_image)
    print("Press any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = input('Enter image path')
    sketch(input_image)
