import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint
from playsound import playsound

CELL_COUNT = 8
CELL_SIZE = 75
GRID_ORIGINX = 150
GRID_ORIGINY = 150
W_WIDTH = 900
W_HEIGHT = 900

class TribeBubbles(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tribe Bubbles')
        self.setGeometry(100, 100, W_WIDTH, W_HEIGHT)
        self.__board=[[1 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]
        self.__list=list()
        self.__gameover=False
        self.__score=0
        self.__multiplier=1
        self.show()

    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                qp.setPen(QPen(Qt.black, 2))
                qp.setBrush(QBrush(Qt.white))
                qp.drawRect(col*CELL_SIZE+GRID_ORIGINX,row*CELL_SIZE+GRID_ORIGINY,CELL_SIZE,CELL_SIZE)
                if self.__board[row][col]==-1:
                    qp.setPen(QPen(Qt.gray,1))
                    qp.setBrush(QBrush(Qt.gray))
                    qp.drawRect(col*CELL_SIZE+GRID_ORIGINX+CELL_SIZE//25,row*CELL_SIZE+GRID_ORIGINY+CELL_SIZE//20,CELL_SIZE-CELL_SIZE//10,CELL_SIZE-CELL_SIZE//10)
                elif self.__board[row][col]==0:
                    qp.setPen(QPen(Qt.blue,3))
                    qp.drawEllipse(col*CELL_SIZE+GRID_ORIGINX+CELL_SIZE//25,row*CELL_SIZE+GRID_ORIGINY+CELL_SIZE//15,CELL_SIZE-CELL_SIZE//10,CELL_SIZE-CELL_SIZE//10)
        qp.setPen(QPen(Qt.black,1))
        qp.drawText(375,775,'Score: '+str(self.__score))
        qp.drawText(450,775,'Multiplier: X '+str(self.__multiplier))
        #check for game over
        if 1 not in self.__board[0] and 1 not in self.__board[1] and 1 not in self.__board[2] and 1 not in self.__board[3]\
        and 1 not in self.__board[4] and 1 not in self.__board[5] and 1 not in self.__board[6] and 1 not in self.__board[7]:
            self.__gameover=True
            qp.setPen(QPen(Qt.red))
            qp.drawText(315,100,'Game Over! Click restart to begin a new game.')
        #reset button
        qp.setPen(QPen(Qt.black,1))
        qp.setBrush(QBrush(Qt.red))
        qp.drawRect(25,25,50,50)
        qp.drawText(32,50,'RESET')
        qp.end()

    def mousePressEvent(self,event):
        if 25<event.x()<75 and 25<event.y()<75:             #reset button
            self.__score=0
            self.__multiplier=1
            self.__gameover=False
            self.__board=[[1 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]
        if self.__gameover==True:
            return
        col=(event.x()-GRID_ORIGINX)//CELL_SIZE
        row=(event.y()-GRID_ORIGINY)//CELL_SIZE
        if 0<=col<=7 and 0<=row<=7:
            if self.__board[row][col]==1:
                self.__board[row][col]=0
                clickEvent=True
            else:
                clickEvent=False
            self.__checkLines()
            self.__score_checker()
            if clickEvent==True:
                self.__board[randint(0,7)][randint(0,7)]=-1
        self.update()

    def __checkLines(self):
        w=0
        x=0
        y=0
        z=0
        #vertical
        for row in range(5):
            for col in range(8):
                if self.__board[row][col]==self.__board[row+1][col]==self.__board[row+2][col]==self.__board[row+3][col]==0:
                    for i in range(4):
                        if [row+i,col] not in self.__list:
                            self.__list.append([row+i,col])
                    w=1
        #horizontal
        for row in range(8):
            for col in range(5):
                if self.__board[row][col]==self.__board[row][col+1]==self.__board[row][col+2]==self.__board[row][col+3]==0:
                    for j in range(4):
                        if [row,col+j] not in self.__list:
                            self.__list.append([row,col+j])
                    x=1
        #diagonal upleft
        for row in range(5):
            for col in range(5):
                if self.__board[row][col]==self.__board[row+1][col+1]==self.__board[row+2][col+2]==self.__board[row+3][col+3]==0:
                    for n in range(4):
                        if [row+n,col+n] not in self.__list:
                            self.__list.append([row+n,col+n])
                    y=1
        #diagonal upright
        for row in range(5):
            for col in range(8):
                if self.__board[row][col]==self.__board[row+1][abs(col-1)]==self.__board[row+2][abs(col-2)]==self.__board[row+3][abs(col-3)]==0:
                    for n in range(4):
                        if [row+n,abs(col-n)] not in self.__list:
                            self.__list.append([row+n,col-n])
                    z=1
        if w==x==y==z==0:
            self.__multiplier=1
        else:
            self.__multiplier=(w+x+y+z)**2
        print(self.__list)

    def __score_checker(self):
        for coord in self.__list:
            self.__board[coord[0]][coord[1]]=1
            self.__score+=1*self.__multiplier
        self.__list.clear()
        self.update()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeBubbles()
  sys.exit(app.exec_())
