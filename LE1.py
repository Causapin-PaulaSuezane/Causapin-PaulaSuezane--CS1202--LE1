# Causapin, Paula Suezane Z.
# CS-1202
# Code is created in jupyter notebook and pasted here in vscode
# SOME FINAL EDITS ARE MADE HERE IN VSCODE.
# This file is the final output code.
# Some commits are in the branch.




#_____________________________DICTIONARIES-&-ADD_ONS_____________________________________________________________________________


# Game library for available games
game_library = {
    "Donkey Kong": {"copy": 3, "price": 2},
    "Super Mario Bros": {"copy": 5, "price": 3},
    "Tetris": {"copy": 2, "price": 1}
}


# where created accounts are in
account = {}

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# I need this to be used for a line of code to exit program althogether
import sys

# just a display function
def decor():
    print("=====================================")
    
def decor2():
    print("- - - - - - - - - - - - - - - - - - -")


    
#_____________________________LOGIN-&-SIGNUP_____________________________________________________________________________________
                            #  (FOR USER)

# Sign up or creating new account
def create_acc():
    username = input("Enter a Username: ")                          # Creates a username
    if username in account:                                         # Checks if the username created already exists
        print("Username already taken. Please another username.")   
        return
    password = input("Enter a Password: ")                          # Creates password
    account[username] = {"password": password, 
                         "wallet": 0.0, 
                         "points": 0, 
                            "borrowed" : {
                                "Donkey Kong": {"name": "Donkey Kong", "amount": 0},
                                "Super Mario Bros": {"name": "Super Mario Bros", "amount": 0},
                                "Tetris": {"name": "Tetris", "amount": 0}
                            }
                        }# Puts the created username, password to the 'account' dictionary
                         # Have its own wallet, points and borrowed inventory.
    
    print("\nTop-up first before you proceed any further for a smoother experience!\n")
    add_ammount(username)     
    print("\nRegistered Successfully!!")

    
# Logging in...
def log_in():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username in account and account[username]["password"] == password: # Checks if all information typed is in the account dictionary
        print("\nLog In Successfully !!")
        return menu(username)
    else:
        print("\nLog In Failed....")

        

#_____________________________USER-FUNCTIONS_____________________________________________________________________________________

# function to show available games
def display_library():
    print("Current Store: ")
    for count, (game, details) in enumerate(game_library.items(), start=1):   # Makes a list to be printed. (starts count to 1)
        print(f"{count}. {game}: ${details['price']} - Copies {details['copy']}")
        
# function to display your borrowed games
def display_borrowed(username):
    print("Borrowed Game: ")
    for count, (game, details) in enumerate(account[username]["borrowed"].items(), start=1):    # Makes a list to be printed. (starts count to 1)
        print(f"{count}. {details['name']} - Copies {details['amount']}")
        
# To display your current money
def display_walletbalance(username):
    user_wallet = account[username]["wallet"]             # Assigns the users wallet to the user_wallet variable
    print(f"Your current balance is: ${user_wallet}")   
    
# To display your current points
def display_pointbalance(username):
    user_points = account[username]["points"]            # Assigns the users points to the user_points variable
    print(f"Your current points is: {user_points}")

# Add money to your wallet
def add_ammount(username):
    while True:
        try:
            wallet = float(input("Add ammount: $ "))           # Assigns the inputted amount the the walet variable
            account[username]["wallet"] += wallet              # Inputs the amount of 'wallet' into the user's wallet
            print(f"Your new balance now is: $ {account[username]['wallet']}")
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")
            
# Function to borrow games        
def borrow_game(username):
    user_wallet = account[username]["wallet"]                          # Assigns the "account[username]["wallet"]" to the user_wal
    user_points = account[username]["points"]                          # Same step as the other one and will also be applied to the next line
    borrowed = account[username]["borrowed"]
    
    display_library()
    decor()
    try:
        choice = int(input("Choose a game to borrow (enter the number): "))
        if choice >= 1 and choice <= len(game_library):                 # Checks if the number typed is within the scope of the number of items in game_library.
            game = list(game_library.keys())[choice - 1]                # variable 'game' is where the selected game will be stored. ('choice - 1' is to match the number typed in the index of the game_library )
            game_details = game_library[game]                           # will retrive the data you've selected.

            if game_library[game]["copy"] > 0:                          # Checks if there's any copy left.
                game_price = game_details["price"]                      # Assigns the price of the game to the variable 'game_price'.
                print(f"\nPrice of {game}: ${game_price} with {game_details['copy']} copies left")
                ans = input("\nBorrow it? (Y to proceed, ENTER to cancel) : ")  # For confirmation.

                if ans.upper() == 'Y':
                    if user_wallet >= game_price:                       # Checks if money is enough for the borrow price of the game.
                        user_wallet -= game_price                       # Then it will deduct user's money by the price of the game.
                        account[username]["wallet"] = user_wallet
                        game_library[game]["copy"] -= 1                 # Deducts 1 copy to the game library.

                        if game in borrowed:                      # Checks if game is in inventory
                            borrowed[game]["amount"] += 1         # Adds 1 if there is.
                        else:
                            borrowed[game] = {"name": game, "amount": 1}    # Else if none, makes the amount to 1.

                        points = float(game_price/2)                    # will add points to the user for every $2 spent.
                        user_points += points                           # Adds point to the user_points.
                        account[username]["points"] = user_points       # Updates earned points in the account/user's points
                        
                        decor()
                        print(f"You've borrowed a copy of {game}")
                        print(f"You now have a total of {borrowed[game]['amount']} copy/ies of {game}")
                        print(f"Remaining Balance: ${user_wallet}")
                        print(f"Earned Points : {user_points}")

                    else:
                        print(f"\nInsufficient Funds!")                   
                else:
                    print("\nCancelling order......")                     
                    return
            else:
                print("\nNo more copies!")
        else:
            print("\nInvalid choice!")
    except ValueError:
        print ("\nPlease select a number you want from the choices.")
        decor()
        return borrow_game(username)

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    user_points = account[username]["points"]
    borrowed = account[username]["borrowed"]
    
    try:
        if user_points >= 3:      # Checks if user have enough points before proceeding to the next.
            display_library()
            while True:
                choice = int(input("Select a game to borrow for FREE!!! (enter the number): "))
                if choice >= 1 and choice <= len(game_library):
                    game = list(game_library.keys())[choice - 1]
                    game_details = game_library[game]

                    if game_library[game]["copy"] > 0:
                        print(f"{game} : {game_details['copy']} copies left")
                        ans = input("Borrow it (Y or N): ")      # For confirmation.

                        if ans.upper() == 'Y':
                                user_points -= 3                 # Deducts 3 points from the user once confirmed.
                                game_library[game]["copy"] -= 1  # Deducts a copy from the game library
                                borrowed[game]["amount"] += 1    # Adds a game to the user's borrowed

                                print(f"You've borrowed a copy of {game}")
                                print(f"You now have a total of {borrowed[game]['amount']} copy/ies of {game}")
                                print(f"Remaining Points: {user_points}")
                                break
                        else:
                            return
                    else:
                        print("No more copies!")
                        break
                else:
                    print("Invalid choice!")
                    break
        else:
            print("Insufficient points!")
            print(f"You have {user_points} points.")
            print("Please borrow first to earn points. 1 point for every $2 spent!!!")
            
    except ValueError:
        print("/nValueError, please type a valid number within the choices.")
        return

# function to return your borrowed games 
def return_game(username):
    display_borrowed(username)                                              # Displays Inventory 
    decor()
    borrowed = account[username]["borrowed"]
    
    try:
        choice = int(input("Choose a game to return (enter the number): "))

        if choice >= 1 and choice <= len(borrowed):                     # Checks if the number typed is within the scope of the number of items in 'borrowed' dictionary.
            game = list(borrowed.keys())[choice - 1]                    # variable 'game' is where the selected game will be stored. ('choice - 1' is to match the number typed in the index of the 'borrowed' dictionary )
            if game in game_library:
                if borrowed[game]["amount"] > 0:                        # Checks if there is any borrowed items in 'borrowed' dictionary for selected game.
                    borrowed[game]["amount"] -= 1                       # Deducts the item in 'borrowed' dictionary
                    game_library[game]["copy"] += 1                     # Adds/returns the copy of the selected game cak in the 'game_library'
                    print(f"\nReturned a game of {game} successfully!")
                else:
                    print("\nYou haven't borrowed any copies of this game.")
                    return
            else:
                print("\nGame not found in store!")
                return menu(username)                                   # Returns to the menu function.
        else:
            print("\nInvalid choice!")
            return
    except ValueError:
        print("\nValueError, please type a valid number within the choices.")
        return

        
        
#_____________________________ADMIN-FUNCTIONS_____________________________________________________________________________________

# Function to update game prices
def admin_game_price():
    display_library()
    while True:
        try:
            decor()
            choice = int(input("Select a game to update its price (enter the number): "))
            decor()

            if choice >= 1 and choice <= len(game_library):
                game = list(game_library.keys())[choice - 1]
                game_details = game_library[game]
                print(f"Current in-Store : {game} - ${game_details['price']}")  
                while True:
                    try:
                        updated_price = float(input("Update the current price of the game selected into : ")) # Will update the price of the game
                        if updated_price < 0:        # Checks if the typed number is less than 0
                            print("Please input a positive number")
                        else:
                            game_details['price'] = updated_price  # Updates the price of the game.
                            print(f"\nPrice for '{game}' is update to ${updated_price}.")
                            return
                    except ValueError:
                        decor()
                        print("Please input your price.")
                        decor()
            else:
                print("Invalid Choice")
                decor()
        except ValueError:
                    print("Please input a valid number within the given choices.")

# Function to update game copy
def admin_game_copy():
    display_library()
    decor()
    while True:
        try:
            choice = int(input("Choose a game to update its number of copies (enter a number): "))
            decor()
            
            if choice >= 1 and choice <= len(game_library):
                game = list(game_library.keys())[choice - 1]
                game_details = game_library[game]

                print(f"Current in-Store : {game} - {game_details['copy']}")
                while True:
                    try:
                        updated_copies = int(input("Update the current copies of the game selected into : ")) # Will update the number of copies of the game

                        if updated_copies < 0:       # Checks if the typed number is less than 0.
                            print("Please input a positive number")
                        else:
                            game_details['copy'] = updated_copies   # Updates the copy of the game
                            decor()
                            print(f"Copies for '{game}' is updated to {updated_copies}.")
                            decor()
                            return  # Exit the inner loop and the function
                    except ValueError:
                        print("\nPlease input a valid number to update the copy of your chosen game.")
            else:
                print("\nInvalid Choice")
        except ValueError:
            print("\nPlease input a valid number to update the copy of your chosen game.")


# Function to Add new game
def admin_add_game():
    display_library()
    while True:
        try:
            new_games = int(input("Enter how many new games you want to add: "))   # Prompts the user to enter how many games he wants to add.
            if new_games >= 10:                    # Limits the admin to add games less than zero at a time
                print("Too many new games to add. Please keep it slow haha!")
                decor()
            elif new_games <= 0:                   # Checks if number typed is less than or equal to 0 
                print("Please enter a valid number greater than 0.")
                decor()
            else:
                decor()
                break
        except ValueError:
            print("Invalid input. Please enter a vaid input")
    for i in range(new_games):                     # Loops the user till the number of games it wants to add is complete.
        game_name = str(input("Enter game name : ")) # Names the new game
        while True:
            try:
                copy = int(input("Enter number of copies : "))  # How many copies it wants.
                if copy <= 0:                                   # Checks if the copy it types is less of equal to zero
                    print ("Please enter a number of copy for your new game.")
                else:
                    break
            except ValueError:
                    print("Invalid input.")
        while True:
            try: 
                price = float(input("Enter price :"))           # How much is the new game/s?
                decor()
                if price < 0:                                   # Checks if the price it typed is less or equal to zero
                    print("Please enter a valid positive number to price your new game.")
                else:
                    break
            except ValueError:
                print("Invalid input")
                decor()
        game_library[game_name] = {"copy" : copy, "price" : price}  # Updates the new game/s to the game_library
        print("Updated Game Library :")
        display_library()
        
     
    
#_____________________________ADMIN-LOGIN_____________________________________________________________________________________

# Function for admin login
def admin_login():
    global admin_username
    global admin_password
    Admin_username = input("\nEnter admin username: ")
    Admin_password = input("Enter admin password: ")
    if Admin_username == admin_username and Admin_password == admin_password:
        print("\nLog In Successfully !!")
        return admin_menu()
    else:
        print("\nUsername or password is Invalid !!")

        
        
#_____________________________MENUS/MAINS_____________________________________________________________________________________
                            # (FOR USERS)
    
# Menu to create account and log your account in.
def regis_menu():
    decor2()
    print("\tWelcome To Game Center!")
    decor2()
    
    while True:
        print("\n1. Register \n2. Login \n3. Admin Login \n4. Exit")
        choice = input("\nPlease select a number: ")
        decor()
        if choice == "1":
            create_acc()
        elif choice == "2":
            log_in()
        elif choice == "3":
            admin_login()
        elif choice == "4":
            print("Exiting the program...")
            sys.exit(0) #exit program altogther. 
        else:
            print("Invalid Choice, Please Try Again. ")

# Menu once you're logged in. Where majority of functions are to be used.
def menu(username):
    while True:
        decor()
        print(f"Hello {username},")
        print("1. Display Game")
        print("2. Borrow Game")
        print("3. Return Game")
        print("4. Check Wallet Balance")
        print("5. Check Point Balance")
        print("6. Check Borrowed Games")
        print("7. Add Balance")
        print("8. Redeem Free Game")
        print("9. Back")
        print("10. Exit")
        
        choice = input("Choice between (1-10): ")
        decor()
        
        if choice == "1":
            display_library()
        elif choice == "2":
            borrow_game(username)
        elif choice == "3":
            return_game(username)
        elif choice == "4":
            display_walletbalance(username)
        elif choice == "5":
            display_pointbalance(username)
        elif choice == "6":
            display_borrowed(username)
        elif choice == "7":
            add_ammount(username)
        elif choice == "8":
            redeem_free_rental(username)
        elif choice == "9":
            return regis_menu()
        elif choice == "10":
            print("Exiting the program...")
            sys.exit(0) #exit program altogther.    
        else:
             print("Invalid Input!") 


                
#_____________________________MENUS/MAINS_____________________________________________________________________________________
                            # (FOR ADMIN)

# Admin menu
def admin_menu():
    while True:
        decor()
        print(f"Hello {admin_username}!")
        print("1. View Game Library")
        print("2. Update Game prices")
        print("3. Update Game copy")
        print("4. Add New Games")
        print("5. Back")
        print("6. Exit")

        choice = input("Choice between (1-5): ")
        decor()
        
        if choice == "1":
            display_library()
        elif choice == "2":
            admin_game_price()
        elif choice == "3":
            admin_game_copy()
        elif choice == "4":
            admin_add_game()
        elif choice == "5":
            return regis_menu()
        elif choice == "6":
            print("Exiting the program...")
            sys.exit(0) #exit program altogther.    
        else:
             print("Invalid Input!") 
                
                
                
#_____________________________INITIATION_____________________________________________________________________________________            

regis_menu()





