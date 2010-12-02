#!/usr/bin/env python
# *-* coding: utf-8 *-*
import pygame
from pygame.locals import *
from sys import exit
from os import sep
from tela import *

def Zerando():
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
		
	pygame.init()

	tela = Tela(None,None,tipo_tela)

	image = pygame.image.load('imagens' + sep + "imagens" + sep + "zerando.png").convert_alpha()
	
	img_width, img_height = image.get_size()

	x, y = tela.screen_width/2 - img_width/2, tela.screen_height/2 - img_height/2;

	varia_x, varia_y = 1, 1

	anglo = 0
	zoom = 0
	a = ''
	
	while True:
		clock = pygame.time.Clock()
		clock.tick(60)
		for event in pygame.event.get():
			if event.type is QUIT:
				exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_RETURN:
					a= 'menu'
					exit()
					
		if a == 'menu':
			return 'menu'

		if x + img_width >= tela.screen_width or x <= 0:
			varia_x = -varia_x

		if y + img_height >= tela.screen_height or y <= 0:
			varia_y = -varia_y

		x += varia_x
		y += varia_y

		anglo += 0.5
		if zoom < 1:
			zoom += 0.001
		elif zoom == 1:
			zoom = 0
			
		tela.screen.blit(pygame.transform.rotozoom(image, anglo, zoom), (x, y))

		pygame.display.flip() 
#Zerando()


