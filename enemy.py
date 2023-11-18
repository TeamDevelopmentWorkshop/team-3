import pyxel

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.dir = 1
        self.timer_offset = pyxel.rndi(0, 59)
        self.is_alive = True

    def update(self):
        # y方向には一定の速度(ENEMY_SPEED)で移動

        # x方向の速度は一定の間隔で向きを変える
        # ヒント１：frame_count変数を適当な値で割った時の余りを使って条件分岐する
        # ヒント２：frame_countに乱数（timer_offset）を加えて、向きを変えるタイミングをランダムにする

        # yが画面の下端より大きいとき、is_aliveをFalseにする
        return
    
    def draw(self):
        # イメージバンクの(u, v)からサイズ(w, h)の領域を、(x, y)にコピー
        return

    def test(self):
        pyxel.image(0).set(
            8,
            0,
            [
                "00088000",
                "00ee1200",
                "08e2b180",
                "02882820",
                "00222200",
                "00012280",
                "08208008",
                "80008000"
            ],
        )
        pyxel.run(self.update, self.draw)


if __name__ == '__main__':
    pyxel.init(120, 160, title="Pyxel Shooter example")
    enemy_test = Enemy(10, 20)
    Enemy.test(enemy_test)