import pygame
from sys import exit
from pygame.locals import *
from os import sep
class Tela:
	def __init__(self, pasta, imagem, tipo):
		self.tipo = {'FULLSCREEN': FULLSCREEN, "0": 0}
		self.screen_width, self.screen_height = 800,600
		self.screen = pygame.display.set_mode((self.screen_width,self.screen_height), self.tipo[tipo], 32)
		pygame.display.set_caption("Fire shot")
		self.background = pygame.image.load('imagens'+ sep + pasta + sep + imagem).convert()
		self.background_size = self.background.get_size()
		self.background_position= [0,0]
		self.icon = pygame.image.load('imagens'+ sep +"menu" + sep + "icon.bmp")
		pygame.display.set_icon(self.icon)
	
	def movimenta_background(self):
		self.background_position[0] -= 10
		
	def fullscreen(self):
		self.screen = pygame.display.set_mode((self.screen_width,self.screen_height), FULLSCREEN , 32)
	
	def sair_fullsreen(self):
		self.screen = pygame.display.set_mode((self.screen_width,self.screen_height), 0 , 32)
		
	
	
