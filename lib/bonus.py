from personagem import *

class Bonus(Personagem):
	def __init__(self, pasta , image):
		self.image = pygame.image.load('imagens'+sep+ pasta+sep+ image).convert_alpha()
		
	def encontra_bonus(self):
		pass 
