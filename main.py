import pyxel
import player as Player
import enemy as Enemy
import bullet as Bullet
import blast as Blast

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2


class App:
    def __init__(self):
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
        self.scene = SCENE_TITLE
        self.player = Player.Player(pyxel.width / 2, pyxel.height - 20)
        self.enemies = []
        self.bullets = []
        self.blasts = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()
        return

    def update_title_scene(self):
        # ENTERキーが押されたら、self.sceneをSCENE_PLAYに更新
        if pyxel.btnp(pyxel.KEY_RETURN) :
            self.scene = SCENE_PLAY
        
        return

    def update_play_scene(self):
        # frame_countが適当な値の倍数のとき、ememiesリストに新たなEnemyを追加する
        
        if pyxel.frame_count % 100==0:    # pyxel.frame_countが適当な値の倍数の時
            self.enemies.append(
                # 敵キャラクターをリストに追加する
                # 追加する要素は「Enemy.Enemy(x座標, y座標)」と書く
                Enemy.Enemy(pyxel.rndi(0,pyxel.width),0)


            )
        


        # プレイヤーと敵キャラクターの当たり判定
        
        for enemy in self.enemies:
            if (
                # プレイヤーが敵キャラクターと当たったときの条件
                # x軸方向の条件①
                # かつ x軸方向の条件②
                # かつ y軸方向の条件①
                # かつ y軸方向の条件②
                self.player.x + self.player.w < enemy.x  and self.player.x > enemy.x + enemy.w and
                self.player.y < enemy.y + enemy.h and self.player.h +self.player.y > enemy.y 
            ):
                enemy.is_alive =  False  # 敵キャラクターを消す
                self.scene =  SCENE_GAMEOVER  # ゲーム画面をゲームオーバー画面に切り替える

                # 爆発エフェクトを描画する
                # append関数を使ってself.blastsにBlast.Blast(x座標, y座標)を追加する
                self.blasts.append(
                Blast.Blast((self.player.w-self.player.x)/2,(self.player.h-self.player.y)/2)
            )
        

        # 弾丸と敵キャラクターの当たり判定
        # 当たった敵キャラクターと弾丸を消す
        
        for enemy in self.enemies:
            for bullet in self.bullets:
                if (
                    # 敵キャラクターが弾丸と当たったときの条件
                    # x軸方向の条件①
                    # かつ x軸方向の条件②
                    # かつ y軸方向の条件①
                    # かつ y軸方向の条件②
                    enemy.x < self.x +self.w and enemy.x +enemy.w > self.x and
                    enemy.y < self.y + self.h and enemy.y+enemy.h > self.h
                ):
                    # 敵キャラクターと弾丸を消す
                    enemy.is_alive = False
                    bullet.is_alive = False

                    # 爆発エフェクトを描画する
                    # append関数を使ってself.blastsにBlast.Blast(x座標, y座標)を追加する
                    self.blasts.append(
                Blast.Blast((enemy.w-enemy.x)/2,(enemy.h-enemy.y)/2)
            )
        
        

        # スペースキーが押されたら弾丸を発射する
        
        if  pyxel.btnp(pyxel.KEY_SPACE) :    # スペースキーが押されたら
            self.bullets.append(
                # 弾丸をリストに追加する
                # 追加する要素は、「Bullet.Bullet(x座標, y座標)」と書く
                self.bullets.append(
                Bullet.Bullet((self.player.w-self.player.x)/2,self.player.y)
            )

            )
    

        self.player.update()
        self.update_list(self.enemies)
        self.update_list(self.bullets)
        self.update_list(self.blasts)
        self.cleanup_list(self.enemies)
        self.cleanup_list(self.bullets)
        self.cleanup_list(self.blasts)
        return

    def update_gameover_scene(self):
        self.update_list(self.enemies)
        self.update_list(self.bullets)
        self.update_list(self.blasts)
        self.cleanup_list(self.enemies)
        self.cleanup_list(self.bullets)
        self.cleanup_list(self.blasts)
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_PLAY
            self.player.x = pyxel.width / 2
            self.player.y = pyxel.height - 20
            self.enemies.clear()
            self.bullets.clear()
            self.blasts.clear()
        return

    def draw(self):
        pyxel.cls(0)
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()
        return

    def draw_title_scene(self):
        # (22, 66)の位置に、タイトル「Pyxel Shooter Example」を表示
        # (31, 126)の位置に、「- PRESS ENTER -」を表示
        # 文字の位置と内容は好きな値に変更してください
        pyxel.text(22,66,"Pyxel shooter Example", pyxel.frame_count % 16)
        pyxel.text(31,126,"Pless Enter", 13)




        return

    def draw_play_scene(self):
        self.player.draw()
        self.draw_list(self.enemies)
        self.draw_list(self.bullets)
        self.draw_list(self.blasts)
        return

    def draw_gameover_scene(self):
        self.draw_list(self.enemies)
        self.draw_list(self.bullets)
        self.draw_list(self.blasts)
        pyxel.text(43, 66, "GAME OVER", 8)
        pyxel.text(31, 126, "- PRESS ENTER -", 13)
        return

    def update_list(self, list):
        for elem in list:
            elem.update()
        return
    
    def draw_list(self, list):
        for elem in list:
            elem.draw()
        return

    def cleanup_list(self, list):
        i = 0
        while i < len(list):
            elem = list[i]
            if elem.is_alive == False:
                list.pop(i)
            else:
                i += 1
        return


App()
