import csv
import os

while True: 
    unit = int(input("Are your iutputs in KJ or Cal? enter 1 for KJ, 0 for Cal: "))
    if unit == 0:
        print("input in Calories")
        break
    elif unit == 1:
        print("input in KJ")
        break

print()
# get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# check if there are any CSV files
if not csv_files:
    print("No CSV files found in the current directory.")
else:
    # print the list of CSV files with their numbers
    print("CSV files in the current directory:")
    for i, f in enumerate(csv_files):
        print(f"{i+1}. {f}")

    # prompt the user to select a file by number
    while True:
        try:
            file_number = int(input("Enter the number of the CSV file you want to output: "))
            selected_file = csv_files[file_number-1]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid file number.")


# Open the CSV file and read the numbers
with open(selected_file, 'r') as file:
    reader = csv.reader(file)
    calories = [float(row[0]) for row in reader]

# Sum up the numbers and print the result
total = sum(calories)  
print("The result is in output.txt")
with open("output.txt", 'w') as f:
    if unit == 0:
        f.write("Cal: " + str(total) + '\n')
        f.write("KJ: " + str(round(total*4.184, 2)))

    elif unit == 1:
        f.write("Cal: " + str(round(total/4.184, 2)) + '\n')
        f.write("KJ: "+ str(total))
