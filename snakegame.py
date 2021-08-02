import pygame
import random
import os

pygame.mixer.init()
pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0 , 0)
black = (0 , 0, 0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load("snakeback.jpg")
bgimg = pygame.transform.scale(bgimg , (screen_width, screen_height)).convert_alpha()
backimg = pygame.image.load("snakehome.png")
backimg = pygame.transform.scale(backimg, (screen_width, screen_height)).convert_alpha()
gmover = pygame.image.load("gameover.png")
gmover = pygame.transform.scale(gmover, (screen_width, screen_height)).convert_alpha()
pygame.display.set_caption("SnakesLunch")
pygame.display.update()



def plot_snake(gameWindow, color,  sn_list, sn_size):
    for x,y in sn_list :
        pygame.draw.rect(gameWindow, color, [x, y, sn_size, sn_size])

clock = pygame.time.Clock()
font = pygame.font.SysFont('Forte', 40)
def screen_fontappear (text, color, x, y) :
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def welcome():
    pygame.mixer.music.fadeout(100)
    pygame.mixer.music.load('harrypotter.mp3')
    pygame.mixer.music.play(50)
    pygame.mixer.music.set_volume(.4)
    exit_game = False
    while not exit_game:
        gameWindow.blit(backimg, (0, 0))
        screen_fontappear("Welcome to Snakes Lunch Party", (0, 245, 10), 210, 250)
        screen_fontappear("Press Space Bar To Play", (0, 255, 20), 255, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load('avengersback.mp3')
                    pygame.mixer.music.play(10)
                    pygame.mixer.music.set_volume(.8)
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    sn_x = 45
    sn_y = 55
    vel_x = 0
    vel_y = 0
    sn_size = 20
    fps = 60
    init_velocity = 5
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    sn_list = []
    sn_length = 1
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as  f :
            f.write("0")
    with open("highscore.txt", "r") as f:
        high = f.read()

    while not exit_game :
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(high))
            gameWindow.blit(gmover, (0, 0))
            screen_fontappear("Score : " + str(score), white, 300, 500)
            screen_fontappear("Press Enter to Continue", white, 250, 550)

            if score >= int(high) :
                screen_fontappear(" CONGRATS!!!!  New High Scoreee!!!!!", (0, 25, 255), 100, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_velocity
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x = - init_velocity
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_y = -init_velocity
                        vel_x = 0
                    if event.key == pygame.K_DOWN:
                        vel_y = init_velocity
                        vel_x = 0

            sn_x += vel_x
            sn_y += vel_y

            if abs(sn_x - food_x) < 10 and abs(sn_y - food_y) < 10 :
                score+=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                sn_length += 5
                if  score > int(high) :
                    high = score


            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            screen_fontappear("Score : " + str(score) + "                                       " + "High Score : " + str(high), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, sn_size, sn_size])
            head = []
            head.append(sn_x)
            head.append(sn_y)
            sn_list.append(head)

            if len(sn_list) > sn_length:
                del sn_list[0]

            if head in sn_list[:-1]:
                game_over = True



            if sn_x > screen_width or sn_x < 0 or sn_y < 0 or sn_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, sn_list, sn_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()



