import ball
import functions
import paddle
import pygame
from pygame.sprite import Group

if __name__ == "__main__":
    pygame.init()

    win = pygame.display.set_mode((750, 500))
    paddle_left = paddle.Paddle("left")
    paddle_right = paddle.Paddle("right")
    ball = ball.Ball()
    all_sprites = Group()
    all_sprites.add(paddle_left, paddle_right, ball)

    while True:
        pygame.time.delay(50)

        ball.rect.x += ball.speed * ball.dx
        ball.rect.y += ball.speed * ball.dy

        functions.check_events(paddle_left, paddle_right)
        functions.check_collisions(paddle_left, paddle_right, ball)
        functions.redraw(win, paddle_left, paddle_right, all_sprites)


    pygame.quit()