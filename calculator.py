#calculator
input1 = float(input("enter first number="))
operator = input("enter your operator(*,/,+,-)=")
input2 = float(input("enter second number="))
if (operator == '+'):
           resultant = input1+input2
           print(resultant)
if (operator == '-'):
           resultant = input1-input2
           print(resultant)
if (operator == '*'):
           resultant = input1*input2
           print(resultant)
if (operator == '/'):
           resultant = input1/input2
           print(resultant)                   


x=0
for odd_even in range(0,10):
        print("duck")
        x+=1
        if x%3 == 0:
           print("goose")            

