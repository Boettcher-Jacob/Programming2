lines = ["Hello, ", "World", "!"]

with open("data/myfile.txt", 'w') as f:
  # Write data to a file
  f.write("Hi \n")
  f.writelines(lines)
  # or, for line in lines: file.write(line)

with open("data/myfile.txt", 'r') as f:
  #reading from a file
  print(f.read())