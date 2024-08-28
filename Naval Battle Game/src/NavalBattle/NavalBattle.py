import random

class NotEnoughSpace(Exception):
    pass


class BoardIsTooSmall(Exception):
    pass

class BoardIsTooBig(Exception):
    pass

class RowOutOfRange(Exception):
    pass

class ColumnOutOfRange(Exception):
    pass

class BoardIsBigAndSmall(Exception):
    pass

class BoardError(Exception):
    pass

class InvalidCoordinate(Exception):
    pass

class NavalBattle():
    last_hit= None
    ships = 0
    columns = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    fixed_columns = [" A"," B"," C"," D"," E"," F"," G"," H"," I"," J"," K"," L"," M"," N"," O"," P"," Q"," R"," S"," T"]
    board= None

    def generateBoard(self, w=8, h=5):
        if w < 0 or h < 0:
            raise BoardError("Board can't have negative rows or columns")
        elif w == 0 or h == 0:
            raise BoardError("Board can't have zero rows or columns")
        elif (w < 5 and h >9) or (h < 5 and w >9):
            raise BoardIsBigAndSmall
        elif w < 5 or h < 5:
            raise BoardIsTooSmall
        elif w > 9 or h > 9:
            raise BoardIsTooBig
        self.w = w
        self.h = h
        self.board = [[0 for j in range(w)] for i in range(h)] 
        self.player_board = [["\U00002754" for i in range(w)] for i in range(h)]

        return self.board
    
    def addShipsInPosition(self, position, vertical=True, len=3):
            enough_space = True

            i = position[1]
            j = position[0]

            if vertical:
                for s in range(len):
                        
                    if self.board[i][j] != 0:
                            enough_space=False

                    i+=1
                i-=len
                if enough_space:
                    for s in range(len):
                        self.board[i][j]=len
                        i+=1
                    self.ships+=1
                    len-=1
                else:
                    print("No hay espacio disponible")
                

            elif not vertical:
                for s in range(len):
                    
                    if self.board[i][j] != 0:
                            enough_space=False

                    j+=1
                j-=len
                if enough_space:
                    for s in range(len):
                        self.board[i][j]=len
                        j+=1
                    self.ships+=1
                    len-=1
                else:
                    print("No hay espacio disponible")
             



    def addShips(self, num_ships, limit=8):
        if num_ships>limit:
            raise NotEnoughSpace
        ship_len = num_ships+1
        if self.board == None:
            raise BoardError("There's no board yet")
        while self.ships < num_ships:
            enough_space=True
            
            vertical = random.choice([True, False])

            if vertical:
                i = random.randint(0, self.h - ship_len)
                j = random.randint(0, self.w-1)
                for s in range(ship_len):
                    
                    if self.board[i][j] != 0:
                            enough_space=False

                    i+=1
                i-=ship_len
                if enough_space:
                    for s in range(ship_len):
                        self.board[i][j]=ship_len
                        i+=1
                    self.ships+=1
                    ship_len-=1

            else:
                i = random.randint(0, self.h-1)
                j = random.randint(0, self.w - ship_len)
                for s in range(ship_len):

                    if self.board[i][j] != 0:
                            enough_space=False

                    j+=1
                j-=ship_len
                if enough_space:
                    for s in range(ship_len):
                        self.board[i][j]=ship_len
                        j+=1
                    self.ships+=1
                    ship_len-=1

    def shoot(self, coordinate: str):
        coordinate = coordinate.upper()
        column = coordinate[0]
        if len(coordinate) != 2:
            raise InvalidCoordinate
        row = int(coordinate[1])-1
        if row >= len(self.board):
            raise RowOutOfRange
        if column in self.columns:
            column = self.columns.index(column)
            if column >= len(self.board[0]):
                raise ColumnOutOfRange
        else:
            raise ColumnOutOfRange
        if self.board[row][column]=="x":
            print("No malgastes tus disparos")
            return False
        elif self.board[row][column] !=0:
            self.last_hit = self.board[row][column]
            self.board[row][column]="x"
            self.player_board[row][column]="\U0001F4A5"
            print(f"\U0001F6A2 IMPACTO \U0001F4A5")
            return True
        else:
            self.player_board[row][column]="\U0001F30A"
            
            print(f"\U0001F4A6 AGUA \U0001F4A6")
            return False
        
    def downedShip(self):
        for h in range(len(self.board)):
            for w in range(len(self.board[0])):
                if self.last_hit == self.board[h][w]:
                    return False

        print("Barco derribado")
        self.ships-=1
        for i in range(self.last_hit):
            print("\U0001F4A5", end=" ")
        print("\n")
        self.showInfo()
        return True

    def showInfo(self):
        print(f"Barcos restantes: {self.ships}")
        
    def showPlayerBoard(self):
        print(self.fixed_columns[:self.w])
        for fila in self.player_board:
            print(fila)


if __name__ == "__main__":
    navalBattle = NavalBattle()
    print("Ingrese el tamaño del tablero en el que desea jugar en el formato: ")
    print("(min:5, max:9)")

    w = int(input("Columnas: "))
    h = int(input("Filas: "))
    navalBattle.generateBoard(w,h)
    
    
    if w == h:
        print(f"Máximo {w} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships, w)
    elif w>h:
        print(f"Máximo {h} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships, h)
    elif w<h:
        print(f"Máximo {w} barcos")
        num_ships = int(input("Ingrese el número de barcos: "))
        navalBattle.addShips(num_ships,w)
    
    #print(navalBattle.board)
    print("Ingrese la coordenada que desea atacar en el formato: C2")
    print("Siendo 'C' la columna y '2' la fila")
    navalBattle.showInfo()
    navalBattle.showPlayerBoard()
    while True:
        
        coordenada = input(f"Coordenada: ")
        if navalBattle.shoot(coordenada):
            navalBattle.downedShip()
        if navalBattle.ships==0:
            navalBattle.showPlayerBoard()
            print("Has ganado")
            break
        navalBattle.showPlayerBoard()

