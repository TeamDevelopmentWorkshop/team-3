import pyxel

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

class Blast:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.is_alive = True

    def update(self):
        # 自身の半径を1だけ大きくする
        # 閾値（BLAST_END_RADIUS）より半径が大きくなったら、is_aliveをFalseにする
        self.radius += 1
        if(self.radius > BLAST_END_RADIUS):
            self.is_alive = False
        else:
            self.is_alive = True

        return

    def draw(self):
        # 位置（x, y）に半径がradiusの円を描く
        # 位置（x, y）に半径がradiusの円の輪郭線を描く
        pyxel.circ(self.x,self.y,self.radius,BLAST_COLOR_IN)
        pyxel.circb(self.x,self.y,self.radius,BLAST_COLOR_OUT)
        return

    def test(self):
        pyxel.init(120, 160, title="Pyxel Shooter example")
        pyxel.run(self.update, self.draw)


if __name__ == '__main__':
    blast_test = Blast(10, 20)
    Blast.test(blast_test)