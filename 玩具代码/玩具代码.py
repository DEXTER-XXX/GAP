import pygame
pygame.init()

w,h=1280,720
pygame.display.set_mode((w,h))
screen=pygame.display.get_surface()

# 载入背景图并且缩放到宽高
bgpic=pygame.image.load('Sprite-0002.png')
bgpic=pygame.transform.scale(bgpic,(w,h))

# 载入素材
bt42_image=pygame.image.load('bt42-1.png')

# 创建精灵
bt42=pygame.sprite.Sprite()
bt42.image=bt42_image
bt42.rect=bt42.image.get_rect()
bt42.rect.x,bt42.rect.y=w/2,h/2

# 玩家组
player_group=pygame.sprite.Group()
player_group.add(bt42)

# 开始游戏
while True:
    # 更新部分
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                bt42.rect.y +=10
            if keys[pygame.K_UP]:
                bt42.rect.y -=10

# 画图部分
    screen.blit(bgpic,(0,0))
    player_group.draw(screen)
    pygame.display.update()
                
