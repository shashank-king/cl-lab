function read_and_write_pickle(file_path, data=struct())
  if isempty(data)
    % Read data from file
    data = load(file_path);
  else
    % Write data to file
    save(file_path, "-struct", "data");
  end
end

# Example usage (reading)
file_path = "data.pkl";
data = read_and_write_pickle(file_path);
disp(data);

# Example usage (writing)
data = struct("name", "Alice", "age", 30, "city", "New York");
read_and_write_pickle("output.pkl", data);
