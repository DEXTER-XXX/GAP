# 工具和游戏主控
import os
import random
import pygame


class Game:
    def __int__(self):
        pygame.init()
        # pygame.display.set_mode((1280, 720))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        # 开始游戏
        GRAPHICS = load_graphics('resources/graphics')
        while True:
            # 更新部分
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            image = get_image(GRAPHICS['bt42-1'], 37, 12, 156, 363, (0, 0, 0), 1)
            # 图片名字,左上角x,y,宽,高,抠图底色,放大倍数
            self.screen.blit(image, (1280, 720))
            pygame.display.update()
            self.clock.tick(60)

def load_graphics(path, accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img =pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics
#
# def get_image(sheet, x, y, width, height, colorkey, scale):
#     image = pygame.Surface([width, height])
#     rect = image.get_rect()
#     image.blit(sheet, (0, 0), (x, y, width, height))
#     image.set_colorkey(colorkey)
#     image = pygame.transform.scale(image, (int(rect.width * scale), int(rect.height * scale)))
#     return image
#
#

