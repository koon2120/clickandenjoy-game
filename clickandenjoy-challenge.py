import pygame,threading,time,random

#-- init --

#pygame screen
pygame.init()
pygame.display.set_caption("click enjoy! : Challenge!!")
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
first = True

#font
pygame.font.init()
font = pygame.font.Font("./font/vgafix.fon",20)
text = font.render(" ",True,(255,255,255))
text_rect = text.get_rect(center=(250,480))
text_player_level = font.render("Level : Unknow",True,(255,255,255))
text_player_level_rect = text_player_level.get_rect(x=10,y=10)

#mixer
pygame.mixer.init()
track = [1,2,3,4,5,6,7,8,9]
for x in range(9):
    track[x] = pygame.mixer.Sound("./track/{}.wav".format(x+1))

win_sound = pygame.mixer.Sound("./track/win.wav")
lose_sound = pygame.mixer.Sound("./track/lose.wav")

#-- setup --

#bg
bg = pygame.image.load("./img/bg.png")
bg_rect = bg.get_rect()

#surface
surface_image = pygame.image.load("./img/surface_img.png")
surface_image_click = pygame.image.load("./img/surface_img_click.png")
surface_image_learn = pygame.image.load("./img/surface_img_learn.png")

surface_size = (100,100)
surface_origin = 50
surface_plus = 150

surface_list = [1,2,3,4,5,6,7,8,9]
surface_rect_list = [1,2,3,4,5,6,7,8,9]

for x in range(9):
    surface_list[x] = surface_image
    surface_rect_list[x] = surface_list[x].get_rect()

a = 0
for x in range(3):
    for i in range(3):
        surface_rect_list[a].y = surface_origin+(surface_plus*x)
        surface_rect_list[a].x = surface_origin+(surface_plus*i)
        a+=1

#cursor
cursor = pygame.surface.Surface((1,1))
cursor.set_alpha(0)
cursor_rect = cursor.get_rect()

def cursor_update():
    cursor_rect.center = pygame.mouse.get_pos()

cilck_check = []

def cursor_collide():
    for x in range(9):
        if cursor_rect.colliderect(surface_rect_list[x]) and pygame.mouse.get_pressed()[0]:
            cilck_check.append(x)
            surface_list[x] = surface_image_click
            track[x].play()

def cursor_clear():
    if pygame.mouse.get_pressed()[0] == False:
        for x in range(9):
            surface_list[x] = surface_image

#-- gameplay --
            
#level
level_list = []
player_level = 1

def re_level():
    for num in range(player_level):
        level_list.append(random.randint(0,8))

def level_preview():
    global level_play,text,text_rect
    if first:
        text = font.render("STARTING!",True,(0,0,255))
    text_rect = text.get_rect(center=(250,480))
    for x in range(9):
        surface_list[x] = surface_image
    time.sleep(1)
    for lv in range(len(level_list)):
        if running:
            surface_list[level_list[lv]] = surface_image_learn
            track[level_list[lv]].play()
            text = font.render(" ",True,(255,255,255))
            text_rect = text.get_rect(center=(250,480))
            time.sleep(0.3)
            surface_list[level_list[lv]] = surface_image
            time.sleep(0.3)
    text = font.render("YOU TURN!",True,(0,0,255))
    text_rect = text.get_rect(center=(250,480))
    level_play = True

def level_gameplay():
    global level_play,level_start,text,text_rect,text_player_level,text_player_level_rect,player_level
    if len(cilck_check) == len(level_list):
        level_play = False
        if level_list == cilck_check:
            if not first:
                win_sound.play()
                win_text = ["GREAT JOB!","VERY GOOD!","WOW!","NICE!","SUGOI!","GOOD GAME!"]
                text = font.render(win_text[random.randint(0,5)],True,(0,255,0))
                player_level+=1
            text_player_level = font.render("Level : " + str(player_level),True,(255,255,255))
            text_player_level_rect = text_player_level.get_rect(x=10,y=10)
            text_rect = text.get_rect(center=(250,480))
            cilck_check.clear()
            level_list.clear()
            re_level()
        else:
            lose_sound.play()
            text = font.render("FAILED!",True,(255,0,0))
            text_rect = text.get_rect(center=(250,480))
            cilck_check.clear()
            level_list.clear()
            re_level()
        level_start = True

level_start = True
level_play = False

#starting
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level_play:
                cursor_collide()
    screen.fill((0,0,0))
    screen.blit(bg,bg_rect)
    cursor_update()
    level_gameplay()
    if level_start:
        threading.Thread(target=level_preview).start()
        level_start=False
    if level_play:
        cursor_clear()
    for x in range(9):
        screen.blit(surface_list[x],surface_rect_list[x])
    screen.blit(cursor,cursor_rect)
    screen.blit(text,text_rect)
    screen.blit(text_player_level,text_player_level_rect)
    pygame.display.flip()
    clock.tick(60)
    first = False