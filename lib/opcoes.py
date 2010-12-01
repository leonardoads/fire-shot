import pygame
from sys import exit
from pygame.locals import *
from os import sep
from tela import *

screen_width, screen_height = 800,600

def opcoes():
	arquivo = open('tipo_tela.fs','rw')
	tipo_tela = arquivo.read().strip()
	pygame.init()
	x = 0
	tipo = 0
	tela = Tela("opcoes","image_opcoes.jpg", tipo_tela)
	##DEFINICAO DA TELA
	
	#Palavras a ser impressas
	tipo_tela = pygame.image.load('imagens'+ sep +"opcoes" + sep + "tela_cheia.png")
	volume = pygame.image.load('imagens'+ sep +"opcoes" + sep + "Volume.png")

	#DEFINICOES DOS BOTOES DO OPCOES
	#definicao do botao voltar
	botoes_voltar = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_voltar" + str(i) + \
	".png").convert_alpha() for i in xrange(2)]
	botao_voltar = botoes_voltar[0]
	voltar_size = botao_voltar.get_size()
	voltar_position = (100,500)

	#definicao do botao de volume mais
	botoes_mais = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_vol_max" + str(i) + \
	".bmp").convert_alpha() for i in xrange(3)]
	botao_mais = botoes_mais[0]
	mais_size = botao_mais.get_size()
	mais_position = (590,310)
	
	#definicao do botao de volume mais
	botoes_menos = [pygame.image.load("imagens" + sep+ 'botoes'+ sep + "botao_vol_min" + str(i) + \
	".bmp").convert_alpha() for i in xrange(3)]
	botao_menos = botoes_menos[0]
	menos_size = botao_menos.get_size()
	menos_position = (460,310)
	
	#definicao do anime volume
	animes_volume = [pygame.image.load("imagens" + sep+ 'opcoes'+ sep + "select_volume_" + str(i) + \
	".png").convert_alpha() for i in xrange(3)]
	anime_volume = animes_volume[1]
	anime_volume_size = anime_volume.get_size()
	anime_volume_position = (500,260)
	
	#definicao botao tela cheia
	botoes_tela = [pygame.image.load("imagens" + sep+ 'opcoes'+ sep + "tela_cheia_select" + str(i) + \
	".png").convert_alpha() for i in xrange(2)]
	botao_escolha_tela = botoes_tela[1]
	botao_escolha_tela_size = botao_escolha_tela.get_size()
	botao_escolha_tela_position = (450,400)
	
	
	
	contador = 0
	while True:
			contador += 1
			for event in pygame.event.get():
					if event.type == QUIT:
							exit
			#Chamada das teclas
			pressed_keys = pygame.key.get_pressed()
			
			pressed = False
			#CHAMADA DA UTILIZACAO DO MOUSE
			mouse_position = pygame.mouse.get_pos()
			mouse_pressionado = pygame.mouse.get_pressed()
			
			
			#escolha do botao volume mais	
			if mais_position[0] <= mouse_position[0] <= mais_position[0] + mais_size[0] \
			and mais_position[1] <= mouse_position[1] <= mais_position[1] + mais_size[1]or pressed_keys[K_v]:
				botao_mais = botoes_mais[1]
				
				if mouse_pressionado[0]:
					botao_mais = botoes_mais[2]
					if not anime_volume == animes_volume[2]  and contador % 10 == 0:
						if anime_volume == animes_volume[1]:
							anime_volume = animes_volume[2]
						else:
							anime_volume = animes_volume[1]
			else: botao_mais = botoes_mais[0]
			
			#escolha do botao volume menos	
			if menos_position[0] <= mouse_position[0] <= menos_position[0] + menos_size[0] \
			and menos_position[1] <= mouse_position[1] <= menos_position[1] + menos_size[1]or pressed_keys[K_v]:
				botao_menos = botoes_menos[1]
				
				if mouse_pressionado[0]:
					botao_menos = botoes_menos[2]
					if not anime_volume == animes_volume[0] and contador % 10 == 0:
						if anime_volume == animes_volume[1]:
							anime_volume = animes_volume[0]
						else:
							anime_volume = animes_volume[1]
			else: botao_menos = botoes_menos[0]
			
			#escolha do botao escolha da tela
			if botao_escolha_tela_position[0] <= mouse_position[0] <= botao_escolha_tela_position[0] + botao_escolha_tela_size[0] \
			and botao_escolha_tela_position[1] <= mouse_position[1] <= botao_escolha_tela_position[1] + botao_escolha_tela_size[1]or pressed_keys[K_v]:
				
				if mouse_pressionado[0]:
					if botao_escolha_tela == botoes_tela[0]:
						botao_escolha_tela = botoes_tela[1]
					else:
						botao_escolha_tela = botoes_tela[0]
					if botao_escolha_tela == botoes_tela[1]:
						arquivo = open('tipo_tela.fs','w+')
						arquivo.write('FULLSCREEN')
						arquivo.close()
						tela.sair_fullsreen()
						tela.fullscreen()
						
					else:
						arquivo = open('tipo_tela.fs','w+')
						arquivo.write('0')
						arquivo.close()
						tela.sair_fullsreen()
				
			else: botao_voltar = botoes_voltar[0]
			if pressed_keys[K_F11]:
					x += 1
					if x % 5 == 0:
						arquivo = open('tipo_tela.fs','w+')
						arquivo.write('FULLSCREEN')
						arquivo.close()
						tela.fullscreen()
					else:
						arquivo = open('tipo_tela.fs','w+')
						arquivo.write('FULLSCREEN')
						arquivo.close()
						tela.sair_fullsreen()
			
			#escolha do botao voltar	
			if voltar_position[0] <= mouse_position[0] <= voltar_position[0] + voltar_size[0] \
			and voltar_position[1] <= mouse_position[1] <= voltar_position[1] + voltar_size[1]or pressed_keys[K_v]:
				botao_voltar = botoes_voltar[1]
				
				if mouse_pressionado[0] or pressed_keys[K_v]:
					arquivo.close()
					break
				
			else: botao_voltar = botoes_voltar[0]

			
			tela.screen.blit(tela.background , tela.background_position)
			tela.screen.blit(tipo_tela, (300,400))
			tela.screen.blit(volume, (300,300))
			tela.screen.blit(anime_volume, anime_volume_position)
			tela.screen.blit(botao_mais, mais_position)
			tela.screen.blit(botao_menos, menos_position)
			tela.screen.blit(botao_escolha_tela, botao_escolha_tela_position)
			tela.screen.blit(botao_voltar, voltar_position)
			pygame.display.update()

#opcoes()					