n = int(input("Please enter a number "))
if(n >= 1 and n <= 100):
    if(n % 2 == 0):
      if(n >=2 and n<=5):
        print("Not Weird")
      elif(n >= 6 and n<= 20):
        print(" Weird")
      else:
        print("Not Weird")
    else:
      print("Weird")
else:
  print("Not Weird")