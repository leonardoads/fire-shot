#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep
from menu import *
screen_width, screen_height = 800,600

pygame.init()
#DEFINICAO DA TELA
screen = pygame.display.set_mode((screen_width,screen_height), FULLSCREEN, 32)
pygame.display.set_caption("Fire shot")

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
		
