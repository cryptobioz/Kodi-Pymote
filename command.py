#!/bin/env/python
#-*- coding: UTF-8
from xbmcjson import XBMC, PLAYER_VIDEO
import pygame
from pygame.locals import *
import ConfigParser

def main(host, login, passwd):
    # Initialisation de la fenêtre d'affichage
    pygame.init()

    xbmc = XBMC(host, login, passwd)
    
    screen = pygame.display.set_mode((600, 336))
    pygame.display.set_caption('Remote Command for Kodi/XBMC')
 
    # Remplissage de l'arrière-plan
    background = pygame.image.load("kodi.png").convert()
    background = background.convert()
 
 
    # Blitter le tout dans la fenêtre
    screen.blit(background, (0, 0))
    pygame.display.flip()
    mute = 0
    fullscreen = 0
    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    xbmc.Input.Up()
                if event.key == K_DOWN:
                    xbmc.Input.Down()
                if event.key == K_LEFT:
                    xbmc.Input.Left()
                if event.key == K_RIGHT:
                    xbmc.Input.Right()
                # SELECT    
                if event.key == K_RETURN:
                    xbmc.Input.Select()
                # ECHAP
                if event.key == K_ESCAPE:
                    xbmc.Input.Home()
                # BACK
                if event.key == K_BACKSPACE:
                    xbmc.Input.Back()
                # CONTEXT MENU
                if event.key == K_c:
                    xbmc.Input.ContextMenu()
                # PLAY/PAUSE
                if event.key == K_SPACE:
                    xbmc.Player.PlayPause([PLAYER_VIDEO])
                # MUTE/UNMUTE
                if event.key == K_m:
                    if mute == 0:
                        mute = 1
                        xbmc.Application.SetMute({"mute":True})
                    else:
                        mute = 0
                        xbmc.Application.SetMute({"mute":False})
                # STOP
                if event.key == K_s:
                    xbmc.Player.Stop([PLAYER_VIDEO])
                # OSD
                if event.key == K_TAB:
                    xbmc.Input.ShowOSD()

        screen.blit(background, (0, 0))
        pygame.display.flip()
 
if __name__ == "__main__":
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.read("config.txt")
    host = config.get('config', 'host')
    login = config.get('config', 'login')
    passwd = config.get('config', 'passwd')

    main(host, login, passwd)