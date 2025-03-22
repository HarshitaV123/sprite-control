import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500
CAPTION = "Rocket Game"
FPS = 60

WHITE = (255,255,255)

def load_image(img,size=None):
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

def start_game():
    player = Player()
    sprites = pygame.sprite.Group()
    sprites.add(player)
    bg = load_image("bg.png")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.blit(bg,(0,0))
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()

start_game()