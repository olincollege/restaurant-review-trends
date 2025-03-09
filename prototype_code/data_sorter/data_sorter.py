import csv
import pandas as pd

# Import Data File
with open("\\prototype_code\api_caller\sample_response.txt", "r") as f:
    data = pd.DataFrame(f, columns=["rating", "text", "title"])

print(data)
# Check if review is for restaurant


# Check if review rating is 1 or 5 stars
# Sort to appropriate data set in .csv file

# # example
# import csv

# # Writing to a CSV file
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Alice", 30])
#     writer.writerow(["Bob", 25])

# # Reading from a CSV file
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
