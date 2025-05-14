import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Parking Simulator")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car settings
car_width, car_height = 50, 30
car_x, car_y = 100, 300
car_speed = 2
car_color = BLUE

# Parking slot settings
slot_x, slot_y = 600, 250
slot_width, slot_height = 60, 35
slot_color = GREEN

# Font
font = pygame.font.SysFont("Arial", 20)

# State
parked = False

def draw_environment():
    screen.fill(WHITE)
    pygame.draw.rect(screen, slot_color, (slot_x, slot_y, slot_width, slot_height), 3)
    screen.blit(font.render("Parking Slot", True, BLACK), (slot_x - 10, slot_y - 25))
    pygame.draw.rect(screen, car_color, (car_x, car_y, car_width, car_height))
    screen.blit(font.render("Car", True, WHITE), (car_x + 10, car_y + 5))
    if parked:
        status = "Status: Parked Successfully!"
    else:
        status = "Status: Parking..."
    screen.blit(font.render(status, True, BLACK), (20, 20))

def autonomous_parking():
    global car_x, car_y, parked
    if not parked:
        if car_x + car_width < slot_x:
            car_x += car_speed
        elif car_y + car_height < slot_y + slot_height:
            car_y += car_speed
        else:
            parked = True

# Main loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    autonomous_parking()
    draw_environment()
    pygame.display.update()

pygame.quit()
sys.exit()
