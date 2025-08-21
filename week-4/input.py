with open('input.txt', 'w') as f:
    f.write("My name is SpongBob.\nMy best friend is Patrick.")

with open('input.txt', 'r') as f:
    content = f.read()

modified_content = content.upper()
word_count = len(content.split())

with open('output.txt', 'w') as file:
    file.write(modified_content + "\n\nWord count:" + str(word_count))

print("Succefully created output.txt with modified text and word count.")