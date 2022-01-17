# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 600), 0, 32)

font = pygame.font.SysFont(None, 20)
pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        startbackground = pygame.image.load('start_bg.png')
        screen.blit(startbackground, (0, 0))


        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(65, 50, 200, 78)
        button_2 = pygame.Rect(65, 150, 200, 78)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                instructions()


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
        mainClock.tick(60)


def game():
    running = True
    # making the screen
    screen = pygame.display.set_mode((800, 600))

    # for setting font
    base_font = pygame.font.Font(None, 32)

    # setting title and logo
    pygame.display.set_caption("FOOTBALL")
    icon = pygame.image.load('football_fb.png')
    pygame.display.set_icon(icon)

    # Background
    background = pygame.image.load('football_bg.png')

    # starting position of ball (basically centre)
    iconX = 400
    iconY = 300

    # making the football
    def football(x, y):
        screen.blit(icon, (x, y))

    # defining user answer
    userans = ''

    # making the question
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

    # making variable for the amount by which the ball moves left when user gives the right answer
    p = 0

    # for user inputs
    while running:
        for event in pygame.event.get():

            # for making the game quit after user presses cross button

            if event.type == pygame.QUIT:
                running = False

            # making the typing mechanism
            if event.type == pygame.KEYDOWN:
                # making backspace mechanism
                if event.key == pygame.K_BACKSPACE:
                    userans = userans[:-1]
                # for making the letter mechanism
                else:
                    userans += event.unicode

                # for entering the answer
                if event.key == pygame.K_SPACE:
                    # if user enters wrong answer
                    if userans.strip() not in (ans1) or userans.strip == "":
                        userans = "WRONG"
                    else:
                        # for printing new question after user enters right answer
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

                        p += 0.104

                        '''for increasing the value of 'p' (variable which dcides the amount by which ball 
                        moves left / the speed of going right decreases when user enters correct answer)'''

        # for making the ball move left/right.
        iconX += (0.52 - p)

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
        else:
            bye = base_font.render("YOU LOST", True, (0, 0, 0))
            screen.blit(bye, (0, 20))

        pygame.display.update()
        mainClock.tick(60)


def instructions():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('''Instructions: This is basically a twist on the world famous game "Football". \n
        Here the ball by default moves towards our goal (computer is winning) with a constant speed. \n
        The user needs to solve simple addition problems to slow down the ball and eventually make it move towards the left
         (into the computer's goal).''', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()