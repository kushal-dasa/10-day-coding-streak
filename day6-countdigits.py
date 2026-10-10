number=int(input("enter a number:"))
count=0
number=abs(number)
if number==0:
    count=1
else:
    while number>0:
        number=number//10
        count+=1
print("number of digits:",count)