### Created by Ian Jude Timbungco created on 01/21/2024

#  Write a Python program to check the validity of passwords input by users.  (Source: https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php)

'''

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

'''

### Importing Module
import re 


### Setting up variable for receiving user input
p = str(input('Input: '))


### Creating object Password
def password(val):

    ### Function for checking if any special characters (@,#,$) are present in the user input.
    def special(spec):

        count, count2, count3 = spec.count('@'), spec.count('#'), spec.count('$')
        if count or count2 or count3 != 0:
            return "Valid password"

        else:
            return "Invalid password"
    
    ### Function for verifying the user input is within the acceptable range (Minimum of 6 and Maximimum of 16)
    def length(num):
        if len(num) < 6 or len(num) > 16 :
            return "Invalid password"
        
        else:
            return num
    
    ### Function for checking if any numbers are present in the user input
    def num_bet(between):
        between = p
        if re.search("[0-9]", between):
            return "Valid Password"
        else:
            return "Invalid password"
        
    ### Function if any capital letter/s [A...Z] is on the user input
    def cap_let(caps):
        caps = p
        if re.search("[A-Z]", caps):
            return "Valid Password"
        else:
            return "Invalid password"
    
    ### Function if any small letter/s [a...z] is on the user input
    def small_let(small):
        small = p
        if re.search("[A-Z]", small):
            return "Valid Password"
        else:
            return "Invalid password"

    ### Conditional function if any of the created function met the requirements
    def main():

        if (length(val) or special(val)) and (num_bet(val)) and (cap_let(val) or small_let(val))  == "Invalid password":
            return "Use stronger password!"
        
        else:
            return "Valid Password"
        
    return main()


if __name__ == '__main__':
    passwords = password(p)
    print(passwords)