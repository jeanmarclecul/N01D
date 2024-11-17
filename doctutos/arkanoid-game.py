import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Variant with 50 Levels")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


class Paddle:
    WIDTH = 100
    HEIGHT = 20
    SPEED = 10

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.color = color
        self.target_x = x

    def move(self, target_x, smoothing_factor):
        self.target_x = target_x
        self.rect.centerx += (self.target_x - self.rect.centerx) * smoothing_factor
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__(WIDTH // 2 - self.WIDTH // 2, HEIGHT - 40, WHITE)
        self.mouse_control_active = False

    def handle_input(self, smoothing_factor):
        if self.mouse_control_active:
            self.target_x = pygame.mouse.get_pos()[0]
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.target_x -= self.SPEED
            if keys[pygame.K_RIGHT]:
                self.target_x += self.SPEED
        self.move(self.target_x, smoothing_factor)

    def toggle_control(self):
        self.mouse_control_active = not self.mouse_control_active


class EnemyPaddle(Paddle):
    def __init__(self, difficulty):
        super().__init__(WIDTH // 2 - self.WIDTH // 2, 20, GREEN)
        self.difficulty = difficulty

    def track_balls(self, balls):
        active_balls = [ball for ball in balls if ball.active]
        if not active_balls:
            return

        lowest_ball = max(active_balls, key=lambda b: b.rect.y)
        desired_x = lowest_ball.rect.centerx

        max_offset = self.WIDTH * (1 - self.difficulty)
        random_offset = random.uniform(-max_offset, max_offset)
        desired_x += random_offset

        speed = 5 + (5 * self.difficulty)
        if self.rect.centerx < desired_x:
            self.target_x += min(speed, desired_x - self.rect.centerx)
        elif self.rect.centerx > desired_x:
            self.target_x -= min(speed, self.rect.centerx - desired_x)

        self.move(self.target_x, 1)  # Use smoothing factor of 1 for immediate movement


class Ball:
    SIZE = 15

    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - self.SIZE // 2,
            HEIGHT // 2 - self.SIZE // 2,
            self.SIZE,
            self.SIZE,
        )
        self.speed = [random.choice([-5, 5]), random.choice([-5, 5])]
        self.active = True

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[0]

    def bounce(self, axis):
        self.speed[axis] *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, RED, self.rect)


class Brick:
    WIDTH = 80
    HEIGHT = 30

    def __init__(self, x, y, color=BLUE, strength=1):
        self.rect = pygame.Rect(x, y, self.WIDTH - 2, self.HEIGHT - 2)
        self.color = color
        self.strength = strength

    def hit(self):
        self.strength -= 1
        return self.strength <= 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Level:
    def __init__(self, layout):
        self.bricks = []
        for row, line in enumerate(layout):
            for col, char in enumerate(line):
                if char != " ":
                    color = BLUE
                    strength = 1
                    if char == "2":
                        color = GREEN
                        strength = 2
                    elif char == "3":
                        color = RED
                        strength = 3
                    self.bricks.append(
                        Brick(
                            col * Brick.WIDTH, row * Brick.HEIGHT + 50, color, strength
                        )
                    )


def generate_levels(num_levels):
    levels = []
    for _ in range(num_levels):
        layout = []
        for row in range(8):
            line = ""
            for col in range(10):
                if random.random() < 0.7:  # 70% chance of a brick
                    line += str(
                        random.choices(["1", "2", "3"], weights=[0.6, 0.3, 0.1])[0]
                    )
                else:
                    line += " "
            layout.append(line)
        levels.append(Level(layout))
    return levels


class Game:
    def __init__(self):
        self.player_paddle = PlayerPaddle()
        self.enemy_paddle = EnemyPaddle(difficulty=0.7)
        self.balls = [Ball()]
        self.levels = generate_levels(50)
        self.current_level = 0
        self.load_level(self.current_level)
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.game_won = False

    def load_level(self, level_index):
        self.bricks = self.levels[level_index].bricks.copy()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.player_paddle.toggle_control()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.balls.append(Ball())
                elif event.key == pygame.K_r and (self.game_over or self.game_won):
                    self.__init__()  # Restart the game
        return True

    def update(self):
        if self.game_over or self.game_won:
            return

        self.player_paddle.handle_input(smoothing_factor=0.2)
        self.enemy_paddle.track_balls(self.balls)

        for ball in self.balls:
            if not ball.active:
                continue

            ball.move()

            # Ball collision with walls
            if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
                ball.bounce(0)
            if ball.rect.top <= 0:
                ball.bounce(1)

            # Ball collision with paddles
            for paddle in (self.player_paddle, self.enemy_paddle):
                if ball.rect.colliderect(paddle.rect):
                    relative_intersect_x = (paddle.rect.centerx - ball.rect.centerx) / (
                        Paddle.WIDTH / 2
                    )
                    bounce_angle = relative_intersect_x * (math.pi / 3)
                    speed = math.sqrt(ball.speed[0] ** 2 + ball.speed[1] ** 2)
                    ball.speed[0] = -speed * math.sin(bounce_angle)
                    ball.speed[1] = -speed * math.cos(bounce_angle)
                    if paddle == self.enemy_paddle:
                        ball.speed[1] = abs(
                            ball.speed[1]
                        )  # Ensure the ball moves downward
                    else:
                        ball.speed[1] = -abs(
                            ball.speed[1]
                        )  # Ensure the ball moves upward

            # Ball collision with bricks
            for brick in self.bricks[:]:
                if ball.rect.colliderect(brick.rect):
                    if brick.hit():
                        self.bricks.remove(brick)
                    ball.bounce(1)

            # Check if ball is out of bounds
            if ball.rect.top >= HEIGHT:
                ball.active = False

        # Remove inactive balls
        self.balls = [ball for ball in self.balls if ball.active]

        # Check for level completion
        if not self.bricks:
            self.current_level += 1
            if self.current_level < len(self.levels):
                self.load_level(self.current_level)
            else:
                self.game_won = True

        # Check for game over
        if not self.balls:
            self.game_over = True

    def draw(self):
        screen.fill(BLACK)
        self.player_paddle.draw(screen)
        self.enemy_paddle.draw(screen)
        for ball in self.balls:
            ball.draw(screen)
        for brick in self.bricks:
            brick.draw(screen)

        # Draw control mode indicator and ball count
        control_text = (
            "Mouse" if self.player_paddle.mouse_control_active else "Keyboard"
        )
        ball_count_text = f"Balls: {len(self.balls)}"
        level_text = f"Level: {self.current_level + 1}"
        control_surface = self.font.render(f"Control: {control_text}", True, WHITE)
        ball_count_surface = self.font.render(ball_count_text, True, YELLOW)
        level_surface = self.font.render(level_text, True, WHITE)
        screen.blit(control_surface, (10, HEIGHT - 40))
        screen.blit(ball_count_surface, (WIDTH - 150, HEIGHT - 40))
        screen.blit(level_surface, (WIDTH // 2 - 50, HEIGHT - 40))

        if self.game_over:
            game_over_text = self.font.render(
                "GAME OVER - Press R to Restart", True, RED
            )
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        elif self.game_won:
            win_text = self.font.render("YOU WON! - Press R to Restart", True, GREEN)
            screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))

        pygame.display.flip()

    def run(self):
        while True:
            if not self.handle_events():
                return

            self.update()
            self.draw()

            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
