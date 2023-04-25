citizen="Indian"
familyincome=800000
studentcourselist=["Engineering","Bds","Bcom","Bsc","Mbbs"]
enteredcitizen=str(input())
enteredfamilyincome=int(input())
enteredcourse=str(input())
if(citizen==enteredcitizen)and(enteredfamilyincome<=800000)and(enteredcourse in studentcourselist):
    print("you are eligible for scholarship")
else:
    print("sorry!! you are not eligible for scholarship")