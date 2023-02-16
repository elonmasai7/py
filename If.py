
# If statement
x=1
marks=49
grade=70
Bal=200
if(x>0):
    print("The number is positive")
# if... else statement
if(marks>=50):
    print("you've passed the exam")
else:
    print("you've failed your exam")
# If... elif.. else statement
if grade<=29 and grade>=0:
    print("you've failed")
elif grade>=30 and grade<=49:
    print("you've passed")
elif grade>=50 and grade<=79:
    print("you've a credit")
elif grade>=80 and grade<=100:
    print("you've a distinction")
else:
    print("Wrong grade entered")
# Mpesa ballance
if Bal<=29 and Bal>=0:
    print("Insuficient ballance")
elif Bal>=30 and Bal<=49000:
    print("Widthdraw")
elif Bal>=50000 and Bal<=790000:
    print("you can only widthdraw Ksh 200000 a day or wait")
elif Bal>=800000 and Bal<=1000000:
    print("Visit any of our dealers near you or call mathare help line")
else:
    print("Input amount again")



