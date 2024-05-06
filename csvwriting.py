import csv
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
    ["Charlie", 42, "Paris"],
]
filename = "output.csv"
with open(filename, 'w', newline='') as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(data[0])
  csv_writer.writerows(data[1:])
