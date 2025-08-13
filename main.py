import pygame
pygame.init()

class character():
    def __init__(self, x, y, width, len, vel):
        self.x = x
        self.y = y
        self.width = width
        self.len = len
        self.vel = vel

class window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

mainWin = window(1500, 800)

window = pygame.display.set_mode((mainWin.width, mainWin.height))
clock = pygame.time.Clock()

pygame.display.set_caption("Plankton Bloom")
#icon = pygame.image.load("")
#pygame.display.set_icon(icon)

def draw(p):
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 255, 255), (p.x, p.y, p.width, p.len))
    pygame.display.update()

def main():
    playerWidth = 25
    playerHeight = 25
    player = character((mainWin.width / 2) - playerWidth, (mainWin.height / 2) - playerHeight, playerWidth, playerHeight, 2)

    while True:
        draw(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        clock.tick(60)

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player.vel >= 0:
            player.y -= player.vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.vel <= mainWin.height:
            player.y += player.vel
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player.vel >= 0:
            player.x -= player.vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.vel <= mainWin.width:
            player.x += player.vel


main()