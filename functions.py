import pygame
import sys

def check_events(paddle_left, paddle_right):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle_left.rect.y -= paddle_left.speed
    if key[pygame.K_s]:
        paddle_left.rect.y += paddle_left.speed
    if key[pygame.K_UP]:
        paddle_right.rect.y -= paddle_right.speed
    if key[pygame.K_DOWN]:
        paddle_right.rect.y += paddle_right.speed


def check_collisions(paddle_left, paddle_right, ball):
    if ball.rect.y > 480:
        ball.dy = -1
    if ball.rect.y < 10:
        ball.dy = 1
    if paddle_left.rect.colliderect(ball.rect):
        ball.dx = 1
    if paddle_right.rect.colliderect(ball.rect):
        ball.dx = -1
    if ball.rect.x > 730:
        ball.rect.x, ball.rect.y = 370, 245
        paddle_left.points += 1
    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 370, 245
        paddle_right.points += 1



def redraw(win, paddle_left, paddle_right, all_sprites):
    white = (255, 255, 255)
    win.fill((0, 0, 0))
    # Title Font
    font = pygame.font.SysFont("Comic Sans MS", 20)
    text = font.render("PONG", False, white)
    text_rect = text.get_rect()
    text_rect.center = (750//2, 25)
    win.blit(text, text_rect)

    # Player 1 Score
    p1_score = font.render(str(paddle_left.points), False, white)
    p1_rect = p1_score.get_rect()
    p1_rect.center = (50, 50)
    win.blit(p1_score, p1_rect)

    # Player 2 Score
    p2_score = font.render(str(paddle_right.points), False, white)
    p2_rect = p1_score.get_rect()
    p2_rect.center = (700, 50)
    win.blit(p2_score, p2_rect)

    all_sprites.draw(win)
    pygame.display.update()
