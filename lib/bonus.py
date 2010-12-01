from personagem import *

class Bonus(Personagem):
	def __init__(self, pasta , image1, image2):
		self.econde_imagem = pygame.image.load('imagens'+sep+ pasta+ sep + image1).convert_alpha()
		self.imagem = pygame.image.load('imagens'+sep+ pasta+sep+ image2).convert_alpha()
		self.encontra = False
		
	def encontra_bonus(self):
		if self.rect[1] < 200:
			self.rect[1] -= 50
