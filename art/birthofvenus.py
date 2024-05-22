import pygame
import sys

pygame.init()

grid_width = 13
grid_height = 9
pixel_size = 50
screen_width = pixel_size * grid_width
screen_height = pixel_size * grid_height


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Glitch of Venus")

# Load images for each layer
layer_images = [
    pygame.image.load("layer1.png"),
    pygame.image.load("layer2.png"),
    pygame.image.load("layer3.png"),
    pygame.image.load("layer4.png"),
    pygame.image.load("layer5.png"),
    pygame.image.load("layer6.png"),
    pygame.image.load("layer7.png")
]

for i, image in enumerate(layer_images, start=1):
    layer_images[i-1] = pygame.transform.scale(image, (screen_width, screen_height))
grid_images = []
for image in layer_images:
    grid_image = []
    for x in range(0, image.get_width(), pixel_size):
        row = []
        for y in range(0, image.get_height(), pixel_size):
            rect = pygame.Rect(x, y, pixel_size, pixel_size)
            row.append(image.subsurface(rect))
        grid_image.append(row)
    grid_images.append(grid_image)

current_layer = [[0] * 9 for _ in range(13)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Convert mouse position to grid coordinates
            grid_x = mouse_x // pixel_size
            grid_y = mouse_y // pixel_size
            # Update the current layer for the clicked pixel/button
            current_layer[grid_x][grid_y] += 1
            # If any pixel/button reaches the 7th layer, update the entire screen to the 7th layer and delay before quitting
            if any(layer >= len(layer_images) for row in current_layer for layer in row):
                current_layer = [[6] * 9 for _ in range(13)]
                pygame.time.delay(2000)  # 2000 milliseconds (2 seconds) delay
                running = False
    # Update the display
    for x in range(13):
        for y in range(9):
            screen.blit(grid_images[current_layer[x][y]][x][y], (x * pixel_size, y * pixel_size))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()