import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.5)
musica = pygame.mixer.music.load('03. Underwater Theme.mp3')
pygame.mixer.music.play(-1)

barulho = pygame.mixer.Sound('smb_1-up.wav')
barulho.set_volume((0.1))

largura = 640
altura = 480
x_maca = randint(40, 600)
y_maca = randint(50, 430)

velocidade = 4
x_controle = velocidade
y_controle = 0


pontos = 0
lista_cobra = []
comprimento_inicial = 5

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
x_cobra = largura/2
y_cobra = altura/2
relogio = pygame.time.Clock()
morreu = False

fonte = pygame.font.SysFont('impact', 40, False, True)

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar():
    global pontos, x_cobra, y_cobra, comprimento_inicial, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    x_cobra = largura//2
    y_cobra = altura//2
    comprimento_inicial = 5
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(20, 660)
    y_maca = randint(20, 460)
    morreu = False


while True:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, False, (0, 0 ,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = -(velocidade)
                y_controle = 0
            elif event.key == K_d and x_controle != -(velocidade):
                x_controle = velocidade
                y_controle = 0
            elif event.key == K_w and y_controle != velocidade:
                x_controle = 0
                y_controle = -(velocidade)
            elif event.key == K_s and y_controle != -(velocidade):
                x_controle = 0
                y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle
    ''' if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20'''

    if x_cobra >= largura:
      x_cobra = 0
    if y_cobra >= altura:
      y_cobra = 0
    if x_cobra < 0:
      x_cobra = largura
    if y_cobra < 0:
      y_cobra = altura

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))


    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho.play()
        comprimento_inicial += 2


    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
        fonte_2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem_2 = 'GAME OVER! Pressione a tecla R para jogar novamente'
        texto = fonte_2.render(mensagem_2, True, (0, 0, 0))
        ret_texto = texto.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto, ret_texto)
            pygame.display.update()
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    #pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40,)
    #pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)

    tela.blit(texto, (400, 20))
    pygame.display.update()
    pygame.font.get_fonts()