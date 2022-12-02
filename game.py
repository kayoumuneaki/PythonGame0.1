# coding: UTF-8

class Cat:
    def __init__(self, x, y):
        # プレイヤーのポジション
        self.x = x
        self.y = y
        
        # サイズを変える前の画像
        self.rough_image = pygame.image.load("/image/cat.png").convert()
        
        # サイズを変えたあとの画像
        self.image = pygame.transform.scale(self.rough_image, (20, 20))
        
        # ジャンプしてるときの画像
        self.immune_image = pygame.transform.scale(self.rough_image, (30, 30))
        
        # 動きに関するもの
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        
        # ジャンプしてるか否か
        self.immunity = False
        
        # プレイヤーは一定時間以上のジャンプは続けられない
        self.immune_count = 0
        
        # ライフ
        self.life = 4
        
        # ダメージを受けたあと、一定時間ダメージを受けない
        self.life_lost_time = 0
        
        
    # 動きに関して
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_UP:
                self.move_up = True
            if event.key == pygame.K_DOWN:
                self.move_down = True
            if event.key == pygame.K_SPACE:
                self.immunity = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_UP:
                self.move_up = False
            if event.key == pygame.K_DOWN:
                self.move_down = False
                
# ============================================================


# 線とドットの親クラス
class Rope:
    def __init__(self, x=0, y=0, velocity=0, tilt=0, color=0):
        self.x = 0
        self.y = 0
        self.velocity = velocity
        self.tilt = tilt
        self.color = color
    def update(self):
        return
    def judge(self, Cat):
        return

# ============================================================



#垂直の線
class Straight_Rope(Rope):
    def update(self):
        if(self.x > 635):
            self.direction = "LEFT"
        elif(self.x < 5):
            self.direction = "RIGHT"
        if(self.direction == "RIGHT"):
            self.x += self.velocity
        elif(self.direction == "LEFT"):
            self.x -= self.velocity
        pygame.draw.line(screen, COLORS[3], [self.x, 0], [self.x, 480], 5)

    #プレーヤーとぶつかったか判定
    def judge(self, Cat):
        if(self.x > (Cat.x) and self.x < (Cat.x + 20)):
            return True
        else:
            return False

#水平の線
class Straight_Rope_Horizontal(Rope):
    def update(self):
        if(self.y > 475):
            self.direction = "DOWN"
        elif(self.y < 5):
            self.direction = "UP"
        if(self.direction == "DOWN"):
            self.y -= self.velocity
        elif(self.direction == "UP"):
            self.y += self.velocity
        pygame.draw.line(screen, COLORS[3],[0, self.y], [640, self.y], 5)

    #プレーヤーとぶつかったか判定
    def judge(self, Cat):
        if(self.y > (Cat.y) and self.y < (Cat.y + 20)):
            return True
        else:
            return False
        
# ==========================================================


# ドット
class Shooting_Star(Rope):
    def update(self):
        self.x += self.tilt
        self.y += self.velocity
        pygame.draw.circle(screen, COLORS[self.color], [self.x, self.y], 6)
        
    # プレイヤーとぶつかったか判定
    def judge(self, Cat):
        if((self.y > (Cat.y) and self.y < (Cat.y + 20)) and (self.x > (Cat.x) and self.x < (Cat.x + 20))):
            return True
        else:
            return False
        
# =========================================================


def main():
    endFlag = False
    Cat = Cat(400, 400)
    time_elapsed = 0
    
    ropes = []
    
    while endFlag == False:
        time_elapsed += 1
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endFlag = True
            else:
                Cat.update(event)
                
        # プレイヤーを動かす
        if Cat.move_right == True:
            if Cat.x < 620:
                Cat.x += CAT_VELOCITY
        if Cat.move_left == True:
            if Cat.x < 00:
                Cat.x -= CAT_VELOCITY
        if Cat.move_up == True:
            if Cat.y < 00:
                Cat.x -= CAT_VELOCITY
        if Cat.move_down == True:
            if Cat.x < 460:
                Cat.x += CAT_VELOCITY
                
        # 線とドットのインスタンスを作る
        if (time_elapsed == 20):
            straight_rope = Straight_Rope(0,0,3)
            ropes.append(straight_rope)
        if (time_elapsed == 300):
            straight_rope_horizontal = Straight_Rope_Horizontal(0,0,3)
            ropes.append(straight_rope_horizontal)
        if (time_elapsed == 600):
            straight_rope = Straight_Rope(0,0,3)
            ropes.append(straight_rope)
        if (time_elapsed == 860):
            straight_rope_horizontal = Straight_Rope_Horizontal(0,0,3)
            ropes.append(straight_rope_horizontal)
            
        # ランダムなタイミングでランダムな種類のドットを発生させる
        if(random.randrange(200) < 6):
            shooting_star1 = Shooting_Star(random.randrange(640),0,random.randrange(5) + 5,random.randrange(10) - 5)
            ropes.append(shooting_star1)
            shooting_star2 = Shooting_Star(random.randrange(640),0,random.randrange(5) + 5,random.randrange(10) - 5)
            ropes.append(shooting_star2)
            shooting_star3 = Shooting_Star(random.randrange(640),0,random.randrange(5) + 5,random.randrange(10) - 5)
            ropes.append(shooting_star3)
            shooting_star4 = Shooting_Star(random.randrange(640),0,random.randrange(5) + 5,random.randrange(10) - 5)
            ropes.append(shooting_star4)
            
        # 線とドットを動かす
        for rope in ropes:
            rope.update()
            # 画面から出てしまったドットは削除
            if (rope.x < 0 or rope.x > 640) or (rope.y < 0 or rope.y > 480):
                ropes.remove(rope)
            # 一定時間経つごとに、線の動きを早める
            if (time_elapsed % 1000 == 0) and time_elapsed != 0:
                rope.velocity += 1
                
        # プレイヤーがジャンプ中であればｍ当たり判定を行わない
        if(Cat.immunity == True):
            Cat.immunity_count += 1
            if (Cat.immunity_count < CAT_JUMP):
                screen.blit(Cat.immune_image, (Cat.x,Cat.y))
            else:
                Cat.immunity = False
                Cat.immunity_count = 0
                screen.blit(Cat.image, (Cat.x,Cat.y))
        else:
            screen.blit(Cat.image, (Cat.x,Cat.y))
            for rope in ropes:
                # 敵とぶつかった場合でも、前回ダメージを受けてから一定時間が経っていなければダメージを受けない
                if(rope.judge(Cat) == True) and (Cat.life_lost_time + 30 < time_elapsed):
                    Cat.life_lost_time = time_elapsed
                    Cat.life -= 1
                    if Cat.life == 0:
                        endFlag = True
                        
        # プレイヤーのライフの数だけハートを表示する
        for i in range(Cat.life - 1):
            screen.blit(heart_image, (i * 30, 50))
        pygame.display.update()
    quit(time_elapsed)
    
# =========================================================


# ゲームをやめるとき
def quit(score):
    print("your score:" + str(score))
    # ハイスコアを取ってくる
    data = np.loadtxt("score/score.tsv", dtype="string", delimiter=",")
    highest_score = data[1]
    print("highest score so far:" + highest_score)
    if(score > int(highest_score)):
        # もし今回のスコアがハイスコアよりも高ければ、データをtsvファイルに書き込む
        save_data = np.array([str(datetime.datetime.today()), str(score)])
        np.savetxt('score/score.tsv',save_data, delimiter=',', fmt="%s")
    pygame.quit()
    
# ===============================================================
