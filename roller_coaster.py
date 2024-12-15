#entry tickets to roller coaster depend on your height and age.  

#If height >= 120, you can ride, else not. If your age is below 12, you pay rs 5, if <= 18, you pay rs 7, else you pay 12 rs. Age b/w 45 - 55, pay 0 rs. If you want a photo, you pay rs 3 extra. 

  

height = int(input("Enter your height in cm\n")) 

if height >= 120: 

  print("You are tall enough to ride the roller coaster.\n") 

  age = int(input("What is your age?\n")) 

  bill = 0 

  if age < 12: 

    bill = 5 

  elif age <= 18: 

    bill = 7 

  elif age >= 45 and age <= 55: 

    bill = 0 

    print("Everything is going to be fine. Have a free ride on us.") 

  else: 

    bill = 12 

    

  photo = input("Do you want a photo? Y or N\n") 

  if photo == "Y": 

    bill += 3 

     

  print(f"Your total bill is {bill}") 

     

else: 

  print("Sorry, you have to grow tall before you can ride.") 

 
