print('========== DESAFIO 021 ==========')
import pygame
pygame.init() # iniciando o pygame
pygame.mixer.music.load('desafio021.mp3') # importando a música
pygame.mixer.music.play() # dando play na música
pygame.mixer.event.wait() # esperando a música acabar para encerrar o programa
