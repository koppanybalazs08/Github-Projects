def Game(screen):
    #import
    import json
    import pygame
    from random import shuffle, randint
    from time import sleep
    from Encryption import encryption

    '''
    todo:
    - 1 exe fájlba írni
    - google drive frissítése (weboldal is?)
    - objective log.json-be írása
    '''

    class entity:
        def __init__(self,rect,rect_img,speed:int):
            self.rect = rect
            self.rect_img = rect_img
            self.speed = speed

        def move(self,condition:bool, direction:list, rect_img):
            if condition:
                self.rect.center = [self.rect.center[0] + direction[0] * self.speed, self.rect.center[1] + direction[1] * self.speed]
                self.rect_img = rect_img

    pygame.init()

    #alap változók
    S_Width = 800
    S_Height = 600
    max_fps = 180
    clock = pygame.time.Clock()
    ptouched = False
    log = []
    logcount = 0
    countdown = 3
    points = 1
    most_in_round = 1
    difficulty = 1
    milestones = set([])

    #grafikai változók

    pygame.display.set_caption('Fogócska')
    bg_image = pygame.image.load('images/background.png')
    bg_image = pygame.transform.scale(bg_image, (S_Width, S_Height))
    icon = pygame.image.load('images/objective.png')
    pygame.display.set_icon(icon)
    font = pygame.font.SysFont('Arial', 40)

    #karakterek változói

    #Akadályok (teleport kapuk)
    obstacle1 = pygame.Rect((1, 1, 5, 200))
    obstacle1.center = [randint(150, S_Width-150), randint(150, S_Height-150)]
    obs1color = [180, 90, 130]
    shuffle(obs1color)
    obs1color = tuple(obs1color)

    obstacle2 = pygame.Rect((1, 1, 200, 5))
    obstacle2.center = [randint(150, S_Width-150), randint(150, S_Height-150)]
    obs2color = [180, 90, 130]
    shuffle(obs2color)
    obs2color = tuple(obs2color)

    #Cél (halacska)
    objkoor = [randint(0, S_Width), randint(0, S_Height)]
    objective = pygame.image.load('images/objective.png')

    #Ellenfél (cápa)
    enemy = entity(pygame.Rect((0, 0, 50, 50)), pygame.image.load('images/enemyS.png'), 2)
    enemy.rect.center = [60, 60]

    #Játékos (búvár)
    player = entity(pygame.Rect((300, 250, 50, 50)), pygame.image.load('images/playerS.png'), 3)
    player.rect.center = [300, 250]
    log.append(list(player.rect.center).copy())

    #Gameloop
    run = True
    while run:
        for event in pygame.event.get():
            #Kilépés esetén pont rekord beolvasása, esetleges módosítása, és mentése
            if event.type == pygame.QUIT:

                try:
                    #record beolvasás, titkosítás feloldása
                    with open('log.json','r') as logjson:

                        data_in = json.load(logjson)
                        record = encryption.decrypt(data_in["record"])

                        if most_in_round > int(record):
                            record = most_in_round
                        
                        data_out = {}

                except FileNotFoundError:
                    data_out = {}
                    record = most_in_round
                
                except json.decoder.JSONDecodeError:
                    data_out = {}
                    record = most_in_round
                
                #adat titkosítás
                abc = encryption.abc
                modifier = abc[randint(0,len(abc) - 1)]
                data_out["log"] = encryption.encrypt(str(log),modifier)
                data_out["most_in_round"] = encryption.encrypt(str(most_in_round),modifier)
                data_out["record"] = encryption.encrypt(str(record),modifier)

                with open('log.json','w') as logjson:
                    json.dump(data_out, logjson)

                run = False

        #visszaszámlálás
        if countdown >= 0:
            screen.fill((120, 200, 250))
            text = font.render(str(countdown), True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (S_Width // 2, S_Height // 2)
            screen.blit(text, textrect)
            sleep(1)
            countdown -= 1
            pygame.display.update()
        else:
            #játék elveszítése
            if points < 0:
                screen.fill((120, 200, 250))
                text = font.render('Efogytak a pontjaid, legtöbb pont ebben a körben: ' + str(most_in_round), True, (255, 255, 255))
                textrect = text.get_rect()
                textrect.center = (S_Width // 2, S_Height // 2)
                screen.blit(text, textrect)
                pygame.display.update()
                             
            else:
                logcount -= 1

                #háttér, karakterek megrajzolása
                screen.blit(bg_image, (0, 0)) 

                pygame.draw.rect(screen, obs1color, obstacle1)
                pygame.draw.rect(screen, obs2color, obstacle2)
                screen.blit(player.rect_img, tuple(player.rect.topleft))
                screen.blit(enemy.rect_img, tuple(enemy.rect.topleft))

                key = pygame.key.get_pressed()

                #pont szerzés, a cél generálása
                pobjkoordif = [player.rect.center[0] - objkoor[0], player.rect.center[1] - objkoor[1]]

                if pobjkoordif[0] < 40 and pobjkoordif[0] > -40 and pobjkoordif[1] < 40 and pobjkoordif[1] > -40:
                    points += 1
                    objkoor = [randint(20, S_Width-20), randint(20, S_Height-20)]

                    if points > most_in_round:
                        most_in_round = points

                screen.blit(objective, (objkoor[0], objkoor[1])) 

                #Ellenfél mozgása
                #Játékos-Ellenfél collision kalkuláció
                p_e_koordif = [player.rect.center[0] - enemy.rect.center[0], player.rect.center[1] - enemy.rect.center[1]]
                if p_e_koordif[0] > 10 or p_e_koordif[0] < -10 or p_e_koordif[1] > 10 or p_e_koordif[1] < -10 :
                    ptouched = False
                    
                    if enemy.rect.colliderect(obstacle1) or enemy.rect.colliderect(obstacle2):
                        enemy.rect.center = [randint(20, S_Width-20), randint(20, S_Height-20)]

                    #balra
                    enemy.move(
                        p_e_koordif[0] < -10 and enemy.rect.center[0] > 0,
                        [-1,0],
                        pygame.image.load('images/enemyW.png')
                    )

                    #jobbra
                    enemy.move(
                        p_e_koordif[0] > 10 and enemy.rect.center[0] < S_Width,
                        [1,0],
                        pygame.image.load('images/enemyE.png')
                    )

                    #fel
                    enemy.move(
                        p_e_koordif[1] < -10 and enemy.rect.center[1] > 0,
                        [0,-1],
                        pygame.image.load('images/enemyN.png')
                    )

                    #le
                    enemy.move(
                        p_e_koordif[1] > 10 and enemy.rect.center[1] < S_Height,
                        [0,1],
                        pygame.image.load('images/enemyS.png')
                    )

                #találkozás esetén pontlevonás a nehézség alapján
                elif ptouched == False and (p_e_koordif[0] == 10 or p_e_koordif[0] == -10 or p_e_koordif[1] == 10 or p_e_koordif[1] == -10):
                    points -= difficulty
                    ptouched = True

            # 0,0 koordináta bal felső sarokban
                #játékos mozgása
                if player.rect.colliderect(obstacle1) or player.rect.colliderect(obstacle2):
                    player.rect.center = [randint(20, S_Width-20), randint(20, S_Height-20)]

                #balra
                player.move(
                    key[pygame.K_a] == True and player.rect.center[0] > 0,
                    [-1,0],
                    pygame.image.load('images/playerW.png')
                    )

                #jobbra
                player.move(
                    key[pygame.K_d] == True and player.rect.center[0] < S_Width,
                    [1,0], 
                    pygame.image.load('images/playerE.png')
                    )

                #fel
                player.move(
                    key[pygame.K_w] == True and player.rect.center[1] > 0,
                    [0,-1],
                    pygame.image.load('images/playerN.png')
                )

                #le
                player.move(
                    key[pygame.K_s] == True and player.rect.center[1] < S_Height,
                    [0,1],
                    pygame.image.load('images/playerS.png')
                    )

                #"Pontod" kiírása
                text = font.render('Pontod: ' + str(points), True, (255, 255, 255))
                textrect = text.get_rect()
                textrect.center = (120, 30)
                screen.blit(text, textrect)

                #"Nehézség" kiírása
                text = font.render('Nehézség: ' + str(difficulty), True, (255, 255, 255))
                textrect = text.get_rect()
                textrect.center = (120, 100)
                screen.blit(text, textrect)

                #nehézség kezelése: minden 10. elért pont után kétszereződik a nehézség (levont pontok mennyisége)
                if most_in_round % 10 == 0 and most_in_round not in milestones:
                    difficulty *= 2
                    milestones.add(most_in_round)

                #log kezelése
                if logcount < 1 :
                    logcount = 25
                    log.append(list(player.rect.center).copy())

                clock.tick(max_fps)

                pygame.display.update()
