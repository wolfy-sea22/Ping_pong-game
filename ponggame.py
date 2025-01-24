from pygame import *  # Mengimpor Pygame

# Kelas untuk Sprite (objek permainan)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Kelas untuk pemain (racket)
class Player(GameSprite):
    def update_r(self):  # Gerakan untuk pemain kanan
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):  # Gerakan untuk pemain kiri
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# Inisialisasi Pygame
back = (200, 255, 255)  # Warna latar belakang
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

# Variabel permainan
game = True
finish = False
clock = time.Clock()
FPS = 60

# Membuat objek permainan
racket1 = Player(r"D:\pingponggame\racket.png", 30, 200, 4, 50, 150)
racket2 = Player(r"D:\pingponggame\racket.png", 520, 200, 4, 50, 150)
ball = GameSprite(r"D:\pingponggame\tenis_ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

# Loop utama
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Pantulan bola
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        # Pemain kalah
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        # Tampilkan objek
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
