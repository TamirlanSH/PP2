import pygame
import random

# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Snake")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
# Frames Per Second

font_style = pygame.font.SysFont("None", 35)
level_font = pygame.font.SysFont("None", 35)

color = GREEN
block = 10
radius = 8

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [10, SCREEN_HEIGHT / 3])

def gameLoop():
    # Load
    d = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/The Snake/savedata.txt", "r")
    score = int(d.read())

    FPS = 5
    level = 1
    lvlup = 0
    dx, dy = block, 0

    game_close = False
    running = True

    #food_location = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
    food_location = round(random.randrange(0, SCREEN_WIDTH - block) / 10.0) * 10.0, round(random.randrange(0, SCREEN_HEIGHT - block) / 10.0) * 10.0

    walls = [[round(random.randrange(0, SCREEN_WIDTH - block) / 10.0) * 10.0, round(random.randrange(0, SCREEN_HEIGHT - block) / 10.0) * 10.0, 20, 20]]

    body = [[70, 100], [90, 100], [110, 100]]

    # Init
    # 1) [70, 100], [90, 100], [110, 100]

    # Moving to the right
    # 2) [90, 100], [110, 100], [80, 100]

    # Main loop
    while running:
        # Close or not
        while game_close == True:
            screen.fill(BLUE)
            message("You Lost! Press C -Play Again or Q - Quit", RED)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
    
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save
                d = open("d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/The Snake/savedata.txt", "w")   
                d.write(str(score))           
                d.close()
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx, dy = block, 0
                if event.key == pygame.K_LEFT:
                    dx, dy = -block, 0
                if event.key == pygame.K_UP:
                    dx, dy = 0, -block
                if event.key == pygame.K_DOWN:
                    dx, dy = 0, block

        # Move our snake
        for i in range(len(body) - 1, 0, -1):
            body[i][0] = body[i - 1][0] # x - point
            body[i][1] = body[i - 1][1] # y - point

        body[0][0] += dx
        body[0][1] += dy

        if body[0][0] > SCREEN_WIDTH:
            body[0][0] = 0
    
        if body[0][0] < 0:
            body[0][0] = SCREEN_WIDTH
    
        if body[0][1] > SCREEN_HEIGHT:
            body[0][1] = 0

        if body[0][1] < 0:
            body[0][1] = SCREEN_HEIGHT

        # Food function
        if body[0][0] == food_location[0] and body[0][1] == food_location[1]:
            body.append([body[1][0], body[1][1]])
            food_location = round(random.randrange(0, SCREEN_WIDTH - block) / 10.0) * 10.0, round(random.randrange(0, SCREEN_HEIGHT - block) / 10.0) * 10.0
            lvlup += 1

        # Score
        score = len(body) - 3
    

        # Level
        if score % 5 == 0 and score != 0 and lvlup % 2 != 0:
            level += 1
            FPS += 1
            walls.append([round(random.randrange(0, SCREEN_WIDTH - block) / 10.0) * 10.0, round(random.randrange(0, SCREEN_HEIGHT - block) / 10.0) * 10.0, 20, 20])
            lvlup +=1

        # Walls
        for i in range(len(walls)):
            if body[0][0] == walls[i][0] and body[0][1] == walls[i][1]:
                game_close = True
    
        # Check for collision head of the snake with food location

        screen.fill(WHITE)

        # Draw food
        pygame.draw.circle(screen, GREEN, food_location, radius)


        # Draw snake
        for i, point in enumerate(body):
            color = RED if i == 0 else BLUE
            pygame.draw.circle(screen, color, point, radius)

        # Draw score
        valueS = font_style.render("Your Score: " + str(score), True, BLACK)
        screen.blit(valueS, [0, 0])

        # Draw Level
        valueL = level_font.render("Level: " + str(level), True, BLACK)
        screen.blit(valueL, [200, 0])

        # Draw walls
        for i in walls:
            pygame.draw.rect(screen, RED, i)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()