#!/bin/env/python
#-*- coding: UTF-8
from xbmcjson import XBMC, PLAYER_VIDEO
from Tkinter import *
from PIL import ImageTk, Image
import ConfigParser, Image, ImageTk

def goUp(event):
    xbmc.Input.Up()
def goDown(event):
    xbmc.Input.Down()
def goRight(event):
    xbmc.Input.Right()
def goLeft(event):
    xbmc.Input.Letf()
def goHome(event):
    xbmc.Input.Home()
def Select(event):
    xbmc.Input.Select()
def goBack(event):
    xbmc.Input.Back()
def ContextMenu(event):
    xbmc.Input.ContextMenu()
def Play_Pause(event):
    xbmc.Player.PlayPause([PLAYER_VIDEO])
def Mute(event):
    if m == 0:
        m = 1
        xbmc.Application.SetMute({"mute":True})
    else:
        m = 0
        xbmc.Application.SetMute({"mute":False})

def Stop(event):
    xbmc.Player.Stop([PLAYER_VIDEO])

def Fullscreen(event):
    if fullscreen == 0:
        fullscreen = 1
        xbmc.GUI.SetFullscreen({"fullscreen":True})
    else:
        fullscreen = 0
        xbmc.GUI.SetFullscreen({"fullscreen":False})

def ShowOSD(event):
    xbmc.Input.ShowOSD()


def main(host, login, passwd):
    # Initialisation de la fenêtre d'affichage
    root = Tk()

    global xbmc, fullscreen
    xbmc = XBMC("http://"+host+"/jsonrpc", login, passwd)
    

    root.title('Remote Control for Kodi/XBMC')
    root.geometry('600x336')
    
    image = Image.open("kodi.jpg") 
    photo = ImageTk.PhotoImage(image) 
 
    canvas = Canvas() 
    canvas.create_image(200,500, image=photo)
    canvas.pack() 

    running = Label(root, text="Pymote is running ...")
    running.pack()

    mute = 0
    fullscreen = 0
    # Boucle d'évènements
    root.bind("<Up>", goUp)
    root.bind("<Down>", goDown)
    root.bind("<Right>", goRight)
    root.bind("<Left>", goLeft)
    root.bind("<Escape>", goHome)
    root.bind("<Return>", Select)
    root.bind("<BackSpace>", goBack)
    root.bind("c", ContextMenu)
    root.bind("<space>", Play_Pause)
    root.bind("m", Mute)
    root.bind("s", Stop)
    root.bind('f', Fullscreen)
    root.bind("<Tab>", ShowOSD)

    root.mainloop()

def register(config, host_var, user_var, pass_var, root):
    config_file = open("config.txt",'w')

    config.set('config', 'host', host_var.get())
    config.write(config_file)
    config_file.close()
    root.destroy()

def Intercepte():
    sys.exit()
def intro(host, login, passwd, config):
    root = Tk()
    root.title('Remote controller configuration')
    root.geometry('600x336')
    
    host_label = Label(root, text="Host")
    host_label.pack()

    host_var = StringVar()
    host_var.set(host)
    host_widget = Entry(root, textvariable=host_var, width=30)
    host_widget.pack()

    user_label = Label(root, text="Login")
    user_label.pack()

    user_var = StringVar()
    user_var.set(login)
    user_widget = Entry(root, textvariable=user_var, width=30)
    user_widget.pack()

    pass_label = Label(root, text="Password")
    pass_label.pack()
    pass_var = StringVar()
    pass_var.set(passwd)
    pass_widget = Entry(root, textvariable=pass_var, width=30)
    pass_widget.pack()

    go_button = Button(root, text="Go", command=lambda:register(config, host_var, user_var, pass_var, root))
    go_button.pack()

    root.protocol("WM_DELETE_WINDOW", Intercepte) 
    root.mainloop()
    

if __name__ == "__main__":
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.read("config.txt")
    host = config.get('config', 'host')
    login = config.get('config', 'login')
    passwd = config.get('config', 'passwd')

    while 1:
        intro(host, login, passwd, config)

        main(host, login, passwd)