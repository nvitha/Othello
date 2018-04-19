'''
Daniel 
Brian Ramaswami
Nicholas Vitha


CPSC 



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
	white_moved = True
	black_moved = True
	def __init__(self, _board): #initialize the board configuration
		self.board = copy.deepcopy(_board)
		self.whites = [(3,3),(4,4)]
		self.blacks = [(3,4),(4,3)]
		self.white_moved = True
		self.black_moved = True
		self.previous_board = copy.deepcopy(_board)

	def side_selection(self): #select which side 
		self.player_white = True

		choice = raw_input("Do you want to be white? (y)es/(n)o\n")
		if ((choice.lower() == "y") or (choice.lower() == "yes")):
			self.player_white = True
			print "Player is playing white"
		elif ((choice.lower() == "n") or (choice.lower() == "no")):
			self.player_white = False
			print "AI is playing white"
		else:
			print "You have not selected yes or no."	
			print "Exiting program now."
			return


	def print_board(self):
		row = 0
		column = 0
		print ' ',
		for i in xrange(0,8):
			print str(i) + '  ',
		print 
        	for line in self.board:
			print str(row),
			row += 1
        	        column = 0
			for char in line:
                	        print char,
				column += 1
				if column != 8:
					print '|',
			if(row !=8):
				print
				print ' ',
				print '_'*31
		print
		print
		print "White score = " + str(len(self.whites))
		print "Black score = " + str(len(self.blacks))



	def print_blacks(self):
		print self.blacks

	def print_whites(self):
		print self.whites

	def valid_moves_white(self):
		valid_moves = []
		for black_piece in self.blacks:
			column = black_piece[1]
			row = black_piece[0]
			
			# Top
			if(self.board[row-1][column] == ' '):
				white_piece_in_way = False
				for i in xrange(row,8):
					if self.board[i][column] == 'w':
						white_piece_in_way = True
						break
					if self.board[i][column] == ' ':
						break
				if white_piece_in_way:
					valid_moves.append((row-1,column))
			# Left
			if(self.board[row][column-1] == ' '):
				white_piece_in_way = False
				for i in xrange(column,8):
					if self.board[row][i] == 'w':
						white_piece_in_way = True
						break
					if self.board[row][i] == ' ':
						break
				if white_piece_in_way:
					valid_moves.append((row,column-1))
			# Below
			if(self.board[row+1][column] == ' '):
				white_piece_in_way = False
				for i in xrange(row,0,-1):
					if self.board[i][column] == 'w':
						white_piece_in_way = True
						break
					if self.board[i][column] == ' ':
						break
				if white_piece_in_way:
					valid_moves.append((row+1,column))
			# Right
			if(self.board[row][column+1] == ' '):
				white_piece_in_way = False
				for i in xrange(column,0,-1):
					if self.board[row][i] == 'w':
						white_piece_in_way = True
						break
					elif self.board[row][i] == ' ':
						break
				if white_piece_in_way:
					valid_moves.append((row,column+1))

			# Bottom Right
			if(self.board[row+1][column+1] == ' '):
				white_piece_in_way = False
				if row > column:
					counter = 0
					for i in xrange(column, -1, -1):
						current_item = self.board[row-counter][i]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(row, -1, -1):
						current_item = self.board[i][column-counter]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if white_piece_in_way:
					valid_moves.append((row+1,column+1))

			# Top Left			
			if(self.board[row-1][column-1] == ' '):
				white_piece_in_way = False
				if row < column:
					counter = 0
					for i in xrange(column, 8, 1):
						current_item = self.board[row+counter][i]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(row, 8, 1):
						current_item = self.board[i][column+counter]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if white_piece_in_way:
					valid_moves.append((row+1,column+1))

			# Top Right
			if(self.board[row-1][column+1] == ' '):
				white_piece_in_way = False
				if 8-row < column:
					counter = 0
					for i in xrange(row, 8, 1):
						current_item = self.board[i][column-counter]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(column, 0, -1):
						current_item = self.board[row-counter][i]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if white_piece_in_way:
					valid_moves.append((row-1,column+1))


			# Bottom Left
			if(self.board[row+1][column-1] == ' '):
				white_piece_in_way = False
				if row < 8-column:
					counter = 0
					for i in xrange(row, 0, -1):
						current_item = self.board[i][column-counter]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(column, 8, 1):
						current_item = self.board[row-counter][i]
						if current_item == 'w':
							white_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if white_piece_in_way:
					valid_moves.append((row+1,column-1))

		return valid_moves

	def valid_moves_black(self):
		valid_moves = []
		for white_piece in self.whites:
			column = white_piece[1]
			row = white_piece[0]
			
			# Top
			if(self.board[row-1][column] == ' '):
				black_piece_in_way = False
				for i in xrange(row,8):
					if self.board[i][column] == 'b':
						black_piece_in_way = True
						break
					if self.board[i][column] == ' ':
						break
				if black_piece_in_way:
					valid_moves.append((row-1,column))
			# Left
			if(self.board[row][column-1] == ' '):
				black_piece_in_way = False
				for i in xrange(column,8):
					if self.board[row][i] == 'b':
						black_piece_in_way = True
						break
					if self.board[row][i] == ' ':
						break
				if black_piece_in_way:
					valid_moves.append((row,column-1))
			# Below
			if(self.board[row+1][column] == ' '):
				black_piece_in_way = False
				for i in xrange(row,0,-1):
					if self.board[i][column] == 'b':
						black_piece_in_way = True
						break
					if self.board[i][column] == ' ':
						break
				if black_piece_in_way:
					valid_moves.append((row+1,column))
			# Right
			if(self.board[row][column+1] == ' '):
				black_piece_in_way = False
				for i in xrange(column,0,-1):
					if self.board[row][i] == 'b':
						black_piece_in_way = True
						break
					elif self.board[row][i] == ' ':
						break
				if black_piece_in_way:
					valid_moves.append((row,column+1))

			# Bottom Right
			if(self.board[row+1][column+1] == ' '):
				black_piece_in_way = False
				if row > column:
					counter = 0
					for i in xrange(column, -1, -1):
						current_item = self.board[row-counter][i]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(row, -1, -1):
						current_item = self.board[i][column-counter]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if black_piece_in_way:
					valid_moves.append((row+1,column+1))

			# Top Left			
			if(self.board[row-1][column-1] == ' '):
				black_piece_in_way = False
				if row < column:
					counter = 0
					for i in xrange(column, 8, 1):
						current_item = self.board[row+counter][i]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(row, 8, 1):
						current_item = self.board[i][column+counter]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if black_piece_in_way:
					valid_moves.append((row+1,column+1))

			# Top Right
			if(self.board[row-1][column+1] == ' '):
				black_piece_in_way = False
				if 8-row < column:
					counter = 0
					for i in xrange(row, 8, 1):
						current_item = self.board[i][column-counter]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(column, 0, -1):
						current_item = self.board[row-counter][i]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if black_piece_in_way:
					valid_moves.append((row-1,column+1))


			# Bottom Left
			if(self.board[row+1][column-1] == ' '):
				black_piece_in_way = False
				if row < 8-column:
					counter = 0
					for i in xrange(row, 0, -1):
						current_item = self.board[i][column-counter]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1
							
				else:
					counter = 0
					for i in xrange(column, 8, 1):
						current_item = self.board[row-counter][i]
						if current_item == 'b':
							black_piece_in_way = True
							break
						elif current_item == ' ':
							break
						counter +=1

				if black_piece_in_way:
					valid_moves.append((row+1,column-1))

		return valid_moves


		

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

	def take_turn(self):
		while (self.white_moved or self.black_moved):
			self.white_moved = self.white_turn()
			self.black_moved = self.black_turn()
			self.print_board()
			return


	def white_turn(self):
		if self.player_white:
			counter = 1
			print "Valid white moves are: (row,column)"
			valid_moves = self.valid_moves_white()
			if len(valid_moves) == 0:
				return false
			correct = 'n'
			while (correct == 'n'):
				for move in valid_moves:
					print str(counter) + '. ',
					print move
					counter +=1
				choice = raw_input('What move do you choose?\n')
				choice = int(choice) - 1
				correct = raw_input("You have chosen: " + str(valid_moves[choice]) + "\nCorrect? (y)es/(n)o\n")
				choice = valid_moves[choice]
		else:
			valid_moves = self.valid_moves_white()

			if len(valid_moves) == 0:
				return false			

			choice = random.choice(valid_moves)
		print "White's move is: ",
		print choice

		self.effect_turn('w',choice)
		return True

	def black_turn(self):
		if not self.player_white:
			counter = 1
			print "Valid black moves are: (row,column)"
			valid_moves = self.valid_moves_black()
			for move in valid_moves:
				print str(counter) + '. ',
				print move
				counter +=1
		return False

	def find_colors(self):
		blacks = []
		whites = []
		row_num = 0
		col_num = 0
		for row in self.board:
			for color in row:
				if color == 'w':
					whites.append((row_num,col_num))
				elif color == 'b':
					blacks.append((row_num,col_num))
				col_num += 1
			row_num +=1
		return 
		


	def effect_turn(self, color, coords):
		row = coords[0]
		column = coords[1]


		self.board[row][column] = color

		tl,tl_changed = self.up_left(color,(row-1,column-1))
		top,top_changed = self.up(color, (row-1,column))
		tr,tr_changed = self.up_right(color, (row-1,column+1))
		left,left_changed = self.left(color, (row,column-1))
		right,right_changed = self.right(color, (row,column+1))
		bl,bl_changed = self.bot_left(color, (row+1,column-1))
		bot,bot_changed = self.bot(color, (row+1,column))
		br,br_changed = self.bot_right(color,(row+1,column+1))
		total_changed = tl_changed + top_changed + tr_changed + left_changed + right_changed + bl_changed + bot_changed + br_changed

		print "total changed: " + str(total_changed)


#def runner(board):


def main():
	board = Othello_Board(get_start_state())
	board.print_board()
	board.side_selection()
	board.take_turn()
	

if __name__ == '__main__':
	main()
