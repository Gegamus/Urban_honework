file_name = "file.txt"
file = open(file_name, mode="rb")
file.content = file.read()
file.close()
print(file.content)