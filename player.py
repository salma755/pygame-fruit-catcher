import pygame
import random
import sys


# Screen setup
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()
FPS = 60

# Paths for images
IMAGE_PATHS = {
    "player": "images/player.png",
    "background": "images/background2.jpeg",
    "bomb": "images/bomb.png",
    "objects": [
        "images/strawberry.png",
        "images/apple.png",
        "images/carrot.png",
        "images/grapes.png",
    ],
}

# Helper function to load and scale images
def load_image(path, width, height):
    try:
        img = pygame.image.load(path)
        return pygame.transform.scale(img, (width, height))
    except pygame.error as e:
        print(f"Error loading image at {path}: {e}")
        sys.exit()

# Player class
class Player:
    def __init__(self):
        self.image = load_image(IMAGE_PATHS["player"], 150, 200)
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
        self.speed = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x = min(self.rect.x + self.speed, WIDTH - self.rect.width)

    def draw(self):
        screen.blit(self.image, self.rect)