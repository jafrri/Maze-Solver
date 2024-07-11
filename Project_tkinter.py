from cgitb import small
from tkinter import Tk,Label, Button ,PhotoImage
import game
import time
import random
import time
from work import interim
import Kruskal
import pygame

def medium():
    Kruskal.generator("medium")
    game.run_game("small.txt")
def easy():
    Kruskal.generator("easy")
    game.run_game("small.txt")
def hard():
    Kruskal.generator("hard")
    game.run_game("small.txt")
def help():
    root= Tk()
    root.geometry("350x550")
    root.title("Help Menu")
    root.config(bg='light blue')
    labelx=Label(root,text="For decreasing speed Press c")
    labelp=Label(root,text="For increasing speed Press v")
    labelh=Label(root,text='For current location Press z')
    labelh1=Label(root,text='For destination location Press x')
    labely=Label(root,text="For hint Press t")
    labela=Label(root,text="Left movement by left key")
    labeld=Label(root,text="Right movement by right key")
    labelw=Label(root,text="Up movement by left key")
    labels=Label(root,text="Down movement by left key")
    labelx.place(x=100,y=50)
    labely.place(x=100,y=100)
    labela.place(x=100,y=150)
    labeld.place(x=100,y=200)
    labelw.place(x=100,y=250)
    labels.place(x=100,y=300)
    labelp.place(x=100,y=350)
    labelh.place(x=100,y=400)
    labelh1.place(x=100,y=450)
    button1=Button(root,text="Exit",command=root.destroy)
    button1.place(x=100,y=500)
window = Tk()
window .geometry("1072x500")
window.title("AMAZATHON")
bg=PhotoImage(file="maze.png")

pygame.mixer.init()
sound=pygame.mixer.Sound("game_intro.mpeg")
sound.play()

label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

label=Label(window,text="WELCOME TO AMAZATHON, A LAND OF CONFUSION",bd='5',font="Raleway",justify='center',bg="light blue")
label.place(x=300,y=50)

label2=Label(window,text='Select your Difficulty',bd='5',width=72,justify='center',bg="orange")
label2.place(x=300,y=100)


btn1 = Button(window, text = 'Exit', bd = '5',width=72,command=window.destroy,justify='center',bg='orange')
btn1.place(x=300,y=350)

btn3=Button(window,text="Medium",bd="5",width=72,command=medium,justify='center',bg='orange')
btn3.place(x=300,y=200)

btn3=Button(window,text="Easy",bd="5",width=72,command=easy,justify='center',bg='orange')
btn3.place(x=300,y=150)

btn3=Button(window,text="Hard",bd="5",width=72,command=hard,justify='center',bg='orange')
btn3.place(x=300,y=250)

btn3=Button(window,text="Help",bd="5",width=72,command=help,justify='center',bg='orange')
btn3.place(x=300,y=300)

window.mainloop()
