import sys

import pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 400, 400
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = int(SQUARE_SIZE * 0.75)
CIRCLE_WIDTH = 15
SPACE = SQUARE_SIZE + 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def draw_lines():
    # Vertical lines
    pygame.draw.line(win, WHITE, (0, 0), (WIDTH, 0), LINE_WIDTH)
    pygame.draw.line(win, WHITE, (0, HEIGHT), (WIDTH, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(win, WHITE, (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(win, WHITE, (0, i*SQUARE_SIZE), (WIDTH, i*SQUARE_SIZE), LINE_WIDTH)

def draw_board():
    # Reset the screen
    win.fill(BLACK)
    draw_lines()
    # Add marks
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            color = WHITE
            x = (col + 0.5) * SQUARE_SIZE
            y = (row + 0.5) * SQUARE_SIZE
            pygame.draw.circle(win, color, (int(x), int(y)), CIRCLE_RADIUS - 5, CIRCLE_WIDTH - 5)

def mark_square(row, col, player):
    pygame.draw.circle(win, RED if player == 1 else GREEN, (int(col*SQUARE_SIZE + SQUARE_SIZE//2), int(row*SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
    draw_board()

def check_win(player):
    # Check horizontal spaces
    for row in range(BOARD_ROWS):
        if len(set([mark_square(row, col, player) for col in range(BOARD_COLS)])) == 1:
            return True
    # Check vertical spaces
    for col in range(BOARD_COLS):
        if len(set([mark_square(row, col, player) for row in range(BOARD_ROWS)])) == 1:
            return True
    # Check diagonals
    if len(set([mark_square(i, i, player) for i in range(BOARD_COLS)])) == 1:
        return True
    if len(set([mark_square(i, BOARD_COLS-i-1, player) for i in range(BOARD_COLS)])) == 1:
        return True
    return False

def main():
    player = 1
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                if not game_over:
                    if check_win(player):
                        print("Player {} wins!".format(player))
                        game_over = True
                    else:
                        mark_square(clicked_row, clicked_col, player)
                        player *= -1

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
