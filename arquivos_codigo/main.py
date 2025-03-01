import pygame
from sys import exit
import random
import time

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

passaro1 = pygame.image.load("./assets/objetos/yellowbird-upflap.png")
passaro1 = pygame.transform.scale(passaro1, (51, 36))

passaro2 = pygame.image.load("./assets/objetos/yellowbird-midflap.png")
passaro2 = pygame.transform.scale(passaro2, (51, 36))

passaro3 = pygame.image.load("./assets/objetos/yellowbird-downflap.png")
passaro3 = pygame.transform.scale(passaro3, (51, 36))

bola_fogo1 = pygame.image.load("./assets/objetos/FB001.png")
bola_fogo1 = pygame.transform.scale(bola_fogo1, (112, 56))
bola_fogo1 = pygame.transform.rotate(bola_fogo1, 180)

# BOLAS DE FOGO
bola_fogo2 = pygame.image.load("./assets/objetos/FB002.png")
bola_fogo2 = pygame.transform.scale(bola_fogo2, (112, 56))
bola_fogo2 = pygame.transform.rotate(bola_fogo2, 180)

bola_fogo3 = pygame.image.load("./assets/objetos/FB003.png")
bola_fogo3 = pygame.transform.scale(bola_fogo3, (112, 56))
bola_fogo3 = pygame.transform.rotate(bola_fogo3, 180)

bola_fogo4 = pygame.image.load("./assets/objetos/FB004.png")
bola_fogo4 = pygame.transform.scale(bola_fogo4, (112, 56))
bola_fogo4 = pygame.transform.rotate(bola_fogo4, 180)

bola_fogo5 = pygame.image.load("./assets/objetos/FB005.png")
bola_fogo5 = pygame.transform.scale(bola_fogo5, (112, 56))
bola_fogo5 = pygame.transform.rotate(bola_fogo5, 180)

# PÁSSARO E BOLA DE FOGO
animacao_passaro = [passaro1, passaro2, passaro3]
animacao_bola_fogo = [bola_fogo1, bola_fogo2, bola_fogo3, bola_fogo4, bola_fogo5]
indice_animacao = 0
contador_animacao = 0


# FUNÇÕES
def jogo_rodando():
    global posicao_passaro_y, velocidade_passaro_y, indice_animacao, contador_animacao

    posicao_passaro_y += velocidade_passaro_y
    velocidade_passaro_y += gravidade

    screen.blit(fundo_ceu, (0, 0))
    screen.blit(base_rect, (0, 540))

    if posicao_passaro_y >= 515:
        # O pássaro atingiu o chão, ou seja: fim de jogo
        return True

    if contador_animacao >= 5:  # A cada 5 quadros, troca a animação
        contador_animacao = 0
        indice_animacao = (indice_animacao + 1) % len(animacao_passaro) # Alterna entre as imagens do pássaro

    # Desenha o pássaro através do índice de animação
    screen.blit(animacao_passaro[indice_animacao], (225, posicao_passaro_y))

    contador_animacao += 1

    return False

bola_fogo_posicoes = []

def gerar_bola_fogo():
    y = random.randint(50, 400)
    return {"x": 550, "y": y, "visivel": True, "tempo_desaparecer": time.time(), "indice_animacao": 0, "contador_animacao": 0}

def mover_bolas_fogo():
    global bola_fogo_posicoes
    novas_bolas = []

    for bola in bola_fogo_posicoes:
        if bola["visivel"]:
            bola["x"] -= 5

        elif bola["visivel"] == False:
            bola["tempo_desaparecer"] = time.time()

        if not bola["visivel"]:
            if time.time() - bola["tempo_desaparecer"] >= 2:  # Espera 2 segundos
                bola["visivel"] = True  # Torna a bola visível novamente
                bola["x"] = 550  # Coloca a bola novamente no início
                bola["y"] = random.randint(50, 400)  # Nova posição aleatória

        # ANIMAÇÃO DA BOLA DE FOGO
        bola["contador_animacao"] += 1
        if bola["contador_animacao"] >= 5:
            bola["contador_animacao"] = 0
            bola["indice_animacao"] = (bola["indice_animacao"] + 1) % len(animacao_bola_fogo)

        screen.blit(animacao_bola_fogo[bola["indice_animacao"]], (bola["x"], bola["y"]))

        novas_bolas.append(bola)

    bola_fogo_posicoes = novas_bolas

def verificar_colisao():
    for bola in bola_fogo_posicoes:
        if bola["visivel"]:
            # Ajustando o cálculo da colisão
            if (bola["x"] < 275 and bola["x"] + 112 > 225) and (bola["y"] < posicao_passaro_y + 36 and bola["y"] + 56 > posicao_passaro_y):
                return True
    return False

def desenhar_bolas_fogo():
    for bola in bola_fogo_posicoes:
        if bola["visivel"]:
            screen.blit(animacao_bola_fogo[bola["indice_animacao"]], (bola["x"], bola["y"]))

def tela_derrota():
    screen.blit(fundo_ceu, (0, 0))  
    screen.blit(base_rect, (0, 540)) 

    texto_derrota1 = fonte.render("Você perdeu!", True, (255, 255, 255))
    texto_derrota2 = fonte.render("Clique para voltar", True, (255, 255, 255))
    texto_derrota3 = fonte.render("à tela inicial", True, (255, 255, 255))
    
    screen.blit(texto_derrota1, (155, 85))
    screen.blit(texto_derrota2, (75, 155))
    screen.blit(texto_derrota3, (75, 195))
    
    screen.blit(animacao_passaro[indice_animacao], (225, posicao_passaro_y))

def tela_inicio():
    screen.blit(fundo_ceu, (0, 0))
    screen.blit(base_rect, (0, 540))

    texto_inicio = fonte.render("Clique para começar", True, (255, 255, 255))
    screen.blit(texto_inicio, (75, 85)) 
    
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

    elif jogo_situacao == situacoes["jogando"]:
        if jogo_rodando():
            jogo_situacao = situacoes["derrota"]
        
        if random.randint(1, 100) == 1:
            bola_fogo_posicoes.append(gerar_bola_fogo())
        
        mover_bolas_fogo()
        if verificar_colisao():  # Verifica colisão durante o jogo
            jogo_situacao = situacoes["derrota"]
            print("Colisao detectada]")

    elif jogo_situacao == situacoes["derrota"]:
        tela_derrota()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Reinicia o jogo
                posicao_passaro_y = 250
                velocidade_passaro_y = -1
                bola_fogo_posicoes = []  # Reseta as bolas de fogo
                jogo_situacao = situacoes["inicio"]  # Volta para o início

    pygame.display.update()
    clock.tick(60)
