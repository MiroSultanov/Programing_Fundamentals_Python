# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.

double_char = input()
double_string = ""

for char in double_char:
    double_string += char * 2
print(double_string)

