from personagem import *

class Obstaculos (Personagem):
	def __init__(self, pasta,imagem):
		self.image = pygame.image.load("imagens" + sep + pasta + sep + imagem).convert_alpha()
		self.tamanho = self.image.get_size()
	def retangulos(self):
		self.ret_direita = pygame.Rect(self.rect[0]-10,self.rect[1] +15,self.tamanho[0]-60,self.tamanho[1])
		self.ret_esquerda = pygame.Rect(self.rect[0]+10, self.rect[1]+15,self.tamanho[0],self.tamanho[1])
		self.ret_cima = pygame.Rect(self.rect[0],self.rect[1]+10,self.tamanho[0],self.tamanho[1])
		
