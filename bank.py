balance=10000

while True:
    print("=========================")
    print("====Welcome to K-ATM=====")
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Deposit Cash")
    print("4. Transfer cash")
    print("5. Exit")
    print("=========================")

    choose= int(input("Enter choice: "))
    

    if choose==1:
        print("Your balance is: ", balance)
#withdraw money
    elif choose==2:
        amount = float(input(" Enter amount you want to withdraw:R "))
        if amount > 0 and amount<=balance:
            balance=balance - amount
            print("You new balance is:R", balance)
        elif amount<=0:
                print("Invalid withdrawal amount")
        else:
            print("Insufficient amount")

    elif choose==3:
        amount=float(input("Enter amount you want to deposit:R "))
        if amount>0:
             balance=balance + amount
             print("Your new balance is:R ", balance)
        else:
            print("Invalid amount")

#sending money
    elif choose==4:
        
         while True:
             #ask for acc number 
            transferacc=int(input("Enter account no:"))
            
            if transferacc.isdigit() and 7<=len(transferacc)<=10:
               # print("Account number valid")
                break
            else:
                print("Inavlid account number.Must be a 7-10 digit number")
                continue #ask again
            amount=float(input("Enter an amount to transfer:R "))

                #confirming
         while True:
            confirm=input(f"Confirm transaction of R{amount} to account number:{transferacc}? (y/n): ")

            if confirm =="y" and amount>0:
                    balance=balance-amount
                    print("Transaction confirmed!")
                    print("Your new balance is:R",balance)
                    break

            elif confirm =="n":
                print("Trasaction terminated")
                break
            else:
                print("Invalid imput.Enter a y (yes) or  (no):")
                
    else:
        break
    