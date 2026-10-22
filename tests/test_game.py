import os
os.environ.setdefault('SDL_VIDEODRIVER','dummy')
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
import unittest
import FlappyBird as game

class GameTests(unittest.TestCase):
    def test_cano_se_move_para_esquerda(self):
        cano=game.Cano(500)
        cano.mover()
        self.assertLess(cano.x,500)
    def test_canos_deixam_espaco_de_passagem(self):
        cano=game.Cano(500)
        self.assertEqual(cano.pos_base-cano.altura,cano.DISTANCIA)

if __name__=='__main__':unittest.main()
