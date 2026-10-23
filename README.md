# Flappy Bird em Python

## Descrição

Jogo em Python/Pygame inspirado em Flappy Bird, com movimentação do pássaro, obstáculos e pontuação. O repositório preserva duas implementações históricas alternativas; a execução completa exige ambiente gráfico.

## Stack e bibliotecas

Python e Pygame.

Dependências e versões declaradas: [requirements.txt](requirements.txt).

## Funcionalidades

- Movimento do pássaro.
- Obstáculos.
- Pontuação.

## Licença

Não há uma licença de distribuição definida para este repositório. Nenhuma licença MIT, Apache ou equivalente é concedida por este README. As atribuições e os direitos dos materiais de terceiros permanecem preservados.

## Validação e limites

Geometria/movimento e recursos; gameplay completo exige execução gráfica.

## Executar
Requer Python 3.11+ e uma sessão gráfica:
```sh
python -m pip install -r requirements.txt
python FlappyBird.py
```
Pressione Espaço para pular. As imagens são resolvidas em relação ao arquivo do jogo, independentemente do diretório do terminal.

## Testar
```sh
python -m unittest discover -s tests -v
```
Os testes usam o driver gráfico dummy do SDL e verificam a movimentação/geometria dos canos. A experiência visual deve ser conferida manualmente.

## Organização e manutenção

As duas implementações históricas permanecem identificadas como alternativas. Classes de pássaro/cano já delimitam entidades; caminhos dos assets são relativos ao script e testes usam SDL sem janela. Não é necessária arquitetura MVVM para o loop de jogo.

Veja [a revisão de desenvolvimento](docs/REVISAO.md) para decisões, testes e limites, e [o guia de contribuição](CONTRIBUTING.md) para o fluxo de manutenção.
