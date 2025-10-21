import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()
# Define the food
food = pygame.Rect(random.randrange(0, 380, 20),
                   random.randrange(0, 380, 20), 20, 20)
font = pygame.font.Font(None, 36)
snake = [(200, 200)]
snake_dir = (0, 0)
score = 0
running = True 

# Define the main loop control variable
def reset_game():
    """Resets the snake, direction, food position, and score."""
    global snake, snake_dir, food, score
    snake = [(200, 200)]
    snake_dir = (0, 0)
    
    new_food_pos = (random.randrange(0, 380, 20), random.randrange(0, 380, 20))
    food.topleft = new_food_pos
    score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Key Press Handling
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_UP] and snake_dir != (0, 20):
        snake_dir = (0, -20)
    elif keys[pygame.K_DOWN] and snake_dir != (0, -20):
        snake_dir = (0, 20)
    elif keys[pygame.K_LEFT] and snake_dir != (20, 0):
        snake_dir = (-20, 0)
    elif keys[pygame.K_RIGHT] and snake_dir != (-20, 0):
        snake_dir = (20, 0) 

    # Snake Movement and Logic
    if snake_dir != (0, 0):
    
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        
        snake.insert(0, head)
        
        if pygame.Rect(head, (20, 20)).colliderect(food):
            score += 1
            place_food = False
            while not place_food:
                food.topleft = (random.randrange(0, 380, 20), 
                                random.randrange(0, 380, 20))
                if food.topleft not in snake:
                    place_food = True
        else:
            snake.pop() 
        
        if (head in snake[1:] or # Self-Collision
            head[0] < 0 or head[0] >= 400 or # Wall Collision (X-axis)
            head[1] < 0 or head[1] >= 400): # Wall Collision (Y-axis)
            reset_game()
    
    screen.fill((0, 0, 0)) 
    
    for pos in snake:
        pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 20, 20)) 
        
    
    pygame.draw.rect(screen, (255, 90, 0), food)
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    
    clock.tick(15)

pygame.quit()