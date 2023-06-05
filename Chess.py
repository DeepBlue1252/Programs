class Chess:
    def __init__(self):
        self.board = []
        self.bank = []
        self.checkMatePawn = Pawn(None,None,None)
        self.attacker = None

    def definePieces(self):
        b = "black"
        w = "white"
        black_King = King(b, [0,4], self.bank)
        black_Queen = Queen(b, [0,3], self.bank)
        black_Bishop1 = Bishop(b, [0,2], self.bank)
        black_Bishop2 = Bishop(b, [0,5], self.bank)
        black_Rook1 = Rook(b, [0,0], self.bank)
        black_Rook2 = Rook(b, [0,7], self.bank)
        black_Knight1 = Knight(b, [0,1], self.bank)
        black_Knight2 = Knight(b, [0,6], self.bank)
        for i in range(8):
            Pawn(b, [1,i], self.bank)
        white_King = King(w, [7,4], self.bank)
        white_Queen = Queen(w, [7,3], self.bank)
        white_Bishop1 = Bishop(w, [7,2], self.bank)
        white_Bishop2 = Bishop(w, [7,5], self.bank)
        white_Rook1 = Rook(w, [7,0], self.bank)
        white_Rook2 = Rook(w, [7,7], self.bank)
        white_Knight1 = Knight(w, [7,1], self.bank)
        white_Knight2 = Knight(w, [7,6], self.bank)
        for i in range(8):
            Pawn(w, [6,i], self.bank)

    def createBoard(self):
        self.board = [['_'] * 8 for _ in range(8)]
        self.definePieces()
        for piece in self.bank:
            if piece.xy != None:
                self.board[piece.xy[0]][piece.xy[1]] = piece.symbol
    
    def makeMoves(self, num):
        player = ''
        if num % 2 == 0:
            player = "white"
        else:
            player = "black"
        move = input("Make a move "+ player+ ": ")
        pos1 = []
        pos2 = []
        pos1.append(int(move[1]))
        pos1.append(int(move[3]))
        pos2.append(int(move[7]))
        pos2.append(int(move[9]))
        for piece in self.bank:
            if piece.color == player:
                if piece.xy == pos1:
                    if piece.canMove(pos2, self.bank):
                        if not self.willIBeInCheck(piece, pos1, pos2):
                            self.move(piece, pos2)
                            return True
        return False
    
    def move(self, piece, pos2):
        for pieces in self.bank:
            if pieces.xy == pos2:
                defeated = pieces
        self.board[pos2[0]][pos2[1]] = piece.symbol
        self.board[piece.xy[0]][piece.xy[1]] = '_'
        piece.xy = pos2
        try:
            return(defeated)
        except:
            return

    def reverseMove(self, piece, pos1, pos2, defeated = None):
        self.move(piece, pos1)
        if defeated:
            defeated.xy = pos2
        

    def checkForChecks(self, num):
        player = ''
        if num % 2 == 0:
            player = "white"
        else:
            player = "black"
        position = []
        for pieces in self.bank:
            if pieces.color == player and (pieces.symbol =='K' or pieces.symbol=='k'):
                position = pieces.xy
        for pieces in self.bank:
            if pieces.color != player:
                if pieces.canMove(position,self.bank):
                    self.attacker = pieces
                    #print(player+ " is in check!")
                    return True
        return False

    def willIBeInCheck(self, piece, pos1, pos2):
        defeated = self.move(piece, pos2)
        for pieces in self.bank:
            if pieces.color == piece.color and (pieces.symbol == 'K' or pieces.symbol == 'k'):
                kingXY = pieces.xy
        for pieces in self.bank:
            if pieces.color != piece.color:
                if pieces.canMove(kingXY, self.bank):
                    self.reverseMove(piece, pos1, pos2, defeated)
                    return True
        self.reverseMove(piece, pos1, pos2, defeated)
        return False

    def checkMatePawncheck(self, pos2):
        present = False
        for pieces in self.bank:
            if pieces.xy == pos2:
                present = True
                #print(pieces.xy, " ", pos2)
                return
        if not present:
            self.board[pos2[0]][pos2[1]] = self.checkMatePawn.symbol
            if self.checkMatePawn.xy:
                self.board[self.checkMatePawn.xy[0]][self.checkMatePawn.xy[1]] = '_'
            self.checkMatePawn.xy = pos2
        return

    def moveFromCheck(self, piece):
        availableMoves = [[piece.xy[0]+1,piece.xy[1]+1],[piece.xy[0]+1,piece.xy[1]],[piece.xy[0]+1,piece.xy[1]-1],[piece.xy[0],piece.xy[1]-1],[piece.xy[0]-1,piece.xy[1]-1],[piece.xy[0]-1,piece.xy[1]],[piece.xy[0]-1,piece.xy[1]+1],[piece.xy[0],piece.xy[1]+1]]
        for move in availableMoves:
            if not self.willIBeInCheck(piece, piece.xy, move):
                return True

    def checkForCheckmate(self, num):
        player = ''
        if num % 2 == 0:
            player = "white"
            self.checkMatePawn.color = "white"
        else:
            player = "black"
            self.checkMatePawn.color = "black"
        for pieces in self.bank:
            if pieces.color == self.checkMatePawn.color:
                if pieces.symbol == 'K' or pieces.symbol == 'k':
                    if self.moveFromCheck(pieces):
                        return False
                if pieces.canMove(self.attacker.xy, self.bank):
                    if not self.willIBeInCheck(pieces, pieces.xy, self.attacker.xy):
                        return False
        for yPos in range(len(self.board)):
            for xPos in range(len(self.board[yPos])):
                self.bank.append(self.checkMatePawn)
                self.checkMatePawncheck([xPos,yPos])
                if not self.checkForChecks(num):
                    for pieces in self.bank:
                        if pieces.color == self.checkMatePawn.color:
                            if pieces.canMove([xPos,yPos], self.bank):
                                #print("can stop at", [xPos,yPos], " with ", pieces.xy)
                                #print(self.checkMatePawn.color)
                                #print(self.bank)
                                if self.checkMatePawn.xy == [xPos,yPos]:
                                    self.board[xPos][yPos] = '_'
                                self.checkMatePawn.xy = None
                                self.bank.remove(self.checkMatePawn)
                                return False
                if self.checkMatePawn.xy == [xPos,yPos]:
                    self.board[xPos][yPos] = '_'
                self.checkMatePawn.xy = None
                self.bank.remove(self.checkMatePawn)
        return True

    def playGame(self):
        checkmate = False
        self.createBoard()
        self.printBoard()
        movesmade = 0
        player = ''
        while not checkmate:
            if movesmade % 2 == 0:
                player = "WHITE"
            else:
                player = "BLACK"
            if(self.makeMoves(movesmade)):
                movesmade += 1
            else:
                print("Invalid Move -- Try Again")
            self.printBoard()
            print(self.board)
            if self.checkForChecks(movesmade):
                if player == "WHITE":
                    print("BLACK is in check!")
                else:
                    print("WHITE is in check!")
                if self.checkForCheckmate(movesmade):
                    checkmate = True
            #print(self.board)
        print(player+" WINS!")
        return

    def printBoard(self):
        line = ""
        print("  0 1 2 3 4 5 6 7")
        for i in range(len(self.board)):
            for j in self.board[i]:
                line += j
                line += ' '
            print(str(i)+" "+line)
            line = ""

class Pieces(Chess):
    def __init__(self, color, location, status=True, symbol='p'):
        self.moves = []
        self.status = status
        self.color = color
        self.xy = location
        self.symbol = symbol
        
    def checkForPiecesInTheWay(self, move, bank):
        xDifference = move[1] - self.xy[1]
        yDifference = move[0] - self.xy[0]
        xPos = self.xy[1]
        yPos = self.xy[0]
        xAlter = 0
        yAlter = 0
        if xDifference != 0:
            xAlter = (xDifference/abs(xDifference))
        if yDifference != 0:
            yAlter = yDifference/abs(yDifference)
        while xPos != (move[1]-xAlter) or yPos != (move[0]-yAlter):
            if xDifference<0:
                xPos -= 1
            elif xDifference>0:
                xPos += 1
            if yDifference<0:
                yPos -= 1
            elif yDifference>0:
                yPos +=1
            for pieces in bank:
                if pieces.xy == [yPos,xPos]:
                    return False
        for pieces in bank:
            if pieces.xy == move and pieces.color == self.color:
                return False
        return True

class King(Pieces):
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'K'
        else:
            self.symbol = 'k'
        bank.append(self)
        
    def canMove(self, move, bank):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        availableMoves = [[self.xy[0]+1,self.xy[1]+1],[self.xy[0]+1,self.xy[1]],[self.xy[0]+1,self.xy[1]-1],[self.xy[0],self.xy[1]-1],[self.xy[0]-1,self.xy[1]-1],[self.xy[0]-1,self.xy[1]],[self.xy[0]-1,self.xy[1]+1],[self.xy[0],self.xy[1]+1]]
        if move in availableMoves:
            return True
        

    
class Queen(Pieces):
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'Q'
        else:
            self.symbol = 'q'
        bank.append(self)

    def canMove(self, move, bank, copybank=[]):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        #vertical
        if move[0] == self.xy[0]:
            if move[1] in range(0,8):
                if self.checkForPiecesInTheWay(move, bank):
                    return True
        #horizontal
        if move[1] == self.xy[1]:
            if move[0] in range(0,8):
                if self.checkForPiecesInTheWay(move, bank):
                    return True
        #diagonal
        if abs(move[0]-self.xy[0]) == abs(move[1]-self.xy[1]):
            if self.checkForPiecesInTheWay(move, bank):
                    return True

class Bishop(Pieces): 
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'B'
        else:
            self.symbol = 'b'
        bank.append(self)

    def canMove(self, move, bank):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        #diagonal
        if abs(move[0]-self.xy[0]) == abs(move[1]-self.xy[1]):
            return True

class Rook(Pieces):
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'R'
        else:
            self.symbol = 'r'
        bank.append(self)

    def canMove(self, move, bank):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        #vertical
        if move[0] == self.xy[0]:
            if move[1] in range(0,8):
                return True
        #horizontal
        if move[1] == self.xy[1]:
            if move[0] in range(0,8):
                return True

class Knight(Pieces):
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'N'
        else:
            self.symbol = 'n'
        bank.append(self)

    def canMove(self, move, bank):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        availableMoves = [[self.xy[0]+2,self.xy[1]+1],[self.xy[0]+1,self.xy[1]+2],[self.xy[0]-1,self.xy[1]+2],[self.xy[0]-2,self.xy[1]+1],[self.xy[0]-2,self.xy[1]-1],[self.xy[0]-1,self.xy[1]-2],[self.xy[0]+1,self.xy[1]-2],[self.xy[0]+2,self.xy[1]-1]]
        if move in availableMoves:
            return True

class Pawn(Pieces):
    def __init__(self, color, location, bank):
        super().__init__(color, location)
        if color == 'black':
            self.symbol = 'P'
        else:
            self.symbol = 'p'
        if bank:
            bank.append(self)
        
    def canMove(self, move, bank):
        if move[0] not in range(0,8) and move[1] not in range(0,8):
            return False
        #firstmove
        if self.xy[0] == 1 and self.color == "black":
            availableMoves = [[self.xy[0]+1,self.xy[1]],[self.xy[0]+2,self.xy[1]]]
        elif self.color == "black":
            availableMoves = [[self.xy[0]+1,self.xy[1]]]
        elif self.xy[0] == 6 and self.color == "white":
            availableMoves = [[self.xy[0]-1,self.xy[1]],[self.xy[0]-2,self.xy[1]]]
        elif self.color=="white":
            availableMoves = [[self.xy[0]-1,self.xy[1]]]

        if self.color == "black":
            for pieces in bank:
                if pieces.color == "white":
                    if pieces.xy == [self.xy[0]+1,self.xy[1]-1]:
                        availableMoves += [self.xy[0]+1,self.xy[1]-1]
                    elif pieces.xy == [self.xy[0]+1,self.xy[1]+1]:
                        availableMoves += [self.xy[0]+1,self.xy[1]+1]
        if self.color == "white":
            for pieces in bank:
                if pieces.color == "black":
                    if pieces.xy == [self.xy[0]-1,self.xy[1]-1]:
                        availableMoves += [self.xy[0]-1,self.xy[1]-1]
                    elif pieces.xy == [self.xy[0]-1,self.xy[1]+1]:
                        availableMoves += [self.xy[0]-1,self.xy[1]+1]
        if move in availableMoves:
            return True


def main():
    chess1 = Chess()
    chess1.playGame()

main()