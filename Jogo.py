#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports

import pygame
from sys import exit
from pygame.locals import *
from os import sep
from leon import *
from inimigo import *
from tela import *
from tiro import *

def main():
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
	
	pygame.init()
	
	tela = Tela("fase1","fundo_fase1_0.png", tipo_tela)
	
	#Definicao de Leon	
	leon = Leon()
	leon.troca_imagem_mira()
	leon.atualiza_posicao(0,480)
	seletor_image_leon = 1
	controle_velocidade_troca_imagens = 0
	
	#definicao inimigo
	lista_inimigos = [Inimigo() for i in xrange(10)]
	inimigo = lista_inimigos[0]
	inimigo.atualiza_posicao(750, 480)
	seletor_imagem_inimigo = 0
	inimigo.morreu = False
	mor = False
	novo_inimigo, novo_inimigo_heli = 0, 0
	inimigos_mortos = 0
	
	#definicao do Tiro DE LEON
	leon_tiro = Tiro(leon.rect)
	som_tiro = pygame.mixer.Sound("soms" + sep + "tiro.wav")
	atirar = False
	
	#verifica se o boneco deve se deslocar pra cima ou pra baixo
	desliza_cima = False
	desliza_baixo = False
	while True:
		#inimigo.atualiza_posicao(750, 480)
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
		
		#Controla a posicao do fogo para que fique sempre proximo a leon
		leon_tiro.fogo_rect = [leon.rect[0]+80,leon.rect[1]+39]
		
		#ATIRA: FAZ COM QUE TANTO LEON COMO O INIMIGO ATIRE
		leon_tiro.atira('RIGHT')
			
		
		if leon_tiro.atirar and leon_tiro.rect[0] > 800:
			leon_tiro.rect = [leon.rect[0]+80,leon.rect[1]+43]
			leon_tiro.atirar = False
			
		if inimigo.morreu == True :
			inimigo.morreu = False
		
		inimigo.colide_tela()
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
			leon_tiro.fogo_rect = (leon.rect[0]+85,leon.rect[1]+25)
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
			
		elif pressed_keys[K_DOWN]:
			leon.desliza_baixo (seletor_image_leon)
			
		else:
			seletor_image_leon = 0 
			leon.anda()
		if pressed_keys[K_p]:
			leon_tiro.atirar = True
			som_tiro.play()
		
		
		if leon_tiro.atirar and pygame.sprite.collide_mask(leon_tiro, inimigo):
			print '1'
			inimigo.morre()
			inimigo.morreu = True
			inimigos_mortos += 1
					
		tela.screen.fill((0,0,0))
		#colocacao da imagem de fundo na tela
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao dos personagens na tela
		
		
		if inimigo.morreu == False and inimigos_mortos < 100:
			#print inimigo.rect
			tela.screen.blit(inimigo.image,inimigo.rect)
		tela.screen.blit(leon.image, leon.rect)
			
		if leon_tiro.atirar and leon_tiro.rect[0] < 800:
			tela.screen.blit(leon_tiro.image , leon_tiro.rect)
			tela.screen.blit(leon_tiro.image_fogo , leon_tiro.fogo_rect)
			
		
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
