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
		self.background = pygame.image.load('imagens'+ sep +"fase2" + sep + "caminho2.png").convert_alpha()
		self.background_size = self.background.get_size()
		self.background_position= [0,0]
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
	mor = False
	novo_inimigo, novo_inimigo_heli = 0, 0
	
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
	
	#DEFINICAO OBSTACULOS:
	pedra = pygame.image.load("imagens"+sep+"imagens"+sep+"pedra2.bmp")
	ponte = pygame.image.load("imagens"+sep+"imagens"+sep+"ponte1.png")
	def obstaculo_type1(pedra):
		pedra_position = [tela.background_position[0] + 600,tela.background_position[1] + 500]
		if pedra_position[0] < 0:
			pedra_position[0] += 1000
		tela.screen.blit(pedra,pedra_position)
		global ret_pedra1
		ret_pedra1 = pygame.Rect(pedra_position[0],pedra_position[1] + 100,pedra.get_size()[0],pedra.get_size()[1])
	def obstaculo_type2(pedra):
		pedra_position = [tela.background_position[0] + 1000,tela.background_position[1] + 450]
		tela.screen.blit(pedra,pedra_position)
		global ret_pedra2
		ret_pedra2 = pygame.Rect(pedra_position[0],pedra_position[1]-100,pedra.get_size()[0],pedra.get_size()[1])
	def ponte1(ponte):
		ponte_position = [tela.background_position[0] + 2000,tela.background_position[1] + 410]
		tela.screen.blit(ponte,ponte_position)
		global ret_ponte1
		ret_ponte1 = pygame.Rect(ponte_position[0],ponte_position[1] - 100,ponte.get_size()[0],ponte.get_size()[1])
	image_fundo = pygame.image.load('imagens'+ sep +"fase2" + sep + "fundo_fase2.jpg").convert()
	image_fundo_position = [-470,0]
	while True:
		obstaculo_type2(pedra)
		obstaculo_type1(pedra)
		ponte1(ponte)
		ret_player = pygame.Rect(leon.rect[0],leon.rect[1],leon.image.get_size()[0],leon.image.get_size()[1])
		lista_ret = [ret_pedra1,ret_pedra2,ret_ponte1]
		for event in pygame.event.get():
			if event.type is pygame.QUIT:
				exit()
			if event.type is KEYDOWN:
				if pressed_keys[K_o]:
					if seletor_lista_imagem_da_vez == 'normal':
						lista_imagem_leon_vez = lista_leon_mira_cima
						leon.image = lista_imagem_leon_vez[0]
						seletor_lista_imagem_da_vez = 'cima'
					elif seletor_lista_imagem_da_vez == 'cima':			
						lista_imagem_leon_vez = lista_leon_mira_normal
						leon.image = lista_imagem_leon_vez[0]
						seletor_lista_imagem_da_vez = 'normal'
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
		if mor == True and novo_inimigo % 100 == 0:
			x1,y1 = 750, 450
			mor = False
		
		
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
		if pressed_keys[K_ESCAPE]:
			break
		if pressed_keys[K_RIGHT] and ret_player.collidelist(lista_ret) == -1:
			fogo_position = (leon.rect[0]+85,leon.rect[1]+25)
			leon.image = lista_imagem_leon_vez[seletor_image_leon]
			if leon.rect[0] > 400 and tela.background_position[0] > -7200:
				tela.background_position[0] -= 10
			else:
				leon.rect[0] += 10
				
		elif pressed_keys[K_LEFT] and ret_player.collidelist(lista_ret) == -1:
			fogo_position = (leon.rect[0]+85,leon.rect[1]+25)
			leon.image = lista_imagem_leon_vez[seletor_image_leon]
			if leon.rect[0] < 0 and tela.background_position[0] >0:
				tela.background_position[0] += 10
			else:
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
#		if pressed_keys[K_i] and pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
#			leon.image = lista_imagem_leon_vez[seletor_image_leon]
#			cont = 0
#			for dist in range(25):
#				leon.rect[1] -= 6
#				if (leon.rect[0] - 8) >= 0:
#					leon.rect[0] -= 4
#				tela.screen.blit(tela.background, tela.background_position)
#				tela.screen.blit(leon.image, leon.rect)
#				pygame.display.update()
#			for dis in range(25):
#				leon.rect[1] += 6
#				if (leon.rect[0] - 4) >= 0:
#					leon.rect[0] -= 4
#				leon.rect[0] -= 4
#				tela.screen.blit(tela.background, tela.background_position)
#				tela.screen.blit(leon.image, leon.rect)
#				pygame.display.update()
#			leon.image = lista_imagem_leon_vez[seletor_image_leon]
#		if pressed_keys[K_i] and not pressed_keys[K_LEFT] and pressed_keys[K_RIGHT]:
#			leon.image = lista_imagem_leon_vez[seletor_image_leon]
#			cont = 0
#			for dist in range(25):
#				leon.rect[1] -= 6
#				if (leon.rect[0] + 8) <= 400:
#					leon.rect[0] += 4
#				leon.rect[0] += 4
#				tela.screen.blit(tela.background, tela.background_position)
#				tela.screen.blit(leon.image, leon.rect)
#				pygame.display.update()
#			for dis in range(25):
#				leon.rect[1] += 6
#				if (leon.rect[0] + 4) <= 400:
#					leon.rect[0] += 4
#				tela.screen.blit(tela.background, tela.background_position)
#				tela.screen.blit(leon.image, leon.rect)
#				pygame.display.update()
#			leon.image = lista_imagem_leon_vez[seletor_image_leon]
			
#		if pressed_keys[K_a]:
#			if seletor_lista_imagem_da_vez == 'normal':
#				lista_imagem_leon_vez = lista_leon_mira_cima
#				leon.image = lista_imagem_leon_vez[0]
#				seletor_lista_imagem_da_vez = 'cima'
#			elif seletor_lista_imagem_da_vez == 'cima':			
#				lista_imagem_leon_vez = lista_leon_mira_normal
#				leon.image = lista_imagem_leon_vez[0]
#				seletor_lista_imagem_da_vez = 'normal'
		
		if pressed_keys[K_p]:
			atirar = True
			som_tiro.play()
			
		if pygame.sprite.collide_mask(tiro, inimigo):
			inimigo.rect = [750, 480]
			mor = True
		tela.screen.fill((0,0,0))
		
		#blita a imagem do inimigo
		
		tela.screen.fill((0,0,0))
		#colocacao da imagem de fundo na tela
		tela.screen.blit(image_fundo, image_fundo_position)
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao obstaculo2:
		obstaculo_type2(pedra)
		
		#colocacao ponte
		ponte1(ponte)
		#colocacao dos personagens na tela
		tela.screen.blit(leon.image, leon.rect)
		
		#colocacao obstaculo1:
		obstaculo_type1(pedra)
		
		if (mor == False):
			tela.screen.blit(inimigo.image,inimigo.rect)
			#inimigo.rect[0] -= 5
		#tela.screen.blit(inimigo.image, inimigo.rect)
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
		novo_inimigo += 1
if __name__ == '__main__':
	
	main()
