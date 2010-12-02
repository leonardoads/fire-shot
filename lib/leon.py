from personagem import *

class Leon(Personagem):
	
	def __init__(self):
		Personagem.__init__(self)
		self.images_mira_normal = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7)]
		self.images_mira_cima = [pygame.image.load('imagens' + sep + 'leon' + sep + 'leon' + str(i) + '.png').convert_alpha() for i in xrange(7,14)]
		self.imagem_da_vez = self.images_mira_normal
		self.imagens_mira = [self.images_mira_normal,self.images_mira_cima]
		self.vida = 5
		self.game_over = False
		self.controle_pulo = {'sob': -10, 'desce':1}
		self.ativa_pulo = False
		self.controlador_pulo = 'sob'
		self.posicao = 'cima'
		self.collide_direction = None
		self.cima_obstaculo = False
		self.pontuacao = 0
		
		#self.y_inicial = self.rect[1]
	def troca_imagem_mira(self):
		self.seletor_mira += 1
		self.imagem_da_vez = self.imagens_mira[self.seletor_mira % 2]		
		self.image = self.imagem_da_vez[0]
		self.tamanho = self.image.get_size()
	
	
	def colide_tela(self):
		if self.rect[0]	< 0: 
			self.atualiza_posicao(0,self.rect[1])
			self.image =  self.imagem_da_vez[0]
	def collide_obstaculo(self, local):
		self.cima_obstaculo = local
		
	
				
	def desliza_cima(self,seletor_image_leon):
		if self.rect[1] > 390:
			self.atualiza_posicao(self.rect[0]+10, self.rect[1] -10)
			#self.image = self.imagem_da_vez[seletor_image_leon]
			
	def desliza_baixo(self, seletor_imagens_leon):
		if self.rect[1] < 500:
			self.atualiza_posicao(self.rect[0]-10 , self.rect[1] +10)
			self.image = self.imagem_da_vez[seletor_imagens_leon]
		
	def pula(self):
		if self.posicao == 'cima':
			self.y_inicial = 390
			#self.rect[1] += self.controle_pulo[self.controlador_pulo]
		elif self.posicao == 'baixo':
			self.y_inicial = 500
	
		self.rect[1] += self.controle_pulo[self.controlador_pulo]
		
	def controla_pulo(self):
		if self.y_inicial == self.rect[1]:
			self.controlador_pulo = 'sob'
			self.ativa_pulo = False	
		elif self.y_inicial > self.rect[1] <= (self.y_inicial - 100):
			self.controlador_pulo = 'desce'
		if self.ativa_pulo == False:
			self.controlador_pulo = 'sob'
			
	def alterna_posicao(self):
		if self.rect[1] == 390:
			self.posicao = 'cima'
		elif self.rect[1] == 500:
			self.posicao = 'baixo'
		elif self.rect[1] == 440:
			self.posicao = 'pulo'
			
	def morre(self):
		self.vida -= 1
	
	def gameOver(self):
		if self.vida < 0:
			self.game_over = True
			print self.vida, self.game_over
	
	def pontua(self):
		self.pontuacao += 10
		
	
