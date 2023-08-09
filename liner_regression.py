import pickle

# Replace 'example.pkl' with your .pkl file's path
file_path = r'D:\Desktop\Car\WEB_PAGE\WEB_PAGE\linear_regression_model.pkl'

# Load data from the .pkl file
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# Print the loaded data
print(data)