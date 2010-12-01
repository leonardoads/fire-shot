from personagem import *
import random
from pygame.locals import *

class Inimigo(Personagem):
	
	posicoesY = [390,500]
	posicoesX = [750,1000,1500,2000]
	
	def __init__(self):
		Personagem.__init__(self)
		self.imagem_da_vez = [pygame.image.load('imagens' + sep + 'inimigo' + sep + 'inimigo_'+ str(i) + '.png').convert_alpha() for i in xrange(6)]
		self.image = self.imagem_da_vez[0]
		self.posicaoY = random.randint(0,len(self.posicoesY)-1)
		self.posicaoX = random.randint(0,len(self.posicoesX)-1)
		
	def morre(self):
		self.posicaoY = random.randint(0,len(self.posicoesY)-1)
		self.posicaoX = random.randint(0,len(self.posicoesX)-1)
		self.atualiza_posicao(self.posicoesX[self.posicaoX], self.posicoesY[self.posicaoY])
	
	def colide_tela(self):
		if self.rect[0]	< 0: 
			self.morre()
	
