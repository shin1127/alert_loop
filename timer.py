from mutagen.mp3 import MP3 as mp3
import pygame
import time

filename = 'se_maoudamashii_onepoint26.mp3'  # 再生したいmp3ファイル
pygame.mixer.init()
pygame.mixer.music.load(filename)  # 音源を読み込み
mp3_length = mp3(filename).info.length  # 音源の長さ取得

while True:
    pygame.mixer.music.play(1)
    time.sleep(30)

pygame.mixer.music.stop()  # 音源の長さ待ったら再生停止
