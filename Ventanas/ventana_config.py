import pygame, sys
from GameV0 import *

def save_config (final_config):
    global save
    save = None
    ruta = "configuracion.txt"
    file = open(ruta,"w")
    for value in final_config:
        value_int = int(value)
        if isinstance(value_int, int) and 1 <= value_int <= 6:
            file.write(value)
            file.write('\n')
            save = True
        else:
            save = False
            #print("error")
    file.close()

def config():
    # color de la ventana

    screen.fill(dark)

    # Imagenes

    music_on = pygame.image.load("resource/music_on.png").convert()
    music_on.set_colorkey(white)
    music_off = pygame.image.load("resource/music_off.png").convert()
    music_off.set_colorkey(white)
    flechador_raw = pygame.image.load("resource/avatar_flechador.png").convert()
    flechador_raw.set_colorkey(white)
    flechadorimg = pygame.transform.scale(flechador_raw, (80, 80))
    escudero_raw = pygame.image.load("resource/avatar_escudero.png").convert()
    escudero_raw.set_colorkey(white)
    escuderoimg = pygame.transform.scale(escudero_raw, (80, 80))
    leñador_raw = pygame.image.load("resource/avatar_lenador.png").convert()
    leñador_raw.set_colorkey(white)
    leñadorimg = pygame.transform.scale(leñador_raw, (80, 80))
    carnival_raw = pygame.image.load("resource/avatar_canival.png").convert()
    carnival_raw.set_colorkey(white)
    carnivalimg = pygame.transform.scale(carnival_raw, (80, 80))

    sand_raw = pygame.image.load("resource/rook_sand.png").convert()
    sand_raw.set_colorkey(white)
    sandimg = pygame.transform.scale(sand_raw, (80, 80))
    rock_raw = pygame.image.load("resource/rook_rock.png").convert()
    rock_raw.set_colorkey(white)
    rockimg = pygame.transform.scale(rock_raw, (80, 80))
    fire_raw = pygame.image.load("resource/rook_fire.png").convert()
    fire_raw.set_colorkey(white)
    fireimg = pygame.transform.scale(fire_raw, (80, 80))
    water_raw = pygame.image.load("resource/rook_water.png").convert()
    water_raw.set_colorkey(white)
    waterimg = pygame.transform.scale(water_raw, (80, 80))

    # ------------------------------------ Dibujos ------------------------------------ #

    saveconfig_button = pygame.Rect(380, 650, 220, 50)
    avatar = pygame.Rect(0, 40, 500, 70)
    rook = pygame.Rect(0, 340, 500, 70)
    rook_box = pygame.Rect(70, 590, 860, 50)

    # Avatars
    flechador = pygame.Rect(70, 130, 200, 200)
    escudero = pygame.Rect(290, 130, 200, 200)
    leñador = pygame.Rect(510, 130, 200, 200)
    carnival = pygame.Rect(730, 130, 200, 200)
    # Rooks
    sand = pygame.Rect(70, 430, 200, 150)
    rock = pygame.Rect(290, 430, 200, 150)
    fire = pygame.Rect(510, 430, 200, 150)
    water = pygame.Rect(730, 430, 200, 150)

    # Entry box speed
    entrybox_f = pygame.Rect(170, 250, 90, 25)
    entrybox_e = pygame.Rect(390, 250, 90, 25)
    entrybox_l = pygame.Rect(610, 250, 90, 25)
    entrybox_c = pygame.Rect(830, 250, 90, 25)

    # Entry box atack
    entrybox_f_at = pygame.Rect(170, 295, 90, 25)
    entrybox_e_at = pygame.Rect(390, 295, 90, 25)
    entrybox_l_at = pygame.Rect(610, 295, 90, 25)
    entrybox_c_at = pygame.Rect(830, 295, 90, 25)
    entrybox_rooks = pygame.Rect(320, 600, 600, 30)

    pygame.draw.rect(screen, green, saveconfig_button)
    pygame.draw.rect(screen, darkpurple, avatar)
    pygame.draw.rect(screen, darkpurple, rook)
    pygame.draw.rect(screen, brown, rook_box)
    # Se dibuja las cartas de los avatars
    pygame.draw.rect(screen, brown, flechador)
    pygame.draw.rect(screen, brown, escudero)
    pygame.draw.rect(screen, brown, leñador)
    pygame.draw.rect(screen, brown, carnival)
    # Se dibuja las cartas de los rooks
    pygame.draw.rect(screen, brown, sand)
    pygame.draw.rect(screen, brown, rock)
    pygame.draw.rect(screen, brown, fire)
    pygame.draw.rect(screen, brown, water)

    # ------------------------------------ texto en pantalla ------------------------------------ #
    # texto de la entry
    text("Velocidad", font3, dark, screen, flechador.x + 50, flechador.y + 130)
    text("Ataque", font3, dark, screen, flechador.x + 40, flechador.y + 175)
    text("Velocidad", font3, dark, screen, escudero.x + 50, escudero.y + 130)
    text("Ataque", font3, dark, screen, escudero.x + 40, escudero.y + 175)
    text("Velocidad", font3, dark, screen, carnival.x + 50, carnival.y + 130)
    text("Ataque", font3, dark, screen, carnival.x + 40, carnival.y + 175)
    text("Velocidad", font3, dark, screen, carnival.x + 50, carnival.y + 130)
    text("Ataque", font3, dark, screen, carnival.x + 40, carnival.y + 175)
    text("Velocidad", font3, dark, screen, leñador.x + 50, leñador.y + 130)
    text("Ataque", font3, dark, screen, leñador.x + 40, leñador.y + 175)

    # Text boton y titulos

    text('Guardar cambios', font2, brown, screen, saveconfig_button.x + 110, saveconfig_button.y + 25)
    text("Avatars", font, purple, screen, avatar.x + 250, avatar.y + 35)
    text("Rooks", font, purple, screen, rook.x + 250, rook.y + 35)
    text("Velocidad de ataque", font3, dark, screen, entrybox_rooks.x - 120, entrybox_rooks.y + 15)

    # Text names
    text("Arquero", font2, purple, screen, flechador.x + 100, flechador.y + 15)
    text("Escudero", font2, purple, screen, escudero.x + 100, escudero.y + 15)
    text("Leñador", font2, purple, screen, leñador.x + 100, leñador.y + 15)
    text("Caníval", font2, purple, screen, carnival.x + 100, carnival.y + 15)
    text("Arena", font2, purple, screen, sand.x + 100, sand.y + 15)
    text("Roca", font2, purple, screen, rock.x + 100, rock.y + 15)
    text("Fuego", font2, purple, screen, fire.x + 100, fire.y + 15)
    text("Agua", font2, purple, screen, water.x + 100, water.y + 15)
    # active speed
    active_f = False
    active_e = False
    active_l = False
    active_c = False

    # active atack
    active_f_at = False
    active_e_at = False
    active_l_at = False
    active_c_at = False
    active_rook_at = False

    # ------------------------------------ variables de texto ------------------------------------ #
    global speed_f, speed_e, speed_l, speed_c, atack_f, atack_e, atack_l, atack_c, atack_rook
    speed_f = ""
    speed_e = ""
    speed_l = ""
    speed_c = ""
    atack_f = ""
    atack_e = ""
    atack_l = ""
    atack_c = ""
    atack_rook = ""

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if entrybox_f.collidepoint(event.pos):
                    active_f = True
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_e.collidepoint(event.pos):
                    active_f = False
                    active_e = True
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_l.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = True
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_c.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = True
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False

                # activar entry para ataque
                elif entrybox_f_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = True
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_e_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = True
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_l_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = True
                    active_c_at = False
                    active_rook_at = False
                elif entrybox_c_at.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = True
                    active_rook_at = False
                elif entrybox_rooks.collidepoint(event.pos):
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = True
                elif 850 < mouse_pos[0] < 914 and 730 < mouse_pos[1] < 794:
                    pygame.mixer.music.load("resource/song1.wav")
                    pygame.mixer.music.play(loops=-1)
                    print("si funciono")
                elif 930 < mouse_pos[0] < 994 and 730 < mouse_pos[1] < 794:
                    pygame.mixer.music.stop()


                elif saveconfig_button.collidepoint(event.pos):
                    global save
                    save_config(final_config)
                    if save:
                        from Ventanas import ventana_de_menu
                        run = False
                    else:
                        text("Favor introducir valores entre 1 y 6 segundos", font2, green, screen, 500, 750)

                else:
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_rook_at = False

            elif event.type == pygame.KEYDOWN:
                if active_f:
                    if event.key == pygame.K_BACKSPACE:
                        speed_f = speed_f[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_f = speed_f
                    else:
                        speed_f += event.unicode # ver solo numero
                elif active_e:
                    if event.key == pygame.K_BACKSPACE:
                        speed_e = speed_e[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_e = speed_e

                    else:
                        speed_e += event.unicode # ver solo numero
                elif active_l:
                    if event.key == pygame.K_BACKSPACE:
                        speed_l = speed_l[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_l = speed_l
                    else:
                        speed_l += event.unicode # ver solo numero
                elif active_c:
                    if event.key == pygame.K_BACKSPACE:
                        speed_c = speed_c[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_c = speed_c
                    else:
                        speed_c += event.unicode # ver solo numero

                # typing rooks

                elif active_f_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_f = atack_f[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_f = atack_f
                    else:
                        atack_f += event.unicode # ver solo numero
                elif active_e_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_e = atack_e[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_e = atack_e

                    else:
                        atack_e += event.unicode # ver solo numero
                elif active_l_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_l = atack_l[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_l = atack_l
                    else:
                        atack_l += event.unicode # ver solo numero
                elif active_c_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_c = atack_c[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_c = atack_c
                    # elif event.key == pygame.K_
                    else:
                        atack_c += event.unicode # ver solo numero
                elif active_rook_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_rook = atack_rook[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_rook = atack_rook
                    else:
                        atack_rook += event.unicode # ver solo numero

        # Lista que contien todos los segundos
        final_config = [speed_f, speed_e, speed_l, speed_c,
                        atack_f, atack_e, atack_l, atack_c,
                        atack_rook]

        # Se dibujan iconos de musica
        screen.blit(music_on, (850, 730))
        screen.blit(music_off, (930, 730))
        # Se dibujan avatars
        screen.blit(flechadorimg, (flechador.x + 60, flechador.y + 35))
        screen.blit(escuderoimg, (escudero.x + 60, escudero.y + 35))
        screen.blit(leñadorimg, (leñador.x + 60, leñador.y + 35))
        screen.blit(carnivalimg, (carnival.x + 60, carnival.y + 35))
        # Se dibujan rook
        screen.blit(sandimg, (sand.x + 60, sand.y + 40))
        screen.blit(rockimg, (rock.x + 60, rock.y + 40))
        screen.blit(fireimg, (fire.x + 60, fire.y + 40))
        screen.blit(waterimg, (water.x + 60, water.y + 40))
        # Se dibuja los entry box de speed
        pygame.draw.rect(screen, white, entrybox_f)
        pygame.draw.rect(screen, white, entrybox_e)
        pygame.draw.rect(screen, white, entrybox_l)
        pygame.draw.rect(screen, white, entrybox_c)

        # Se dibuja los entry box de atack
        pygame.draw.rect(screen, white, entrybox_f_at)
        pygame.draw.rect(screen, white, entrybox_e_at)
        pygame.draw.rect(screen, white, entrybox_l_at)
        pygame.draw.rect(screen, white, entrybox_c_at)
        pygame.draw.rect(screen, white, entrybox_rooks)

        # Se dibuja text de speed avatar
        text(speed_f, font3, dark, screen, entrybox_f.x + 45, entrybox_f.y + 12)
        text(speed_e, font3, dark, screen, entrybox_e.x + 45, entrybox_e.y + 12)
        text(speed_l, font3, dark, screen, entrybox_l.x + 45, entrybox_l.y + 12)
        text(speed_c, font3, dark, screen, entrybox_c.x + 45, entrybox_c.y + 12)

        # Se dibuja text de atack avatar
        text(atack_f, font3, dark, screen, entrybox_f_at.x + 45, entrybox_f_at.y + 12)
        text(atack_e, font3, dark, screen, entrybox_e_at.x + 45, entrybox_e_at.y + 12)
        text(atack_l, font3, dark, screen, entrybox_l_at.x + 45, entrybox_l_at.y + 12)
        text(atack_c, font3, dark, screen, entrybox_c_at.x + 45, entrybox_c_at.y + 12)
        # Se dibuja text de atack rook
        text(atack_rook, font3, dark, screen, entrybox_rooks.x + 300, entrybox_rooks.y + 15)

        pygame.display.flip()


config()
