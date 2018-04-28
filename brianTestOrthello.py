'''
Daniel
Brian Ramaswami
Nicholas Vitha


CPSC 427



'''
import copy
import random


def get_start_state(): # just useful for building the state
        x = [[' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ','w','b',' ',' ',' '],
             [' ',' ',' ','b','w',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ']]
        return x


class Othello_Board():
        board = [[]]
        whites = []
        blacks = []
        player_white = False
        player_black = False #
        white_moved = True
        black_moved = True

        def __init__(self, _board):
                self.board = copy.deepcopy(_board)
                self.whites = [(3,3),(4,4)]
                self.blacks = [(3,4),(4,3)]
                self.white_moved = True
                self.black_moved = True
                self.previous_board = copy.deepcopy(_board)

        def restore_state_previous(self):
                self.board = copy.deepcopy(previous_states[-1])
                del self.previous_states[-1]
                self.print_board


        def game_selection(self):
                gm = input("Do you want play a human or computer (h)uman/(c)omputer\n")
                if((gm.lower() == 'c') or (gm.lower() == 'computer')):
                        gm = 'c'
                        self.side_selection(gm);
                elif((gm.lower() == 'h') or (gm.lower() == 'human')):
                        gm = 'h'
                        self.side_selection(gm);



        def side_selection(self,gm):
                self.player_white = True

                choice = input("Do you want to be black? (do you want to go first?) (y)es/(n)o\n")
                if ((choice.lower() == "y") or (choice.lower() == "yes")):
                        self.player_white = False
                        print ("Player is playing black")
                        self.take_turn(gm)
                elif ((choice.lower() == "n") or (choice.lower() == "no")):
                        self.player_white = True
                        if(gm == 'c'):
                                print ("AI is playing black")
                        self.take_turn(gm)
                else:
                        print ("You have not selected yes or no.")
                        print ("Exiting program now.")
                        return

        def print_board(self):
                row = 0
                column = 0
                print (' ', end = ' ')
                for i in range(0,8):
                        print(str(i) , end = '   '),
                print ('')
                print('')
                for line in self.board:
                        print (str(row), end = ' ')
                        row += 1
                        column = 0
                        for char in line:
                                print(char, end = ' '),
                                column += 1
                                if column != 8:
                                    print('|', end= ' '),
                        if(row !=8):
                                print
                                print(' ');
                                print('_'*31)
                                print
                print('');
                print("White score = " + str(len(self.whites)))
                print("Black score = " + str(len(self.blacks)))



        def print_blacks(self):
                print(self.blacks)

        def print_whites(self):
                print(self.whites)

        def valid_moves_white(self):
                valid_moves = []
                for black_piece in self.blacks:
                        column = black_piece[1]
                        row = black_piece[0]

                        print(black_piece);

                        # Top
                        if(self.board[row-1][column] == ' ' and row > 0):
                                white_piece_in_way = False
                                for i in range(row,8):
                                        ##print('testing', 'row:', i, 'to 8');
                                        if self.board[i][column] == 'w':
                                                white_piece_in_way = True
                                               ## print(i,column);
                                                ##print(self.board[i][column]);
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row-1,column))
                        print('top: ', valid_moves);

                        # Left
                        if(self.board[row][column-1] == ' ' and column> 0):
                                white_piece_in_way = False
                                for i in range(column,8):
                                        if self.board[row][i] == 'w':
                                                white_piece_in_way = True
                                                break
                                        if self.board[row][i] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row,column-1))
                        print('left: ', valid_moves);
                        
                        # Below
                        if(self.board[row+1][column] == ' ' and row < 7):
                                white_piece_in_way = False
                                for i in range(row,0,-1):
                                        if self.board[i][column] == 'w':
                                                white_piece_in_way = True
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row+1,column))
                        print('Below: ', valid_moves);    

                        # Right
                        if(self.board[row][column+1] == ' ' and column < 7):
                                white_piece_in_way = False
                                for i in range(column,0,-1):
                                        if self.board[row][i] == 'w':
                                                white_piece_in_way = True
                                                break
                                        elif self.board[row][i] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row,column+1))

                        print('Right: ', valid_moves);

                        # Bottom Right
                        if(self.board[row+1][column+1] == ' ' and row < 7 and column< 7):
                                white_piece_in_way = False
                                if row > column:
                                        counter = 1
                                        for i in range(column, -1, -1):
                                                current_item = self.board[row-counter][i-1]
                                                print(current_item)
                                                if current_item == 'w':
                                                        print(row - counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, -1, -1):
                                                current_item = self.board[i-1][column-counter]
                                                print(current_item)
                                                if current_item == 'w':
                                                        print(row - counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row+1,column+1))

                        print('Bot Right: ', valid_moves);

                        # Top Left
                        if(self.board[row-1][column-1] == ' ' and row > 0 and column >0):
                                white_piece_in_way = False
                                if row < column:
                                        counter = 1
                                        for i in range(column, 8, 1):
                                                current_item = self.board[row+counter][i+1]
                                                if current_item == 'w':
                                                        print(row + counter, i + counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, 8, 1):
                                                current_item = self.board[i+1][column+counter]
                                                if current_item == 'w':
                                                        print(row + counter, i + counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row-1,column-1))
                        print('top left: ', valid_moves);

                        # Top Right
                        if(self.board[row-1][column+1] == ' ' and row> 0 and column < 7):
                                white_piece_in_way = False
                                if 8-row < column:
                                        counter = 1
                                        for i in range(row, 8, 1):
                                                current_item = self.board[i+1][column-counter]
                                                if current_item == 'w':
                                                        print(row_counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 0, -1):
                                                current_item = self.board[row+counter][i-1]
                                                if current_item == 'w':
                                                        print(row_counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row-1,column+1))

                        print('top right: ', valid_moves);

                        # Bottom Left
                        if(self.board[row+1][column-1] == ' ' and row < 7 and column > 0):
                                white_piece_in_way = False
                                if row < 8-column:
                                        counter = 1
                                        for i in range(row, 0, -1):
                                                current_item = self.board[i-1][column+counter]
                                                if current_item == 'w':
                                                        print(i - counter, column + counter)
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 8, 1):
                                                current_item = self.board[row-counter][i+1]
                                                if current_item == 'w':
                                                        print(i - counter, column + counter)
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row+1,column-1))
                        print('bottom left: ', valid_moves);

                print(valid_moves)
                i = 0;
                for move in valid_moves:
                        print(self.board[move[0]][move[1]])
                        if(self.board[move[0]][move[1]] != " "):
                                del valid_moves[i]
                        i += 1;

                print(valid_moves);
##                print(list(valid_moves));
##                print(list(set(valid_moves)))
                return list(set(valid_moves));

##        def valid_moves_white(self):
##                valid_moves = []
##                for black_piece in self.blacks:
##                        column = black_piece[1]
##                        row = black_piece[0]
##
##                        print(black_piece);
##
##                        # Top
##                        if(self.board[row-1][column] == ' '):
##                                white_piece_in_way = False
##                                for i in range(row,8):
##                                        ##print('testing', 'row:', i, 'to 8');
##                                        if self.board[i][column] == 'w':
##                                                white_piece_in_way = True
##                                               ## print(i,column);
##                                                ##print(self.board[i][column]);
##                                                break
##                                        if self.board[i][column] == ' ':
##                                                break
##                                if white_piece_in_way:
##                                        valid_moves.append((row-1,column))
##                        print('top: ', valid_moves);
##
##                        # Left
##                        if(self.board[row][column-1] == ' '):
##                                white_piece_in_way = False
##                                for i in range(column,8):
##                                        if self.board[row][i] == 'w':
##                                                white_piece_in_way = True
##                                                break
##                                        if self.board[row][i] == ' ':
##                                                break
##                                if white_piece_in_way:
##                                        valid_moves.append((row,column-1))
##                        print('left: ', valid_moves);
##                        
##                        # Below
##                        if(self.board[row+1][column] == ' '):
##                                white_piece_in_way = False
##                                for i in range(row,0,-1):
##                                        if self.board[i][column] == 'w':
##                                                white_piece_in_way = True
##                                                break
##                                        if self.board[i][column] == ' ':
##                                                break
##                                if white_piece_in_way:
##                                        valid_moves.append((row+1,column))
##                        print('Below: ', valid_moves);    
##
##                        # Right
##                        if(self.board[row][column+1] == ' '):
##                                white_piece_in_way = False
##                                for i in range(column,0,-1):
##                                        if self.board[row][i] == 'w':
##                                                white_piece_in_way = True
##                                                break
##                                        elif self.board[row][i] == ' ':
##                                                break
##                                if white_piece_in_way:
##                                        valid_moves.append((row,column+1))
##
##                        print('Right: ', valid_moves);
##
##                        # Bottom Right
##                        if(self.board[row+1][column+1] == ' '):
##                                white_piece_in_way = False
##                                if row > column:
##                                        counter = 1
##                                        for i in range(column, -1, -1):
##                                                current_item = self.board[row-counter][i-counter]
##                                                print(current_item)
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                else:
##                                        counter = 1
##                                        for i in range(row, -1, -1):
##                                                current_item = self.board[i-counter][column-counter]
##                                                print(current_item)
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                if white_piece_in_way:
##                                        valid_moves.append((row+1,column+1))
##
##                        print('Bot Right: ', valid_moves);
##
##                        # Top Left
##                        if(self.board[row-1][column-1] == ' '):
##                                black_piece_in_way = False
##                                if row < column:
##                                        counter = 1
##                                        for i in range(column, 8, 1):
##                                                current_item = self.board[row+counter][i+counter]
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                else:
##                                        counter = 1
##                                        for i in range(row, 8, 1):
##                                                current_item = self.board[i+counter][column+counter]
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                if white_piece_in_way:
##                                        valid_moves.append((row-1,column-1))
##                        print('top left: ', valid_moves);
##
##                        # Top Right
##                        if(self.board[row-1][column+1] == ' '):
##                                white_piece_in_way = False
##                                if 8-row < column:
##                                        counter = 1
##                                        for i in range(row, 8, 1):
##                                                current_item = self.board[i+counter][column-counter]
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                else:
##                                        counter = 1
##                                        for i in range(column, 0, -1):
##                                                current_item = self.board[row+counter][i-counter]
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                if white_piece_in_way:
##                                        valid_moves.append((row-1,column+1))
##
##                        print('top right: ', valid_moves);
##
##                        # Bottom Left
##                        if(self.board[row+1][column-1] == ' '):
##                                white_piece_in_way = False
##                                if row < 8-column:
##                                        counter = 1
##                                        for i in range(row, 0, -1):
##                                                current_item = self.board[i-counter][column+counter]
##                                                if current_item == 'w':
##                                                        white_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                else:
##                                        counter = 1
##                                        for i in range(column, 8, 1):
##                                                current_item = self.board[row-counter][i+counter]
##                                                if current_item == 'w':
##                                                        black_piece_in_way = True
##                                                        break
##                                                elif current_item == ' ':
##                                                        break
##                                                counter +=1
##
##                                if white_piece_in_way:
##                                        valid_moves.append((row+1,column-1))
##                        print('bottom left: ', valid_moves);
##
##                print(valid_moves)
##                i = 0;
##                for move in valid_moves:
##                        print(self.board[move[0]][move[1]])
##                        if(self.board[move[0]][move[1]] != " "):
##                                del valid_moves[i]
##                        i += 1;
##
##                print(valid_moves);
####                print(list(valid_moves));
####                print(list(set(valid_moves)))
##                return list(set(valid_moves));

        def valid_moves_black(self):
                valid_moves = []
                for white_piece in self.whites:
                        column = white_piece[1]
                        row = white_piece[0]

                        print(white_piece);

                        # Top
                        if(self.board[row-1][column] == ' ' and row > 0):
                                black_piece_in_way = False
                                for i in range(row,8):
                                        ##print('testing', 'row:', i, 'to 8');
                                        if self.board[i][column] == 'b':
                                                black_piece_in_way = True
                                               ## print(i,column);
                                                ##print(self.board[i][column]);
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row-1,column))
                        print('top: ', valid_moves);

                        # Left
                        if(self.board[row][column-1] == ' ' and column> 0):
                                black_piece_in_way = False
                                for i in range(column,8):
                                        if self.board[row][i] == 'b':
                                                black_piece_in_way = True
                                                break
                                        if self.board[row][i] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row,column-1))
                        print('left: ', valid_moves);
                        
                        # Below
                        if(self.board[row+1][column] == ' ' and row < 7):
                                black_piece_in_way = False
                                for i in range(row,0,-1):
                                        if self.board[i][column] == 'b':
                                                black_piece_in_way = True
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row+1,column))
                        print('Below: ', valid_moves);    

                        # Right
                        if(self.board[row][column+1] == ' ' and column < 7):
                                black_piece_in_way = False
                                for i in range(column,0,-1):
                                        if self.board[row][i] == 'b':
                                                black_piece_in_way = True
                                                break
                                        elif self.board[row][i] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row,column+1))

                        print('Right: ', valid_moves);

                        # Bottom Right
                        if(self.board[row+1][column+1] == ' ' and row < 7 and column< 7):
                                black_piece_in_way = False
                                if row > column:
                                        counter = 1
                                        for i in range(column, -1, -1):
                                                current_item = self.board[row-counter][i-counter]
                                                print(current_item)
                                                if current_item == 'b':
                                                        print(row-counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, -1, -1):
                                                current_item = self.board[i-counter][column-counter]
                                                print(current_item)
                                                if current_item == 'b':
                                                        print(row-counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row+1,column+1))

                        print('Bot Right: ', valid_moves);

                        # Top Left
                        if(self.board[row-1][column-1] == ' ' and row > 0 and column >0):
                                black_piece_in_way = False
                                if row < column:
                                        counter = 1
                                        for i in range(column, 8, 1):
                                                current_item = self.board[row+counter][i+counter]
                                                if current_item == 'b':
                                                        print(i + counter, column + counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, 8, 1):
                                                current_item = self.board[i+counter][column+counter]
                                                if current_item == 'b':
                                                        print(i + counter, column + counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row-1,column-1))
                        print('top left: ', valid_moves);

                        # Top Right
                        if(self.board[row-1][column+1] == ' ' and row> 0 and column < 7):
                                black_piece_in_way = False
                                if 8-row < column:
                                        counter = 1
                                        for i in range(row, 8, 1):
                                                current_item = self.board[i+counter][column-counter]
                                                if current_item == 'b':
                                                        print(row+counter, i - counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 0, -1):
                                                current_item = self.board[row+counter][i-counter]
                                                if current_item == 'b':
                                                        print(row+counter, i - counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row-1,column+1))

                        print('top right: ', valid_moves);

                        # Bottom Left
                        if(self.board[row+1][column-1] == ' ' and row < 7 and column > 0):
                                black_piece_in_way = False
                                if row < 8-column:
                                        counter = 1
                                        for i in range(row, 0, -1):
                                                current_item = self.board[i-1][column+counter]
                                                if current_item == 'b':
                                                        print(i-counter,column+counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 8, 1):
                                                current_item = self.board[row-counter][i+1]
                                                if current_item == 'b':
                                                        print(i-counter,column+counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row+1,column-1))
                        print('bottom left: ', valid_moves);

                print(valid_moves)
                i = 0;
                for move in valid_moves:
                        print(self.board[move[0]][move[1]])
                        if(self.board[move[0]][move[1]] != " "):
                                del valid_moves[i]
                        i += 1;

                print(valid_moves);
##                print(list(valid_moves));
##                print(list(set(valid_moves)))
                return list(set(valid_moves));



        def up_left(self,color,coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.up_left(color, (row-1,column-1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0


        def up(self,color,coords): # recursively search upwards
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0                  

                        color_found, number = self.up(color, (row-1,column))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0


        def up_right(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0                  

                        color_found, number = self.up_right(color, (row-1,column+1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0




        def left(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.left(color, (row,column-1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0



        def right(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.right(color, (row,column+1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0

        def bot_left(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.bot_left(color, (row+1,column-1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0
        def bot(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.bot(color, (row+1,column))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0

        def bot_right(self, color, coords):
                row = coords[0]
                column = coords[1]
                
                if row == 0 or column == 0:
                        if self.board[row][column] == ' ':
                                return False, 0
                        elif self.board[row][column] == color:
                                return True, 0
                        else:
                                return False, 0
                else:
                        if self.board[row][column] == ' ':
                                return False, 0
                        if self.board[row][column] == color:
                                return True, 0          

                        color_found, number = self.bot_right(color, (row+1,column+1))
                        if color_found:
                                self.board[row][column] = copy.deepcopy(color)
                                return True, number+1
                        else:
                                return False, 0



        def take_turn(self,gm):
                round = 1
                while (self.white_moved or self.black_moved):
                        print('ROUND : ', round, '\n');
                        self.black_moved = self.black_turn(gm)
                        print('\n''TURN CHANGE!','\n')
                        self.white_moved = self.white_turn(gm)
                        #self.print_board()
                        print('\n' 'white moved = ', self.white_moved, '  ', 'black moved = ', self.black_moved, '\n');
                        round = round + 1;
                return;

        def white_turn(self, gm):
        #print(self.player_white)
        #if self.player_white:
                counter = 1
                print("Valid white moves are: (row,column)")
                valid_moves = self.valid_moves_white()
                if len(valid_moves) == 0:
                         return False

                for move in valid_moves:
                        row = move[0];
                        col = move[1];
                        ## adding * to the board to represent possible moves
                        self.board[row][col] = "*";
                        print( str(counter) + '. '),
                        print( move)
                        counter +=1
                self.print_board();


                if(gm == 'h'):
                        #INPUT MOVE HERE
                        choiceI = int(input("Enter your choice: "));
                        choice = choiceI -1;
                        choiceT = valid_moves[choice] 
                        #clean up board before showing potential moves
                        for move in valid_moves:
                                row = move[0];
                                col = move[1];
                                self.board[row][col] = " ";
                        #self.print_board();
                        self.effect_turn('w', choiceT);  ##check to see potential results
                        print(self.whites);
                        
                        correct = input("You have chosen: " + str(valid_moves[choice]) + "\nCorrect? (y)es/(n)o\n")
                        if(correct == 'n'):
                                print(self.blacks);
                                self.board = self.previous_board;
                                print(self.blacks);
                                ###change score back !!!!
                                self.white_turn(gm);
                        else:              
                                choice = valid_moves[choice]
                                self.effect_turn('w', choice);  ##check to see potential results
                                return True


                elif(gm == 'c'):
                        choice = random.choice(valid_moves)
                        print("Whites's move is: "),
                        print(choice)
                        self.effect_turn('w',choice)
                        return True


        def black_turn(self,gm):
        #print(not self.player_white)
        #if not self.player_white:
                counter = 1
                print("Valid black moves are: (row,column)")
                valid_moves = self.valid_moves_black()
                if len(valid_moves) == 0:
                         return False

                for move in valid_moves:
                        row = move[0];
                        col = move[1];
                        ## adding * to the board to represent possible moves
                        self.board[row][col] = "*";
                        print( str(counter) + '. '),
                        print( move)
                        counter +=1
                self.print_board();
                
                if(gm == 'h'):
                        #INPUT MOVE HERE
                        choiceI = int(input("Enter your choice: "));
                        choice = choiceI -1;
                        choiceT = valid_moves[choice] 
                        

                        #clean up board before showing potential moves
                        for move in valid_moves:
                                row = move[0];
                                col = move[1];
                                self.board[row][col] = " ";
                        #self.print_board();
                        self.effect_turn('b', choiceT);  ##check to see potential results
                        print(self.blacks);
                        
                        correct = input("You have chosen: " + str(valid_moves[choice]) + "\nCorrect? (y)es/(n)o\n")
                        if(correct == 'n'):
                                print(self.blacks);
                                self.board = self.previous_board;
                                print(self.blacks);
                                ###change score back !!!!
                                self.black_turn(gm);
                        else:
                                # MIGHT NOT NEED THIS MIGHT NEED ONLY RETURN. ALREADY CHECKED THIS CASE
                               # choice = valid_moves[choice] 
                               # self.effect_turn('b', choice);  ##check to see potential results
                                return True


                elif(gm == 'c'):
                        choice = random.choice(valid_moves)
                        print("Blacks's move is: "),
                        print(choice)
                        self.effect_turn('b',choice)
                        return True



                
        def find_pieces(self):
                black_pieces = []
                white_pieces = []
                row = 0
                col = 0
                for y in self.board:
                        for x in y:
                                if x == 'w':
                                        white_pieces.append((row,col))
                                elif x == 'b':
                                        black_pieces.append((row,col))
                                col +=1
                        col = 0
                        row +=1
                return black_pieces, white_pieces

        def effect_turn(self, color, coords):
                row = coords[0]
                column = coords[1]


                self.board[row][column] = color
                total_changed = tl_changed = top_changed = tr_changed = left_changed = right_changed = bl_changed = bot_changed = br_changed = 0;
                
                if row > 0:
                        if column > 0:
                                tl,tl_changed = self.up_left(color,(row-1,column-1))
                        if column < 7:
                                tr,tr_changed = self.up_right(color, (row-1,column+1))                          
                        top,top_changed = self.up(color, (row-1,column))
                if column > 0:
                        left,left_changed = self.left(color, (row,column-1))
                if column < 7:
                        right,right_changed = self.right(color, (row,column+1))
                if row < 7:
                        if column > 0:
                                bl,bl_changed = self.bot_left(color, (row+1,column-1))
                        if column < 7:
                                br,br_changed = self.bot_right(color,(row+1,column+1))
                        bot,bot_changed = self.bot(color, (row+1,column))
                total_changed = tl_changed + top_changed + tr_changed + left_changed + right_changed + bl_changed + bot_changed + br_changed
                
                print("total changed: " + str(total_changed))

                self.blacks, self.whites = self.find_pieces()
                self.print_board()



def main():
        board = Othello_Board(get_start_state())
        board.print_board()
        board.game_selection()



if __name__ == '__main__':
        main()


