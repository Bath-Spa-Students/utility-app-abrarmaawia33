# Using function to print colored text 
def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'bold': '\033[1m',
        'end': '\033[0m'
    } 
    return f"{colors[color]}{text}{colors['end']}"
#Using function to print welcome massage 
def print_welcome():
    welcome = r"""
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║      
    ║  █   █  █████  █      ████   ███   █   █  █████    ║  
    ║  █   █  █      █     █      █   █  ██ ██  █        ║ 
    ║  █ █ █  █████  █     █      █   █  █ █ █  █████    ║ 
    ║  █ █ █  █      █     █      █   █  █   █  █        ║
    ║   █ █   █████  █████  ████   ███   █   █  █████    ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """
# printing other welcome massage 
    welcome_text = """┌─────────── •✧✧• ───────────┐
  My Vending Machine cafe <3
└─────────── •✧✧• ───────────┘
    \n"""
# Printing the two welcome message's with colors     
    print(print_colored(welcome_text, 'blue'))
    print(print_colored(welcome, 'yellow'))

# Display the welcome massage 
print_welcome()

# Vending machine menu dictionary
my_vending_machine_menu = {             
        'Drinks': [ 
                {'code': 'A1' , 'name':'☕ Coffee    ','price': 13.5 ,'stock': 12},
                {'code': 'A2' , 'name':'☕ Cappuccino','price':23.1,'stock':  7},
                {'code': 'A3' , 'name':'☕ Espresso  ','price':     2.55   ,'stock': 6},
                {'code': 'A4' , 'name':'💧 Water     ','price': 2.89 ,'stock': 5},
                {'code': 'A5' , 'name':'🍵 Mocha     ','price': 20.3 ,'stock': 18},
                {'code': 'A6' , 'name':'☕ latte     ','price': 18.5 ,'stock': 5 },
                {'code': 'A7' , 'name':'🧋 Milkshake  ','price': 30.00,'stock': 6},
                {'code': 'A8' , 'name':'🥤 Soda      ','price': 18.5 ,'stock': 5 },
        ],
        'Snacks': [
                {'code': 'B1' , 'name':'🍫 Chocolate chips','price': 25.6 ,'stock': 10},
                {'code': 'B2' , 'name':'🍪 Cookies        ','price': 20.5 ,'stock': 6 },
                {'code': 'B3' , 'name':'🧁 Cupcakes       ','price': 7.99 ,'stock':  5 },
                {'code': 'B4' , 'name':'🍓 strawberry cake','price': 11.7 ,'stock':7},
                {'code': 'B5' , 'name':'🍰 cheesecake     ','price': 16.9  ,'stock': 6},
                {'code': 'B6' , 'name':'🥞 Pancakes       ','price': 33.8 ,'stock': 8},
                {'code': 'B7' , 'name':'🍏 Apple pie      ','price': 26.2 ,'stock': 9},
        ],              
}

# using function to display "the vending machine menu" with colored highlighting 
def display_menu():
    print(print_colored("\n=== The Vending Machine Menu ===", 'purple'))
    for category, items in my_vending_machine_menu.items():
        print(print_colored(f"\n{category}:", 'cyan'))
        for item in items:
            menu_item = f"  {item['code']} - {item['name']} | Price: ${item['price']} | Stock: {item['stock']}"
            if item['stock'] == 0:  # highlighting 'out-of-stock' items in (red) and 'low-stock' items in (yellow)
                print(print_colored(menu_item, 'red'))
            elif item['stock'] < 5:
                print(print_colored(menu_item, 'yellow'))
            else:
                print(menu_item)
 

# Using Function to get input from the user for item selection  
def get_user_input():
    return input(print_colored("Enter the code of the item you want or type exit to end ➤ : ", 'green'))

# using function to process a user's purchase based on the selected item and amount intserted 
def make_purchase(item_code, amount_inserted):
    for category, items in my_vending_machine_menu.items():
        for item in items:
            if item['code'] == item_code:
                if item['stock'] > 0 and amount_inserted >= item['price']: 
                    item['stock'] -= 1  # decreaseing the item stock and calculate the change if it's necessary 
                    change = amount_inserted - item['price']
                    if change > 0:
                        print(print_colored(f"\nDispensing {item['name']}. Your change is ${change:.2f}.", 'yellow'))
                    else:
                        print(print_colored(f"\nDispensing {item['name']}. Enjoy your {item['name']}, thank you <3", 'purple'))
                else:  # displaying a message if the item is out of stock or no enough money insserted 
                    print(print_colored("\nSorry, the item is out of stock or you haven't inserted enough money.", 'red'))
                return

# using function to handle user input for money insertion 
def handle_money():
    try:
        amount_inserted = float(input(print_colored("Insert money: $", 'green')))
        return amount_inserted
    except ValueError:   # prompt the user for a valid amount if an invalid input is provided 
        print(print_colored("Invalid amount:( . Please enter a valid amount.", 'red'))
        return handle_money()

# printing the main vending machine simulation function 
def vending_machine():
    print_colored("\nWelcome to My Vending Machine!", 'bold')

    while True:  # displaying the vending machine menu and get user input for item selection 
        display_menu()
        item_code = get_user_input()
        # using 'exit' to end the program 
        if item_code.lower() == 'exit':
            print(print_colored(""" _____ _                 _                          _                         
|_   _| |__   __ _ _ __ | | __  _   _  ___  _   _  | |                        
  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | |                        
  | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |_|                        
 _|_|_|_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| (_)                      _ 
| ____|_ __  (_) ___  _   _   _ |___/___  _   _ _ __   _ __ ___   ___  __ _| |
|  _| | '_ \ | |/ _ \| | | | | | | |/ _ \| | | | '__| | '_ ` _ \ / _ \/ _` | |
| |___| | | || | (_) | |_| | | |_| | (_) | |_| | |    | | | | | |  __/ (_| | |
|_____|_| |_|/ |\___/ \__, |  \__, |\___/ \__,_|_|    |_| |_| |_|\___|\__,_|_|
           |__/       |___/   |___/                                           """, 'purple'))
            break
        # checking if the entered item code is valid 
        if any(item_code == item['code'] for items in my_vending_machine_menu.values() for item in items):
            # get user input for money insertion and process the purchase 
            amount_inserted = handle_money()
            make_purchase(item_code, amount_inserted)
        else: # displaying an error message for an invalid item code 
            print(print_colored("Invalid code:( . Please enter a valid code from the menu.", 'red'))

# run the whole vending machine simulation 
vending_machine()


# print 'emoji'
emoji=""" 
                      █████████
  ███████          ███▒▒▒▒▒▒▒▒▒███
  █▒▒▒▒▒▒█       ███▒▒▒▒▒▒▒▒▒▒▒▒▒███
   █▒▒▒▒▒▒█    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    █▒▒▒▒▒█   ██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
     █▒▒▒█   █▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
   █████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
   █▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
 ██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
 █▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
 ██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
  ████████████   █████████████████ """

print(print_colored(emoji,'green'))

