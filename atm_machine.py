users=['sabir','nasir','shakeela','yasir']
passwords=['1111','2222','3333','4444']
balance=[50000,10000,20000,30000]
print("\n\n*** Welcom to My ATM System ***\n")
userName=input("Please enter your user name: ")
paswd= input("Please enter your Password: ")
if userName in users and paswd in passwords:
        if users.index(userName) == passwords.index(paswd):

            while(True):
            
                userSelectedOpr= int(input("\n          Menu\n \nPlease select operation: \n - Press 1 to Check your balance\n - Press 2 to withdraw cash\n - Press 3 to deposite amount\n"))
                
                if userSelectedOpr ==1:
                    print("Your Current balance is ",balance[int(users.index(userName))]),'\n'
                    break

                if userSelectedOpr ==2:
                
                    w_amount= int(input("\nPlease enter amount: "))
                    
                    if w_amount <= balance[int(users.index(userName))]:
                        
                        balance[int(users.index(userName))] = balance[int(users.index(userName))] - w_amount
                        print("\nTransaction done successfully! \n")
                        print("This is new balance",balance[int(users.index(userName))])
                        break

                    else:
                        print("Insufcient balance\n")
                        break
                else:
                    print("Please select number from Menu")
                    continue
            else:
                print("\nInvalid user name or password \n")
               


else:
    print("\nIncorrect user name or passwprd \n")