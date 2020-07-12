import pygame, sys
from GameV0 import *





def save_config (final_config):
    ruta = "configuracion.txt"
    file = open(ruta,"w")
    for value in final_config:
        value_int = int(value)
        if isinstance(value_int, int) and 1 <= value_int <= 6:
            file.write(value)
            file.write('\n')
        else:
            print("error")
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

    # Dibujos

    saveconfig_button = pygame.Rect(380, 650, 220, 50)
    avatar = pygame.Rect(0, 40, 500, 70)
    rook = pygame.Rect(0, 340, 500, 70)

    # Avatars
    flechador = pygame.Rect(70, 130, 200, 200)
    escudero = pygame.Rect(290, 130, 200, 200)
    leñador = pygame.Rect(510, 130, 200, 200)
    carnival = pygame.Rect(730, 130, 200, 200)
    # Rooks
    sand = pygame.Rect(70, 430, 200, 200)
    rock = pygame.Rect(290, 430, 200, 200)
    fire = pygame.Rect(510, 430, 200, 200)
    water = pygame.Rect(730, 430, 200, 200)

    # texto en pantalla

    pygame.draw.rect(screen, green, saveconfig_button)
    pygame.draw.rect(screen, darkpurple, avatar)
    pygame.draw.rect(screen, darkpurple, rook)
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
    text("Velocidad", font3, dark, screen, sand.x + 50, sand.y + 130)
    text("Ataque", font3, dark, screen, sand.x + 40, sand.y + 175)
    text("Velocidad", font3, dark, screen, rock.x + 50, rock.y + 130)
    text("Ataque", font3, dark, screen, rock.x + 40, rock.y + 175)
    text("Velocidad", font3, dark, screen, fire.x + 50, fire.y + 130)
    text("Ataque", font3, dark, screen, fire.x + 40, fire.y + 175)
    text("Velocidad", font3, dark, screen, water.x + 50, water.y + 130)
    text("Ataque", font3, dark, screen, water.x + 40, water.y + 175)

    text('Guardar cambios', font2, brown, screen, saveconfig_button.x + 110, saveconfig_button.y + 25)
    text("Avatars", font, purple, screen, avatar.x + 250, avatar.y + 35)
    text("Rooks", font, purple, screen, rook.x + 250, rook.y + 35)

    # Entry box speed
    entrybox_f = pygame.Rect(170, 250, 90, 25)
    entrybox_e = pygame.Rect(390, 250, 90, 25)
    entrybox_l = pygame.Rect(610, 250, 90, 25)
    entrybox_c = pygame.Rect(830, 250, 90, 25)
    entrybox_s = pygame.Rect(170, 550, 90, 25)
    entrybox_r = pygame.Rect(390, 550, 90, 25)
    entrybox_fi = pygame.Rect(610, 550, 90, 25)
    entrybox_w = pygame.Rect(830, 550, 90, 25)
    # Entry box atack
    entrybox_f_at = pygame.Rect(170, 295, 90, 25)
    entrybox_e_at = pygame.Rect(390, 295, 90, 25)
    entrybox_l_at = pygame.Rect(610, 295, 90, 25)
    entrybox_c_at = pygame.Rect(830, 295, 90, 25)
    entrybox_s_at = pygame.Rect(170, 590, 90, 25)
    entrybox_r_at = pygame.Rect(390, 590, 90, 25)
    entrybox_fi_at = pygame.Rect(610, 590, 90, 25)
    entrybox_w_at = pygame.Rect(830, 590, 90, 25)
    # active speed
    active_f = False
    active_e = False
    active_l = False
    active_c = False
    active_s = False
    active_r = False
    active_fi = False
    active_w = False
    # active atack
    active_f_at = False
    active_e_at = False
    active_l_at = False
    active_c_at = False
    active_s_at = False
    active_r_at = False
    active_fi_at = False
    active_w_at = False
    # variables de texto
    global speed_f, speed_e, speed_l, speed_c, speed_s, speed_r, speed_fi, speed_w, atack_f, atack_e, \
        atack_l, atack_c, atack_s, atack_r, atack_fi, atack_w
    speed_f = ""
    speed_e = ""
    speed_l = ""
    speed_c = ""
    speed_s = ""
    speed_r = ""
    speed_fi = ""
    speed_w = ""
    atack_f = ""
    atack_e = ""
    atack_l = ""
    atack_c = ""
    atack_s = ""
    atack_r = ""
    atack_fi = ""
    atack_w = ""

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if entrybox_f.collidepoint(event.pos):
                    active_f = True
                    active_e = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_fi = False
                    active_w = False
                elif entrybox_e.collidepoint(event.pos):
                    active_e = True
                    active_f = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_fi = False
                    active_w = False
                elif entrybox_l.collidepoint(event.pos):
                    active_l = True
                    active_f = False
                    active_e = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_fi = False
                    active_w = False
                elif entrybox_c.collidepoint(event.pos):
                    active_c = True
                    active_f = False
                    active_e = False
                    active_l = False
                    active_s = False
                    active_r = False
                    active_fi = False
                    active_w = False
                elif entrybox_s.collidepoint(event.pos):
                    active_s = True
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_r = False
                    active_fi = False
                    active_w = False
                elif entrybox_r.collidepoint(event.pos):
                    active_r = True
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_fi = False
                    active_w = False
                elif entrybox_fi.collidepoint(event.pos):
                    active_fi = True
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_w = False
                elif entrybox_w.collidepoint(event.pos):
                    active_w = True
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_fi = False
                # activar entry para ataque
                elif entrybox_f_at.collidepoint(event.pos):
                    active_f_at = True
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_e_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = True
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_l_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = True
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_c_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = True
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_s_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = True
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_r_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = True
                    active_fi_at = False
                    active_w_at = False
                elif entrybox_fi_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = True
                    active_w_at = False
                elif entrybox_w_at.collidepoint(event.pos):
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = True
                elif saveconfig_button.collidepoint(event.pos):
                    save_config(final_config)
                    from Ventanas import ventana_de_menu
                    run = False
                else:
                    active_f = False
                    active_e = False
                    active_l = False
                    active_c = False
                    active_s = False
                    active_r = False
                    active_fi = False
                    active_w = False
                    active_f_at = False
                    active_e_at = False
                    active_l_at = False
                    active_c_at = False
                    active_s_at = False
                    active_r_at = False
                    active_fi_at = False
                    active_w_at = False
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
                elif active_s:
                    if event.key == pygame.K_BACKSPACE:
                        speed_s = speed_s[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_s = speed_s
                    else:
                        speed_s += event.unicode # ver solo numero
                elif active_r:
                    if event.key == pygame.K_BACKSPACE:
                        speed_r = speed_r[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_r = speed_r
                    else:
                        speed_r += event.unicode # ver solo numero
                elif active_fi:
                    if event.key == pygame.K_BACKSPACE:
                        speed_fi = speed_fi[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_fi = speed_fi
                    else:
                        speed_fi += event.unicode # ver solo numero
                elif active_w:
                    if event.key == pygame.K_BACKSPACE:
                        speed_w = speed_w[0:-1]
                    elif event.key == pygame.K_TAB:
                        speed_w = speed_w
                    else:
                        speed_w += event.unicode # ver solo numero

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
                elif active_s_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_s = atack_s[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_s = atack_s
                    else:
                        atack_s += event.unicode # ver solo numero
                elif active_r_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_r = atack_r[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_r = atack_r
                    else:
                        atack_r += event.unicode # ver solo numero
                elif active_fi_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_fi = atack_fi[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_fi = atack_fi
                    else:
                        atack_fi += event.unicode # ver solo numero
                elif active_w_at:
                    if event.key == pygame.K_BACKSPACE:
                        atack_w = atack_w[0:-1]
                    elif event.key == pygame.K_TAB:
                        atack_w = atack_w
                    else:
                        atack_w += event.unicode # ver solo numero


        final_config = [speed_f, speed_e, speed_l, speed_c,
                        speed_s, speed_r, speed_fi, speed_w,
                        atack_f, atack_e, atack_l, atack_c,
                        atack_s, atack_r, atack_fi, atack_w]

        screen.blit(music_on, (850, 730))
        screen.blit(music_off, (930, 730))
        # Se dibujan avatars
        screen.blit(flechadorimg, (flechador.x + 60, flechador.y + 20))
        screen.blit(escuderoimg, (escudero.x + 60, escudero.y + 20))
        screen.blit(leñadorimg, (leñador.x + 60, leñador.y + 20))
        screen.blit(carnivalimg, (carnival.x + 60, carnival.y + 20))
        # Se dibujan rook
        screen.blit(sandimg, (sand.x + 60, sand.y + 20))
        screen.blit(rockimg, (rock.x + 60, rock.y + 20))
        screen.blit(fireimg, (fire.x + 60, fire.y + 20))
        screen.blit(waterimg, (water.x + 60, water.y + 20))
        # Se dibuja los entry box de speed
        pygame.draw.rect(screen, white, entrybox_f)
        pygame.draw.rect(screen, white, entrybox_e)
        pygame.draw.rect(screen, white, entrybox_l)
        pygame.draw.rect(screen, white, entrybox_c)
        pygame.draw.rect(screen, white, entrybox_s)
        pygame.draw.rect(screen, white, entrybox_r)
        pygame.draw.rect(screen, white, entrybox_fi)
        pygame.draw.rect(screen, white, entrybox_w)
        # Se dibuja los entry box de atack
        pygame.draw.rect(screen, white, entrybox_f_at)
        pygame.draw.rect(screen, white, entrybox_e_at)
        pygame.draw.rect(screen, white, entrybox_l_at)
        pygame.draw.rect(screen, white, entrybox_c_at)
        pygame.draw.rect(screen, white, entrybox_s_at)
        pygame.draw.rect(screen, white, entrybox_r_at)
        pygame.draw.rect(screen, white, entrybox_fi_at)
        pygame.draw.rect(screen, white, entrybox_w_at)
        # Se dibuja text de speed avatar
        text(speed_f, font3, dark, screen, entrybox_f.x + 45, entrybox_f.y + 12)
        text(speed_e, font3, dark, screen, entrybox_e.x + 45, entrybox_e.y + 12)
        text(speed_l, font3, dark, screen, entrybox_l.x + 45, entrybox_l.y + 12)
        text(speed_c, font3, dark, screen, entrybox_c.x + 45, entrybox_c.y + 12)
        # Se dibuja text de speed rook
        text(speed_s, font3, dark, screen, entrybox_s.x + 45, entrybox_s.y + 12)
        text(speed_r, font3, dark, screen, entrybox_r.x + 45, entrybox_r.y + 12)
        text(speed_fi, font3, dark, screen, entrybox_fi.x + 45, entrybox_fi.y + 12)
        text(speed_w, font3, dark, screen, entrybox_w.x + 45, entrybox_w.y + 12)
        # Se dibuja text de atack avatar
        text(atack_f, font3, dark, screen, entrybox_f_at.x + 45, entrybox_f_at.y + 12)
        text(atack_e, font3, dark, screen, entrybox_e_at.x + 45, entrybox_e_at.y + 12)
        text(atack_l, font3, dark, screen, entrybox_l_at.x + 45, entrybox_l_at.y + 12)
        text(atack_c, font3, dark, screen, entrybox_c_at.x + 45, entrybox_c_at.y + 12)
        # Se dibuja text de atack rook
        text(atack_s, font3, dark, screen, entrybox_s_at.x + 45, entrybox_s_at.y + 12)
        text(atack_r, font3, dark, screen, entrybox_r_at.x + 45, entrybox_r_at.y + 12)
        text(atack_fi, font3, dark, screen, entrybox_fi_at.x + 45, entrybox_fi_at.y + 12)
        text(atack_w, font3, dark, screen, entrybox_w_at.x + 45, entrybox_w_at.y + 12)

        pygame.display.flip()


config()
