#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep
import Jogo
from opcoes import *


def menu():
	pygame.init()
	#DEFINICAO DA TELA
	screen = pygame.display.set_mode((screen_width,screen_height),FULLSCREEN, 32)
	pygame.display.set_caption("Fire shot")

	#definicao da imagem de fundo
	background = pygame.image.load('imagens'+ sep +"menu" + sep + "menu.jpg")
	icon = pygame.image.load('imagens'+ sep +"menu" + sep + "icon.bmp")
	pygame.display.set_icon(icon)
	background_size = background.get_size()
	background_position= (screen_width/2) - (background_size[0]/2), (screen_height/2) - (background_size[1]/2)
	img_width, img_height = background.get_size()
	x, y = (screen_width/2) - (img_width/2), (screen_height/2) - (img_height/2)

	#definicao imagem de creditos
	cred = pygame.image.load("imagens" + sep + "creditos" + sep + "creditos.png").convert_alpha()

	#definicao musica
	pressed_keys = pygame.key.get_pressed()
	musica_menu = pygame.mixer.music.load("music" + sep + "music1.mp3")
	musica_menu = pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(10)
		

	#DEFINICAO MOUSE:
	#pygame.mouse.set_cursor("imagens" + sep + "cursor" + sep + "cursor.png")
	#cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
	#pygame.mouse.set_cursor(cursor)

	#DEFINICOES DOS BOTOES DO MENU
	#definicao do botao jogar
	botoes_jogar = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_jogar" + str(i) + \
	".png").convert_alpha() for i in xrange(3)]
	botao_jogar = botoes_jogar[0]
	jogar_size = botao_jogar.get_size()
	jogar_position = ((screen_width/4 - jogar_size[0]/4)*(0.5),
	2*screen_height/8- jogar_size[1]/2)

	#definicao do botao opcoes
	botoes_opcoes = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_opcoes" + str(i) +\
	".png").convert_alpha() for i in xrange(3)]
	botao_opcao = botoes_opcoes[0]
	opcoes_size = botao_opcao.get_size()
	opcoes_position = ((screen_width/4 - opcoes_size[0]/4)*(0.5),
	2*screen_height/5 - opcoes_size[1]/2)

	#definicao do botao ranking
	botoes_ranking = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_ranking" + str(i) + ".png").convert_alpha() for i in xrange(3)]
	botao_ranking = botoes_ranking[0]
	ranking_size = botao_ranking.get_size()
	ranking_position = ((screen_width/4 - ranking_size[0]/4)*(0.5), 
	2*screen_height/3.75 - ranking_size[1]/2)

	#definicao dos botao creditos
	botoes_creditos = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_creditos" + str(i) +\
	".png").convert_alpha() for i in xrange(3)]
	botao_creditos = botoes_creditos[0]
	creditos_size = botao_creditos.get_size()
	creditos_position = ((screen_width/4 - creditos_size[0]/4)*(0.5),
	2*screen_height/3.0 - creditos_size[1]/2)

	#definicoes dos botao sair
	botoes_sair = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_sair" + str(i) + 
	".png").convert_alpha() for i in xrange(3)]
	botao_sair = botoes_sair[0]
	sair_size = botao_sair.get_size()
	sair_position = ((screen_width/4 - sair_size[0]/4)*(0.5), 
	2*screen_height/2.5 - sair_size[1]/2)

	def load ():
		ind, cont = 0,0
		for i in range(999999):
			imagens = ['loading..bmp','loading...bmp','loading....bmp','loading.....bmp']
			cont += 1
			if cont == 222222:
				load = pygame.image.load('imagens'+ sep +"loading" + sep + imagens[ind])
				ind += 1
				screen.blit(load,(x,y))
				pygame.display.update()
				if ind > 3:
					ind = 0
	def filme():
		pygame.time.delay(17)
		filme_menu = pygame.movie.Movie("videos" + sep + "inicio2_menu.mpg")
		filme_menu.play()
		
	creditos = False
	comeco = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		#Chamada das teclas
			pressed_keys = pygame.key.get_pressed()
		
		
			pressed = False
		#CHAMADA DA UTILIZAÇÃO DO MOUSE
			mouse_position = pygame.mouse.get_pos()

			mouse_pressionado = pygame.mouse.get_pressed()
			#while comeco == 0:
				#filme = pygame.movie.Movie('videos' + sep + 'inicio2_menu.mpg')
				#comeco += 1
				#filme.play()
				#pygame.display.update()
		
		#Escolha das opcoes do menu
		
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
					#pressed_keys = pygame.key.get_pressed()
					#screen.blit(cred, (x+100,y+200))
					#pygame.display.update()
					if creditos == False:
						creditos = True
					else:
						creditos = False
					#while True:
					#    for event in pygame.event.get():
					#        if event.type == QUIT:
					#            exit()
					#        if pressed_keys[K_s]:
					#            break
						
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
		screen.blit(background, background_position)
		
		#colocacao dos botoes de menu na tela
		screen.blit(botao_jogar,jogar_position)
		screen.blit(botao_opcao, opcoes_position)
		screen.blit(botao_ranking, ranking_position)
		screen.blit(botao_creditos, creditos_position)
		screen.blit(botao_sair, sair_position)
		if creditos == True:
			screen.blit(cred, (x+100,y+200))
		pygame.display.update()
