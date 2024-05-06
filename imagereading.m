function read_and_write_image(image_path, output_path)
  image = imread(image_path);
  fwrite(image, output_path, "wb");
end

# Example usage
image_path = "path/to/your/image.jpg";
output_path = "output.bin";
read_and_write_image(image_path, output_path);
