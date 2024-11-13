import pygame

#-- init --

#pygame screen
pygame.init()
pygame.display.set_caption("click enjoy! : Free!")
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
first = True

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

level_start = True
level_play = False

#starting
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor_collide()
    screen.fill((0,0,0))
    screen.blit(bg,bg_rect)
    cursor_update()
    cursor_clear()
    for x in range(9):
        screen.blit(surface_list[x],surface_rect_list[x])
    screen.blit(cursor,cursor_rect)
    pygame.display.flip()
    clock.tick(60)
    first = False