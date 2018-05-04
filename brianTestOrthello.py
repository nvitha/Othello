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
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ']]
        return x


class Othello_Board():
        board = [[]]
        whites = []
        blacks = []
        prev_whites = []
        prev_blacks = []
        player_white = False
        player_black = False #
        white_moved = True
        black_moved = True

        def __init__(self, _board):
                self.board = copy.deepcopy(_board)
                self.previous_board = copy.deepcopy(_board)
                self.whites = [(3,3),(4,4)]
                self.blacks = [(3,4),(4,3)]
##                self.whites = [(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (1, 4), (1, 5), (1, 6), (2, 0), (2, 4), (2, 5), (3, 0), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 0), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 0), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)];
##                self.blacks = [(0, 3), (1, 1), (1, 2), (1, 3), (1, 7), (2, 1), (2, 2), (2, 3), (2, 6), (2, 7), (3, 1), (3, 2), (4, 1), (4, 4), (5, 1), (7, 1)];
                self.white_moved = True
                self.black_moved = True

                
        def restore_state_previous(self):
                self.board = copy.deepcopy(previous_states[-1])
                del self.previous_states[-1]
                self.print_board

        def restart_board(self):
                self.board = [[' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' '],
                              [' ',' ',' ',' ',' ',' ',' ',' ']]


        def game_selection(self):
                b = input("Do you want  black to be a human or computer (h)uman/(c)omputer\n")
                if((b.lower() == 'c') or (b.lower() == 'computer')):
                        b = 'c'
                elif((b.lower() == 'h') or (b.lower() == 'human')):
                        b = 'h'

                w = input("Do you want  white to be a human or computer (h)uman/(c)omputer\n")
                if((w.lower() == 'c') or (w.lower() == 'computer')):
                        w = 'c'
                elif((w.lower() == 'h') or (w.lower() == 'human')):
                        w = 'h'

                self.side_selection(b,w);



        def side_selection(self,b, w):
                if(b == 'c' and w == 'c'):
                        choice = "NA"
                        self.take_turn(b,w,choice);
                        return
                elif(b == 'h' and w == 'h'):
                        choice = input("Do you want to be black? (do you want to go first?) (y)es/(n)o\n")
                        if ((choice.lower() == "y") or (choice.lower() == "yes")):
                                print ("Player is playing black")
                                self.take_turn(b,w,choice)
                        elif ((choice.lower() == "n") or (choice.lower() == "no")):
                                print ("You are playing White")
                                self.take_turn(b,w,choice);
                        
                else:
                        choice = input("Do you want to be black? (do you want to go first?) (y)es/(n)o\n")
                        if ((choice.lower() == "y") or (choice.lower() == "yes")):
                                print ("Player is playing black")
                                self.take_turn(b,w,choice);
                        elif ((choice.lower() == "n") or (choice.lower() == "no")):
                                print ("You are playing White")
                                self.take_turn(b,w,choice);
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

###                        print(black_piece);

                        # Top
                        if(row > 0 and self.board[row-1][column] == ' '):
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
###                       print('top: ', valid_moves);

                        # Left
                        if(column> 0 and self.board[row][column-1] == ' '):
                                white_piece_in_way = False
                                for i in range(column,8):
                                        if self.board[row][i] == 'w':
                                                white_piece_in_way = True
                                                break
                                        if self.board[row][i] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row,column-1))
###                        print('left: ', valid_moves);
                        
                        # Below
                        if(row < 7 and self.board[row+1][column] == ' '):
                                white_piece_in_way = False
                                for i in range(row,-1,-1):
                                        if self.board[i][column] == 'w':
                                                white_piece_in_way = True
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row+1,column))
###                        print('Below: ', valid_moves);    

                        # Right
                        if(column < 7 and self.board[row][column+1] == ' '):
                                white_piece_in_way = False
                                for i in range(column,-1,-1):
                                        if self.board[row][i] == 'w':
                                                white_piece_in_way = True
                                                break
                                        elif self.board[row][i] == ' ':
                                                break
                                if white_piece_in_way:
                                        valid_moves.append((row,column+1))

###                        print('Right: ', valid_moves);

                        # Bottom Right
                        if(row < 7 and column< 7 and self.board[row+1][column+1] == ' '):
                                white_piece_in_way = False
                                if row > column:
                                        counter = 1
                                        for i in range(column, -1, -1):
                                                current_item = self.board[row-counter][i-1]
 ###                                               print(current_item)
                                                if current_item == 'w':
###                                                        print(row - counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, -1, -1):
                                                current_item = self.board[i-1][column-counter]
###                                                print(current_item)
                                                if current_item == 'w':
###                                                        print(row - counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row+1,column+1))

###                        print('Bot Right: ', valid_moves);

                        # Top Left
                        if(row > 0 and column >0  and self.board[row-1][column-1] == ' '):
                                white_piece_in_way = False
                                if row < column:
                                        counter = 1
                                        for i in range(column, 7, 1):
                                                current_item = self.board[row+counter][i+1]
                                                if current_item == 'w':
 ###                                                       print(row + counter, i + counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, 7, 1):
                                                current_item = self.board[i+1][column+counter]
                                                if current_item == 'w':
###                                                        print(row + counter, i + counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row-1,column-1))
###                        print('top left: ', valid_moves);

                        # Top Right
                        if((row> 0 and column < 7) and (self.board[row-1][column+1] == ' ')):
                                white_piece_in_way = False
                                if 8-row <= column:
                                        counter = 1
                                        for i in range(row, 7, 1):
                                                current_item = self.board[i+1][column-counter]
                                                if current_item == 'w':
###                                                        print(row+counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 0, -1):
                                                current_item = self.board[row+counter][i-counter] #changed from i -1
                                                if current_item == 'w':
 ###                                                       print(row+counter, i - counter);
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row-1,column+1))

###                        print('top right: ', valid_moves);

                        # Bottom Left
                        if(row < 7 and column > 0 and self.board[row+1][column-1] == ' '):
                                white_piece_in_way = False
                                if row < 8-column:
                                        counter = 1
                                        for i in range(row, 0, -1):
                                                current_item = self.board[i-1][column+counter]
                                                if current_item == 'w':
###                                                        print(i - counter, column + counter)
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 7, 1):
                                                current_item = self.board[row-counter][i+1]
                                                if current_item == 'w':
###                                                        print(i - counter, column + counter)
                                                        white_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if white_piece_in_way:
                                        valid_moves.append((row+1,column-1))
###                        print('bottom left: ', valid_moves);

###                print(valid_moves)
                i = 0;
                for move in valid_moves:
###                        print(self.board[move[0]][move[1]])
                        if(self.board[move[0]][move[1]] != " "):
                                del valid_moves[i]
                        i += 1;

                print(valid_moves);
##                print(list(valid_moves));
##                print(list(set(valid_moves)))
                return list(set(valid_moves));



        def valid_moves_black(self):
                valid_moves = []
                for white_piece in self.whites:
                        column = white_piece[1]
                        row = white_piece[0]

###                        print(white_piece);

                        # Top
                        if(row > 0 and self.board[row-1][column] == ' '):
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
 ###                       print('top: ', valid_moves);

                        # Left
                        if(column> 0 and self.board[row][column-1] == ' '):
                                black_piece_in_way = False
                                for i in range(column,8):
                                        if self.board[row][i] == 'b':
                                                black_piece_in_way = True
                                                break
                                        if self.board[row][i] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row,column-1))
###                        print('left: ', valid_moves);
                        
                        # Below
                        if(row < 7 and self.board[row+1][column] == ' '):
                                black_piece_in_way = False
                                for i in range(row,-1,-1):
                                        if self.board[i][column] == 'b':
                                                black_piece_in_way = True
                                                break
                                        if self.board[i][column] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row+1,column))
###                        print('Below: ', valid_moves);    

                        # Right
                        if(column < 7 and self.board[row][column+1] == ' '):
                                black_piece_in_way = False
                                for i in range(column,-1,-1):
                                        if self.board[row][i] == 'b':
                                                black_piece_in_way = True
                                                break
                                        elif self.board[row][i] == ' ':
                                                break
                                if black_piece_in_way:
                                        valid_moves.append((row,column+1))

###                        print('Right: ', valid_moves);

                        # Bottom Right
                        if(row < 7 and column< 7 and self.board[row+1][column+1] == ' '):
                                black_piece_in_way = False
                                if row > column:
                                        counter = 1
                                        for i in range(column, -1, -1):
                                                current_item = self.board[row-counter][i-1]
###                                                print(current_item)
                                                if current_item == 'b':
###                                                        print(row - counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, -1, -1):
                                                current_item = self.board[i-1][column-counter]
 ###                                               print(current_item)
                                                if current_item == 'b':
 ###                                                       print(row - counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row+1,column+1))

    ###                    print('Bot Right: ', valid_moves);

                        # Top Left
                        if(row > 0 and column >0  and self.board[row-1][column-1] == ' '):
                                black_piece_in_way = False
                                if row < column:
                                        counter = 1
                                        for i in range(column, 7, 1):
                                                current_item = self.board[row+counter][i+1]
                                                if current_item == 'b':
###                                                        print(row + counter, i + counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(row, 7, 1):
                                                current_item = self.board[i+1][column+counter]
                                                if current_item == 'b':
###                                                        print(row + counter, i + counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row-1,column-1))
###                        print('top left: ', valid_moves);

                        # Top Right
                        if(row> 0 and column < 7 and self.board[row-1][column+1] == ' '):
                                black_piece_in_way = False
                                if 8-row <= column:  #changed from (<)
                                        counter = 1
                                        for i in range(row, 7, 1):
                                                current_item = self.board[i+1][column-counter]
                                                if current_item == 'b':
 ###                                                       print(row+counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 0, -1):
                                                current_item = self.board[row+counter][i-counter] #changed from (i-1)
                                                if current_item == 'b':
  ###                                                      print(row+counter, i - counter);
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row-1,column+1))

 ###                       print('top right: ', valid_moves);

                        # Bottom Left
                        if(row < 7 and column > 0 and self.board[row+1][column-1] == ' '):
                                black_piece_in_way = False
                                if row < 8-column:
                                        counter = 1
                                        for i in range(row, 0, -1):
                                                current_item = self.board[i-1][column+counter]
                                                if current_item == 'b':
    ###                                                    print(i - counter, column + counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                else:
                                        counter = 1
                                        for i in range(column, 7, 1):
                                                current_item = self.board[row-counter][i+1]
                                                if current_item == 'b':
 ###                                                       print(i - counter, column + counter)
                                                        black_piece_in_way = True
                                                        break
                                                elif current_item == ' ' or current_item == '*':
                                                        break
                                                counter +=1

                                if black_piece_in_way:
                                        valid_moves.append((row+1,column-1))
    ###                    print('bottom left: ', valid_moves);

       ###         print(valid_moves)
                i = 0;
                for move in valid_moves:
          ###              print(self.board[move[0]][move[1]])
                        if(self.board[move[0]][move[1]] != " "):
                                del valid_moves[i]
                        i += 1;

          ###      print(valid_moves);
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
                
                if row == 0:
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
                
                if row == 0 or column == 7:
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
                
                if column == 0:
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
                
                if  column == 7:
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
                
                if row == 7 or column == 0:
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
                
                if row == 7:
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
                
                if row == 7 or column == 7:
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



        def take_turn(self,b,w,choice):
                round = 1
                if(b == 'c' and w == 'c'):
                        while (self.white_moved or self.black_moved):
                                print('ROUND : ', round, '\n');
                                self.black_moved = self.black_turn('c')
                                print('\n''TURN CHANGE!','\n')
                                self.white_moved = self.white_turn('c')
                                #self.print_board()
                                print('\n' 'white moved = ', self.white_moved, '  ', 'black moved = ', self.black_moved, '\n');
                                round = round + 1;
                                if(self.white_moved == False and self.black_moved == False):
                                        print("THE GAME IS OVER! THEN FINAL BOARD AND SCORES ARE: ");
                                        self.print_board();    
                                        return;

                elif(b == 'h' and w == 'h'):
                        while (self.white_moved or self.black_moved):
                                print('ROUND : ', round, '\n');
                                self.black_moved = self.black_turn('h')
                                print('\n''TURN CHANGE!','\n')
                                self.white_moved = self.white_turn('h')
                                #self.print_board()
                                print('\n' 'white moved = ', self.white_moved, '  ', 'black moved = ', self.black_moved, '\n');
                                round = round + 1;
                                if(self.white_moved == False and self.black_moved == False):
                                        print("THE GAME IS OVER! THEN FINAL BOARD AND SCORES ARE: ");
                                        self.print_board();
                                        return;

                

                elif(choice == 'y'):
                        while (self.white_moved or self.black_moved):
                                print('ROUND : ', round, '\n');
                                self.black_moved = self.black_turn('h')
                                print('\n''TURN CHANGE!','\n')
                                self.white_moved = self.white_turn('c')
                                #self.print_board()
                                print('\n' 'white moved = ', self.white_moved, '  ', 'black moved = ', self.black_moved, '\n');
                                round = round + 1;
                                if(self.white_moved == False and self.black_moved == False):
                                        print("THE GAME IS OVER! THEN FINAL BOARD AND SCORES ARE: ");
                                        self.print_board();    
                                        return;

                elif(choice == 'n'):
                        while (self.white_moved or self.black_moved):
                                print('ROUND : ', round, '\n');
                                self.black_moved = self.black_turn('c')
                                print('\n''TURN CHANGE!','\n')
                                self.white_moved = self.white_turn('h')
                                #self.print_board()
                                print('\n' 'white moved = ', self.white_moved, '  ', 'black moved = ', self.black_moved, '\n');
                                round = round + 1;
                                if(self.white_moved == False and self.black_moved == False):
                                        print("THE GAME IS OVER! THEN FINAL BOARD AND SCORES ARE: ");
                                        self.print_board();    
                                        return;



        def white_turn(self, gm):
        #print(self.player_white)
        #if self.player_white:
                counter = 1
                print("Valid white moves are: (row,column)")
                valid_moves = self.valid_moves_white()
                if len(valid_moves) == 0:
                         return False

                self.prev_blacks = self.blacks
                self.prev_whites = self.whites

                for move in valid_moves:
                        row = move[0];
                        col = move[1];
                        ## adding * to the board to represent possible moves
                        self.board[row][col] = "*";
                        print( str(counter) + '. '),
                        print( move)
                        counter +=1
                print('\nWHITES TURN: \n');
                self.print_board();


                if(gm == 'h'):
                        while(True):
                                #INPUT MOVE HERE
                                choice_string = input ("Enter your choice: ")
                                broken = False
                                try:
                                        choiceI = int(choice_string)
                                except:
                                        broken = True
                                        choiceI = 0
                                        choice_string = ""
                                        continue
                                choice = choiceI -1;
                                choiceT = valid_moves[choice] 

                                #clean up board before showing potential moves
                                for move in valid_moves:
                                        row = move[0];
                                        col = move[1];
                                        self.board[row][col] = " ";
                                #self.print_board();
                                self.effect_turn('w', choiceT);  ##check to see potential results
##                                print('whites: ', self.whites);
##                                print('blacks: ', self.blacks);
##                                
                                correct = input("You have chosen: " + str(valid_moves[choice]) + "\nCorrect? (y)es/(n)o\n")
                                if(correct == 'n'):
                                        #RESETING MOVES
                                        self.blacks = self.prev_blacks;
                                        self.whites = self.prev_whites
                                        ## CHANGE THE BOARD BACK
                                        self.restart_board();
                                        ## ADDING OLD PIECES BACK
                                        self.init_board();
                                        ###change score back !!!!
                                        self.white_turn(gm);

                                elif(correct == 'y'):
                                        ##print('whites: ', self.whites);
                                        ##print('blacks: ', self.blacks);
                                        ##choice = valid_moves[choice]
                                        ##self.effect_turn('w', choice);  ##check to see potential results
                                        return True
                                        break;
                                else:
                                        continue;


                elif(gm == 'c'):
                        while(True):
                                choice = random.choice(valid_moves)
                                choiceS = str(choice);
                                print("White's move is: "),
                                print(choice)
                                
                                for move in valid_moves:
                                        row = move[0];
                                        col = move[1];
                                        self.board[row][col] = " ";
                                #self.print_board();
                                self.effect_turn('w', choice);  ##check to see potential results
                                
                                
                                correct = input("You have chosen: " + choiceS + "\nCorrect? (y)es/(n)o\n")
                                if(correct == 'n'):
                                        #RESETING MOVES
                                        self.blacks = self.prev_blacks;
                                        self.whites = self.prev_whites
                                        ## CHANGE THE BOARD BACK
                                        self.restart_board();
                                        ## ADDING OLD PIECES BACK
                                        self.init_board();
                                        ###change score back !!!!
                                        self.white_turn(gm);

                                elif(correct == 'y'):
                                        ##print('whites: ', self.whites);
                                        ##print('blacks: ', self.blacks);
##                                        choice = valid_moves[choice]
                                        ##self.effect_turn('w', choice);  ##check to see potential results
                                        return True
                                        break;
                                else:
                                        continue;

                 



        def black_turn(self,gm):
##                print(self.blacks,'\n');
                counter = 1
                print("Valid black moves are: (row,column)")
                valid_moves = self.valid_moves_black()
                if len(valid_moves) == 0:
                         return False

                self.prev_blacks = self.blacks
                self.prev_whites = self.whites

                for move in valid_moves:
                        row = move[0];
                        col = move[1];
                        ## adding * to the board to represent possible moves
                        self.board[row][col] = "*";
                        print( str(counter) + '. '),
                        print( move)
                        counter +=1
                print('\nBLACKS TURN: \n');
                self.print_board();
                
                if(gm == 'h'):
                        while(True):
                                #INPUT MOVE HERE
                                choice_string = input ("Enter your choice: ")
                                broken = False
                                try:
                                        choiceI = int(choice_string)
                                except:
                                        broken = True
                                        choiceI = 0
                                        choice_string = ""
                                        continue
                                choice = choiceI -1;
                                choiceT = valid_moves[choice] 
                                

                                #clean up board before showing potential moves
                                for move in valid_moves:
                                        row = move[0];
                                        col = move[1];
                                        self.board[row][col] = " ";
                                #self.print_board();
                                self.effect_turn('b', choiceT);  ##check to see potential results
##                                print(self.blacks);

                        
                                correct = input("You have chosen: " + str(valid_moves[choice]) + "\nCorrect? (y)es/(n)o\n")
                                if(correct == 'n'):
                                        #RESETING MOVES
                                        self.blacks = self.prev_blacks;
                                        self.whites = self.prev_whites
                                        ## CHANGE THE BOARD BACK
                                        self.restart_board();
                                        ## ADDING OLD PIECES BACK
                                        self.init_board();
                                        ###change score back !!!!
                                        self.black_turn(gm);
                                elif(correct == 'y'):
                                        # MIGHT NOT NEED THIS MIGHT NEED ONLY RETURN. ALREADY CHECKED THIS CASE
                                       # choice = valid_moves[choice]
                                        ##print('whites: ', self.whites);
                                        ##print('blacks: ', self.blacks);
                                        ##self.effect_turn('b', choiceT);  ##check to see potential results
                                        return True
                                        break;
                                else:
                                        continue;


                elif(gm == 'c'):
                        while(True):
                                choice = random.choice(valid_moves)
                                choiceS = str(choice);
                                print("Blacks's move is: "),
                                print(choice)
                                
                                #clean up board before showing potential moves
                                for move in valid_moves:
                                        row = move[0];
                                        col = move[1];
                                        self.board[row][col] = " ";
                                #self.print_board();
                                self.effect_turn('b', choice);  ##check to see potential results
                                print(self.blacks);

                        
                                correct = input("You have chosen: " + choiceS + "\nCorrect? (y)es/(n)o\n")
                                if(correct == 'n'):

                                        #RESETING MOVES
                                        self.blacks = self.prev_blacks;
                                        self.whites = self.prev_whites
                                        ## CHANGE THE BOARD BACK
                                        self.restart_board();
                                        ## ADDING OLD PIECES BACK
                                        self.init_board();
                                        ###change score back !!!!
                                        self.black_turn(gm);
                                        
                                elif(correct == 'y'):
                                        #print('whites: ', self.whites);
                                        #print('blacks: ', self.blacks);
                                        # MIGHT NOT NEED THIS MIGHT NEED ONLY RETURN. ALREADY CHECKED THIS CASE
                                       # choice = valid_moves[choice] 
                                        #self.effect_turn('b', choice);  ##check to see potential results
                                        return True
                                        break;
                                else:
                                        continue;

        def init_board(self):
                for piece in self.whites:
                        row = piece[0];
                        col = piece[1];
                        self.board[row][col] = 'w'

                for piece in self.blacks:
                        row = piece[0];
                        col = piece[1];
                        self.board[row][col] = 'b'
        
                        
 


                
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
        board.init_board();
        board.print_board()
        board.game_selection()



if __name__ == '__main__':
        main()


