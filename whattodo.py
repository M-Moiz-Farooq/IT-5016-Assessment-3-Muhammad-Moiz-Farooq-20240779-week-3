def whattodonow():
    message="time to"
    prompt="enter selection (1,2,3):"
    userchoice=int(input(prompt))

    if userchoice==1:
        print(message,"eat")
    if userchoice==2:
        print(message,"play")
    elif userchoice==3:
        print(message,"sleep")
    else:
        print("incorrect selection !")
whattodonow()            