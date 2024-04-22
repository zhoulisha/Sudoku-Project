import pygame
import sys
from board import Board
from cell import *
from constants import *
from sudoku_generator import *


screen=pygame.display.set_mode((WIDTH,HEIGHT))
def game_start_screen():
    pygame.init()
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SUDOKU")
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    game_over = False
    # Sets the background to white
    screen.fill(WHITE)

    # Title
    title_font = pygame.font.Font(None, 64)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Displays "Select Game Mode:"
    mode_font = pygame.font.Font(None, 32)
    mode_text = mode_font.render("Select Game Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_text, mode_rect)

    # Creates easy, medium, and hard buttons
    button_font = pygame.font.Font(None, 32)
    easy_button = button_font.render("Easy", True, BLACK)
    easy_surface=pygame.Surface((easy_button.get_size()[0]+20, easy_button.get_size()[1]+20))
    easy_surface.fill((255,100,180))
    easy_surface.blit(easy_button,(10,10))
    easy_rect = easy_button.get_rect(center=(WIDTH // 4, HEIGHT * 3 // 4))
    screen.blit(easy_surface, easy_rect)

    medium_button = button_font.render("Medium", True, BLACK)
    medium_surface=pygame.Surface((medium_button.get_size()[0]+20, medium_button.get_size()[1]+20))
    medium_surface.fill((255,0,230))
    medium_surface.blit(medium_button,(10,10))
    medium_rect = medium_button.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(medium_surface, medium_rect)

    hard_button = button_font.render("Hard", True, BLACK)
    hard_surface=pygame.Surface((hard_button.get_size()[0]+20, hard_button.get_size()[1]+20))
    hard_surface.fill((220,0,255))
    hard_surface.blit(hard_button,(10,10))
    hard_rect = hard_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT * 3 // 4))
    screen.blit(hard_surface, hard_rect)




#def main_menu():#main menu screen
    #pygame.init()
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #.display.set_caption("SUDOKU")
    #game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    #game_over = False

    # screen.fill(BG_COLOR)
    # b = Board(2, 2, screen, 1)
    # b.draw()
    # c = Cell(1, 8, 0, screen)
    # c.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
                if easy_rect.collidepoint(event.pos):
                    easy_screen()

            if event.type == pygame.KEYDOWN:
                x, y = event.pops
                row = y // SQUARE_SIZE
                col = (x // SQUARE_SIZE)
        # Clear the screen
        #screen.fill((0, 0, 0))

        pygame.display.update()

def easy_screen():
    o=1
    while True:

        screen.fill(BG_COLOR)

        b = Board(2, 2, screen, 1)
        b.draw()
        if o==1:
            o=0
            z = generate_sudoku(9, 30)
            for j in range(9):
                for i in range(9):
                    value = z[i][j]

                    c = Cell(value, i, j, screen)
                    c.draw()

            pygame.display.update()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_start_screen()
