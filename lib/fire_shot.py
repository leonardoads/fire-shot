#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep
from menu import *
from tela import *

pygame.init()
arquivo = open('tipo_tela.fs')
tipo_tela = arquivo.read().strip()
arquivo.close()

#DEFINICAO DA TELA
tela = Tela("menu","menu.jpg", tipo_tela)

#DEFINICAO DO SOM
som_menu = pygame.mixer.music.load("music" + sep + "som_menu.mp3")
som_menu = pygame.mixer.music.play(-1)
som_helicoptero = pygame.mixer.music.load("music" + sep + "som_helicopter.mp3")
som_helicoptero = pygame.mixer.music.play(-1)


#DEFINICAO VIDEO
video_introducao = pygame.movie.Movie('videos' + sep + 'inicio2_menu.mpg')
video_introducao.play()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
				
		if event.type is KEYDOWN:
			video_introducao.stop()
			som_menu = pygame.mixer.music.stop()
			som_helicoptero = pygame.mixer.music.stop()
			menu()
		