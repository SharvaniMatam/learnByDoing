def checkforEvenNumber(n):
    if(n%2==0):
        return True
    else:
        return False



def checkforRange(n):
    if(n>=1000 and n<=9999):
        return True
    else:
        return False

def checkfordivisibility(n):
    if(n%4==0):
        return True
    else:
        return False

phonenumber=input('enter a phonenumber')
if(len(phonenumber)==10):
    formattednumber=int(phonenumber)
    if(checkforEvenNumber(formattednumber)and checkfordivisibility(formattednumber)):
       print("Its is a special number")
    else:
       print("Its is not a special number")
else:
    print("please enter a valiid phone number")