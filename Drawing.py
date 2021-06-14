import math
import numpy as np
from Controller import Controller
class Drawing:
    def __init__(self,scene,board):
        self.board,self.scene = (board,scene)
        self.controller = Controller(scene,board)
        self.end = False

    def drawFancy(self):
        indexes = np.where(self.scene == 1)
        indexes = list(zip(indexes[0],indexes[1]))
        points = []
        lines = []


        for i in range(len(indexes)):
            if not indexes[i] in points: points.append(indexes[i])
            for j, point in enumerate(indexes):
                if (not points[-1] ==  indexes[j]) and checkAdjacent(points[-1],indexes[j]) and (not indexes[i] in points):
                    points.append(indexes[j])

        head = 0
        for i,point in enumerate(points):
            if not head:
                head =  i
            elif i < len(points)-1 and (not checkAdjacent(point,points[i+1])):
                lines.append(points[head:i+1])
                head = None

        for line in lines:
            for i,point in enumerate(line):
                x,y = point
                if i == len(line)-1:
                    self.controller.moveAt(x*10,y*10,True,False)
                else:
                    self.controller.moveAt(x*10,y*10,True,True)
        self.controller.initPos()
                
        

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