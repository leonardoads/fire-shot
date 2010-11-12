#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep
class Leon(pygame.sprite.Sprite):
	def __init__(self ):
		self.sprite =  pygame.sprite.Sprite()

def main():
	screen_width, screen_height = 800,600
	
	pygame.init()
	#DEFINICAO DA TELA
	screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
	pygame.display.set_caption("Fire shot")

	#definicao da imagem de fundo
	background = pygame.image.load('imagens'+ sep +"fase1" + sep + "fundo_fase1_0.png").convert()
	background_size = background.get_size()
	background_position= (400 - (background_size[0]/2), 300 - (background_size[1]/2))
	
	#Definicao de Leon
	leon = Leon()
	lista_image_leon = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png') for i in xrange(14)]
	leon.image = lista_image_leon[0]
	leon.rect = [0,450]
	
	#definicao inimigo
	inimigo = pygame.image.load('imagens' + sep + 'inimigo' + sep + 'inimigo.png')
	x1,y1 = 750, 450
	
	mor = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		#Chamada das teclas
		pressed_keys = pygame.key.get_pressed()

		if pressed_keys[K_UP]:
			leon.image = lista_image_leon[7]
			screen.blit(leon.image,(leon.rect))
			pygame.display.update()
		i = 0
		if pressed_keys[K_x] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
			leon.image = lista_image_leon[1]
			cont = 0
			for dist in range(25):
				leon.rect[1] -= 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			for dis in range(25):
				leon.rect[1] += 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			leon.image = lista_image_leon[0]
		if pressed_keys[K_x] and not pressed_keys[K_LEFT] and pressed_keys[K_RIGHT]:
			leon.image = lista_image_leon[1]
			cont = 0
			for dist in range(25):
				leon.rect[1] -= 4
				leon.rect[0] += 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			for dis in range(25):
				leon.rect[1] += 4
				leon.rect[0] += 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			leon.image = lista_image_leon[0]
		if pressed_keys[K_x] and pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] :
			leon.image = lista_image_leon[1]
			cont = 0
			for dist in range(25):
				leon.rect[1] -= 4
				leon.rect[0] -= 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			for dis in range(25):
				leon.rect[1] += 4
				leon.rect[0] -= 4
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
			leon.image = lista_image_leon[0]
		x = leon.rect[:]
		if pressed_keys[K_SPACE]:
			som_tiro = pygame.mixer.Sound("soms" + sep + "tiro.wav")
			som_tiro.play()
			bala = pygame.image.load('imagens' + sep + 'tiro' + sep + 'bala.png').convert_alpha()
			cont = 0
			fogo_tiro = pygame.image.load('imagens' + sep + 'tiro' + sep + 'tiro1.png').convert_alpha()
			if not pressed_keys[K_UP]:
				x[1] += 40
				x[0] += 80
				local_fogo = x[:]
				local_fogo[1] -= 5
				for i in xrange(20):
					screen.blit(background, background_position)
					screen.blit(bala, x)
					if cont >= 0 and cont <= 5:
						screen.blit(fogo_tiro, local_fogo)
						cont += 1
					screen.blit(leon.image, leon.rect)
					pygame.display.update()
					x[0] += 30
					if x[1] == x1:
						mor == True
			if pressed_keys[K_UP]:
				x[1] += 0
				x[0] += 70
				#local_fogo = x[:]
				leon.image = lista_image_leon[7]
				for i in xrange(20):
					screen.blit(background, background_position)
					screen.blit(bala, x)
					#if cont == 0 and cont <= 5:
					#	screen.blit(fogo_tiro, local_fogo)
					#	cont += 1
					screen.blit(leon.image, leon.rect)
					pygame.display.update()
					x[0] += 30
					x[1] -= 20
					if x[1] == x1:
						mor == True
		if pressed_keys[K_s]:
			break
		if pressed_keys[K_RIGHT]:
			leon.rect[0] += 10
			if not pressed_keys[K_UP]:
				for i in xrange(7):
					leon.image = lista_image_leon[i]
					leon.rect[0] += 5
					screen.fill((0,0,0))
					screen.blit(background, background_position)
					screen.blit(leon.image, leon.rect)
			elif pressed_keys[K_UP]:
				for i in range(7,14):
					leon.image = lista_image_leon[i]
					leon.rect[0] += 5
					screen.fill((0,0,0))
					screen.blit(background, background_position)
					screen.blit(leon.image, leon.rect)
			pygame.display.update()
		elif pressed_keys[K_LEFT] and not pressed_keys[K_UP]:
			leon.rect[0] -= 10
			for i in xrange(7):
				leon.image = lista_image_leon[i]
				leon.rect[0] -= 5
				screen.fill((0,0,0))
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
		if not pressed_keys[K_UP]:
			leon.image = lista_image_leon[0]		
		#elif pressed_keys[K_LEFT]:
			#nova_direcao = 'esquerda'
		#elif pressed_keys[K_e]:
			#screen.fill(black)
			#break
					#leon.rect[0] += 10
				
		#colocacao da imagem de fundo na tela
		screen.blit(background, background_position)
		
		#colocacao do boneco na tela
		screen.blit(leon.image, leon.rect)

		#colocacao do inimigo na tela
		if mor == False:
			screen.blit(inimigo,(x1,y1))
			x1 -= 1	
		#else:
	#		screen.blit(inimigo,(x1,y1))
		#atualiza a tela
		pygame.display.update()

if __name__ == '__main__':
	
	main()
