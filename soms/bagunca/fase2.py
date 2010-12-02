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
from pausa import *

def Fase2():
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
	
	pygame.init()
	
	tela = Tela("fase2","caminho.png", tipo_tela)
	#definicao paisagem
	paisagem = pygame.image.load("imagens"+sep+"fase2"+sep+"fundo_fase2.jpg")
	
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
	som_tiro = pygame.mixer.Sound("sons" + sep + "tiro.wav")
	atirar = False
	
	#verifica se o boneco deve se deslocar pra cima ou pra baixo
	desliza_cima = False
	desliza_baixo = False
	#DEFINICAO OBSTACULOS:
	pedra = pygame.image.load("imagens"+sep+"imagens"+sep+"pedra2.png")
	ponte = pygame.image.load("imagens"+sep+"imagens"+sep+"ponte1.png")
	def obstaculo_type1(pedra):
		pedra_position = [tela.background_position[0] + 600,tela.background_position[1] + 480]
		if pedra_position[0] < 0:
			pedra_position[0] += 1100
		tela.screen.blit(pedra,pedra_position)
		global ret_pedra1type1
		ret_pedra1type1 = pygame.Rect(pedra_position[0],pedra_position[1] + 80,pedra.get_size()[0]-60,pedra.get_size()[1])
		global ret_pedra1type2
		ret_pedra1type2 = pygame.Rect(pedra_position[0]+60,pedra_position[1] + 80,pedra.get_size()[0]-60,pedra.get_size()[1])
		global ret_pedra1
		ret_pedra1 = pygame.Rect(pedra_position[0],pedra_position[1]+50,pedra.get_size()[0],pedra.get_size()[1])
		global ret_pedra1_sobre
		ret_pedra1_sobre = pygame.Rect(pedra_position[0],pedra_position[1]+10,pedra.get_size()[0],pedra.get_size()[1])
	def obstaculo_type2(pedra):
		pedra_position = [tela.background_position[0] + 2000,tela.background_position[1] + 430]
		if pedra_position[0] < 0:
			pedra_position[0] += 1400
		tela.screen.blit(pedra,pedra_position)
		global ret_pedra2type1
		ret_pedra2type1 = pygame.Rect(pedra_position[0],pedra_position[1]-100,pedra.get_size()[0]-60,pedra.get_size()[1]-20)
		global ret_pedra2type2
		ret_pedra2type2 = pygame.Rect(pedra_position[0]+60,pedra_position[1]-100,pedra.get_size()[0]-60,pedra.get_size()[1]-20)
		global ret_pedra2
		ret_pedra2 = pygame.Rect(pedra_position[0],pedra_position[1]-100,pedra.get_size()[0],pedra.get_size()[1]+10)
		global ret_pedra2_sobre
		ret_pedra2_sobre = pygame.Rect(pedra_position[0],pedra_position[1]+10,pedra.get_size()[0],pedra.get_size()[1])

	pular = False
	contador_pulo = 0
	while True:
		obstaculo_type2(pedra)
		obstaculo_type1(pedra)
		#ponte1(ponte)
		ret_player = pygame.Rect(leon.rect[0],leon.rect[1],leon.image.get_size()[0],leon.image.get_size()[1])
		lista_ret_frente = [ret_pedra1type1,ret_pedra2type1]
		lista_ret_left = [ret_pedra2type2,ret_pedra1type2]
		lista_ret_up = [ret_pedra2]
		lista_ret_down = [ret_pedra1]
		lista_ret_sobre_type1 = [ret_pedra1_sobre,ret_pedra2_sobre]
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
		if seletor_imagem_inimigo >2:
			seletor_imagem_inimigo = 0
		

		#define a imagem ,possibilita que se alterne e faz com que o inimigo se movimete
		inimigo.image = inimigo.imagem_da_vez[seletor_imagem_inimigo]
		inimigo.anda('LEFT', seletor_imagem_inimigo)
		
		#pausa
		if pressed_keys[K_PAUSE]:
			pausa()
		#inimigo.atualiza_posicao(inimigo.rect[0] -5, inimigo.rect[1])
		if pressed_keys[K_ESCAPE]:
			break
		#pular
		if pressed_keys[K_i]:
			if pular == False:
				pular = True
		#controla o movimento de Leon
		if (pressed_keys[K_RIGHT] and ret_player.collidelist(lista_ret_frente) == -1) or (pressed_keys[K_RIGHT] and contador_pulo >= 10):
			leon_tiro.fogo_rect = (leon.rect[0]+85,leon.rect[1]+25)
			if leon.rect[0] > 400 and tela.background_position[0] > -7200:
				tela.movimenta_background()
				leon.anda('tImage', seletor_image_leon)
			else:
				leon.anda('RIGHT', seletor_image_leon)
				
		elif (pressed_keys[K_LEFT] and ret_player.collidelist(lista_ret_left) == -1) or (pressed_keys[K_LEFT] and contador_pulo >= 10):
			fogo_position = (leon.rect[0]+85,leon.rect[1]+25)
			if leon.rect[0] < 0 and tela.background_position[0] >0:
				tela.movimenta_background()
				leon.anda('tImage', seletor_image_leon)
			else:
				leon.anda('LEFT', seletor_image_leon)


		elif pressed_keys[K_UP] and ret_player.collidelist(lista_ret_up) == -1:
			leon.desliza_cima (seletor_image_leon)
			
		elif pressed_keys[K_DOWN] and ret_player.collidelist(lista_ret_down) == -1 and pular == False:
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
		tela.screen.blit(paisagem , (0,0))
		tela.screen.blit(tela.background, tela.background_position)
		
		
		#faz o pulo de Leon
		if pular == True and contador_pulo < 10:
			contador_pulo += 1
			if leon.rect[0] < 586:
				leon.rect[0] += 15
			leon.rect[1] -= 15
		elif pular == True and contador_pulo < 20:
			if ret_player.collidelist(lista_ret_sobre_type1) == -1:
				if leon.rect[0] < 586:
					leon.rect[0] += 15
				leon.rect[1] += 15
				contador_pulo += 1
		elif contador_pulo == 20:
			pular = False
			contador_pulo = 0
		if inimigo.rect[1] <= 450:
			if inimigo.morreu == False and inimigos_mortos < 25:
				#print inimigo.rect
				tela.screen.blit(inimigo.image,inimigo.rect)		
		#colocacao dos personagens na tela
		obstaculo_type2(pedra)
		#if leon.rect[1] > 450:
		tela.screen.blit(leon.image, leon.rect)
		if inimigo.rect[1] > 450:
			if inimigo.morreu == False and inimigos_mortos < 25:
				#print inimigo.rect
				tela.screen.blit(inimigo.image,inimigo.rect)
		if leon_tiro.atirar and leon_tiro.rect[0] < 800:
			tela.screen.blit(leon_tiro.image , leon_tiro.rect)
			tela.screen.blit(leon_tiro.image_fogo , leon_tiro.fogo_rect)
			
		obstaculo_type1(pedra)
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
