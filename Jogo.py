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
	background = pygame.image.load('imagens'+ sep +"fase1" + sep + "fundo_fase1_0.png")
	background_size = background.get_size()
	background_position= (400 - (background_size[0]/2), 300 - (background_size[1]/2))
	
	#Definicao de Leon
	leon = Leon()
	lista_image_leon = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png') for i in xrange(7)]
	leon.image = lista_image_leon[0]
	leon.rect = [0,450]

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			
		#Chamada das teclas
		pressed_keys = pygame.key.get_pressed()

		# Movimentacao da cobra
		#if pressed_keys[K_UP]:
			#nova_direcao = 'cima'
		#elif pressed_keys[K_DOWN]:
			#nova_direcao = 'baixo'
		i = 0
		if pressed_keys[K_SPACE]:
			som_tiro = pygame.mixer.music.load("soms" + sep + "tiro.mp3")
			som_tiro = pygame.mixer.music.play(-1)
			bala = pygame.image.load('imagens' + sep + 'tiro' + sep + 'bala.png').convert()
			x = leon.rect[:]
			x[1] += 30
			x[0] += 80
			for i in xrange(20):
				screen.blit(background, background_position)
				screen.blit(bala, x)
				screen.blit(leon.image, leon.rect)
				pygame.display.update()
				x[0] += 30
			som_tiro = pygame.mixer.music.stop()
		if pressed_keys[K_s]:
                        break
		if pressed_keys[K_RIGHT]:
			leon.rect[0] += 10
			for i in xrange(7):
				leon.image = lista_image_leon[i]
				leon.rect[0] += 5
				screen.fill((0,0,0))
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				
				pygame.display.update()
		elif pressed_keys[K_LEFT]:
			leon.rect[0] -= 10
			for i in xrange(7):
				leon.image = lista_image_leon[i]
				leon.rect[0] -= 5
				screen.fill((0,0,0))
				screen.blit(background, background_position)
				screen.blit(leon.image, leon.rect)
				
				pygame.display.update()
		else:
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
		
		#atualiza a tela
		pygame.display.update()

if __name__ == '__main__':
	
	main()
