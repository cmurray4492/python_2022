import re

my_string = input("Please enter a string: ")
pattern = re.compile(r"[0-9]")
# pattern = re.compile(r"[0-9]+")
# pattern = re.compile(r"\d")
# pattern = re.compile(r"\d+")
result = pattern.sub("_", my_string)
print(result)
