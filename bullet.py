import pyxel

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 11
BULLET_SPEED = 4

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.is_alive = True
        return

    def update(self):
        # 弾の速度（BULLET_SPEED）分だけ画面の上方向に移動する
        self.y -= BULLET_SPEED
        # 弾の上端が画面の端に来たら、is_aliveをFalseにする
        if self.y == 0:
            self.is_alive = False
        return

    def draw(self):
        # 位置（x, y）に、幅がw、高さがhの長方形を描く
        pyxel.rect(self.x,self.y,self.w,self.h,3)
        return

    def test(self):
        pyxel.init(120, 160, title="Pyxel Shooter example")
        pyxel.run(self.update, self.draw)


if __name__ == '__main__':
    bulllet_test = Bullet(10, 120)
    Bullet.test(bulllet_test)