import pygame

pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("SPATIPHAY")

bg_image = pygame.image.load(r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\g3IzU4-1019432547.jpg')
icon = pygame.image.load(r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\Spotify-Emblem-1498407971.png')
pygame.display.set_icon(icon)

_songs = [
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\01 Foreword.mp3',
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\02 Where This Flower Blooms.mp3',
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\08 Boredom.mp3',
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\We Find Love.mp3',
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\Hold Me Down.mp3',
    r'C:\Users\User\Desktop\univer\2nd_sem\pp2_lab\lab7\music\Loose.mp3'
]
current_song_index = 0
pygame.mixer.music.load(_songs[current_song_index])


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(_songs)
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()


running = True
while running:
    bg_x = (screen.get_width() - bg_image.get_width()) / 2
    bg_y = (screen.get_height() - bg_image.get_height()) / 2
    screen.blit(bg_image, (bg_x, bg_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop() 
                else:
                    pygame.mixer.music.play()
                    
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()
    
    pygame.display.update()
