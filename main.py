# importing required modules/ classes:
import pygame, sys, random, time
from pygame.locals import *
from pygame import mixer

# setting up pygame/ other things required later
pygame.init()
pygame.display.set_caption('FOOTBALL')
screen = pygame.display.set_mode((800, 600), 0, 32)
mixer.music.load('start_music.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()
font1 = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 25)
pygame.display.update()


# making a function which prints required texts as we can't use the print statement
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# making a function which starts the main menu and connects to different parts
def main_menu():
    while True:

        # setting up the main menu background
        startbackground = pygame.image.load('start_bg.png')
        screen.blit(startbackground, (0, 0))
        pygame.display.set_caption("FOOTBALL")

        # setting up the clickable buttons system
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(65, 50, 200, 78)
        button_2 = pygame.Rect(65, 150, 200, 78)
        button_3 = pygame.Rect(65, 260, 200, 78)

        # making the buttons perform functions which run different things like the main game, instructions and credits
        if button_1.collidepoint((mx, my)):
            if click:
                difficulty()
        if button_2.collidepoint((mx, my)):
            if click:
                instructions()
        if button_3.collidepoint((mx, my)):
            if click:
                credits()

        # setting up the exit mechanism
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


# making a function which sets the difficulty of the game
def difficulty():
    running = True
    global d

    # setting up the main menu background
    diffbackground = pygame.image.load('diff_bg.png')
    screen.blit(diffbackground, (0, 0))
    pygame.display.set_caption("FOOTBALL")

    while running:

        # setting up the exit mechanism
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # setting up the clickable buttons system
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(270, 37, 237, 90)
        button_2 = pygame.Rect(270, 168, 237, 90)
        button_3 = pygame.Rect(270, 300, 237, 90)
        button_4 = pygame.Rect(270, 430, 237, 90)
        # making the buttons perform functions which run different things like the main game, instructions and credits
        if button_1.collidepoint((mx, my)):
            if click:
                d = 0.75
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                d = 1.25
                game()
        if button_3.collidepoint((mx, my)):
            if click:
                d = 2
                game()
        if button_4.collidepoint((mx, my)):
            if click:
                d = 5
                game()

        pygame.display.update()


# making a function which runs the game
def game():
    # making the screen
    running = True
    time.sleep(0.5)
    screen = pygame.display.set_mode((800, 600))
    mixer.music.load('football_music.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    background = pygame.image.load('football_bg.png')

    # for setting font, title and logo
    base_font = pygame.font.Font(None, 32)
    pygame.display.set_caption("FOOTBALL")
    icon = pygame.image.load('football_fb.png')
    pygame.display.set_icon(icon)

    # making the football
    iconX = 400
    iconY = 300

    def football(x, y):
        screen.blit(icon, (x, y))

    # setting up the mechanism which makes the questions
    userans = ''
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    if n1 < n2:
        n1, n2 = n2, n1
    o = random.randint(0, 1)
    ol = [' + ', ' - ']
    if o == 0:
        ans1 = n1 + n2
    else:
        ans1 = n1 - n2
    ans1 = str(ans1)
    nn1 = str(n1)
    nn2 = str(n2)
    nn3 = nn1 + ol[o] + nn2
    question = ("What is " + nn3 + " ? (Press Space After Writing ans)")
    p = 0
    st = time.time()

    # setting the user input mechanism
    while running:
        for event in pygame.event.get():

            # making the exit and typing mechanism
            if event.type == pygame.QUIT:
                mixer.music.fadeout(50)
                mixer.music.load('start_music.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                running = False
            if event.type == pygame.KEYDOWN:

                # making the backspace mechanism
                if event.key == pygame.K_BACKSPACE:
                    userans = userans[:-1]

                # making the letter mechanism
                else:
                    userans += event.unicode

                # for entering the answer
                if event.key == pygame.K_SPACE:

                    # if user enters wrong answer
                    if userans.strip() not in (ans1) or userans.strip == "":
                        userans = "WRONG"
                        p -= (0.01) * d
                    else:

                        # for making and printing new questions after user enters right answers after the first attempt
                        userans = ""
                        n1 = random.randint(0, 100)
                        n2 = random.randint(0, 100)
                        if n1 < n2:
                            n1, n2 = n2, n1
                        o = random.randint(0, 1)
                        ol = [' + ', ' - ']
                        if o == 0:
                            ans1 = n1 + n2
                        else:
                            ans1 = n1 - n2
                        ans1 = str(ans1)
                        nn1 = str(n1)
                        nn2 = str(n2)
                        nn3 = nn1 + ol[o] + nn2
                        question = ("What is " + nn3 + " ? (Press Space After Writing ans)")

                        # for inscreasing the speed
                        p += (0.01) * d
                if event.key == K_ESCAPE:
                    mixer.music.fadeout(50)
                    mixer.music.load('start_music.mp3')
                    mixer.music.set_volume(0.2)
                    mixer.music.play()
                    running = False

        # for making the ball move left/right.
        iconX += (0.05) * d - p

        # for making background green
        screen.fill((0, 255, 0))

        # making background appear
        screen.blit(background, (0, 0))

        # for making the football appear
        football(iconX, iconY)

        # for printing the question
        questionbox = base_font.render(question, True, (0, 0, 0))
        screen.blit(questionbox, (0, 0))

        # for printing answer bar
        if iconX < 799 and iconX > 0:
            useranswertext = base_font.render(userans, True, (0, 0, 0))
            screen.blit(useranswertext, (0, 20))
        elif iconX < 0:
            hello = base_font.render("YOU WON", True, (0, 0, 0))
            screen.blit(hello, (0, 20))
            draw_text("Pro tip: Press esc (x2) to go to main menu.", font2, (0, 0, 0), screen, 10, 80)
            mixer.music.fadeout(50)
            mixer.music.load('start_music.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
        else:
            bye = base_font.render("YOU LOST", True, (0, 0, 0))
            screen.blit(bye, (0, 20))
            draw_text("Pro tip: Press esc (x2) to go to main menu.", font2, (0, 0, 0), screen, 10, 80)
            mixer.music.fadeout(50)
            mixer.music.load('start_music.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
        pygame.display.update()


# making a function which shows the instructions
def instructions():
    running = True
    while running:

        # making the screen black
        screen.fill((0, 0, 0))

        # printing the instructions using the draw_text function defined earlier
        draw_text("Instructions: ", font1, (255, 255, 255), screen, 20, 20)
        draw_text("I) This is basically a twist on the world famous game \"Football\".", font1, (255, 255, 255), screen,
                  20, 60)
        draw_text("II) Here the ball by default moves towards our goal (computer is winning) with a constant speed.",
                  font1, (255, 255, 255), screen, 20, 100)
        draw_text(
            "III) The user needs to solve simple arithmetic problems to slow down the ball and towards the computer's goal.",
            font1, (255, 255, 255), screen, 20, 140)
        draw_text("IV) Problems will be flashed on the screen and the user needs to solve them as fast as possible.",
                  font1, (255, 255, 255), screen, 20, 180)
        draw_text("V) The user has to type the answer and then press space bar.", font1, (255, 255, 255), screen, 20,
                  220)
        draw_text(
            "VI) If the answer is correct the rate of going right of the ball will get reduced and eventually the ball will move left.",
            font1, (255, 255, 255), screen, 20, 260)
        draw_text(
            "VII) If the answer is wrong then FALSE will be printed which the user has to manually remove by pressing backspace.",
            font1, (255, 255, 255), screen, 20, 300)
        draw_text(
            "VIII) The more the user solves questions correctly , faster will the ball move left (into computer's goal).",
            font1, (255, 255, 255), screen, 20, 340)
        draw_text("IX) If the user gets a question wrong, the speed of movement towards left gets slower.", font1,
                  (255, 255, 255), screen, 20, 380)
        draw_text("X) Choose the difficulty wisely, greater the risk, greater the reward.", font1, (255, 255, 255),
                  screen, 20, 420)
        draw_text("Pro tip: Press esc to go to main menu.", font2, (255, 255, 255), screen, 400, 550)

        # setting up the exit machanism
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


# making a function which shows the credits
def credits():
    running = True
    while running:

        # making the screen black
        screen.fill((0, 0, 0))

        # printing the credits using the draw_text function defined earlier
        draw_text("Credits: ", font2, (255, 255, 255), screen, 20, 20)
        draw_text("This game was made by Aditya Banka and Archit Choudhary of class XI- G. ", font2, (255, 255, 255),
                  screen, 20, 60)
        draw_text("It took us a lot of time to make this so please give us a good rating if you are able to see this!",
                  font2, (255, 255, 255), screen, 20, 100)
        draw_text("Pro tip: Press esc to go to main menu.", font2, (255, 255, 255), screen, 400, 550)

        # making the exit machanism
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


# running the title screen, which further connects to all parts of the game
main_menu()