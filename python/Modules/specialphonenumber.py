
from commonlogic import checkforEvenNumber,checkfordivisibility
def checkfor10digit(n):
    if len(str(n))==10:
         return True 
    else:
        return False
n=int(input("please enter a phone number"))      

if(checkforEvenNumber(n) and checkfordivisibility(n) and checkfor10digit(n)):
    print("Its is a special number")
else:
    print("Its is not a special number")