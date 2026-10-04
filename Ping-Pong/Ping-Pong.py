from pygame import *
mixer.init()
mixer.music.load('geoffharvey-ping-pong-427889.mp3')
font.init()
window = display.set_mode((900,650))
mixer.music.play()
mixer.music.set_volume(0.2)
hit = mixer.Sound('the-sound-of-hitting-the-ball.mp3')
hit.set_volume(0.4)




display.set_caption('Ping-Pong')

background = transform.scale(image.load('background.png'), (900,650))


class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_speed,p_x,p_y,s_x,s_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (s_x,s_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.y = p_y
        self.rect.x = p_x
        self.s_x = s_x
        self.s_y = s_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, p_image, p_speed, p_x, p_y, s_x, s_y, k_up, k_down):
        super().__init__(p_image, p_speed, p_x, p_y, s_x, s_y)
        self.k_up = k_up
        self.k_down = k_down
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[self.k_up] and self.rect.y > 28:
            self.rect.y -= self.speed
        if keys_pressed[self.k_down] and self.rect.y < 501:
            self.rect.y += self.speed

            
class Ball(GameSprite):
    def __init__(self,p_image,p_speed,p_x,p_y,s_x,s_y):
        super().__init__(p_image,p_speed,p_x,p_y,s_x,s_y)
        self.speed = p_speed
        self.speed_x = p_speed 
        self.speed_y = p_speed
        self.s_x = s_x
        self.s_y = s_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.speed_x > 0:
            self.speed_x += 0.002  
        else:
            self.speed_x -= 0.002  

        if self.speed_y > 0:
            self.speed_y += 0.002  
        else:
            self.speed_y -= 0.002  


P2_score = 0
P1_score = 0

font = font.Font(None, 100)



red = 59, 176, 143
P1 = Player('paddle_left.png', 10, 30, 435, 20, 120, K_w, K_s)
P2 = Player('paddle_right.png', 10, 852, 435, 20, 120,K_UP,K_DOWN )
BALL = Ball('ball_circle.png',2, 435, 325, 32, 32)



clock = time.Clock()
FPS = 120
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    if finish != True:
        window.blit(background,(0,0))
        Player1 = font.render(str(P1_score), True, (255, 255, 255))
        Player2 = font.render(str(P2_score), True, (255, 255, 255))

        window.blit(Player1,(210,40))
        window.blit(Player2,(665,40))
        BALL.reset()
        BALL.update()
        P2.update()
        P1.reset()  
        P1.update()
        P2.reset()   
        if BALL.rect.y <= 28 or BALL.rect.y >= 600:
            BALL.speed_y *= -1
            hit.play()
        if sprite.collide_rect(BALL, P1) or sprite.collide_rect(BALL,P2):
            BALL.speed_x *= -1
            hit.play()
        if  BALL.rect.x <= -5:
            P2_score +=1
            BALL.rect.x = 435
            BALL.rect.y = 325
            BALL.speed_x = BALL.speed
            BALL.speed_y = BALL.speed
        elif BALL.rect.x >= 852:
            P1_score +=1
            BALL.rect.x = 435
            BALL.rect.y = 325
            BALL.speed_x = -BALL.speed
            BALL.speed_y = BALL.speed


    display.update()
