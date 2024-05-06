import csv
import pickle

def read_csv_write_pickle(csv_file, pickle_file):
  with open(csv_file, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    data = list(csv_reader)

  with open(pickle_file, "wb") as pklfile:
    pickle.dump(data, pklfile)

# Example usage
csv_file = "/home/rguktrkvalley/AllClLabPrograms/output.csv"
pickle_file = "output.pkl"
read_csv_write_pickle(csv_file, pickle_file)

