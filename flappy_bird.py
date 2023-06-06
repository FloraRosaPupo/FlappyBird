import pygame
import os  # itegra o cod. com os arquivos do pc
import random

# constantes
TELA_LARGURA = 500
TELA_ALTURA = 800

# pygame.image.load(...)) -> carrega a imagem
# os.path.join(...) -> itegra a pasta e a imagem no cod.
# pygame.transform.scale2x(...) -> aumenta o tamanho da imagem

IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imagens', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imagens', 'base.png')))
IMAGEM_FUNDO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imagens', 'bg.png')))

# lista com as imagens do passaro
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imagens', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imagens', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imagens', 'bird3.png')))
]

# incializar a font
pygame.font.init()

FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGENS_PASSARO

    # animação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # atributos
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y  # altura dele no eixo Y
        self.tempo = 0  # da parabola
        self.contagem_imagem = 0  # freme da imagem

        self.imagem = self.IMGS[0]  # acesso a primeira imagem da lista

    # eixo Y

    def pular(self):
        self.velocidade = -10.5  # negativa pra cima
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento:
        self.tempo += 1  # a cada frame
        # s = so+vot+at^2/2  -> 1.5 é a aceleração
        deslocamento = 1.5*(self.tempo**2) + self.velocidade*self.tempo

        # ajustar deslocamento:
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # angulo do passaro:
        # altura é a ultima vez q ele pulou
        if deslocamento < 0 or self.y < (self.altura+50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # imagem do passaro
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]  # asas pra cima
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]  # asas pro meio
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]  # asas pra baixo
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]  # asas pro meio
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4+1:
            self.imagem = self.IMGS[0]  # asas pra cima
            self.contagem_imagem = 0

        # se o passaro tiver caindo nao bate asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * \
                2  # a proxima batida vai ser da imagem 2

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centroimg = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centroimg)

        # funcao do pygame pra desenhar na tela, preciso passar a tela como paramentro
        tela.blit(imagem_rotacionada, retangulo.topleft)

        # dividir o retangulo do passaro em pixels
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200  # distancia no eixo y dos canos
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.postopo = 0  # eixo Y
        self.posbaixo = 0  # eixo Y
        # pygame.transform.flip(Nome da imagem, No eixo X?, No eixo Y?)
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()  # rodar a Funcao

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.postopo = self.altura - self.CANO_TOPO.get_height()
        self.posbaixo = self.altura + self.DISTANCIA

     # movimentacao cano

    def mover_cano(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.postopo))
        tela.blit(self.CANO_BASE, (self.x, self.posbaixo))

    def colisao(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        # round ->arredonda o valor -> faço isso pq a posição do passaro no eixo y muda mto
        distancia_topo = (self.x - passaro.x, self.postopo - round(passaro.y))
        distancia_baixo = (self.x - passaro.x,
                           self.posbaixo - round(passaro.y))

        # verifico o ponto de colisão do passaro e dos canos
        base_ponto = passaro_mask.overlap(base_mask, distancia_baixo)
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)

        if base_ponto or topo_ponto:  # se um desses dois é True é pq houve colisao
            return True
        else:
            return False


class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x0 = 0  # CHAO 1
        self.x1 = self.LARGURA  # CHAO 2

    def mover_chao(self):
        self.x0 -= self.VELOCIDADE
        self.x1 -= self.VELOCIDADE

        if self.x0 + self.LARGURA < 0:  # se o CHAO 1 saiu da tela
            self.x0 = self.x1 + self.LARGURA  # coloco ele pro final da tela denovo

        if self.x1 + self.LARGURA < 0:  # se o CHAO 2 saiu da tela
            self.x1 = self.x0 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x0, self.y))
        tela.blit(self.IMAGEM, (self.x1, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_FUNDO, (0, 0))

    for passaro in passaros:
        passaro.desenhar(tela)

    # mais de um cano na tela ao mesmo tempo
    for cano in canos:
        cano.desenhar(tela)

    # render -> renderizar o texto na tela
    texto = FONTE_PONTOS.render("Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA-10-texto.get_width(), 10))
    chao.desenhar(tela)

    # criar a tela
    pygame.display.update()

# criar todas as "coisa" do jogo


def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]

    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0

    # atualizar a tela por segundo
    relogio = pygame.time.Clock()

    # jogo pra rodar
    """LOOP infinito"""
    rodando = True

    while rodando:
        relogio.tick(30)  # 30 frames por seg.

        # interação com o usuario -> lista de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        # mover na tela
        for passaro in passaros:
            passaro.mover()

        chao.mover_chao()

        adicionar_cano = False
        remover_canos = []

        for cano in canos:
            # cano bateu co o passaro?
            # posicao do passaro dentro da lista
            for i, passaro in enumerate(passaros):
                if cano.colisao(passaro):
                    passaros.pop(i)

                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True

                cano.mover_cano()

                # adicionano o cano que precisa ser excluido
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)
                if cano.x + cano.CANO_BASE.get_width() < 0:
                    remover_canos.append(cano)

            if adicionar_cano:
                pontos += 1
                canos.append(Cano(600))

            for cano in remover_canos:
                canos.remove(cano)

            # verificando se o passaro passo do chao ou passou pelo ceu
            for i,  passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                    passaros.pop(i)

        desenhar_tela(tela, passaros, canos, chao, pontos)

if __name__ == '__main__':
    main()
