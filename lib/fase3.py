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
from game_over import *
from obstaculos import *
from pausa import *
from bonus import *
from zerando import *

#from   import *

def obstaculo_type1(pedra, background_position):
	pedra_position = [background_position[0] + 1000, background_position[1] + 535]
	#tela.screen.blit(pedra,pedra_position)
	global ret_pedra1type1
	ret_pedra1type1 = pygame.Rect(pedra_position[0],pedra_position[1] + 80,pedra.get_size()[0]-60,pedra.get_size()[1])
	global ret_pedra1type2
	ret_pedra1type2 = pygame.Rect(pedra_position[0]+60,pedra_position[1] + 80,pedra.get_size()[0]-60,pedra.get_size()[1])
	global ret_pedra1
	ret_pedra1 = pygame.Rect(pedra_position[0],pedra_position[1]+50,pedra.get_size()[0],pedra.get_size()[1])
	global ret_pedra1_sobre
	ret_pedra1_sobre = pygame.Rect(pedra_position[0],pedra_position[1]+10,pedra.get_size()[0],pedra.get_size()[1])
	return (pedra,pedra_position)
	
def obstaculo_type2(pedra, background_position):
	pedra_position = [background_position[0] + 3000, background_position[1] + 430]
	if pedra_position[0] < 0:
		pedra_position[0] += 1400
	#tela.screen.blit(pedra,pedra_position)
	global ret_pedra2type1
	ret_pedra2type1 = pygame.Rect(pedra_position[0],pedra_position[1]-100,pedra.get_size()[0]-60,pedra.get_size()[1]-20)
	global ret_pedra2type2
	ret_pedra2type2 = pygame.Rect(pedra_position[0]+60,pedra_position[1]-100,pedra.get_size()[0]-60,pedra.get_size()[1]-20)
	global ret_pedra2
	ret_pedra2 = pygame.Rect(pedra_position[0],pedra_position[1]-100,pedra.get_size()[0],pedra.get_size()[1]+10)
	global ret_pedra2_sobre
	ret_pedra2_sobre = pygame.Rect(pedra_position[0],pedra_position[1]+10,pedra.get_size()[0],pedra.get_size()[1])
	return(pedra, pedra_position)
	
def Fase3():
	#Abre o arquivo que contem as imformacoes sobre tela Cheia
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
	
	# Iniciliza os modulos do pygame 
	pygame.init()
	
	#Define a Tela 
	tela = Tela("fase3",'3.png', tipo_tela)
	tela.background_position= [-10,-30]
	paisagem = pygame.image.load("imagens"+sep+"fase3"+sep+"fundo3.jpg")
	#Definicao de Leon	
	leon = Leon()
	leon.troca_imagem_mira()
	leon.atualiza_posicao(0,390)
	seletor_image_leon = 1
	controle_velocidade_troca_imagens = 0
	direita = False
	esquerda = False
	cima = False
	#Definicao dos Inimigos
	inimigo = Inimigo()
	inimigo.atualiza_posicao(750, 490)
	seletor_imagem_inimigo = 0
	inimigo.morreu = False
	inimigos_mortos = 0
	
	#definicao do Tiro dos Personagens
	leon_tiro = Tiro(leon.rect)
	direcao_tiro = 'normal'
	inimigo_tiro = Tiro(inimigo.rect)
	inimigo_tiro.atirar = True
	som_tiro = pygame.mixer.Sound("soms" + sep + "tiro.wav")
	atirar = False
	
	#verifica se o boneco deve se deslocar pra cima ou pra baixo
	desliza_cima = False
	desliza_baixo = False
	#DEFINICAO OBSTACULOS:
	pedra = pygame.image.load("imagens"+sep+"imagens"+sep+"pedra2.png")
	ponte = pygame.image.load("imagens"+sep+"imagens"+sep+"ponte1.png")
	
	pular = False
	contador_pulo = 0
	pontuacao = 0
	bonus = Bonus('bonus', 'maca_verde_10.png')
	bonus_aparece = True
	bonus_pontos = Bonus('bonus', 'maca_verde_10.png')
	bonus_pontos_aparece = True
	
	while True:
		clock = pygame.time.Clock()
		clock.tick(500)
		for event in pygame.event.get():
			if event.type is pygame.QUIT:
				exit()
			
			if event.type is KEYDOWN:
				if event.key == K_o:
					leon.troca_imagem_mira()
					leon_tiro.troca_direcao_tiro()
					
		#ZEROU (ATE Q EM FIIIIIIIIIIIIIIIMMMMMMMMMMMM)
		if  tela.background_position[0] < -7100:
			b = Zerando()
			if b == 'menu':			break 
		
		###########Variaveis que devem ser atualizadas em cada laço#######
		# criacao dos obstaculos		
		obstaculo1 = obstaculo_type2(pedra, tela.background_position)
		obstaculo2 = obstaculo_type1(pedra, tela.background_position)
		
		if bonus_aparece == True:
			bonus.atualiza_posicao(tela.background_position[0]+1800,tela.background_position[1]+300 )
		if bonus_pontos_aparece == True:
			bonus_pontos.atualiza_posicao(obstaculo2[1][0]+50 , obstaculo2[1][1] )
			
		#Criacao das listas de retangulos dos obstaculos
		ret_player = pygame.Rect(leon.rect[0],leon.rect[1],leon.image.get_size()[0],leon.image.get_size()[1])		
		lista_ret_frente = [ret_pedra1type1,ret_pedra2type1]
		lista_ret_left = [ret_pedra2type2,ret_pedra1type2]
		lista_ret_up = [ret_pedra2]
		lista_ret_down = [ret_pedra1]
		lista_ret_sobre_type1 = [ret_pedra1_sobre,ret_pedra2_sobre]
		
		#verifica se os personagens chegaram ao limite da tela
		leon.colide_tela()
		inimigo.colide_tela()
		
		pontuacao = "Score:%04i         vidas: %02i"%(leon.pontuacao, leon.vida)
		tela.imprime_texto(pontuacao, tamanho = 30)
		
		#Controla a posicao do fogo para que fique sempre proximo a leon
		leon_tiro.fogo_rect = [leon.rect[0]+80,leon.rect[1]+39]
		
		#ATIRA: FAZ COM QUE TANTO LEON COMO O INIMIGO ATIRE
		leon_tiro.atira('RIGHT')
		inimigo_tiro.atira('LEFT')
				
		if inimigo_tiro.atirar == False: 
			inimigo_tiro.atirar	= True
		if leon_tiro.atirar and leon_tiro.rect[0] > 800:
			leon_tiro.rect = [leon.rect[0]+80,leon.rect[1]+43]
			leon_tiro.atirar = False
		if inimigo_tiro.atirar and inimigo_tiro.rect[0] < 0:
			inimigo_tiro.atirar	= False
			
		if inimigo.morreu == True and inimigos_mortos < 10:
			inimigo.morreu = False
			
		#Verifica se as vidas de Leon se encerraram
		leon.gameOver()	
		# .encontra_ ()
		#controladores do pulo
		leon.alterna_posicao()	
		
		if pular == True: leon.collide_obstaculo(True)
		
		elif pular == False: leon.collide_obstaculo(False)
		
		#controla a imagem a ser usada no  movimento dos Personagens
		if seletor_image_leon  > 6:
			seletor_image_leon = 1
		if seletor_imagem_inimigo >5:
			seletor_imagem_inimigo = 0
		

		#define a imagem ,possibilita que se alterne e faz com que o inimigo se movimete
		inimigo.image = inimigo.imagem_da_vez[seletor_imagem_inimigo]
		if inimigo.morreu == False:
			inimigo.anda('LEFT', seletor_imagem_inimigo)
			
		else:
			inimigo.atualiza_posicao(500,400)
			
		#Chamada das teclas
		pressed_keys = pygame.key.get_pressed()
		if cima == True:
			direita = False
			esquerda = False
		#inimigo.atualiza_posicao(inimigo.rect[0] -5, inimigo.rect[1])
		if pressed_keys[K_ESCAPE]:
			break
		if pressed_keys[K_PAUSE]:
			a = pausa()
			if a == 'menu':
				break 
				
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
		if pressed_keys[K_p]:
			leon_tiro.atirar = True
			som_tiro.play()
			
		if pressed_keys[K_i]:
			if pular == False:
				pular = True
				#contador_pulo = 0
				
		if pressed_keys[K_ESCAPE]:
			break
		
		
		if leon_tiro.atirar and pygame.sprite.collide_mask(leon_tiro, inimigo):
			inimigo.morre()
			inimigo.morreu = True
			inimigos_mortos += 1
			leon.pontua()
			
		if (inimigo.morreu == False) and (inimigo.morreu == False) and pygame.sprite.collide_mask(leon, inimigo) and leon.cima_obstaculo == False:
			leon.atualiza_posicao(0,390)
			inimigo.atualiza_posicao(inimigo.posicoesX[inimigo.posicaoX], inimigo.posicoesY[inimigo.posicaoY])
			leon.morre()
			
		if (pular == True) and pygame.sprite.collide_mask(leon_tiro, bonus): 
			leon.vida += 1
			bonus.atualiza_posicao(bonus.rect[0] + 2000, bonus.rect[1])
			bonus_aparece = False
			
		if pygame.sprite.collide_mask(leon, bonus_pontos): 
			leon.pontuacao += 100
			bonus_pontos.atualiza_posicao(obstaculo1[1][0] + 2000, obstaculo1[1][1])
			bonus_pontos_aparece = False
			
		tela.screen.fill((0,0,0))
		#colocacao da imagem de fundo na tela
		tela.screen.blit(paisagem , (0,0))
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao dos personagens na tela
		
		if inimigos_mortos > 10:
			inimigo.morreu = True
				
		if inimigo.morreu == False:
			tela.screen.blit(inimigo.image,inimigo.rect)
		
		tela.screen.blit(obstaculo1[0] , obstaculo1[1])
		
		tela.screen.blit(bonus.image, bonus.rect)	
		
		if pular == True:
			tela.screen.blit(obstaculo2[0] , obstaculo2[1])
			tela.screen.blit(bonus_pontos.image, bonus_pontos.rect)	
			tela.screen.blit(leon.image, leon.rect)
			
		elif pular == False:
			tela.screen.blit(leon.image, leon.rect)
			tela.screen.blit(obstaculo2[0] , obstaculo2[1])
			tela.screen.blit(bonus_pontos.image, bonus_pontos.rect)	
			
			
		if leon_tiro.atirar and leon_tiro.rect[0] < 800:
			tela.screen.blit(leon_tiro.image , leon_tiro.rect)
			
		if inimigo_tiro.atirar and inimigo_tiro.rect[0] > 0:
			tela.screen.blit(inimigo_tiro.image , inimigo_tiro.rect)
			
		#Imprime a pontuacao
		tela.screen.blit(tela.frase,tela.frase_position)
		
		
		if leon.game_over:
			game_over()
			break
		#atualiza a tela
		pygame.display.update()
		
		#faz com que as imagens dos personagens variem
		if controle_velocidade_troca_imagens % 5 == 0:
			seletor_image_leon += 1	
			seletor_imagem_inimigo += 1	
		controle_velocidade_troca_imagens += 1
		
		
		
if __name__ == '__main__':
	
	fase3()


