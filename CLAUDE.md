# Flappy Bird em Python (estudo)

Jogo em **Pygame** inspirado em Flappy Bird: movimentação do pássaro, obstáculos e pontuação.

## Estrutura
```
flappy_bird.py   implementação principal (cerca de 280 linhas: classes Passaro, Cano, Chao e loop)
FlappyBird.py    implementação histórica alternativa (cerca de 230 linhas), preservada
imagens/, imgs/  sprites
tests/test_game.py  testa regras (colisão e pontuação) sem abrir janela
```

## Comandos (PowerShell)
```powershell
python -m pip install -r requirements.txt     # pygame>=2.5,<3
python -m unittest discover -s tests -v
python flappy_bird.py                         # precisa de ambiente gráfico
```

## CI e deploy
- `ci.yml` roda unittest (headless).
- Não há deploy.

## Regras
- Testes não dependem de janela. Use `SDL_VIDEODRIVER=dummy` se precisar inicializar o pygame.
- Preserve as duas versões históricas. Melhorias vão na `flappy_bird.py`.
- Não adicione assets do jogo original.
