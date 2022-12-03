import pygame
pygame.init()
prozor=pygame.display.set_mode((500,500))
prozor.fill("lightgray")
pygame.draw.circle(prozor,pygame.Color("gold"),(200,200),30)
pygame.draw.circle(prozor,pygame.Color("red"),(100,100),30,2)
for i in range(300):
      prozor.fill("lightgray")
      pygame.draw.circle(prozor,pygame.Color("gold"),(200+i,200+i),30)
      pygame.draw.circle(prozor,pygame.Color("green"),(200-i,200),30)
      pygame.draw.circle(prozor,pygame.Color("blue"),(200,200-i),30)
      pygame.display.update()
      pygame.time.wait(15)
pygame.quit()
