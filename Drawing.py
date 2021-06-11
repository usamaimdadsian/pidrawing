from Controller import Controller
class Drawing:
    def __init__(self,scene,board):
        self.board,self.scene = (board,scene)
        self.controller = Controller(scene,board)
        self.end = False


    def startDrawing(self):
        self.left = True
        for i in range(len(self.board)):
            if self.left:
                for j in range(len(self.board[i])):
                    self.draw(i,j)
                self.left = False
            else:
                for j in range(len(self.board[i])-1,-1,-1):
                    self.draw(i,j)
                self.left = True
            
            if (self.scene == self.board).all():
                break

    def draw(self,x,y):
        print(f"(x,y)=({x},{y},{self.scene[x,y]})")
        if self.scene[x,y] == 1:
            print("Draw it")
            if y == len(self.board[x])-1 or y == 0: self.end = True
            if self.end:
                adjacent = (x < len(self.board)-1 and self.scene[x+1,y] == 1)
                self.end = False
            else:
                if self.left:
                    adjacent = (y<len(self.board[x])-1 and self.scene[x,y+1] == 1) # Check if the adjacent value is 1 or not
                else:
                    adjacent = (y>0 and self.scene[x,y-1] == 1) # Check if the adjacent value is 1 or not

            self.controller.moveAt(x,y,True,adjacent)
            self.board[x,y] = 1
