print("Welcome to the Simple ATM Simulator😉")
balance=1000
user_pin=1234
pin=int(input("Please enter your PIN:"))
if(pin==user_pin ):
    atm_on=True
   
else:
    print("your pin is incorrect!")
    atm_on=False

while atm_on:
    print("Main menu:\n1. Check Balance\n2. Deposit Money\n3.Withdraw Money\n4. Exit\n")
    
    choice=int(input("Enter your choice:"))
    
    if(choice==1):
        print("Your current balance is  Rs."+str(balance))
        
    elif(choice==2):
        amount=float(input("Enter the amount to deposit:"))
        balance+=amount
        print("Rs"+str(amount)+"deposited successfully.")
        
    elif(choice==3):
        amount=float(input("Enter the amount to withdraw:"))
        if amount>balance:
            print("Insufficient balance!")
        else:
            balance-=amount
            print("Rs"+str(amount)+" withdraw successful")
    elif(choice==4):
        print("Thank you for using the ATM. Goodbye!")
        atm_on=False
    else:
        print("Invalid choice. Please try again. ")
        
            

    
    
    
    