# Flappy Bird em Python
Estudo de animação, colisão e pontuação com Pygame. Inclui duas implementações históricas: `FlappyBird.py` e `flappy_bird.py`.

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

## Licença
Não há licença de distribuição definida. Os recursos gráficos também precisam ter seus direitos de uso verificados antes de redistribuição.
