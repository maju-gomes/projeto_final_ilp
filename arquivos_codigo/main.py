import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((550, 650))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fonte = pygame.font.Font("./assets/interface_do_usuario/pixelifsans.ttf", 40)

# Situações do jogo
situacoes = {
    "inicio": 0,
    "jogando": 1,
    "derrota": 2
}

jogo_situacao = situacoes["inicio"]  # O jogo começa desde o inicio

velocidade_passaro_y = 0
gravidade = 0.5
posicao_passaro_y = 250
impulso = -10

# IMAGENS
fundo_ceu = pygame.image.load("./assets/objetos/background-day.png")
fundo_ceu = pygame.transform.scale(fundo_ceu, (550, 650))

base_rect = pygame.image.load("./assets/objetos/base.png")
base_rect = pygame.transform.scale(base_rect, (560, 112))

passaro1_rect = pygame.image.load("./assets/objetos/yellowbird-upflap.png")
passaro1_rect = pygame.transform.scale(passaro1_rect, (51, 36))

passaro2_rect = pygame.image.load("./assets/objetos/yellowbird-midflap.png")
passaro2_rect = pygame.transform.scale(passaro2_rect, (51, 36))

passaro3_rect = pygame.image.load("./assets/objetos/yellowbird-downflap.png")
passaro3_rect = pygame.transform.scale(passaro3_rect, (51, 36))

cano_inferior_rect = pygame.image.load("assets/objetos/pipe-green.png")
cano_inferior_rect = pygame.transform.scale(cano_inferior_rect, (78, 480))

cano_superior_rect = pygame.image.load("assets/objetos/pipe-green.png")
cano_superior_rect = pygame.transform.scale(cano_superior_rect, (78, 480))
cano_superior_rect = pygame.transform.rotate(cano_superior_rect, 180)


# Animação do pássaro
animacao_passaro = [passaro1_rect, passaro2_rect, passaro3_rect]
indice_animacao = 0
contador_animacao = 0

# Funções
# Jogo rodando
def jogo_rodando():
    global posicao_passaro_y, velocidade_passaro_y, indice_animacao, contador_animacao

    # Gravidade e o movimento do pássaro
    posicao_passaro_y += velocidade_passaro_y
    velocidade_passaro_y += gravidade

    # Limpa a tela desenhando o fundo e a base
    screen.blit(fundo_ceu, (0, 0))
    screen.blit(base_rect, (0, 540))

    if posicao_passaro_y >= 515:
        # O pássaro atingiu o chão, ou seja: fim de jogo
        return True

    if contador_animacao >= 5:  # A cada 5 quadros, troca a animação
        contador_animacao = 0
        indice_animacao = (indice_animacao + 1) % len(animacao_passaro)  # Alterna entre as imagens do pássaro

    # Desenha o pássaro com base no índice de animação
    screen.blit(animacao_passaro[indice_animacao], (225, posicao_passaro_y))

    contador_animacao += 1

    return False

# Gerando canos
def gerar_canos():
    altura_cano_superior = random.randint(100, altura_maxima_cano)
    al

# Tela de derrota
def tela_derrota():
    # Limpa a tela desenhando o fundo e a base corretamente
    screen.blit(fundo_ceu, (0, 0))  
    screen.blit(base_rect, (0, 540))  

    texto_derrota1 = fonte.render("Você perdeu!", True, (255, 255, 255))
    texto_derrota2 = fonte.render("Clique para voltar", True, (255, 255, 255))
    texto_derrota3 = fonte.render("à tela inicial", True, (255, 255, 255))
    
    screen.blit(texto_derrota1, (155, 85))
    screen.blit(texto_derrota2, (75, 155))
    screen.blit(texto_derrota3, (75, 195))
    
    screen.blit(animacao_passaro[indice_animacao], (225, posicao_passaro_y))

# Tela de início
def tela_inicio():
    # Limpa a tela desenhando o fundo de céu e a base
    screen.blit(fundo_ceu, (0, 0))  # Desenha o fundo de céu
    screen.blit(base_rect, (0, 540))  # Desenha a base

    texto_inicio = fonte.render("Clique para começar", True, (255, 255, 255))
    screen.blit(texto_inicio, (75, 85))  # Exibe a mensagem de início
    
    screen.blit(animacao_passaro[indice_animacao], (225, posicao_passaro_y))

# Loop principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if jogo_situacao == situacoes["inicio"]:
                    jogo_situacao = situacoes["jogando"]
                if jogo_situacao == situacoes["jogando"]:
                    velocidade_passaro_y = impulso
                    
    # Condicionais para desenhar as telas
    if jogo_situacao == situacoes["inicio"]:
        tela_inicio()
        print("Tela de inicio")

    elif jogo_situacao == situacoes["jogando"]:
        if jogo_rodando():
            jogo_situacao = situacoes["derrota"]
        pygame.display.update()
        print("Jogo rodando")

    elif jogo_situacao == situacoes["derrota"]:
        tela_derrota()
        print("Tela de perda")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Reinicia o jogo
                posicao_passaro_y = 250
                velocidade_passaro_y = -1
                jogo_situacao = situacoes["inicio"]  # Volta para o início

    pygame.display.update()
    clock.tick(60)
