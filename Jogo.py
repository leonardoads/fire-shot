#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
""" Metas
MELHORAR O CODIGO POIS ESTA MUITO REPETITIVO E COMPLEXO"""
import pygame
from sys import exit
from pygame.locals import *
from os import sep
#define a  inicializaçao da tela
class Tela:
	def __init__(self):
		self.screen_width, self.screen_height = 800,600
		self.screen = pygame.display.set_mode((self.screen_width,self.screen_height), 0, 32)
		pygame.display.set_caption("Fire shot")
		self.background = pygame.image.load('imagens'+ sep +"fase1" + sep + "fundo_fase1_0.png").convert()
		self.background_size = self.background.get_size()
		self.background_position= (400 - (self.background_size[0]/2), 300 - (self.background_size[1]/2))
	
class Leon(pygame.sprite.Sprite):
	images = []
	def __init__(self):
		self.leon =  pygame.sprite.Sprite()
		self.posicoes = ['up','left', 'right', 'down']
		self.images_mira_normal = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7)]
		self.images_mira_cima = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7,14)]
			
		
class Inimigo(pygame.sprite.Sprite):
	def __init__(self):
		self.sprite = pygame.sprite.Sprite()
		
class Tiro (pygame.sprite.Sprite):
	def __init__(self, leon_rect):
		self.leon = Leon()
		self.sprite = pygame.sprite.Sprite()
		self.direcao = ('normal','cima')
		self.image_tiro = pygame.image.load('imagens' + sep + 'tiro' + sep + 'bala.png').convert_alpha()		


def main():
	pygame.init()
	
	tela = Tela()
	
	#Definicao de Leon	
	leon = Leon()
	lista_leon_mira_normal = leon.images_mira_normal
	lista_leon_mira_cima =leon.images_mira_cima
	lista_imagem_leon_vez = lista_leon_mira_normal
	leon.image = lista_imagem_leon_vez[0]
	leon.rect = [0,480]
	seletor_image_leon = 0
	seletor_lista_imagem_da_vez = 'normal'
	controle_velocidade_troca_imagens = 0
	#definicao inimigo
	inimigo = Inimigo()
	lista_imagem_inimigo = [pygame.image.load('imagens' + sep + 'inimigo' + sep + 'inimigo_'+ str(i) + '.png') for i in xrange(6)]
	inimigo.rect = [750, 480]
	seletor_imagem_inimigo = 0
	
	#definicao do Tiro
	tiro = Tiro(leon.rect)
	tiro.image = tiro.image_tiro
	fogo_tiro = pygame.image.load('imagens' + sep + 'tiro' + sep + 'tiro1.png').convert_alpha()
	fogo_position = (leon.rect[0],leon.rect[1]+43)
	som_tiro = pygame.mixer.Sound("soms" + sep + "tiro.wav")
	atirar = False
	
	#verifica se o boneco deve se deslocar pra cima ou pra baixo
	desliza_cima = False
	desliza_baixo = False
	while True:
		for event in pygame.event.get():
			if event.type is pygame.QUIT:
				exit()
		
		#controla a velocidade do jogo
		clock = pygame.time.Clock()
		clock.tick(60)
		
		#Controla a posicao da bala para que ela sempre fique proxima da arma
	
		fogo_position = (leon.rect[0]+80,leon.rect[1]+39)
		
		if atirar == True:
			tiro.rect[0] = tiro.rect[0]+50
		else:
			tiro.rect = [leon.rect[0]+80,leon.rect[1]+43]
			
		if atirar and tiro.rect[0] > 800:
			atirar = False
		
		
		#Chamada das teclas
		pressed_keys = pygame.key.get_pressed()
		#controla a imagem a ser usada no  movimento de Leon
		if seletor_image_leon  > 6:
			seletor_image_leon = 0
		if seletor_imagem_inimigo >5:
			seletor_imagem_inimigo = 0
		
		#controla o deslizar do personagem na tela
		if desliza_cima and leon.rect[1] > 422:
			leon.rect[1] -= 10
		if desliza_baixo and leon.rect[1] < 480:
			leon.rect[1] += 10
			
		#define a imagem ,possibilita que se alterne e faz com que o inimigo se movimete
		inimigo.image = lista_imagem_inimigo[seletor_imagem_inimigo]
		inimigo.rect[0] -= 5
			
		if pressed_keys[K_RIGHT]:
			leon.image = lista_imagem_leon_vez[seletor_image_leon]
			leon.rect[0] += 10
		
		elif pressed_keys[K_LEFT]:
			leon.image = lista_imagem_leon_vez[seletor_image_leon]
			leon.rect[0] -= 10

		elif pressed_keys[K_UP]:
			desliza_cima = True
			desliza_baixo = False
			
		elif pressed_keys[K_DOWN]:
			desliza_baixo = True
			desliza_cima = False		
			
		else:
			seletor_image_leon = 0 
			leon.image = lista_imagem_leon_vez[0]
			
		if pressed_keys[K_RCTRL]:
			if seletor_lista_imagem_da_vez == 'normal':
				lista_imagem_leon_vez = lista_leon_mira_cima
				leon.image = lista_imagem_leon_vez[0]
				seletor_lista_imagem_da_vez = 'cima'
			elif seletor_lista_imagem_da_vez == 'cima':			
				lista_imagem_leon_vez = lista_leon_mira_normal
				leon.image = lista_imagem_leon_vez[0]
				seletor_lista_imagem_da_vez = 'normal'
		
		if pressed_keys[K_SPACE]:
			atirar = True
			som_tiro.play()
			
		if pygame.sprite.collide_mask(tiro, inimigo):
			inimigo.rect = [750, 480]
		tela.screen.fill((0,0,0))
		#colocacao da imagem de fundo na tela
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao dos personagens na tela
		tela.screen.blit(leon.image, leon.rect)
		tela.screen.blit(inimigo.image, inimigo.rect)
		if atirar and tiro.rect[0] < 800:
			tela.screen.blit(tiro.image , tiro.rect)
			tela.screen.blit(fogo_tiro , fogo_position)
			
		
		#atualiza a tela
		pygame.display.update()
		
		#faz com que as imagens dos personagens variem
		if controle_velocidade_troca_imagens % 5 == 0:
			seletor_image_leon += 1	
			seletor_imagem_inimigo += 1	
		controle_velocidade_troca_imagens += 1
if __name__ == '__main__':
	
	main()
