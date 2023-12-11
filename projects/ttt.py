def show(board_state):
    print(f"{board_state[0]}|{board_state[1]}|{board_state[2]}")
    print(f"{board_state[3]}|{board_state[4]}|{board_state[5]}")
    print(f"{board_state[6]}|{board_state[7]}|{board_state[8]}")
 
def space_owner(board_state, row_number, column_number):
    return board_state[row_number * 3 + column_number]
 
def set_space_owner(board_state, row_number, column_number, owner):
    board_state[row_number * 3 + column_number] = owner
 
def row_owner(board_state, row_number):
    x_count = 0
    o_count = 0
    for column_number in range(3):
        owner  = space_owner(board_state, row_number, column_number)
        if owner == 'x':
            x_count += 1
        elif owner == 'o':
            o_count += 1
    if x_count == 3:
        return 'x'
    if o_count == 3:
        return 'o'
    else:
        return ' '
 
def column_owner(board_state, col_number):
    x_count = 0
    o_count = 0
    for row_number in range(3):
        owner  = space_owner(board_state, row_number, col_number)
        if owner == 'x':
            x_count += 1
        elif owner == 'o':
            o_count += 1
    if x_count == 3:
        return 'x'
    if o_count == 3:
        return 'o'
    else:
        return ' '
 
def diagonal_owner(board_state, diagonal_number):
    x_count = 0
    o_count = 0
    if diagonal_number == 0:
        for i in range(3):
            owner = space_owner(board_state, i, i)
            if owner == 'x':
                x_count += 1
            elif owner == 'o':
                o_count+= 1
    else:
        for i in range(3):
            owner = space_owner(board_state, i, 2 - i)
            if owner == 'x':
                x_count += 1
            elif owner == 'o':
                o_count+= 1
    if x_count == 3:
        return 'x'
    if o_count == 3:
        return 'o'
    else:
        return ' '
 
def utility(board_state):
    #return 100 if x wins,
    #-1000 if o wins,
    #0 if its a draw,
    #None if the game isn't over
    for row_number in range(3):
        owner = row_owner(board_state, row_number)
        if owner == 'x':
            return 10
        elif owner == 'o':
            return -10
    for column_number in range(3):
        owner = column_owner(board_state, column_number)
        if owner == 'x':
            return 10
        elif owner == 'o':
            return -10
    for diagonal_number in range(2):
        owner = diagonal_owner(board_state, diagonal_number)
        if owner == 'x':
            return 10
        elif owner == 'o':
            return -10
    #No one has won
    #is it a draw or is the game still going
    if ' ' in board_state:
        return None
    else:
        return 0
 
def take_player_turn(board_state, player_symbol):
    print(f"{player_symbol}'s turn:")
    while True:
        player_input = input("enter row,col: ")
        split_player_input = player_input.split(",")
        if len(split_player_input) != 2:
            print("Invalid move, try again.")
            continue
        row_number = int(split_player_input[0])
        column_number = int(split_player_input[1])
        if row_number > -1 and row_number < 3 and \
        column_number > -1 and column_number < 3 and \
        space_owner(board_state, row_number, column_number) == ' ':
            break
        else:
            print("Invalid move, try again.")
    print(f"{player_symbol} takes {row_number},{column_number}")
    set_space_owner(board_state, row_number, column_number, player_symbol)
    show(board_state)


def minimax_min(board_state):
    best_utility = utility(board_state)
    if best_utility != None:
        return [best_utility]
    best_row = None
    best_col = None
    for row_number in range(3):
        for col_number in range(3):
            if space_owner(board_state, row_number, col_number) == ' ':
                new_board_state = board_state[:]
                set_space_owner(new_board_state, row_number, col_number, 'o')
                minimax_result = minimax_max(new_board_state)
                new_board_state_utility = minimax_result[0]
                # new_board_state_utility = minimax_max(new_board_state)[0]
                if best_utility == None or new_board_state_utility < best_utility:
                    best_utility = new_board_state_utility
                    best_row = row_number
                    best_col = col_number
    return [best_utility, best_row, best_col]
    

def minimax_max(board_state):
    best_utility = utility(board_state)
    if best_utility != None:
        return [best_utility]
    best_row = None
    best_col = None
    for row_number in range(3):
        for col_number in range(3):
            if space_owner(board_state, row_number, col_number) == ' ':
                new_board_state = board_state[:]
                set_space_owner(new_board_state, row_number, col_number, 'x')
                new_board_state_utility = minimax_min(new_board_state)[0]
                if best_utility == None or new_board_state_utility > best_utility:
                    best_utility = new_board_state_utility
                    best_row = row_number
                    best_col = col_number
    return [best_utility, best_row, best_col]

def take_cpu_turn(board_state, cpu_symbol):
    print(f"{cpu_symbol}'s turn:")
    if cpu_symbol == 'x':
        minimax_result = minimax_max(board_state)
    else:
        minimax_result = minimax_min(board_state)
    print(f"{cpu_symbol} takes {minimax_result[1]},{minimax_result[2]}")
    set_space_owner(board_state, minimax_result[1], minimax_result[2], cpu_symbol)
    show(board_state)

bs = [' '] * 9
print("Welcome to Tic-Tac-Toe")
player_symbol = None
while player_symbol != 'x' and player_symbol != 'o':
    player_symbol = input("x/o?: ")
show(bs)
while True:
    if player_symbol == 'x':
        take_player_turn(bs, 'x')
        if utility(bs) != None:
            break
        take_cpu_turn(bs, 'o')
        if utility(bs) != None:
            break
    else:
        take_cpu_turn(bs, 'x')
        if utility(bs) != None:
            break
        take_player_turn(bs, 'o')
        if utility(bs) != None:
            break
print(f"utility: {utility(bs)}")
