import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((550, 650))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fonte = pygame.font.Font("./assets/interface_do_usuario/pixelifsans.ttf", 40)
# situacoes do jogo
situacoes = {
"inicio": 0,
"jogando": 1,
"derrota": 2}

jogo_situacao = situacoes["inicio"] # O jogo começa desde o inicio

velocidade_passaro_y = 0
gravidade = 0.5
posicao_passaro_y = 250
impulso = -10

# IMAGENS
fundo_ceu = pygame.image.load("./assets/objetos/background-day.png")
fundo_ceu = pygame.transform.scale(fundo_ceu, (550, 650))

base_rect= pygame.image.load("./assets/objetos/base.png")
base_rect= pygame.transform.scale(base_rect, (560, 112))

passaro1_rect= pygame.image.load("./assets/objetos/yellowbird-midflap.png")
passaro1_rect = pygame.transform.scale(passaro1_rect, (51, 36))



# Lógica do jogo / Funções

# jogo rodando
def jogo_rodando():
    global posicao_passaro_y, velocidade_passaro_y

    # Aplica a gravidade e o movimento do pássaro
    posicao_passaro_y += velocidade_passaro_y
    velocidade_passaro_y += gravidade

    screen.blit(fundo_ceu, (0, 0))  
    screen.blit(base_rect, (0, 540))  
    screen.blit(passaro1_rect,(225, posicao_passaro_y))  

    if posicao_passaro_y >= 540:
        # O pássaro atingiu o chão, ou seja: fim de jogo
        return True

    return False

# dela de perda
def tela_derrota():
        # imagens 
        

        # textos
        texto_derrota1 = fonte.render("Você perdeu!", True, (255, 255, 255))
        texto_derrota2 = fonte.render("Clique para voltar", True, (255, 255, 255))
        texto_derrota3 = fonte.render("à tela inicial", True, (255, 255, 255))
        screen.blit(texto_derrota1, (155, 85))  # Exibe a mensagem de derrota
        screen.blit(texto_derrota2, (75, 155))  # Exibe a mensagem de derrota
        screen.blit(texto_derrota3, (75, 195))  # Exibe a mensagem de derrota

def tela_inicio():
        # imagens


        # textos
        texto_inicio = fonte.render("Clique para começar", True, (255, 255, 255))
        screen.blit(texto_inicio, (75, 85))  # Exibe a mensagem de início

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

# Condicionais 
    if jogo_situacao == situacoes["inicio"]:
        tela_inicio()

    elif jogo_situacao == situacoes["jogando"]:
        if jogo_rodando():
            jogo_situacao = situacoes["derrota"]
        pygame.display.update()

    elif jogo_situacao == situacoes["derrota"]:
        tela_derrota()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Reinicia o jogo
                posicao_passaro_y = 250
                velocidade_passaro_y = -1
                jogo_situacao = situacoes["inicio"]  # Volta para o início
        
    pygame.display.update()
    clock.tick(60)
