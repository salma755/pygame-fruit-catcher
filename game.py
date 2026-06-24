import pygame
import random
import sys

pygame.init()

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

# FallingObject class
class FallingObject:
    def __init__(self, is_bomb=False):
        self.is_bomb = is_bomb
        if self.is_bomb:
            img_path = IMAGE_PATHS["bomb"]
            self.image = load_image(img_path, 100, 100)  # Increase bomb size
        else:
            img_path = random.choice(IMAGE_PATHS["objects"])
            self.image = load_image(img_path, 65, 65)
        self.rect = self.image.get_rect(topleft=(random.randint(0, WIDTH - 50), -50))
        self.speed = random.randint(3, 7)

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.top > HEIGHT

    def is_caught(self, player):
        return self.rect.colliderect(player.rect)

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.objects = []
        self.score = 0
        self.background = load_image(IMAGE_PATHS["background"], WIDTH, HEIGHT)
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.start_time = pygame.time.get_ticks()
        self.countdown_time = 60

    def spawn_object(self):
        if random.randint(1, 50) == 1:
            self.objects.append(FallingObject(is_bomb=random.randint(1, 5) == 1))

    def update_objects(self):
        for obj in self.objects:
            obj.move()
            if obj.is_off_screen():
                self.objects.remove(obj)
            elif obj.is_caught(self.player):
                self.objects.remove(obj)
                if obj.is_bomb:
                    self.score -= 1
                else:
                    self.score += 1

    def draw_objects(self):
        for obj in self.objects:
            obj.draw()

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    
    def display_countdown(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        remaining_time = self.countdown_time - elapsed_time
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        # Display countdown timer
        countdown_text = self.font.render(f"Time Left: {minutes:02}:{seconds:02}", True, (0, 0, 0))
        screen.blit(countdown_text, (WIDTH - 200, 10))

    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game logic
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.spawn_object()
            self.update_objects()

            # Draw everything
            screen.blit(self.background, (0, 0))
            self.player.draw()
            self.draw_objects()
            self.display_score()
            self.display_countdown()

            pygame.display.flip()
            clock.tick(FPS)
            if elapsed_time > 60:
                self.game_over()
            if self.score < 0: 
                self.game_over()
            

    def game_over(self):
        screen.fill((255, 255, 255))
        game_over_text = self.font.render("Game Over!", True, (255, 0, 0))
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 3))
        screen.blit(restart_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()

        # Wait for restart or quit
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()  # Reinitialize the gamea
                        self.run()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

# Main game loop
if __name__ == "__main__":
    Game().run()

