import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_x = (SCREEN_WIDTH - player_size) // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_list = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def create_obstacle():
    x_pos = random.randint(0, SCREEN_WIDTH - obstacle_width)
    y_pos = -obstacle_height
    return [x_pos, y_pos]

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

def update_obstacles(obstacles, speed):
    for obstacle in obstacles:
        obstacle[1] += speed
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < SCREEN_HEIGHT]
    return obstacles

def detect_collision(player_x, player_y, obstacles):
    for obstacle in obstacles:
        if (player_x < obstacle[0] + obstacle_width and
            player_x + player_size > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and
            player_y + player_size > obstacle[1]):
            return True
    return False

def main():
    global player_x, score, obstacle_speed

    obstacle_list = []
    running = True
    spawn_timer = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed

        # Spawn obstacles
        spawn_timer += 1
        if spawn_timer >= 30:  # Spawn a new obstacle every 30 frames
            obstacle_list.append(create_obstacle())
            spawn_timer = 0

        # Update obstacles
        obstacle_list = update_obstacles(obstacle_list, obstacle_speed)

        # Detect collisions
        if detect_collision(player_x, player_y, obstacle_list):
            print(f"Game Over! Final Score: {score}")
            running = False

        # Draw player
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
        #player_image = pygame.image.load("images.jpg")
        #player_image = pygame.transform.scale(player_image, (player_size, player_size))
        #screen.blit(player_image, (player_x, player_y))

        # Draw obstacles
        draw_obstacles(obstacle_list)

        # Update score
        score += 1
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Increase difficulty
        if score % 500 == 0:
            obstacle_speed += 1

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
