firstFile = input("Enter the name of the file you want to copy from: ")
secFile = input("Enter the name of the file you want to copy to: ")

f = open(firstFile, 'r')
allLines = ""
while True:
    line = f.readline()
    if line == "":
        break
    allLines += line

f = open(secFile, 'w')
f.write(allLines)
print(line)
f.close()

print("Your text was successfully copied!")
