import random as r

MAX_LINES = 3 # maximum number of lines which is a constant 
MAX_BET = 100
MIN_BET = 1

ROW = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(col, lines, bet, value):
    winnings = 0
    win_line = []
    for line in range(lines):
        symbol = col[0][line]
        for c in col:
            sym_check = c[line]
            if symbol != sym_check:
                break
        else:
            winnings += value[symbol] * bet
            win_line.append(line + 1)
    return winnings, win_line


def get_slot_machine_spin(rows, cols, symbols):
    symbol_list = []

    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            symbol_list.append(symbol)

    columns = []

    for _ in range(0, cols):
        column = []
        for _ in range(rows):
            value = r.choice(symbol_list)
            column.append(value)
            del symbol_list[symbol_list.index(value)]
        columns.append(column)
    
    return columns



# Get a Deposit
def deposit():
    while True:
        amount = input("Please enter your Deposit? $: ")
        if amount.isdigit(): # also check if its a negative amount
            if int(amount) > 0:
                return int(amount) 
            else:
                print("Amount must be greater than zero. ")
        else:
            print("Please enter a valid Number. ")

# Get a Number of Lines
def get_number_of_lines():
    while True:
        lines = input(f"Please enter the number of Lines [1 - {MAX_LINES}]? : ")
        if lines.isdigit(): # also check if its a negative amount
            if 1 <= int(lines) <= MAX_LINES:
                return int(lines) 
            else:
                print("Lines must be greater than 0. ")
        else:
            print("Please enter a valid Number of Lines. ")

def print_slot_machine(columns):
    for i in range(len(columns)):
        for j in range(len(columns)):
           print(columns[j][i], end=" | ")
        print()

# Get a Bet
def get_bet(balance, lines):
    while True:
        bet = input(f"Please enter your Bet for each Line [${MIN_BET} - ${MAX_BET}]? : ")
        if bet.isdigit(): # also check if its a negative amount
            if MIN_BET <= int(bet) <= MAX_BET and int(bet) * lines <= MAX_BET:
                return int(bet) 
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET} and Below your Balance which is: ${balance}. ")
        else:
            print("Please enter a valid Amount. ")

def main():
    balance = deposit()
   

    while balance > 0:
        lines = get_number_of_lines()
        bet = get_bet(balance, lines)
        total_bet = bet * lines
        balance -= total_bet

        print(f"Your are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
        print(f"Your Balance is now: ${balance}")

        columns = get_slot_machine_spin(ROW,COLS, symbol_count)
        
        print_slot_machine(columns)
       
        result, win_line = check_winnings(columns, lines, bet, symbol_value)

        if result > 0:
            print(f"You Have Won ${result}")
            print("You Won on: line ", *win_line)
            balance += result
            print("You Won on new Balance ", balance)
        else:
            print(f"You Have Lost! ${total_bet}: Balance is now: ${balance}")
        
        # Repeat 
        if input("You wanna play again: [y/n] ").lower() == "y":
            if balance > 0:
                continue
            else:
                if input("Balance is Zero Start over with a new Deposit:  [y/n] ").lower() == "y":
                    balance = deposit()
                else:
                    break      
        else:
            break


if __name__ == '__main__':
    main()