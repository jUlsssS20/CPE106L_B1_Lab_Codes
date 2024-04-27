filename = input("Enter filename: ")
with open(filename, 'r') as file:
    lines = file.readlines()
    print(f"The text file has/have {len(lines)} lines.")

while True:
    line_number = int(input("Choose the line to be read (0 to quit): "))
    if line_number < 0 or line_number > len(lines):
        if line_number != 0:
            print("Invalid number of lines.")
    else:
        if line_number == 0:
            break
        else:
            chosen_line = lines[line_number - 1]
            print(f"The line is: \n{chosen_line}")