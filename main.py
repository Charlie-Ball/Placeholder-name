import pygame
pygame.init()
import random

class character():
    def __init__(self, x, y, width, len, vel):
        self.x = x
        self.y = y
        self.width = width
        self.len = len
        self.vel = vel

windowLength = 1500
windowHeight = 800

window = pygame.display.set_mode((windowLength, windowHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Plankton Bloom")
#icon = pygame.image.load("")
#pygame.display.set_icon(icon)

def draw(p, list, num):
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 255, 255), (p.x, p.y, p.width, p.len))
    returnVals = makePlankton(list, num)

    pygame.display.update()
    return returnVals

def makePlankton(list, num):
    if num <= 100:
        list[0].append(random.randrange(windowLength))
        list[1].append(random.randrange(windowHeight))
        num += 1
    for i in range(0, len(list[0])):
        pygame.draw.rect(window, (255,255,255), (list[0][i], list[1][i], 5, 5))

    return [list, num]

def movement(player):
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player.vel >= 0:
        player.y -= player.vel
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.len + player.vel <= windowHeight:
        player.y += player.vel
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player.vel >= 0:
        player.x -= player.vel
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.width + player.vel <= windowLength:
        player.x += player.vel

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


playerWidth = 25
playerHeight = 25
player = character((windowLength / 2) - playerWidth, (windowHeight / 2) - playerHeight, playerWidth, playerHeight, 2)

def main():
    planktonList = [[], []]
    activePlanktonNum = 0

    while True:
        clock.tick(60)
        quit()
        returnVals = draw(player, planktonList, activePlanktonNum)
        planktonList = returnVals[0]
        activePlanktonNum = returnVals[1]
        movement(player)

main()

