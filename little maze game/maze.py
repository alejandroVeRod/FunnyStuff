import random
import os

MAX_WIDTH=10
MAX_LENGTH=10


class file_read():
    def start(self):
        file=open(str(os.getcwd()+"/story.txt"),"r")
        for linea in file.readlines():
            print(linea)
        file.close()

class cell():
    def __init__(self):
        self.up=random.randint(0,1)
        self.down=random.randint(0,1)
        self.left=random.randint(0,1)
        self.right=random.randint(0,1)
    def __str__(self):
        return "<Cell-> up(%s) down(%s) left(%s) right(%s)>" % (self.up,self.down,self.left,self.right)

class position():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "The position is (%s,%s)" % (self.x,self.y)
class player():
    def __init__(self,maze):
        self.pos=position(random.randint(0,MAX_WIDTH),random.randint(0,MAX_LENGTH))
        self.cell=maze[self.pos.x][self.pos.y]
    def __str__(self):
        print(self.pos)
    def update_cell(self,maze):
        self.cell=maze[self.pos.x][self.pos.y]
    def move(self,op,maze):
        if(op=='up'):
            self.pos.y=self.pos.y-1
        if(op=='down'):
            self.pos.y=self.pos.y+1
        if(op=='right'):
            self.pos.x=self.pos.x+1
        if(op=='left'):
            self.pos.x=self.pos.x-1
        self.update_cell(maze)
             
def entrada(player,maze):
    while(1):
        player.move(input(),maze)
        print(player.pos)
        print(player.cell)
        
            


        
def main():
    maze=[[cell() for x in range(MAX_WIDTH)] for y in range(MAX_LENGTH)]
    pl = player(maze)
    entrada(pl,maze)

    

main()

