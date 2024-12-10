def read_file_to_list(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
    return lines

file_name="file1.txt"
lines_list = read_file_to_list(file_name)
print(lines_list)
