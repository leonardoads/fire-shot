#!/usr/bin/env python
# *-* coding: utf-8 *-*
#imports
import pygame
from sys import exit
from pygame.locals import *
from os import sep

screen_width, screen_height = 800,600

pygame.init()
#DEFINICAO DA TELA
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
pygame.display.set_caption("Fire shot")

#definicao da imagem de fundo
background = pygame.image.load('imagens'+ sep +"menu" + sep + "menu.jpg")
background_size = background.get_size()
background_position= (screen_width/2) - (background_size[0]/2), (screen_height/2) - (background_size[1]/2)

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
	pressed = False
        
	#CHAMADA DA UTILIZAÇÃO DO MOUSE
	mouse_position = pygame.mouse.get_pos()
	mouse_pressionado = pygame.mouse.get_pressed()
	
	#Escolha das opcoes do menu
	
	#escolha do botao jogar	
	if jogar_position[0] <= mouse_position[0] <= jogar_position[0] + jogar_size[0] \
	and jogar_position[1] <= mouse_position[1] <= jogar_position[1] + jogar_size[1]:
		
		botao_jogar = botoes_jogar[1]
		
		if mouse_pressionado[0]:
			botao_jogar = botoes_jogar[2]
			pressed = True
			#Jogo.main()
		if not mouse_pressionado[0] and pressed:
			botao_jogar = botoes_jogar[1]
	
	else: botao_jogar = botoes_jogar[0]
	
	#escolha do botao opcoes
	if opcoes_position[0] <= mouse_position[0] <= opcoes_position[0] + opcoes_size[0] \
	and opcoes_position[1] <= mouse_position[1] <= opcoes_position[1] + opcoes_size[1]:
		
		botao_opcao = botoes_opcoes[1]
		
		if mouse_pressionado[0]:
			botao_opcao = botoes_opcoes[2]
			pressed = True
			#Opcao.main()
		if not mouse_pressionado[0] and pressed:
			botao_opcao = botoes_opcoes[1]
	
	else: botao_opcao = botoes_opcoes[0]
	
	#escolha do botao ranking
	if ranking_position[0] <= mouse_position[0] <= ranking_position[0] + ranking_size[0] \
	and ranking_position[1] <= mouse_position[1] <= ranking_position[1] + ranking_size[1]:
		
		botao_ranking = botoes_ranking[1]
		
		if mouse_pressionado[0]:
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
    
    pygame.display.update()
