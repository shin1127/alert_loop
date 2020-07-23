from mutagen.mp3 import MP3 as mp3
import pygame
import time

filename = 'se_maoudamashii_onepoint26.mp3'  # 再生したいmp3ファイル
interval_time = 5  # 再生間隔を秒数で指定する


pygame.mixer.init()
pygame.mixer.music.load(filename)  # 音源を読み込み


while True:
    pygame.mixer.music.play()
    time.sleep(interval_time)

pygame.quit()
