import cv2
import csv

# Read image
image = cv2.imread("path/to/your/image.png")

# Separate color channels
red, green, blue = cv2.split(image)

# Save channels to CSV files
csv.writerow(open("red.csv", "w"), red.flatten())
csv.writerow(open("gr.csv", "w"), green.flatten())
csv.writerow(open("bl.csv", "w"), blue.flatten())

