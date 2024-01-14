def sum(num1,num2):
    sum=num1+num2
    print(sum)

def difference(num1,num2):
    diff=num1-num2
    print(diff)

def product(num1,num2):
    prod=num1*num2
    print(prod)

def div(num1,num2):
    divi=num1/num2
    print(divi)

print("Enter two Numbers")

a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))

c=int(input("Enter choice(1->sum,2->Difference,3->Product,4->Division): "))

if(c==1):
    sum(a,b)
elif(c==2):
    difference(a,b)
elif(c==3):
    product(a,b)
else:
    div(a,b)
    

    