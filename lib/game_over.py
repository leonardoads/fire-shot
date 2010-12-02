from tela import *

def game_over():
	arquivo = open('tipo_tela.fs')
	tipo_tela = arquivo.read().strip()
	arquivo.close()
	pygame.init()
	tela = Tela('imagens', 'game_over.jpg',tipo_tela)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
					return
					
					
		tela.screen.blit(tela.background, tela.background_position)
		pygame.display.update()
	
#game_over()
