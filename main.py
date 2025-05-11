from pygame import * 

font.init()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_jump):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.jump = player_jump
        self.vel_y = 0
        self.on_ground = False

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_jump):
        super().__init__(player_image, player_x, player_y, player_speed, player_jump)
        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.jump_cooldown = 0

    def update(self):
        global dx,dy
        keys = key.get_pressed()
        dx = 0
        dy = 0
        if (keys[K_a] or keys[K_LEFT]) and self.rect.x > 0:
            dx = -self.speed
            self.image=transform.scale(image.load("player_l.png"), (45, 50))
        if (keys[K_d] or keys[K_RIGHT]) and self.rect.x < 750:
            dx = self.speed
            self.image=transform.scale(image.load("player_r.png"), (45, 50))

        if (keys[K_w] or keys[K_UP]) and self.jump_cooldown == 0:
            if self.on_ground:
                self.vel_y = -16
                self.jump_count = 1
                self.jump_cooldown = 10
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        
        self.on_ground = False
        self.rect.x += dx
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                if dx < 0:
                    self.rect.left = platform.rect.right

        self.rect.y += dy
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.jump_count = 0
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    def fire(self):
        bullet = Bullet("sword.png", self.rect.x + 15, self.rect.y, 10, 0)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x += 10
        if self.rect.y<0:
            self.kill()

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 543:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 713:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update1(self):
        if self.rect.x <= 183:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 313:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update2(self):
        if self.rect.x <= 343:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 243:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update3(self):
        if self.rect.x <= 433:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 513:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update4(self):
        if self.rect.x <= 0:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 213:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update5(self):
        if self.rect.x <= 533:
            self.direction = "right"
            self.image=transform.scale(image.load("enemy_r.png"), (50, 50))
        if self.rect.x >= 703:
            self.direction = "left"
            self.image=transform.scale(image.load("enemy_l.png"), (50, 50))
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Button():
    def __init__(self, color, x, y, w, h, text, fsize, txt_color,font_text="Kavoon.ttf"):

        self.width = w
        self.height = h
        self.color = color

        self.image = Surface([self.width, self.height])
        self.image.fill((color))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fsize = fsize
        self.text = text
        self.txt_color = txt_color
        self.txt_image = font.Font(font_text, fsize).render(text, True, txt_color)
    def draw(self, shift_x, shift_y): # цей метод малює кнопку із тектом в середині. Сам текст зміщенний на величини shift_x та shift_y
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))   

window=display.set_mode((800,600))
display.set_caption("Amazing adventures of the knight")
background=transform.scale(image.load("game_fon2.png"),(800,600))
background2=transform.scale(image.load("game2_fon.jpg"),(800,600))
background_menu=transform.scale(image.load("menu_fon.jpg"),(800,600))
background_win=transform.scale(image.load("WinScreen.jpeg"),(800,600))
background_lose=transform.scale(image.load("Lose.png"),(800,600))

font1=font
btn_start = Button((66, 49, 133, 1), 240, 350, 320, 70, 'START GAME',50, (255, 255, 255))
btn_end = Button((66, 49, 133, 1), 300, 445, 180, 70,'CLOSE' ,50, (255,255,255))

level = [
   "/      0        " ,
   "---   --   --   ",
   "    0        0  ",
   "   --    --  - -",
   " 0   0        0",
   "---  -  ---   --",
   "       0    0   ",
   "   --  -    --  ",
   "    0        0  ",
   "    ---    ---- ",
   "                ",
   "----------------"]

x = 0
y = 0

platforms = sprite.Group()
moneys = sprite.Group()
bullets = sprite.Group()
portales = sprite.Group()
portales2 = sprite.Group()

for plt in level:
    x = 0
    for p in plt:
        if p == "-":
            platform = GameSprite('platform.png', x, y, 0, 0)
            platforms.add(platform)
        if p == "0":
            money = GameSprite('money.png', x, y, 0, 0)
            moneys.add(money)
        if p == "/":
            portale = GameSprite('portale.png', x, y, 0, 0)
            portales.add(portale)
        
        x += 50
    y += 50

level2_active = False
def start_level2():
    global level2_active
    level2_active = True

def reset_level1():
    platforms.empty()
    moneys.empty()
    portales.empty()
    enemy1.rect.y = -150
    enemy.rect.y = -150
    enemy2.rect.y = -150
    enemy3.rect.y = -150

level2 = [
   "0   /  0       0" ,
   "--  -  -      --",
   "       -0       ",
   " --    -----    ",
   "              0 ",
   "-----  0    --- ",
   "0   -  -        ",
   "--- -  -  --    ",
   "    -        0  ",
   "  ---      ---- ",
   "       -0    0  ",
   "------ ---  ----"]

def level_2():
    global level2_active  
    start_level2()
    reset_level1()  
    player.rect.x = 50  
    player.rect.y = 500
    x = 0
    y = 0
    for plt in level2:
        x = 0
        for p in plt:
            if p == "-":
                platform = GameSprite('platform2.png', x, y, 0, 0)
                platforms.add(platform)
            if p == "0":
                money = GameSprite('money.png', x, y, 0, 0)
                moneys.add(money)
            if p == "/":
                portale2 = GameSprite('portale.png', x, y, 0, 0)
                portales2.add(portale2)
            
            x += 50
        y += 50

player = Player("player.png", 50, 500, 5, 15) 
enemy = Enemy("enemy.png", 725, 399, 2, 0)
enemy1 = Enemy("enemy.png", 325, 399, 2, 0)
enemy2 = Enemy("enemy.png", 275, 199, 2, 0)
enemy3 = Enemy("enemy.png", 425, 99, 2, 0)
enemy4 = Enemy("enemy.png", 425, 99, 2, 0)
enemy5 = Enemy("enemy.png", 0, 199, 2, 0)
enemy6 = Enemy("enemy.png", 543, 399, 2, 0)
enemys=sprite.Group()
enemys.add(enemy)
enemys.add(enemy1)
enemys.add(enemy2)
enemys.add(enemy3)
enemys.add(enemy4)
enemys.add(enemy5)
enemys.add(enemy6)
    
FPS=120
clock = time.Clock()
game = False
menu = True
lose = False
win = False
enemy_health = 4
enemy1_health = 4
enemy2_health = 4
enemy3_health = 4
enemy4_health = 4
enemy5_health = 4
enemy6_health = 4
player_health = 1
colletction = 0
font = font.Font(None, 40)



while menu:
    for e in event.get():
        if e.type == QUIT:
                game = False
                menu = False
    window.blit(background_menu,(0,0))
    btn_start.draw(15,5)
    btn_end.draw(15,5)

    pos_x, pos_y = mouse.get_pos()
    for e in event.get():
        if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False 
            game = True
        if btn_end.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
            menu = False
            game = False

    display.update()
    clock.tick(FPS)

while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
                menu = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if level2_active == False:
        window.blit(background, (0, 0))
    if level2_active == True:
        window.blit(background2, (0, 0))

    player.update()
    player.reset()
    bullets.draw(window)
    bullets.update()
    enemy.reset()
    enemy.update()
    enemy1.reset()
    enemy1.update1()
    enemy2.reset()
    enemy2.update2()
    enemy3.reset()
    enemy3.update3()   
    
    

    for platform in platforms:
        platform.reset()
    for money in moneys:
        money.reset()
    for portale in portales:
        portale.reset()
    for portale2 in portales2:
        portale2.reset()

    if level2_active == True:
        enemy4.reset()
        enemy4.update3()
        enemy5.reset()
        enemy5.update4()
        enemy6.reset()
        enemy6.update5()
    for money in moneys:
        if sprite.collide_rect(player, money):
            colletction = colletction + 1
            money.kill()

    for portale in portales:
        if sprite.collide_rect(player,portale):
            level_2()
            
    
    for portale2 in portales2:
        if sprite.collide_rect(player,portale2):
            lose = False
            game = False
            menu = False
            win = True

    if enemy_health ==0:
        enemy.rect.y = -150
    if enemy1_health ==0:
        enemy1.rect.y = -150
    if enemy2_health ==0:
        enemy2.rect.y = -150
    if enemy3_health ==0:
        enemy3.rect.y = -150
    if enemy4_health ==0:
        enemy4.rect.y = -150
    if enemy5_health ==0:
        enemy5.rect.y = -150
    if enemy6_health ==0:
        enemy6.rect.y = -150

    for bullet in bullets:
        if sprite.collide_rect(enemy, bullet):
            enemy_health = enemy_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy1, bullet):
            enemy1_health = enemy1_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy2, bullet):
            enemy2_health = enemy2_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy3, bullet):
            enemy3_health = enemy3_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy4, bullet):
            enemy4_health = enemy4_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy5, bullet):
            enemy5_health = enemy5_health - 1
            bullet.kill()
    for bullet in bullets:
        if sprite.collide_rect(enemy6, bullet):
            enemy6_health = enemy6_health - 1
            bullet.kill()

    if sprite.collide_rect(player, enemy) :
        player_health -= 1
    if sprite.collide_rect(player, enemy1) :
        player_health -= 1
    if sprite.collide_rect(player, enemy2) :
        player_health -= 1
    if sprite.collide_rect(player, enemy3) :
        player_health -= 1
    if sprite.collide_rect(player, enemy4) :
        player_health -= 1
    if sprite.collide_rect(player, enemy5) :
        player_health -= 1
    if sprite.collide_rect(player, enemy6) :
        player_health -= 1

    s = font.render("Монети",1,(255,255,255))
    Text = font.render("      : " + str(colletction),1,(255,255,255))
    window.blit(Text, (700,10))
    window.blit(s, (650,10))

    if player_health == 0 or player.rect.y > 600:
        lose = True
        game = False
        menu = False
        win = False

    display.update()
    clock.tick(FPS)

while win:
    for e in event.get():
        if e.type == QUIT:
            game = False
            menu = False
            win = False
    window.blit(background_win,(0,0))

    s = font.render("Монети",1,(255,255,255))
    Text = font.render("      : " + str(colletction),1,(255,255,255))
    window.blit(Text, (385,400))
    window.blit(s, (335,400))

    display.update()
    clock.tick(FPS)


while lose:
    for e in event.get():
        if e.type == QUIT:
                game = False
                menu = False
                lose = False
    window.blit(background_lose,(0,0))

    s = font.render("Монети",1,(255,255,255))
    Text = font.render("      : " + str(colletction),1,(255,255,255))
    window.blit(Text, (385,400))
    window.blit(s, (335,400))
    
    display.update()
    clock.tick(FPS)