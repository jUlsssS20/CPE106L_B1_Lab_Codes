def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    filename = input("Enter the filename: ")
    lines = read_file(filename)
    if lines is None:
        return
    
    num_lines = len(lines)

    while True:
        print(f"\nNumber of lines in the file: {num_lines}")
        line_number = input("Enter a line number (1 to quit, 0 to exit): ")

        if not line_number.isdigit():
            print("Please enter a valid number.")
            continue

        line_number = int(line_number)

        if line_number == 0:
            print("Exiting program.")
            break
        elif line_number < 0 or line_number > num_lines:
            print("Invalid line number. Please enter a number between 1 and", num_lines)
            continue
        else:
            print("Line", line_number, ":", lines[line_number - 1].strip())


if __name__ == "__main__":
    main()
