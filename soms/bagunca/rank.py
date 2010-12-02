import pygame
from sys import exit
from pygame.locals import *
from os import sep
from tela import *
from instrucoes import *

def Rank():
	arquivo = open('tipo_tela.fs','r')
	tipo_tela = arquivo.read().strip()
	pygame.init()
	
	tela = Tela("rank","fundo_rank.jpg", tipo_tela)
	
		
#definicao do botao voltar
	botoes_voltar = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_voltar" + str(i) + \
	".png").convert_alpha() for i in xrange(2)]
	botao_voltar = botoes_voltar[0]
	voltar_size = botao_voltar.get_size()
	voltar_position = (100,500)	
	
	while True:
		for event in pygame.event.get():
					if event.type == QUIT:
							exit()
		
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
			
			if mouse_pressionado[0] or pressed_keys[K_v]:
				
				break
		else: botao_voltar = botoes_voltar[0]
			
		tela.screen.blit(tela.background , tela.background_position)
		tela.screen.blit(botao_voltar, voltar_position)
		pygame.display.update()
