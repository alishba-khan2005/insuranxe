print("determining the ensurace cost")
insurance=500
surcharge=0
age=int(input("enter your age:"))
if age < 25:
  surcharge+=100
accidents=int(input("enter no of accidents:  "))
if accidents==1:
  surcharge+=50
elif accidents==2:
  surcharge+=125
elif accidents==3:
  surcharge+=225
elif accidents==4:
  surcharge+=375
elif accidents==5:
  surcharge+=575
else:
  surcharge+=0

total_insurance=insurance+surcharge
print("your total insurance cost for your automobile is ", total_insurance)