#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *
from os import sep
from tela import *
from instrucoes import *

def atualiza_rank(score):
	arquivo = open('tipo_tela.fs','w')
	lista_rank = arquivo.readlines()
	nova_lista = [score]
	for valor in lista_rank():
		nova_lista.append(int(valor))
	rank_ordenado = sorted(nova_lista)
	novo_rank = ''
	for num in range(5):
		poss = str(rank_ordenado[num]) + '\n'
		novo_rank += poss
	arquivo.write (novo_rank)
	arquivo.closse()
	
	
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
	
	#abertura do arquivo rank
	arq = open('rank.fs','r')
	lista_rank = arq.readlines()
	
	primeiro = (int(lista_rank[0]))
	segundo = (int(lista_rank[1]))
	terceiro = (int(lista_rank[2]))
	quarto = (int(lista_rank[3]))
	quinto = (int(lista_rank[4]))
	
	#imprimindo texto
	pygame.font.init()
	#definicao para imprimir o rank
	fonte = pygame.font.SysFont('corrier new' ,50, bold = False)
	frase = fonte.render('As cinco maiores pontuacoes:' , True, (255,255,0))
	primeiro_img = fonte.render(str(primeiro) , True, (255,0,0))
	segundo_img = fonte.render(str(segundo) , True, (255,0,0))
	terceiro_img = fonte.render(str(terceiro) , True, (255,0,0))
	quarto_img = fonte.render(str(quarto) , True, (255,0,0))
	quinto_img = fonte.render(str(quinto) , True, (255,0,0))
	
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
		tela.screen.blit(frase, (150,100))
		tela.screen.blit(primeiro_img, (350,150))
		tela.screen.blit(segundo_img, (350,200))
		tela.screen.blit(terceiro_img, (350,250))
		tela.screen.blit(quarto_img, (350,300))
		tela.screen.blit(quinto_img, (350,350))
		pygame.display.update()
