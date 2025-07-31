# Write a python program to translate a message into secret code language. Use the rules  below to translate normal english into secret code language.

# Coding:
# If the word contains atleast 3 characters, remove the first letter and appeal it at the end
# Now append three random character at the starting and the end
# Else:
#  Simply reverse the string

# Decoding:
# If the word contains less than 3 characters, reverse it
# Else:
# Remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.

import random
import string

def generate_rando_chars(n=3):
    return ''.join(random.choices(string.ascii_letters,k=n))
st=input("Enter message: ")
words=st.split(" ")
coding= input("1 For coding 2 for decoding: ")
coding=True if(coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(st)>=3):
            r1=generate_rando_chars()
            r2=generate_rando_chars()
            stnew=r1+ word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

# Decoding
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
