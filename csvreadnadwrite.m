% Data to write
data = [
  "Name", "Age", "City";
  "Alice", 25, "New York";
  "Bob", 30, "London";
];

% Write data to CSV file (assuming comma delimiter)
csvwrite("output.csv", data);


% Read data from CSV file (assuming comma delimiter)
data = csvread("output.csv");

% Access data
disp(data);  # Displays the entire data matrix
