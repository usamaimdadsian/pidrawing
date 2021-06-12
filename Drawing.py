import math
import numpy as np
from Controller import Controller
class Drawing:
    def __init__(self,scene,board):
        self.board,self.scene = (board,scene)
        self.controller = Controller(scene,board)
        self.end = False


    def startDrawing(self):
        # self.left = True
        # for i in range(len(self.board)):
        #     if self.left:
        #         for j in range(len(self.board[i])):
        #             self.draw(i,j)
        #         self.left = False
        #     else:
        #         for j in range(len(self.board[i])-1,-1,-1):
        #             self.draw(i,j)
        #         self.left = True
            
        #     if self.scene == self.board:
        #         break
        indexes = np.where(self.scene == 1)
        indexes = list(zip(indexes[0],indexes[1]))
        lines = []
        for index in indexes:
            if lines:
                line = lines[-1]
                if line["end"]:
                    if self.checkAdjacent(line["end"],index):
                        lines[-1]["end"] = index
                    else:
                        lines.append({"start":index,"end":None})
                else:
                    lines[-1]["end"] = index
            else:
                lines.append({"start": index,"end":None})

        self.left = True
        for line in lines:
            x1,y1 = line["start"]
            if line["end"]:
                x2,y2 = line["end"]
                x,y = self.controller.currentPos()
                dis1 = math.sqrt((x1-x)**2+(y1-y)**2)
                dis2 = math.sqrt((x2-x)**2+(y2-y)**2)
                self.left = (dis1 < dis2)
                if self.left:
                    self.controller.moveAt(x1*10,y1*10,True,True)
                    self.controller.moveAt(x2*10,y2*10,True,False)
                else:
                    self.controller.moveAt(x2*10,y2*10,True,True)
                    self.controller.moveAt(x1*10,y1*10,True,False)

            else:
                self.controller.moveAt(x1*10,y1*10,True,False)
            # break
        self.controller.initPos()

    # def draw(self,x,y):
    #     if self.board[x,y] > 1:
    #         if y == len(self.board[x])-1 or y == 0: self.end = True
    #         if self.end:
    #             adjacent = (x < len(self.board)-1 and self.board[x+1,y] == 1)
    #             self.end = False
    #         else:
    #             if self.left:
    #                 adjacent = (y<len(self.board[x])-1 and self.board[x,y+1] == 1) # Check if the adjacent value is 1 or not
    #             else:
    #                 adjacent = (y>0 and self.board[x,y-1] == 1) # Check if the adjacent value is 1 or not

    #         self.controller.moveAt(x,y,True,adjacent)
    #         self.board[x,y] = 1
            # if (self.scene == self.board).all():
            #     break

    # def draw(self,x,y):
    #     print(f"(x,y)=({x},{y},{self.scene[x,y]})")
    #     if self.scene[x,y] == 1:
    #         print("Draw it")
    #         if y == len(self.board[x])-1 or y == 0: self.end = True
    #         if self.end:
    #             adjacent = (x < len(self.board)-1 and self.scene[x+1,y] == 1)
    #             self.end = False
    #         else:
    #             if self.left:
    #                 adjacent = (y<len(self.board[x])-1 and self.scene[x,y+1] == 1) # Check if the adjacent value is 1 or not
    #             else:
    #                 adjacent = (y>0 and self.scene[x,y-1] == 1) # Check if the adjacent value is 1 or not

    def checkAdjacent(self,ind1,ind2):
        x1,y1 = ind1
        x2,y2 = ind2
        dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return (dis < 2)