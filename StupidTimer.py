import time
import pygame
import sys


def runGame(arg):
    if len(arg) == 1:
        arg.append("90")
        arg.append("1.2")
    elif len(arg) == 2:
        arg.append("1.2")
    timeInterval = float(arg[2])
    timeInterval = int(timeInterval*10)
    initTime = arg[1]
    initTime = int(initTime)

    pygame.init()
    timeTick = 0
    bgcolor = (220, 220, 220)  #背景色
    screen = pygame.display.set_mode((1500, 800)) #窗口分辨率
    screen.fill(bgcolor)
    font = pygame.font.SysFont("arial", 250)
    clock = pygame.time.Clock()

    while initTime:
        clock.tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        hour = initTime//3600
        minute = (initTime%3600) // 60
        second = initTime % 60
        showString = str(hour).zfill(2)+":"+str(minute).zfill(2) + ":" + str(second).zfill(2)#屏幕展示字符串
        stringImage = font.render(showString, False, (255, 255, 255), (60,60,60))#render四个参数为展示字符串 抗锯齿 字体颜色 字体背景色
        stringRect = stringImage.get_rect()
        stringRect.center = (750,400)#字体中心坐标
        screen.blit(stringImage, stringRect)
        time.sleep(0.1)
        timeTick+=1
        if timeTick == timeInterval:
            timeTick = 0
            initTime -= 1
            pygame.display.flip()
            pygame.display.update()

    time.sleep(2)
    sys.exit()

if __name__ == '__main__':
    runGame(sys.argv)