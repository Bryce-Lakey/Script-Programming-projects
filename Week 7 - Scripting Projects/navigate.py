fileName = input("Input your filename: ")

lines = []
while True:
    line = input("Enter a line of text (or 'STOP' to finish): ")
    if line == "STOP":
        break
    lines.append(line)

file = open(fileName, 'a')
for line in lines:
    file.write(line + "\n")
file.close()
print("Finished.")
