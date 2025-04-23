# Importing the regex module
import re

# Example 1: Search for a string starting with 'The' and ending with 'Spain'
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Matches if the string starts with "The" and ends with "Spain"
if x:
    print("Match found:", x.group())  # If match is found, print it

# RegEx Functions
# 1. findall() - Returns a list of all matches
txt = "The rain in Spain"
x = re.findall("ai", txt)
print("findall() matches:", x)  # ['ai', 'ai']

# 2. search() - Returns the first match
x = re.search("Spain", txt)
if x:
    print("search() match:", x.group())  # Spain

# 3. split() - Splits the string at each match
x = re.split("\s", txt)  # Split at each whitespace
print("split() result:", x)  # ['The', 'rain', 'in', 'Spain']

# 4. sub() - Replaces the matches with a new string
x = re.sub("\s", "9", txt)  # Replace all whitespaces with '9'
print("sub() result:", x)  # 'The9rain9in9Spain'

# Metacharacters
# 1. [] - A set of characters
txt = "abc123"
x = re.findall("[a-c]", txt)  # Find characters between 'a' and 'c'
print("Metacharacters [a-c]:", x)  # ['a', 'b', 'c']

# 2. \d - Digits (0-9)
x = re.findall("\d", txt)  # Find digits
print("Metacharacters \\d:", x)  # ['1', '2', '3']

# 3. . - Any character (except newline)
x = re.findall("he..o", "hello world")  # Matches "hello"
print("Metacharacters .:", x)  # ['hello']

# 4. ^ - Start of a string
x = re.findall("^The", txt)  # Match if it starts with "The"
print("Metacharacters ^:", x)  # ['The']

# 5. $ - End of a string
x = re.findall("Spain$", txt)  # Match if it ends with "Spain"
print("Metacharacters $:", x)  # ['Spain']

# Flags
# Case insensitive matching using re.IGNORECASE
txt = "The rain in spain"
x = re.search("spain", txt, re.I)  # Case insensitive match
if x:
    print("Flag re.IGNORECASE match:", x.group())  # 'spain'

# Special Sequences
# 1. \b - Word boundary (matches position where a word starts or ends)
txt = "The rain in Spain"
x = re.findall(r"\bS\w+", txt)  # Find words starting with 'S'
print("Special Sequence \\b:", x)  # ['Spain']

# 2. \d - Digits (numbers from 0 to 9)
txt = "123 abc"
x = re.findall("\d", txt)  # Find digits
print("Special Sequence \\d:", x)  # ['1', '2', '3']

# Sets
# Match any digit between 0-9
x = re.findall("[0-9]", txt)
print("Set [0-9]:", x)  # ['1', '2', '3']

# Match any alphabet from a-z (lowercase)
x = re.findall("[a-z]", txt)
print("Set [a-z]:", x)  # ['a', 'b', 'c']

# The findall() function
# Example: Match all occurrences of 'ai' in the string
txt = "The rain in Spain"
x = re.findall("ai", txt)
print("findall() result:", x)  # ['ai', 'ai']

# Example: No match for 'Portugal'
x = re.findall("Portugal", txt)
print("findall() result for non-matching pattern:", x)  # []

# The search() function
# Example: Search for the first whitespace character
x = re.search("\s", txt)
if x:
    print("search() first whitespace location:", x.start())  # First whitespace location index

# Split function
# Example: Split the string at every whitespace
x = re.split("\s", txt)
print("split() result:", x)  # ['The', 'rain', 'in', 'Spain']

# Control number of splits
x = re.split("\s", txt, 1)
print("split() with maxsplit:", x)  # ['The', 'rain in Spain']

# The sub() function
# Example: Replace every whitespace with '9'
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print("sub() result with replacement:", x)  # 'The9rain9in9Spain'

# Replace only the first 2 occurrences
x = re.sub("\s", "9", txt, 2)
print("sub() with count parameter:", x)  # 'The9rain9in Spain'

# Match Object properties
# Example: Get start, end, and matched string
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
if x:
    print("Match Object span:", x.span())  # (12, 17) -> start and end positions
    print("Match Object string:", x.string)  # 'The rain in Spain'
    print("Match Object group:", x.group())  # 'Spain'
