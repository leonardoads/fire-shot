import pygame
from sys import exit
from pygame.locals import *
from os import sep
class Personagem:
	images = []
	seletor_imagens = 0
	imagem_da_vez = []
	seletor_mira = -1
	#imagens_mira = ['normal', 'cima']
	imagens_mira = []
	
	def __init__(self):
		self.personagem =  pygame.sprite.Sprite()
	
	def atualiza_posicao(self, x,y):
		self.rect = [x,y]
	
	def anda(self,direcao = None, seletor_imagens= None):
		if direcao != None:
			self.image = self.imagem_da_vez[seletor_imagens]
			if direcao == 'RIGHT':
				self.rect[0] += 10
			elif direcao == 'LEFT':
				self.rect[0] -= 10
			else:
				pass		
		else:
			self.image = self.imagem_da_vez[0]
