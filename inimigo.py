from personagem import *

class Inimigo(Personagem):
	def __init__(self):
		Personagem.__init__(self)
		self.imagem_da_vez = [pygame.image.load('imagens' + sep + 'inimigo' + sep + 'inimigo_'+ str(i) + '.png').convert_alpha() for i in xrange(6)]
		self.image = self.imagem_da_vez[0]
	
