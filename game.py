import pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load('C:\Users\Administrator\Desktop\Believer.mp3')
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
