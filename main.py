'''
-------------------------------------------------------------------------------
Name:		main.py

Purpose:	Player can roam around and click around learning parts of the computer. With a little easter egg to find.

Author:	Huang.S

Created:	01/15/2021
------------------------------------------------------------------------------
'''

import pygame

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)

pygame.init()

# Set screen dimensions
size = (770, 430)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Computer Parts")

#Loop until the user clicks the close button.
done = False

# Loading and setting graphics
background_image = pygame.image.load("pictures/background.png").convert_alpha()
player_image = pygame.image.load("pictures/robot1.png").convert_alpha()
clone_image = pygame.image.load("pictures/robot2.png").convert_alpha()
cooler_image = pygame.image.load("pictures/Cooler.png").convert_alpha()
cpu_image = pygame.image.load("pictures/CPU.png").convert_alpha()
gpu_image = pygame.image.load("pictures/GPU.png").convert_alpha()
memory_image = pygame.image.load("pictures/Memory.png").convert_alpha()
motherboard_image = pygame.image.load(
    "pictures/Motherboard.png").convert_alpha()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Image sizing
background_image = pygame.transform.scale(background_image, (770, 430))
player_image = pygame.transform.scale(player_image, (70, 70))
clone_image = pygame.transform.scale(clone_image, (70, 70))
cooler_image = pygame.transform.scale(cooler_image, (160, 70))
cpu_image = pygame.transform.scale(cpu_image, (53, 50))
gpu_image = pygame.transform.scale(gpu_image, (130, 70))
memory_image = pygame.transform.scale(memory_image, (140, 40))
motherboard_image = pygame.transform.scale(motherboard_image, (70, 90))

# Animating properties
left = False
right = False

player_x = 100
player_y = 300
player_width = 70
player_height = 70
player_velocity = 4

# Graphic positions
background_position = (0, 0)
player_position = (100, 300)
clone_position = (600, 300)
cooler_position = (60, 25)
cpu_position = (240, 35)
gpu_position = (316, 25)
memory_position = (472, 38)
motherboard_position = (640, 17)

# Text, font, and size
font1 = pygame.font.SysFont('Comfortaa', 30, True, False)
font2 = pygame.font.SysFont('Comfortaa', 15, True, False)
text1 = font1.render("Click on a computer part :D", True, BLACK)
text2 = font2.render("There's an easter egg!", True, WHITE)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            right = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            right = False

    mouse = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONUP:
        x = mouse[0]
        y = mouse[1]

        if x > 60 and x < 220 and y > 25 and y < 100:
            print(
                "This is a CPU cooler. It makes sure your computer doesn't over heat."
            )
        if x > 240 and x < 300 and y > 30 and y < 95:
            print("This is a CPU. It's like the brain of the computer!")
        if x > 310 and x < 450 and y > 25 and y < 100:
            print(
                "This is a graphics card also known as GPU. It allows everything to run smoothly and is the source of rendering everything."
            )
        if x > 470 and x < 610 and y > 35 and y < 85:
            print("This is computer memory. It holds all your data.")
        if x > 640 and x < 700 and y > 15 and y < 105:
            print(
                "This is a motherboard. It's what brings everything together.")

        if x > 320 and x < 350 and y > 375 and y < 400:
            print("You found me :)")
            screen.blit(clone_image, clone_position)

    # --- Game logic should go here
    if left:
        player_x -= player_velocity
    if right:
        player_x += player_velocity

    if player_x > 740:
        print(" >> YOU HIT A BORDER PLEASE GO LEFT << ")
    if player_x < 0:
        print(" >> YOU HIT A BORDER PLEASE GO RIGHT << ")

    pygame.display.update()

    # First, clear the screen to white or whatever background colour.
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Drawing code
    screen.blit(background_image, background_position)
    screen.blit(player_image, (player_x, player_y))
    screen.blit(cooler_image, cooler_position)
    screen.blit(cpu_image, cpu_position)
    screen.blit(gpu_image, gpu_position)
    screen.blit(memory_image, memory_position)
    screen.blit(motherboard_image, motherboard_position)
    screen.blit(text1, (20, 380))
    screen.blit(text2, (230, 400))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
