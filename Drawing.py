
import cv2
import math
import numpy as np
from Controller import Controller
class Drawing:
    def __init__(self,scene,board):
        self.board,self.scene = (board,scene)
        self.controller = Controller(scene,board)
        self.end = False

        self.dis_index = []
        self.dis_value = []


    def bestDraw(self):
        ret, labels = cv2.connectedComponents(self.scene)
        f_points = []
        for j in range(1,np.unique(labels).max()+1):
            label = np.zeros_like(labels)
            label[labels == j] = 1


            indexes = np.where(label == 1)
            indexes = list(zip(indexes[0],indexes[1]))

            table_sorted = {}
            for st_point in indexes:
                point_arr = []
                point_val = []
                for point in indexes:
                    point_arr.append(point)
                    dis = self.findDistance(st_point,point)
                    point_val.append(dis)

                points = [x for _, x in sorted(zip(point_val, point_arr))]
                table_sorted[points[0]] = points

            points = [indexes[0]]
            while len(points) < len(indexes):
                temp = points[-1]
                temp_arr = table_sorted[temp]
                for t_ele in temp_arr:
                    if not t_ele in points:
                        points.append(t_ele)
                        break

            f_points.append(points)

        
        for line in f_points:
            for i,point in enumerate(line):
                x,y = point
                if point == points[-1]:
                    self.controller.moveAt(x*10,y*10,True,False)
                else:
                    self.controller.moveAt(x*10,y*10,True,True)
        self.controller.initPos()

    
    def findDistance(self,ind1,ind2):
        com_point = (ind1,ind2)
        if (com_point in self.dis_index) or ((ind2,ind1) in self.dis_index):
            if com_point in self.dis_index:
                return self.dis_value[self.dis_index.index(com_point)]
            else:
                return self.dis_value[self.dis_index.index((ind2,ind1))]
        else:
            x1,y1 = ind1
            x2,y2 = ind2
            dis = math.sqrt((x2-x1)**2+(y2-y1)**2)

            self.dis_index.append(com_point)
            self.dis_value.append(dis)
            return dis

    def drawFancy(self):
        indexes = np.where(self.scene == 1)
        indexes = list(zip(indexes[0],indexes[1]))
        points = []
        lines = []


        for i in range(len(indexes)):
            for j, point in enumerate(indexes):
                if points:
                    if (not points[-1] ==  indexes[j]) and self.checkAdjacent(points[-1],indexes[j]) and (not indexes[j] in points):
                        points.append(indexes[j])
                else:
                    points.append(indexes[i])
            if not indexes[i] in points:
                points.append(indexes[i])

        head = -1
        for i,point in enumerate(points):
            if head < 0:
                head =  i
            if i < len(points)-1 and (not self.checkAdjacent(point,points[i+1])):
                lines.append(points[head:i+1])
                head = -1
            else:
                if i == len(points)-1:
                    lines.append([point])


        for line in lines:
            for i,point in enumerate(line):
                x,y = point
                if point == points[-1]:
                    self.controller.moveAt(x*10,y*10,True,False)
                else:
                    self.controller.moveAt(x*10,y*10,True,True)
        self.controller.initPos()
                
    def accurateDraw(self):
        indexes = np.where(self.scene == 1)
        indexes = list(zip(indexes[0],indexes[1]))

        # Get all adjacent points and place them next to each others
        points = []
        lines = []

        while len(indexes) > 0:
            if len(points) == 0:
                points.append(indexes[0])
                indexes.remove(indexes[0])
            else:
                indexes_len = len(indexes)
                data = self.findAdjacent(points[-1],indexes,points)
                if data:
                    _,indexes,points = data
                elif indexes_len == len(indexes):
                    points.append(indexes[0])
                    indexes.remove(indexes[0])

        for i,point in enumerate(points):
            if i < len(points)-1:
                x,y = point
                if self.checkAdjacent(point,points[i+1]):
                    self.controller.moveAt(x*10,y*10,True,True)
                else:
                    self.controller.moveAt(x*10,y*10,True,False)

        self.controller.initPos()

    def findAdjacent(self,index,indexes,points):
        for i in range(-1,2):
            for j in range(-1,2):
                x,y = index
                if (x+i,y+j) in indexes:
                    point = (x+i, y+j) 
                    if point in indexes and (not point in points):
                        points.append(point)
                        indexes.remove(point)
                        return (point,indexes,points)

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
                    if self.checkAdjacent(line["start"],index):
                        lines[-1]["end"] = index
                    else:
                        lines.append({"start":index,"end":None})
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