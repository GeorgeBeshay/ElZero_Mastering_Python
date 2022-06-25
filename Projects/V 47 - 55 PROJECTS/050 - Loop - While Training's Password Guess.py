# ---------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ---------------------------

tries = 4
mainpassword = "Osama@123"
inputpassword = input("Write Your Password: ")
while inputpassword != mainpassword:
    tries -= 1 
    print(f"Wrong Password, { 'Last Chance' if tries == 0 else str(tries) +' Chances Left' } ...")
    inputpassword = input("Write Your Password: ")
    if tries == 0:
        print("Sorry You Have Entered The Password Wrong Several Times, Please Try Again Later.")
        break
    else:
        continue
else:
    print(" Correct Password ".center(50,"*"))
    print("*"*50)