from personagem import *

class Leon(Personagem):
	
	def __init__(self):
		Personagem.__init__(self)
		self.images_mira_normal = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7)]
		self.images_mira_cima = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7,14)]
		self.imagem_da_vez = self.images_mira_normal
		self.imagens_mira = [self.images_mira_normal,self.images_mira_cima]
		
	def troca_imagem_mira(self):
		self.seletor_mira += 1
		self.imagem_da_vez = self.imagens_mira[self.seletor_mira % 2]		
		self.image = self.imagem_da_vez[0]
	
	def colide_tela(self):
		if self.rect[0]	< 0: 
			self.atualiza_posicao(0,480)
			self.image = self.image = self.imagem_da_vez[0]
			
	def desliza_cima(self,seletor_image_leon):
		if self.rect[1] > 422:
			self.atualiza_posicao(self.rect[0]+10, self.rect[1] -10)
			self.image = self.imagem_da_vez[seletor_image_leon]
			
	def desliza_baixo(self, seletor_imagens_leon):
		if self.rect[1] < 480:
			self.atualiza_posicao(self.rect[0]-10 , self.rect[1] + 10)
			self.image = self.imagem_da_vez[seletor_imagens_leon]
			
	
