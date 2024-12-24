# Multiline string: """", ''''

sentence = '''Hello shahab.
How are you?
In which class do you read in?'''
print(sentence)


# Strings are Arrays
greetings = "Shabab lives in Canada"
print(greetings[0:6]) # range is inclusive: 0-5


# Loop throgugh a string
for greet in greetings:
    print(greet)


# String length
print(len(greetings))

# Check string
txt = "My country name is Bangladesh"
target_word = "country"
print(target_word in txt)


# Check string: is not
txt = "My country name is Bangladesh"
target_word = "country"
print(target_word not in txt)


# Check string: if statement
if target_word in txt:
    print("Yes you are correct!")
elif target_word not in txt:
    print("No you are wrong!")
else:
    print("The checking game is over")    

# Converting using function

def guess(question, answer):
    answer = answer.lower() #yes
    if answer == 'yes':
        print("Yes you are correct!")
    elif question == 'no':
        print("No you are wrong!")
    else:
        print("Sorry! The checking game is over")   

question = "Are you from BD?"
answer = "yeS"
guess(question, answer)
