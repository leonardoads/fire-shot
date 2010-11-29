#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep
import Jogo
from tela import *
from opcoes import *
#tela.screen_width, tela.screen_height = 800,600
def load ():
	pass
	

def menu():
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
	pygame.init()
	#definicao da Tela
	tela = Tela("menu","menu.jpg", tipo_tela)

	#definicao imagem de creditos
	cred = pygame.image.load("imagens" + sep + "creditos" + sep + "creditos.png").convert_alpha()

	#definicao musica
	pressed_keys = pygame.key.get_pressed()
	musica_menu = pygame.mixer.music.load("music" + sep + "music1.mp3")
	musica_menu = pygame.mixer.music.play(-1)
	
	#DEFINICOES DOS BOTOES DO MENU
	#definicao do botao jogar
	botoes_jogar = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_jogar" + str(i) + \
	".png").convert_alpha() for i in xrange(3)]
	botao_jogar = botoes_jogar[0]
	jogar_size = botao_jogar.get_size()
	jogar_position = ((tela.screen_width/4 - jogar_size[0]/4)*(0.5),
	2*tela.screen_height/8- jogar_size[1]/2)

	#definicao do botao opcoes
	botoes_opcoes = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_opcoes" + str(i) +\
	".png").convert_alpha() for i in xrange(3)]
	botao_opcao = botoes_opcoes[0]
	opcoes_size = botao_opcao.get_size()
	opcoes_position = ((tela.screen_width/4 - opcoes_size[0]/4)*(0.5),
	2*tela.screen_height/5 - opcoes_size[1]/2)

	#definicao do botao ranking
	botoes_ranking = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_ranking" + str(i) + ".png").convert_alpha() for i in xrange(3)]
	botao_ranking = botoes_ranking[0]
	ranking_size = botao_ranking.get_size()
	ranking_position = ((tela.screen_width/4 - ranking_size[0]/4)*(0.5), 
	2*tela.screen_height/3.75 - ranking_size[1]/2)

	#definicao dos botao creditos
	botoes_creditos = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_creditos" + str(i) +\
	".png").convert_alpha() for i in xrange(3)]
	botao_creditos = botoes_creditos[0]
	creditos_size = botao_creditos.get_size()
	creditos_position = ((tela.screen_width/4 - creditos_size[0]/4)*(0.5),
	2*tela.screen_height/3.0 - creditos_size[1]/2)

	#definicoes dos botao sair
	botoes_sair = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_sair" + str(i) + 
	".png").convert_alpha() for i in xrange(3)]
	botao_sair = botoes_sair[0]
	sair_size = botao_sair.get_size()
	sair_position = ((tela.screen_width/4 - sair_size[0]/4)*(0.5), 
	2*tela.screen_height/2.5 - sair_size[1]/2)

	creditos = False
	comeco = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		
			pressed = False
			
		#CHAMADA DA UTILIZAÇÃO DO MOUSE
			mouse_position = pygame.mouse.get_pos()
			mouse_pressionado = pygame.mouse.get_pressed()	
				
		#escolha do botao jogar	
			if jogar_position[0] <= mouse_position[0] <= jogar_position[0] + jogar_size[0] \
			and jogar_position[1] <= mouse_position[1] <= jogar_position[1] + jogar_size[1]:
			
				botao_jogar = botoes_jogar[1]
			
				if mouse_pressionado[0]:
					creditos = False
					musica_menu = pygame.mixer.music.stop()
					botao_jogar = botoes_jogar[2]
					pressed = True
					carregar = load()
					carregar = load()				
					Jogo.main()
					musica_menu = pygame.mixer.music.play(-1)
				if not mouse_pressionado[0] and pressed:
					botao_jogar = botoes_jogar[1]
		
			else: botao_jogar = botoes_jogar[0]
		#escolha do botao opcoes
			if opcoes_position[0] <= mouse_position[0] <= opcoes_position[0] + opcoes_size[0] \
			and opcoes_position[1] <= mouse_position[1] <= opcoes_position[1] + opcoes_size[1]:
			
				botao_opcao = botoes_opcoes[1]
			
				if mouse_pressionado[0]:
					creditos = False
					botao_opcao = botoes_opcoes[2]
					pressed = True
					opcoes()					
						
				if not mouse_pressionado[0] and pressed:
					botao_opcao = botoes_opcoes[1]
		
			else: botao_opcao = botoes_opcoes[0]
		
		#escolha do botao ranking
			if ranking_position[0] <= mouse_position[0] <= ranking_position[0] + ranking_size[0] \
			and ranking_position[1] <= mouse_position[1] <= ranking_position[1] + ranking_size[1]:
			
				botao_ranking = botoes_ranking[1]
			
				if mouse_pressionado[0]:
					creditos = False
					botao_ranking = botoes_ranking[2]
					pressed = True
					#Ranking.main()
				if not mouse_pressionado[0] and pressed:
					botao_ranking = botoes_ranking[1]
		
				else: botao_ranking = botoes_ranking[0]
		
		#escolha do botao creditos
			if creditos_position[0] <= mouse_position[0] <= creditos_position[1] + creditos_size[1]\
			and creditos_position[1] <= mouse_position[1] <= creditos_position[1] + creditos_size[1]:
			
				botao_creditos = botoes_creditos[1]
			
				if mouse_pressionado[0]:
					botao_creditos = botoes_creditos[2]
					pressed = True
					#Creditos.main()
				
					if creditos == False:
						creditos = True
					else:
						creditos = False
				
						
				if not mouse_pressionado[0] and pressed:
					botao_creditos = botoes_creditos[1]
		
			else: botao_creditos = botoes_creditos[0]
			#escolha da opcao sair
			if sair_position[0] <= mouse_position[0] <= sair_position[1] + sair_size[1]\
			and sair_position[1] <= mouse_position[1] <= sair_position[1] + sair_size[1]:
			
				botao_sair = botoes_sair[1]
			
				if mouse_pressionado[0]:
					botao_sair = botoes_sair[2]
					pressed = True
					exit()
				if not mouse_pressionado[0] and pressed:
					botao_sair = botoes_sair[1]
		
			else: botao_sair = botoes_sair[0]
			
		#colocacao da imagem de fundo na tela
		tela.screen.blit(tela.background, tela.background_position)
		
		#colocacao dos botoes de menu na tela
		tela.screen.blit(botao_jogar,jogar_position)
		tela.screen.blit(botao_opcao, opcoes_position)
		tela.screen.blit(botao_ranking, ranking_position)
		tela.screen.blit(botao_creditos, creditos_position)
		tela.screen.blit(botao_sair, sair_position)
		if creditos == True:
			tela.screen.blit(cred, (90,200))
		pygame.display.update()
#menu()
