import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((550, 650)) # x, y - em pygame, no topo esquerdo está a coordenada 0,0
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock() # cria um objeto para ajudar a rastrear o tempo

# CARREGANDO IMAGENS 
# botao start
botao_iniciar = pygame.image.load("./assets/objetos/botao.png")
# fundo
fundo_ceu = pygame.image.load("./assets/objetos/background-day.png")
novo_tamanho_fundo_ceu = (550, 650)
fundo_ceu = pygame.transform.scale(fundo_ceu, novo_tamanho_fundo_ceu)
# base
base = pygame.image.load("./assets/objetos/base.png")
novo_tamanho_base = (560, 112)
base = pygame.transform.scale(base, novo_tamanho_base)
# passaro
novo_tamanho_passaro = (51, 36)
# 1 frame
passaro1 = pygame.image.load("./assets/objetos/yellowbird-midflap.png")
passaro1 = pygame.transform.scale(passaro1, novo_tamanho_passaro)
# 2 frame
# passaro2 = pygame.image.load("./assets/objetos/yellowbird-downflap.png")
# passaro2 = pygame.transform.scale(passaro2, novo_tamanho_passaro)
# # 3 frame
# passaro3 = pygame.image.load("./assets/objetos/yellowbird-upflap.png")
# passaro3 = pygame.transform.scale(passaro3, novo_tamanho_passaro)
# tubo
# tubo = pygame.image.load("./assets/objetos/pipe-green.png")
# novo_tamanho_tubo = (104, 640)
# tubo = pygame.transform.scale(tubo, novo_tamanho_tubo)

run = True
while True:
    for event in pygame.event.get():
        # loop para todos os eventos que acontecem enquanto o while é true
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(fundo_ceu, (0, 0))
    screen.blit(base, (0, 540))
    screen.blit(passaro1, (225, 300))
    screen.blit(botao_iniciar, (150, 200))

    # screen.blit(tubo, (300, 0))
      
    pygame.display.update()
    # desenha todas as nossas imagens
    # atualiza tudo
    clock.tick(60)
    # By calling Clock.tick(40) once per frame, for example,
    # the program will never run at more than 40 frames per second.