import pickle

def read_and_write_pickle(file_path, data=None):
  with open(file_path, "rb") as f:
    if data is None:
      # Read data from file
      data = pickle.load(f)
    else:
      # Write data to file
      pickle.dump(data, f)
  return data

# Example usage (reading)
file_path = "data.pkl"
data = read_and_write_pickle(file_path)
print(data)

# Example usage (writing)
data = {"name": "Alice", "age": 30, "city": "New York"}
read_and_write_pickle("output.pkl", data)

