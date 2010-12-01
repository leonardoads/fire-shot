import pygame
from sys import exit
from pygame.locals import *
from os import sep
from menu import *
from opcoes import *

screen_width, screen_height = 800,600

def pausa():
	pygame.init()
	
	#DEFINICAO DA TELA
	screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
	pygame.display.set_caption("Fire shot")
	
	#definicao da imagem de fundo
	
	fundo_pausa = pygame.image.load('imagens'+ sep +"pausa" + sep + "fundo_pausa.png")
	icon = pygame.image.load('imagens'+ sep +"menu" + sep + "icon.bmp")
	pygame.display.set_icon(icon)
	fundo_pausa_size = fundo_pausa.get_size()
	fundo_pausa_position = [150,60]
	
	#DEFINICOES DOS BOTOES DO PAUSA
	#definicao do botao voltar
	botoes_voltar = [pygame.image.load("imagens" + sep+ 'pausa'+ sep + "voltar_pausa" + str(i) + \
	".png").convert_alpha() for i in xrange(2)]
	botao_voltar = botoes_voltar[0]
	voltar_size = botao_voltar.get_size()
	voltar_position = (350,150)
	
	#definicao do botao menu principal
	botoes_menu = [pygame.image.load("imagens" + sep+ 'pausa'+ sep + "menu_principal" + str(i) + \
	".png").convert_alpha() for i in xrange(2)]
	botao_menu = botoes_menu[0]
	menu_size = botao_menu.get_size()
	menu_position = (330,400)
	
	while True:
			for event in pygame.event.get():
					if event.type == QUIT:
							exit
			#Chamada das teclas
			pressed_keys = pygame.key.get_pressed()
			
			pressed = False
			#CHAMADA DA UTILIZACAO DO MOUSE
			mouse_position = pygame.mouse.get_pos()
			mouse_pressionado = pygame.mouse.get_pressed()
			
			#escolha do botao voltar	
			if voltar_position[0] <= mouse_position[0] <= voltar_position[0] + voltar_size[0] \
			and voltar_position[1] <= mouse_position[1] <= voltar_position[1] + voltar_size[1]or pressed_keys[K_v]:
				botao_voltar = botoes_voltar[1]
				
				if mouse_pressionado[0]:
					break
				
			else: botao_voltar = botoes_voltar[0]
			
			#escolha do botao menu principal	
			if menu_position[0] <= mouse_position[0] <= menu_position[0] + menu_size[0] \
			and menu_position[1] <= mouse_position[1] <= menu_position[1] + menu_size[1]or pressed_keys[K_v]:
				botao_menu = botoes_menu[1]
				
				if mouse_pressionado[0]:
					menu()
				
			else: botao_menu = botoes_menu[0]
			
			screen.blit(fundo_pausa, fundo_pausa_position)
			screen.blit(botao_voltar, voltar_position)
			screen.blit(botao_menu, menu_position)
			pygame.display.update()
			
