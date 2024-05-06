import cv2

def read_and_write_image(image_path, output_path):
  image = cv2.imread(image_path)
  image_data = image.tobytes()
  with open(output_path, "wb") as f:
      f.write(image_data)

# Example usage
image_path = "/home/rguktrkvalley/AllClLabPrograms/rgbcolorss.jpg"
output_path = "output.bin"
read_and_write_image(image_path, output_path)

