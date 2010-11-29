from personagem import *
import random

class Inimigo(Personagem):
	
	posicoesY = [400,480]
	posicoesX = [750,1000,1500]
	
	def __init__(self):
		Personagem.__init__(self)
		self.imagem_da_vez = [pygame.image.load('imagens' + sep + 'inimigo' + sep + 'inimigotipo1'+ str(i) + '.png').convert_alpha() for i in xrange(3)]
		self.image = self.imagem_da_vez[0]
		
	def morre(self):
		posicaoY = random.randint(0,len(self.posicoesY)-1)
		posicaoX = random.randint(0,len(self.posicoesX)-1)
		self.atualiza_posicao(self.posicoesX[posicaoX], self.posicoesY[posicaoY])
	
	def colide_tela(self):
		if self.rect[0]	< 0: 
			self.morre()
	def tiro_inimigo(self):
		pass