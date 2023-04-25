from commonlogic import checkforEvenNumber,checkfordivisibility
def checkforRange(n):
    if(n>=1000 and n<=9999):
        return True
    else:
        return False
 
n=int(input("please enter a number"))
if(checkforEvenNumber(n) and checkfordivisibility(n) and checkforRange(n)):
    print("Yeah!! Its a special number")
else:
    print("Nooo its not a special number")