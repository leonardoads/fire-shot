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
		self.fogo_rect = [rect[0], rect[1]+43]
		self.rect = [rect[0]+80,rect[1]+43]
		self.rect_fixo = [rect[0]+80,rect[1]+43]
		self.atirar = False
		self.direcao_tiro = {'RIGHT':75, "LEFT": -100}
		
	def atira(self, direcao):
		if self.atirar:
			self.rect[0] += self.direcao_tiro[direcao]
		else:
			self.rect = self.fogo_rect
	
