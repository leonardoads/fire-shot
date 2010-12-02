from tela import *
class Imprime_tela(Tela):
	def imprime_texto(self, mensagem , font = 'corrier new', tamanho = 60, Negrito = False):
		self.fonte = pygame.font.SysFont(font ,tamanho, bold = Negrito)	
		self.frase = self.fonte.render(mensagem , True, (255,0,0))
		self.frase_position = (10,10)
