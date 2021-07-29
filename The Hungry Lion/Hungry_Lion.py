import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
 
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 610:
            self.reset_pos()

class Food(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Hungry Lion")

clock = pygame.time.Clock()
FPS = 60

font_style = pygame.font.SysFont("None", 35)

sound1 = pygame.mixer.Sound('d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/The Hungry Lion/food_take_sound.wav')
sound2 = pygame.mixer.Sound('d:/Документы Тамирлана/KBTU/Summer semester/PP2/PP2code/PP2/The Hungry Lion/block_collusion.wav')

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

food_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(RED, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(SCREEN_HEIGHT)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    # This represents a food
    food = Food(GREEN, 20, 15)
 
    # Set a random location for the food
    food.rect.x = random.randrange(SCREEN_WIDTH)
    food.rect.y = random.randrange(SCREEN_HEIGHT)
 
    # Add the food to the list of objects
    food_list.add(food)
    all_sprites_list.add(food)
 
# Create a RED player block
player = Player(50, 50)
all_sprites_list.add(player)

running = True

score = 0

# Main loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

  
    # Game main logic

    if player.rect.x > SCREEN_WIDTH:
        player.rect.x = 0
    
    if player.rect.x < 0:
        player.rect.x = SCREEN_WIDTH
    
    if player.rect.y > SCREEN_HEIGHT:
        player.rect.y = 0

    if player.rect.y < 0:
        player.rect.y = SCREEN_HEIGHT

    # This calls update on all the sprites
    all_sprites_list.update()

    # Drawing objects
    screen.fill(WHITE)

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    food_hit_list = pygame.sprite.spritecollide(player, food_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        sound2.play()
        score -= 1

    # Check the list of collisions.
    for food in food_hit_list:
        sound1.play()
        score += 1

    for i in food_list:
        i.rect.x += random.randint(-1, 1)
        i.rect.y += random.randint(-1, 1)

    # Draw score
    valueS = font_style.render("Your Score: " + str(score), True, BLACK)
    screen.blit(valueS, [0, 0])

    # Draw sprites
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()