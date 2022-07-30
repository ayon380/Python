a=int(input("Enter your marks in maths"))
b=int(input("Enter your marks in Physics "))
c=int(input("Enter the marks in chemistry"))
d=(a+b+c)/3
e=min(a,b,c)
if(d>=40 and e>=33):
    print("You have passed !!!!!!!!!!")
else:
    print("You have failed !!!!!!!!!!!")