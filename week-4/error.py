filename = input("Enter file name: ")
try:
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")