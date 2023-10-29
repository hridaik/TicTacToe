
import random
import time
def drawBoard(board):
     print("   |   |")
     print(" " + board[1] + " | " + board[2] + " | " + board[3])
     print("   |   |")
     print("-----------")
     print("   |   |")
     print(" " + board[4] + " | " + board[5] + " | " + board[6])
     print("   |   |")
     print("-----------")
     print("   |   |")
     print(" " + board[7] + " | " + board[8] + " | " + board[9])
     print("   |   |")
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
         print( username + ", do you want to be X or O?")
         letter = input().upper()
         if letter == 'X':
                         return['X','O']
         if letter == 'O':
            return['O','X']

def whoGoesFirst():
    if random.randint(1,2) == 1:
        return 'computer'
    else:
        return username
def playAgain():
     print( username +", do you wish to play again? (Yes or No)")
     return input().upper().startswith("Y")
def makeMove(board, letter, move):
     board[move] = letter
def winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[7] == letter and board[5] == letter and board[3] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[7] == letter and board[4] == letter and board[1] == letter) or (board[5] == letter and board[8] == letter and board[2] == letter) or (board[9] == letter and  board[6] == letter and board[3] == letter))
def isBoardSpaceFree(board, move):
    return board[move] == ' '
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
         dupeBoard.append(i)
    return dupeBoard
def getPlayerMove(board):
   move = ''
   while move not in '1 2 3 4 5 6 7 8 9'.split() or not isBoardSpaceFree(board, int(move)):
      print("What is your next move? (select from 1-9)")
      move = input()
   return int(move)
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isBoardSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if winner(copy, computerLetter):
               return i 
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isBoardSpaceFree(copy, i):
           makeMove(copy, playerLetter, i)
           if winner(copy, playerLetter):
              return i 
    move = chooseMoveFromList(board, [7, 9, 1, 3])
    if move != None:
        return move
    if isBoardSpaceFree(board, 5):
         return 5
    return chooseMoveFromList([2, 4, 6, 8])	
		   		   
def chooseMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
       if isBoardSpaceFree(board, i):
          possibleMoves.append(i)
    if len(possibleMoves) !=0:
       return random.choice(possibleMoves)
    else:
       return None 

def isBoardFull(board):
    for i in range(1,10):
       if isBoardSpaceFree(board, i):
          return False
    else: 
       return True
print("TIC TAC TOE                                     © Hridai Khurana 26/12/2017")
username = input("Please enter your name: ")
score = 0
while True:
    if username == 'hridai':
         print("The computer is not worthy of playing you. You win by default.")
         time.sleep(30)
         break
    else:
       board = [' '] * 10
       playerLetter, computerLetter = inputPlayerLetter()
       turn = whoGoesFirst()
       if turn == username:
          print( username + " goes first.")
       else:
            print("The computer goes first.")
       gameIsPlaying = True
       while gameIsPlaying:
          if turn == username :
                   drawBoard(board)
                   move = getPlayerMove(board)
                   makeMove(board, playerLetter, move)
                   if winner(board, playerLetter):
                       drawBoard(board)
                       print(username + " won.")
                       score = score + 1
                       print("SCORE: ")
                       print(score)
                       gameIsPlaying = False
                   elif isBoardFull(board):
                       drawBoard(board)
                       print("Game tied")
                       print("SCORE: " + score)
                       break
                   else:
                       turn = 'computer'
          else:
             move = getComputerMove(board, computerLetter)
             makeMove(board, computerLetter, move)
             if winner(board, computerLetter):
                drawBoard(board)
                print("The computer won.")
                score = score - 1
                print("SCORE: ")
                print(score)
                gameIsPlaying = False
             else:
                if isBoardFull(board):
                   drawBoard(board)
                   print("Game tied.")
                   print("SCORE: ")
                   print(score)
                   break
                else:
                   turn = username
       if not playAgain():
            print("Your final score was: " )
            print(score)
            time.sleep(10)
            break


















































































































