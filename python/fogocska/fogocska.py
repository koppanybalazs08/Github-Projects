#import
from Button import button
import Elements.game
import Elements.replay
import json
import pygame
from Encryption import encryption

pygame.init()

#alap változók
S_Width = 800
S_Height = 600

screen = pygame.display.set_mode((S_Width, S_Height))
icon = pygame.image.load('images/objective.png')
background = pygame.image.load('images/menu_background.png')
pygame.display.set_icon(icon)
font = pygame.font.SysFont('Arial', 40)

#játék, játék gomb
def game(screen):
    Elements.game.Game(screen)

gamebutton = button.button((200,100,100), (200,70,70), screen, S_Width // 2, S_Height // 2 - 50, 100, 50, "Játék", font, (255,255,255), True)
#color1, color2, screen, x, y, width, height, text, text_font, text_color, hover(True/False)

#visszajátszás, visszajátszásgomb
def replay(screen):
    Elements.replay.Replay(screen)

replaybutton = button.button((200,100,100), (200,70,70), screen, S_Width // 2, S_Height // 2 + 50, 200, 50, "Visszajátszás", font, (255,255,255), True)

#menü
in_menu = True
while in_menu:

    #alap beállítások
    pygame.display.set_caption('Menü')

    screen.blit(background, (0, 0))

    m_pos = pygame.mouse.get_pos()

    gamebutton.update_bg(m_pos)
    gamebutton.update()
    replaybutton.update_bg(m_pos)
    replaybutton.update()

    #rekord beolvasása, kiírása
    try:
        with open('log.json', 'r') as logjson:
            data_in = json.load(logjson)
            record = encryption.decrypt(data_in["record"])
    except FileNotFoundError:
        record = 0
    except json.decoder.JSONDecodeError:
        record = 0

    record = font.render('Rekord: ' + str(record), True, (0, 0, 0))
    record_rect = record.get_rect()
    record_rect.center = (S_Width // 2 - 250, S_Height // 2 + 250)

    screen.blit(record, record_rect)

    pygame.display.update()

    #kilépés, gomb input érzékelés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
        gamebutton.check_input(lambda: game(screen), m_pos, event)
        replaybutton.check_input(lambda: replay(screen), m_pos, event)

pygame.quit()