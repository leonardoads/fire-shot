#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
""" Metas
MELHORAR O CODIGO POIS ESTA MUITO REPETITIVO E COMPLEXO"""
import pygame
from sys import exit
from pygame.locals import *
from os import sep
from leon import *
from inimigo import *
from tela import *

class Tiro (pygame.sprite.Sprite):
	def __init__(self, leon_rect):
		self.leon = Leon()
		self.sprite = pygame.sprite.Sprite()
		self.direcao = ('normal','cima')
		self.image_tiro = pygame.image.load('imagens' + sep + 'tiro' + sep + 'bala.png').convert_alpha()		


def main():
	pygame.init()
	
	tela = Tela("fase1","fundo_fase1_0.png")
	
	#Definicao de Leon	
	leon = Leon()
	leon.troca_imagem_mira()
	leon.atualiza_posicao(0,480)
	seletor_image_leon = 1
	controle_velocidade_troca_imagens = 0
	
	#definicao inimigo
	inimigo = Inimigo()
	inimigo.atualiza_posicao(750, 480)
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
	while True:
		leon.colide_tela()
		for event in pygame.event.get():
			if event.type is pygame.QUIT:
				exit()
			
			if event.type is KEYDOWN:
				if event.key == K_o:
					leon.troca_imagem_mira()
					print leon.image
	
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
		
		#controla a imagem a ser usada no  movimento dos Personagens
		if seletor_image_leon  > 6:
			seletor_image_leon = 1
		if seletor_imagem_inimigo >5:
			seletor_imagem_inimigo = 0
		

		#define a imagem ,possibilita que se alterne e faz com que o inimigo se movimete
		inimigo.image = inimigo.imagem_da_vez[seletor_imagem_inimigo]
		inimigo.anda('LEFT', seletor_imagem_inimigo)
		
		#inimigo.atualiza_posicao(inimigo.rect[0] -5, inimigo.rect[1])
		if pressed_keys[K_ESCAPE]:
			break
			
		#controla o movimento de Leon
		if pressed_keys[K_RIGHT]:
			fogo_position = (leon.rect[0]+85,leon.rect[1]+25)
			if leon.rect[0] > 400 and tela.background_position[0] > -7200:
				tela.movimenta_background()
				leon.anda('tImage', seletor_image_leon)
			else:
				leon.anda('RIGHT', seletor_image_leon)
				
		elif pressed_keys[K_LEFT]:
			fogo_position = (leon.rect[0]+85,leon.rect[1]+25)
			if leon.rect[0] < 0 and tela.background_position[0] >0:
				tela.movimenta_background()
				leon.anda('tImage', seletor_image_leon)
			else:
				leon.anda('LEFT', seletor_image_leon)


		elif pressed_keys[K_UP]:
			leon.desliza_cima (seletor_image_leon)
			#desliza_baixo = False
			
		elif pressed_keys[K_DOWN]:
			leon.desliza_baixo (seletor_image_leon)
			#desliza_cima = False		
			
		else:
			seletor_image_leon = 0 
			leon.anda()
		if pressed_keys[K_p]:
			atirar = True
			som_tiro.play()
		
		
		if atirar and pygame.sprite.collide_mask(tiro, inimigo) :
			inimigo.atualiza_posicao(750, 480)
			mor = True
		
		
		tela.screen.fill((0,0,0))
		#colocacao da imagem de fundo na tela
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao dos personagens na tela
		tela.screen.blit(leon.image, leon.rect)
		if (mor == False):
			tela.screen.blit(inimigo.image,inimigo.rect)
			
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
