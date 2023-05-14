import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong Game"

FPS = 60
FONT_SIZE = 30
FONT_COLOR = (255, 255, 255)
FONT_STYLE = pygame.font.SysFont(None, FONT_SIZE)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Set up the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Create the paddles and the ball
player_paddle = pygame.Rect(50, 250, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(740, 250, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(395, 295, BALL_WIDTH, BALL_HEIGHT)

# Set up the scores

player_score = 0
computer_score = 0

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_s] and player_paddle.bottom < WINDOW_HEIGHT:
        player_paddle.move_ip(0, PADDLE_SPEED)

    if computer_paddle.top < ball.y:
        computer_paddle.move_ip(0, PADDLE_SPEED)
    elif computer_paddle.bottom > ball.y:
        computer_paddle.move_ip(0, -PADDLE_SPEED)

    # Move the ball
    ball.move_ip(BALL_SPEED_X, BALL_SPEED_Y)

    # Check for collisions
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        BALL_SPEED_Y *= -1
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        BALL_SPEED_X *= -1
    if ball.left <= 0:
        computer_score += 1
        ball = pygame.Rect(395, 295, BALL_WIDTH, BALL_HEIGHT)
        BALL_SPEED_X *= random.choice((-1, 1))
        BALL_SPEED_Y *= random.choice((-1, 1))
    if ball.right >= WINDOW_WIDTH:
        player_score += 1
        ball = pygame.Rect(395, 295, BALL_WIDTH, BALL_HEIGHT)
        BALL_SPEED_X *= random.choice((-1, 1))
        BALL_SPEED_Y *= random.choice((-1, 1))

    # Draw the game
    game_window.fill(BLACK)
    pygame.draw.rect(game_window, WHITE, player_paddle)
    pygame.draw.rect(game_window, WHITE, computer_paddle)
    pygame.draw.ellipse(game_window, WHITE, ball)
    player_score_text = FONT_STYLE.render("Player Score: " + str(player_score), True, FONT_COLOR)


