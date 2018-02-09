import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
        ball = pygame.image.load("resources/images/skunk.png").convert_alpha()
        screen.blit(ball, (self.x, self.y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load("resources/images/map.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main():

    # declare the size of the canvas
    width = 1280
    height = 720
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Skunk Game')

    # Game initialization
    ball = Ball(100, 100)
    BackGround = Background('background_image.png', [0, 0])

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        ball.update()

        # Draw background
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Game display
        ball.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render('Get the Skunk to Georgia', True, (0, 0, 0))
        screen.blit(text, (500, 0))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()