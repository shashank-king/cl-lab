function read_csv_write_pickle(csv_file, pickle_file)
  data = csvread(csv_file);
  save(pickle_file, "data");
end

# Example usage
csv_file = "data.csv";
pickle_file = "output.pkl";
read_csv_write_pickle(csv_file, pickle_file);
