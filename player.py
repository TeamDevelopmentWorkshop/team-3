import pyxel

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.is_alive = True

    def update(self):
        # Playerを十字キーで操作する
        # ex) 右矢印が押されていたら、xにPLAYER_SPEEDを足す

        # python標準関数のmaxとminを使って、Playerが画面外に出ないようにする
        return

    def draw(self):
        # イメージバンクの(0, 0)からサイズ(w, h)の領域を、(x, y)にコピー
        return

    def test(self):
        pyxel.init(120, 160, title="Pyxel Shooter example")
        pyxel.image(0).set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b07c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0"
            ],
        )
        pyxel.run(self.update, self.draw)


if __name__ == '__main__':
    player_test = Player(10, 20)
    Player.test(player_test)