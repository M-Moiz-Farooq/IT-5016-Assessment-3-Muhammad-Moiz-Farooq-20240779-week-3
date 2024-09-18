'''
Week 3 Lab IT5016
Author: Muhammad Moiz Farooq / 20240779
WhiteCliffe College, AKL

'''
# Wavelength Converter
print("Welcome To our wavelength colour converter")
wavelength=int(input("enter the wavelength in nanometers(750-380):"))
print(F"Thank you, the wavelength you entered is {wavelength}")
if wavelength <= 750 and wavelength>=620:
    print("your colour is red")
elif wavelength >=590 and wavelength>=620:
    print("your colour is orange")
elif wavelength>=495 and wavelength <= 570:
    print("your colour is green")
elif wavelength>= 450 and wavelength<495:
    print("your colour is blue")
elif wavelength==380 and wavelength<450:
    print("your colour is violet")    
else:
    print("Wavelength enter is outside of visible spectrum")         


# Calculator
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

# Earthquake Magnitude Finder
magnitude=float(input("enter the magnitude of the earthquake:"))

if magnitude>=2.0 and magnitude<3.0:
    print("The earthquaake is very minor")
elif magnitude >=3.0 and magnitude<4.0:
    print("The earthquake is minor")
elif magnitude >= 4.0 and magnitude <5.0:
    print("The earthquake is light")
elif magnitude>=5.0 and magnitude<6.0:
    print("The earthquake is moderate")
elif magnitude>= 6.0 and magnitude<7.0:
    print("The earthquake is strong")
elif magnitude>=7.0 and magnitude<8.0:
    print("The earthquake is major") 
elif magnitude>=8.0 and magnitude<10.0:
    print("The earthquake is very great")
elif magnitude>=10.0:
    print("The earthquake is meteoric")           

# Grade Calculator
assessgrade=float(input("Enter your assessment grade:"))
examgrade=float(input("Enter your exam grade:"))
averagegrade=(assessgrade+examgrade)/2
print(averagegrade)
if averagegrade>=90:
    print("Your grade is A")
elif averagegrade>=80:
    print("Your grade is B") 
elif averagegrade>=70:
    print("Your grade is C")
elif averagegrade>=60:
    print("Your grade is D")
elif averagegrade>100:
    print("wrong numbers entered")
else:
    print("You have failed, Better Luck Next Time")                   

# Student ID Generator
studentid=int(input("Enter your student id:"))
firstname=str(input("Enter your first name:"))
lastname=str(input("Enter your last name:"))
university=str(input("Enter the name of your university:"))
if "whitecliffe college" in university and university.islower():
    print("Your student id is:",str(studentid)[:1],lastname[:3],sep="")










                