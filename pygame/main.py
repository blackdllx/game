import tkinter as tk
import random2

# move vectors
ACTIMEMOVE={"Up":False,"Down":False,"Left":False,"Right":False}
COUNT=0
INGAME = 0
width=600
height=400
# Set window
window = tk.Tk()
# Set window icon
window.iconbitmap("favico.ico")
# set window title
window.title("some game")
# set window size
window.geometry('600x400+50+50')
# set background color
window.configure(background="#07cc9b")
# set window size permanently
window.minsize(width, height)
window.maxsize(width, height)
# create game frame
playShield = tk.Frame(window,
                      bg="#07cc9b",
                      height=height,
                      width=width)
playShield.pack()
# create game canvas
playShieldCanvas = tk.Canvas(playShield,
                             height=390,
                             bg="#6DECAF",
                             width=590)
# load game canvas
playShieldCanvas.pack()
playShieldCanvas.focus_set()
# player class
class player(object):
    # load
    def __init__(self):
        # create player circle
        self.player = playShieldCanvas.create_oval(50,50,100,100,
                                                   activefill="#D1D1C7",
                                                   fill="#DFDFB4",
                                                   activeoutline="#D1D1C7",
                                                   outline="#D1D1C7")
    # moving part 1
    def movedown(self,event):

        if event.keysym == "Down":
            ACTIMEMOVE["Down"]=True

        if event.keysym == "Left":
            ACTIMEMOVE["Left"] = True

        if event.keysym == "Up":
            ACTIMEMOVE["Up"]=True

        if event.keysym == "Right":
            ACTIMEMOVE["Right"]=True
    # moving part 2
    def moveup(self,event):
        if event.keysym == "Down":
            ACTIMEMOVE["Down"]=False

        if event.keysym == "Left":
            ACTIMEMOVE["Left"] = False

        if event.keysym == "Up":
            ACTIMEMOVE["Up"]=False

        if event.keysym == "Right":
            ACTIMEMOVE["Right"]=False
    # moving part 3
    def move(self):

        if ACTIMEMOVE["Up"] == True:
            x1, y1, x2, y2 = playShieldCanvas.coords(self.player)
            if y1 != 0:
                playShieldCanvas.coords(self.player,
                                        x1, y1 - 5,
                                        x2, y2 - 5)
        if ACTIMEMOVE["Down"] == True:
            x1, y1, x2, y2 = playShieldCanvas.coords(self.player)
            if y2 != 390:
                playShieldCanvas.coords(self.player,
                                        x1,y1+5,
                                        x2,y2+5)
        if ACTIMEMOVE["Left"] == True:
            x1, y1, x2, y2 = playShieldCanvas.coords(self.player)
            if x1 != 0:
                playShieldCanvas.coords(self.player,
                                        x1-5, y1,
                                        x2-5, y2)
        if ACTIMEMOVE["Right"] == True:
            x1, y1, x2, y2 = playShieldCanvas.coords(self.player)
            if x2!=590:
                playShieldCanvas.coords(self.player,
                                        x1+5, y1,
                                        x2+5, y2)
    # get player position
    def getPos(self):
        return(playShieldCanvas.coords(self.player))

    def dell(self):
        playShieldCanvas.delete(self.player)
# virus class
class virus(object):
    # load
    def __init__(self):
        # create counts
        self.count=0
        self.viruses=[]
        self.lenvirus=4
        # create viruses
        for i in range(self.lenvirus):
            x = random2.randint(0, 590)
            y = random2.randint(0, 390)

            b = playShieldCanvas.create_oval(x, y,
                                             x + 40, y + 40,
                                             fill="#F61067",
                                             outline="#F61067")
            vector = random2.randint(0, 1)
            vector2 = random2.randint(0, 1)
            vector = [vector, vector2]
            b = [b, vector]
            self.viruses.append(b) # add ready virus to massive
    # delete all viruses
    def dell(self):
        for i in self.viruses:
            playShieldCanvas.delete(i[0])
    # move all viruses
    def move(self):
        for i in self.viruses:

            x1,y1,x2,y2 = playShieldCanvas.coords(i[0])
            if x1<=0:
                i[1][0]=1

            if x2>=590:
                i[1][0]=0

            if y1<=0:
                i[1][1]=1

            if y2>=390:
                i[1][1]=0

            if i[1][0] == 1:
                x1, y1, x2, y2 = playShieldCanvas.coords(i[0])
                playShieldCanvas.coords(i[0],
                                        x1 + 1, y1,
                                        x2 + 1, y2)

            if i[1][1] == 1:
                x1, y1, x2, y2 = playShieldCanvas.coords(i[0])
                playShieldCanvas.coords(i[0],
                                        x1, y1+1,
                                        x2, y2+1)

            if i[1][0] == 0:
                x1, y1, x2, y2 = playShieldCanvas.coords(i[0])
                playShieldCanvas.coords(i[0],
                                        x1 - 1, y1,
                                        x2 - 1, y2)

            if i[1][1] == 0:
                x1, y1, x2, y2 = playShieldCanvas.coords(i[0])
                playShieldCanvas.coords(i[0],
                                        x1, y1-1,
                                        x2, y2-1)
    # viruses AI
    def checkCount(self,pl):
        # print(self.viruses)
        px1,py1,px2,py2=pl.getPos()
        t=0
        for i in self.viruses:
            x1,y1,x2,y2=playShieldCanvas.coords(i[0])

            if x1 < px1 <x2 and y1<py1<y2 or x1 < px2 <x2 and y1<py2<y2:
                self.count += 1
                playShieldCanvas.delete(i[0])
                self.viruses.pop(t)

            t+=1
    # retry viruses on death
    def update(self):
        if len(self.viruses) != self.lenvirus:
            x = random2.randint(0, 590)
            y = random2.randint(0, 390)

            b = playShieldCanvas.create_oval(x, y,
                                             x + 50, y + 50,
                                             fill="#F61067",
                                             outline="#F61067")
            vector = random2.randint(0, 1)
            vector2 = random2.randint(0, 1)
            vector = [vector, vector2]
            b = [b, vector]
            self.viruses.append(b)
# killer class
class killer(object):
    def __init__(self):
        self.size = 60
        self.ingame=1
        self.x1=random2.randint(0,590-self.size)
        self.y1=random2.randint(0,390-self.size)
        self.x2=self.x1+self.size
        self.y2=self.y1+self.size
        self.killer= playShieldCanvas.create_oval(self.x1,self.y1,
                                                  self.x2,self.y2,
                                                  fill="#5E239D",
                                                  activefill="#48197A",
                                                  outline="#5E239D",
                                                  activeoutline="#5E239D")
        self.vector=[random2.randint(0,1),random2.randint(0,1)]

    def move(self):
        self.x1,self.y1,self.x2,self.y2=playShieldCanvas.coords(self.killer)
        print("x1:{}, y1:{}, x2:{}, y2:{}".format(self.x1,self.y1,self.x2,self.y2))
        print("vector:{}".format(self.vector))
        if self.x1<=0:
            self.vector[0]=1


        if self.x2>=590:
            self.vector[0]=0

        if self.y1<=0:
            self.vector[1]=1

        if self.y2>=390:
                self.vector[1]=0

        if self.vector[0] == 1:
                x1,y1,x2,y2=playShieldCanvas.coords(self.killer)
                playShieldCanvas.coords(self.killer,
                                        x1 + 1, y1,
                                        x2 + 1, y2)

        if self.vector[0] == 0:
                x1, y1, x2, y2 = playShieldCanvas.coords(self.killer)
                playShieldCanvas.coords(self.killer,
                                        x1 - 1, y1,
                                        x2 - 1, y2)


        if self.vector[1] == 0:
                x1, y1, x2, y2 = playShieldCanvas.coords(self.killer)
                playShieldCanvas.coords(self.killer,
                                        x1, y1-1,
                                        x2, y2-1)
        if self.vector[1] == 1:
            x1, y1, x2, y2 = playShieldCanvas.coords(self.killer)
            playShieldCanvas.coords(self.killer,
                                    x1, y1 + 1,
                                    x2, y2 + 1)

    def kill(self):
        px1,py1,px2,py2=pl.getPos()
        if self.x1 < px1 < self.x2 and self.y1 < py1 < self.y2 or self.x1 < px2 < self.x2 and self.y1 < py2 < self.y2:
            vr.dell()
            self.ingame=0
            playShieldCanvas.delete(self.killer)
            pl.dell()
# counter
count = tk.Label(playShield, text="Loading", foreground="black",background="#6DECAF")
count.place(y=10,x=10)
# game loop func
def main():
    global INGAME
    # if game pending
    if INGAME:
        # move player
        pl.move()
        vr.move()
        vr.checkCount(pl)
        vr.update()
        kl.move()
        kl.kill()

        if kl.ingame == 0:
            INGAME=0

        count.configure(text="Score is: {}".format(vr.count))

    else:
        restart.place(y=190, x=290)

    # retry func
    window.after(10,main)

# Start
def start():
    restart.place_forget()
    global pl, vr, kl, INGAME
    # create class example
    pl = player()
    kl = killer()
    vr = virus()
    # bind move keys
    playShieldCanvas.bind_all("<KeyPress>", pl.movedown)
    playShieldCanvas.bind_all("<KeyRelease>", pl.moveup)
    # run game loop func
    INGAME = 1


imp = tk.PhotoImage(file="button.png")
# restart = tk.Button(playShield, text="restart",foreground="black",background="#6DECAF",command=start)
restart = tk.Button(playShield,image=imp, border=0,background="#6DECAF",command=start)
if __name__ == "__main__":
    start()
    main()
    # window update loop
    window.mainloop()