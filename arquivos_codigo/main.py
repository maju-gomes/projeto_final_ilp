import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((550, 650))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

fonte = pygame.font.Font("./assets/interface_do_usuario/pixelifsans.ttf", 40)

# IMAGENS
fundo_ceu = pygame.image.load("./assets/objetos/background-day.png")
fundo_ceu = pygame.transform.scale(fundo_ceu, (550, 650))

base_rect= pygame.image.load("./assets/objetos/base.png")
base_rect= pygame.transform.scale(base_rect, (560, 112))

passaro1_rect= pygame.image.load("./assets/objetos/yellowbird-midflap.png")
passaro1_rect = pygame.transform.scale(passaro1_rect, (51, 36))

# Variáveis do jogo
passaro_y = 300  # Posição Y inicial do pássaro
passaro_y_velocidade = 0  # Velocidade do movimento do pássaro
gravidade = 0.5  # Força de gravidade que vai puxar o pássaro para baixo
pulo = -10  # Velocidade do pulo do pássaro
jogo_ativo = False  # Controle de início do jogo

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                jogo_ativo = True
                passaro_y_velocidade = pulo 

    if not jogo_ativo:
        screen.blit(fundo_ceu, (0, 0))  
        screen.blit(base_rect, (0, 540))  
        texto = fonte.render("Clique para Começar", False, (225, 225, 255))
        screen.blit(texto, (82,100))
        screen.blit(passaro1_rect, (225, 250))
    else:
        passaro_y_velocidade += gravidade
        passaro_y += passaro_y_velocidade

        if passaro_y >= 540 - passaro1_rect.get_height():
            jogo_ativo = False  # Finaliza o jogo
            texto_perda = fonte.render("Você Perdeu", False, (255, 255, 255))
            screen.blit(texto_perda, (82, 100))


                
        screen.blit(fundo_ceu, (0, 0))  
        screen.blit(base_rect, (0, 540))  
        screen.blit(passaro1_rect,(225, int(passaro_y)))  

    pygame.display.update()
    clock.tick(60)
