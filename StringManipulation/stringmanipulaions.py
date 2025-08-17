# This is a class to perform various string manipulations
text_string="This is a sample string for testing."
print("type of text_string:", type(text_string))
print("value of text_string:", text_string)

# Indexing:

print("Value at index 0:", text_string[0])
print("Value at index 1:", text_string[1])
print("Value at index 2:", text_string[2])
print("Value at index 3:", text_string[3])
print("Value at index 4:", text_string[4]) # This will be blank. Space is also a character.
#Slicing:
print("The values from index 0 to 4 are:", text_string[0:5])
print("Reverse of ", text_string, "is ", text_string[::-1])
print(text_string)
listOfWords=text_string.split(" ")

listOfWordsInReverse=[]
reversed_string=""
for i in range(len(listOfWords)-1, -1, -1):
    reversed_string+=listOfWords[i]+" "
print(reversed_string)
