def Replay(screen):
    import pygame
    import json
    from Encryption import encryption

    pygame.init()

    #Alap változók megadása
    S_Width = 800
    S_Height = 600
    pcenter = []
    i = -1
    clock = pygame.time.Clock()

    #grafikai változók megadása
    pygame.display.set_caption('Visszajátszás')
    bg_image = pygame.image.load('images/background.png')
    bg_image = pygame.transform.scale(bg_image, (S_Width, S_Height))
    icon = pygame.image.load('images/objective.png')
    pygame.display.set_icon(icon)
    font = pygame.font.SysFont('Arial', 40)

    run = True
    screen.blit(bg_image, (0, 0))

    #log olvasása/ bug control
    try:
        with open('log.json') as logjson:
            data = json.load(logjson)
            most_in_round = encryption.decrypt(data["most_in_round"])
            log = encryption.convert_str_to_list_of_lists(encryption.decrypt(data["log"]))
    except FileNotFoundError:
        print('Üres a log :/')
        run = False
        pygame.quit()
    
    except json.decoder.JSONDecodeError:
        print('Üres a log :/')
        run = False
        pygame.quit()
        
    #Visszajátszás
    while run:
        clock.tick(75)
        if i < len(log) - 1:
            i += 1
        elif i >= len(log)-1:
            text = font.render('Legtöbb pont ebben a körben: ' + str(most_in_round), True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (S_Width // 2, S_Height // 2)
            screen.blit(text, textrect)

        if log[i] != log[-1]:
            pcenter = log[i]
            ind = pygame.Rect((pcenter[0], pcenter[1], 3, 3))
            pygame.draw.rect(screen, (0, 255, 0), ind)
            if i >= 1:
                xdiff = pcenter[0] - log[i - 1][0]
                ydiff = pcenter[1] - log[i - 1][1]
                
                if 75 >= xdiff >= -75 and 75 >= ydiff >= -75:
                    pygame.draw.line(screen, (0, 255, 0), pcenter, log[i-1], width = 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
  