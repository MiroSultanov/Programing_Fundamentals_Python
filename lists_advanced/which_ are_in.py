# You will be given two sequences of strings, separated by ", ". 
# Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

strings = input().split(', ')
sentence = input()
result = [el for el in strings if el in sentence]
print(result)