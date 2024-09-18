def getminutes(hours , minutes):
    total = hours*60 + minutes
    return total

hours=float(input("enter the hours:"))
minutes=float(input("enter the minutes:"))
totalminutes= getminutes(hours,minutes)
print("1.", totalminutes, "minutes" )
print("2.", getminutes(5,0), "minutes")
print("3.", getminutes(11,540),"minutes")


def calculateweeklysalary(perhourwage,workhours):
    totalweekly=perhourwage*workhours
    
    return totalweekly
def calculatemonthlysalary(perhourwage,workhours):
    totalmonthly=(perhourwage*workhours)*4
    return totalmonthly



perhourwage=float(input("enter wage per hour:"))
workhours=float(input("enter work hours a week:"))
weeklysalary=calculateweeklysalary(perhourwage,workhours)
monthlysalary=calculatemonthlysalary(perhourwage,workhours)


print("the total weekly salary is", weeklysalary,"and the total monthly salary is",monthlysalary)





def convertcelsiustofarenheit(celsius):
    farenheit=celsius*9/5+32
    return farenheit
celsius=float(input("enter the temperature in celcius:"))
farenheintconverted=convertcelsiustofarenheit(celsius)
print(celsius,"when converted to farenheitr is:", farenheintconverted,"farenheit")



def function1(n1,n2,n3):
    sum=n1+n2+n3
    minimum=min(n1,n2,n3)
    return sum-minimum
n1=int(input("enter the first whole number:"))
n2=int(input("enter the second whole number:"))
n3=int(input("enter the value of the third integer:"))
print(function1(n1,n2,n3))