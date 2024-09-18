'''
bingo

'''           
x=0
numguess=int(input("enter any number from 1-50:"))
bingonumbers=(2, 18 , 41 , 30 , 39)
guessednumber=[]
if numguess in bingonumbers:
       guessednumber.append(numguess)
       while len(guessednumber) < len(bingonumbers) :
              
              if x!=5:
                     x+=1
                     print(bingonumbers)

                     print("you guesseed the right number, guess a number again")
                     numguess=int(input("enter any number from 1-50:"))   
              if numguess not in bingonumbers:

                  print("wrong!!!!!, Try Again")          
                  numguess=int(input("enter any number from 1-50:"))        
              else:
                  print("Bingo!!!!!!")
                  numguess=int(input("enter any number from 1-50:"))