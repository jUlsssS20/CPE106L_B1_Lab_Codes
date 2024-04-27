def navigate_file():

  filename = input("Enter the input file name: ")
  try:
    with open(filename, "r") as file:
      lines = file.readlines()
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return

  num_lines = len(lines)

  while True:
    print(f"The file has {num_lines} lines.")
    line_num = int(input("Enter a line number [0 to quit]: "))
    if line_num == 0:
      break
    elif 0 < line_num <= num_lines:
      print(lines[line_num - 1])  # Adjust for 0-based indexing
    else:
      print(f"Error: Line number must be between 1 and {num_lines}.")

if __name__ == "__main__":
  navigate_file()