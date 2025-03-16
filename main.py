import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500
CAPTION = "Rocket Game"
FPS = 60

WHITE = (255,255,255)

def load_image(img,size):
    image = pygame.image.load(img)
    if size:
        image = pygame.transform.scale(image,size)
    return image

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("rocket.png",(70,100))
        self.rect = self.image.get_rect()
        self.vel=5
    
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.y -= self.vel
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y += self.vel
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        
        self.rect.x = max(0,min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT-self.rect.height))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()