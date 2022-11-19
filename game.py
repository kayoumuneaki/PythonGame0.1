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