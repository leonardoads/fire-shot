import pygame
from sys import exit
from pygame.locals import *
from os import sep
class Tiro (pygame.sprite.Sprite):
	def __init__(self, rect):
		self.sprite = pygame.sprite.Sprite()
		self.direcao = ('normal','cima')
		self.image = pygame.image.load('imagens' + sep + 'tiro' + sep + 'bala.png').convert_alpha()
		self.image_fogo = pygame.image.load('imagens' + sep + 'tiro' + sep + 'tiro1.png').convert_alpha()
		#self.fogo_rect = [rect[0], rect[1]+43]
		self.rect = [rect[0]+80,rect[1]+43]
		self.rect_fixo = [rect[0]+80,rect[1]+43]
		self.atirar = False
		self.direcao_tiro = {'RIGHT':(75,-75), "LEFT": (-100,100)}
		self.seletor_tiro = 0
		self.mira_da_vez = 'normal'
	def atira(self, direcao_tiro):
		if self.atirar:
			if self.mira_da_vez == 'normal':
				self.rect[0] += self.direcao_tiro[direcao_tiro][0]
			elif self.mira_da_vez == 'cima':
				self.rect[0] += self.direcao_tiro[direcao_tiro][0]
				self.rect[1] += self.direcao_tiro[direcao_tiro][1]
		#else:
			#self.rect = self.fogo_rect
	def troca_direcao_tiro(self):
		self.seletor_tiro += 1
		self.mira_da_vez = self.direcao[self.seletor_tiro %2]
		
