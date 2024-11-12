import pygame
import random
def move_mole():
    moleX = random.randrange(0, 608)
    moleY = random.randrange(0, 480)
    moleX = moleX - moleX % 32
    moleY = moleY - moleY % 32
    print("Mole moved to: " + str(moleX) + ", " + str(moleY))
    return moleX, moleY
    
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        moleX = 0
        moleY = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    print("Clicked at: " + str(mouseX) + ", " + str(mouseY))
                    if moleX <= mouseX <= moleX+32 and moleY <= mouseY <= moleY+32:                        
                        moleX, moleY = move_mole()
            screen.fill("light green")
            for y in range(16):#Horizontal lines
                pygame.draw.line(screen, "dark green", (0,y*32), (640,y*32))
            for x in range(20):#Vertical lines
                pygame.draw.line(screen, "dark green", (x*32,0), (x*32,512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX+2,moleY+2))) #The +2 on the coordinates is purely asthetic
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
