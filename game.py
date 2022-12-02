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