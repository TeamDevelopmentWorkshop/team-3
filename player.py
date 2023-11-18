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
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= PLAYER_SPEED

        # ex) 右矢印が押されていたら、xにPLAYER_SPEEDを足す

        # python標準関数のmaxとminを使って、Playerが画面外に出ないようにする
        if self.x <= 0:
            self.x = 112
        if self.x > 112:
            self.x = 0

        """self.x = max(self.x,0)
        self.x = min(self.x,112)"""
        
        self.y = max(self.y,76)
        self.y = min(self.y,152)
        return

    def draw(self):
        # イメージバンクの(0, 0)からサイズ(w, h)の領域を、(x, y)にコピー
        pyxel.blt(self.x,self.y,0,0,0,self.w,self.h)
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