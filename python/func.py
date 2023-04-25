def scholarshipeligibilty():
  citizen=input("enter a citizen name")
  familyincome=800000
  studentcourselist=["Bds","Bcom","Mbbs","Engineerng","Bsc"]
  if(citizen=="Indian")and(familyincome<=800000):
   if("Mbbs" in studentcourselist):
      print("You are eligible for scholarship")
   else:
      print("Sorry!! you are not eligible for scholarship")


def evenNumber():
   n=int(input('PLease enter a number'))
   if(n%2==0):
      print('Its a even number')
   else:
      print('Its a odd number')
evenNumber()
scholarshipeligibilty()

