import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("Bee1.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


def home():
    global SinglePlayer
    SinglePlayer = None
    home_run = True
    clock = pygame.time.Clock()
    bg = pygame.image.load(r'bg.png')
    single = pygame.image.load(r'single.png')
    multi = pygame.image.load(r'multi.png')
    single_rect = single.get_rect(center=(450,650))
    multi_rect = multi.get_rect(center=(450, 850))
    bounce = 1
    back = False
    while home_run:
        title = title_font.render(f'Croaky', True, (255, 255, 255))
        title2 = title_font.render(f'Catcher', True, (255, 255, 255))
        window.fill((0, 204, 255))
        window.blit(bg, (0, 0))
        window.blit(single, (50,650))
        window.blit(multi, (50, 800))
        if bounce == 1:
            window.blit(title, (50, 275))
            window.blit(title2, (100, 440))
            bounce = 2
            back = False
        elif bounce ==2:
            window.blit(title, (50, 280))
            window.blit(title2, (100, 445))
            if back == False:
                bounce = 3
            else:
                bounce = 1
        elif bounce ==3:
            window.blit(title, (50, 285))
            window.blit(title2, (100, 450))
            if back == False:
                bounce = 4
            else:
                bounce = 2
        elif bounce ==4:
            window.blit(title, (50, 290))
            window.blit(title2, (100, 455))
            if back == False:
                bounce = 5
            else:
                bounce = 3
        else:
            window.blit(title, (50, 295))
            window.blit(title2, (100, 460))
            bounce = 4
            back = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    home_run = False
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if single_rect.collidepoint(mouse_pos):
                    home_run = False
                    print("SinglePlayer")
                    SinglePlayer = True
                    main()
                if multi_rect.collidepoint(mouse_pos):
                    home_run = False
                    print("MultiPlayer")
                    SinglePlayer = False
                    main()
        pygame.display.update()
        clock.tick(10)


def main():
    run = True
    score = 0
    player = Player()
    velocity = 10
    player_list = pygame.sprite.Group()
    player_list.add(player)
    clock = pygame.time.Clock()
    screen_rect = window.get_rect()
    frog = pygame.image.load(r'Frog1.png')
    bg = pygame.image.load(r'bg.png')
    lastKey = None
    while run:
        score_text = font.render(f'{score}', True, (255, 255, 255))
        window.fill((0, 204, 255))
        window.blit(bg, (0, 0))
        text_rect = score_text.get_rect(center=(1000 / 2, 700))
        window.blit(score_text, text_rect)
        frog_rect = frog.get_rect(center=(1000 / 2, 1000 / 2))
        window.blit(frog, frog_rect)
        player_list.draw(window)
        pygame.draw.line(window, (255, 50, 0), (498, 460), pygame.mouse.get_pos(), width=20)
        pygame.draw.circle(window, (255, 50, 0), pygame.mouse.get_pos(), 30 // 2)
        pygame.draw.circle(window, (255, 50, 0), (498, 460), 20 // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if player.rect.collidepoint(mouse_pos):
                    lastKey = None
                    score += 1
                    velocity += 0.5
                    if SinglePlayer == True:
                        player.rect.x = random.randint(0, 900)
                        player.rect.y = random.randint(0, 900)
                    if velocity > 100:
                        velocity -= 0.5
                else:
                    score -= 1
                    velocity -= 0.5
                    if velocity < 0.5:
                        velocity += 0.5

            if event.type == pygame.KEYDOWN:
                lastKey = event.key
                if event.key == pygame.K_ESCAPE:
                    score = 0
                    home()
        if SinglePlayer == False:
            if lastKey == pygame.K_LEFT:
                player.rect.x -= velocity
            if lastKey == pygame.K_RIGHT:
                player.rect.x += velocity
            if lastKey == pygame.K_UP:
                player.rect.y -= velocity
            if lastKey == pygame.K_DOWN:
                player.rect.y += velocity

        player.rect.clamp_ip(screen_rect)
        pygame.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Croaky Catcher')
    font = pygame.font.Font("LuckiestGuy.ttf", 800)
    title_font = pygame.font.Font("LuckiestGuy.ttf", 200)
    home()
