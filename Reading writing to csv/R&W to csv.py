import csv
import os


#User input
first_name = input("First Name: ")
last_name = input("Last Name: ")
phone_number = input("Phone: ")

#creates a list from the data the user provided
user_data = [first_name, last_name, phone_number]

#verifies the FLP file
file_exists = os.path.exists('FLP.csv')

#opens(or creates) the csv file in append mode to ensure new data will be added without affecting previous data
with open('FLP.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

#If the file doesn't exist, this line writes the header row  into the CSV file to label the data.
    if not file_exists:
        csv_writer.writerow(['First Name', 'Last Name', 'Phone'])

#writes the data into a new row in the csv file
    csv_writer.writerow(user_data)

#opens the flp.csv in read mode
with open('FLP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#prints the csv file data
    print("\nCSV File:")
    print(f"{'First Name:':<15} {'Last Name:':<15} {'Phone:':<15}")
    print("-" * 45)
    for row in csv_reader:
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15}")
