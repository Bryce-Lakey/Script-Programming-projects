# Name: Bryce Lakey
# Semster: Fall 2024
# Due date: October 20th, 2024
# Instructor: Rene Hurst

fileName = input("Enter the name of the file you want to scan: ")
# User inputs the name of the file to scan.

file = open(fileName, 'r', encoding='utf-8')
lines = file.readlines()
# File opens in read mode, with a text encoding. 
# For some reason, the program would not read any text without it. The output would be 0 every time and it took me hours to figure out why.
# There is also a function for the program to read the lines of the text file.

lineCount = len(lines)
wordCount = sum(len(line.split()) for line in lines)
charCount = sum(len(line) for line in lines)
# Here we have a function to count and total the amount of lines of text within the program.
# Then for word count, the .split() function will split the string of words in the file into a list by the spaces.
## Which removes spaces and using the len statement, will count the individual words between the spaces. Then we take the sum of that to get the total word count.
# Using the same function without .split(), it will count the raw characters.

uniqueWords = []
for line in lines:
    allWords = line.split()
    for word in allWords:
        if word not in uniqueWords:
            uniqueWords.append(word)
# This one is complex but basically, this function creates an empty list for the unique words to be stored in.
# Then a new variable for the total list of words (allWords) is created, and split so it can rule out the duplicates.
# The last 3 lines tell the program to take a word from all the words scanned, and if it is not in the unique words list, add it to the end of the list (.append).
# This goes until all words in the text file are scanned and written to the output file. 

outputFileName = fileName + "Analysis.txt"
# Takes the name of the input file and adds "Analysis" to the name.
# Without the .txt at the end it changes the file extension lol.

outputFile = open(outputFileName, 'w', encoding='utf-8')
for word in uniqueWords:
    outputFile.write(word + '\n')
# This is the function I wrote for taking the list of unique words, and printing them to an output file.
# It uses the same text encoding to display the text in the file, and writes whats in the uniqueWords list to the .txt file.

outputFile.close()
file.close()
# Closing the file function will tell the program when I am done working with them. Not closing them creates errors.

print("The list of unique words will be in the output file titled:", outputFileName)
print("The amount of lines in this file is:", lineCount)
print("The amount of words in this file is:", wordCount)
print("The amount of characters in this file is:", charCount)
# Then we show the outputs for the counts, and one showing that a file has been created for the unique words with the name of said file.
