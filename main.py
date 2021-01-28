import  pygame
from random import randrange

RES = 800 #квадратній єкран
SIZE = 50 #разрешение змеййки(размер)

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) # начальное положение змейки будет случйным
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)] #список координат
dx, dy =0, 0 #направление движения
fps = 5 #количество кадров в секунду либо же скорость змейки

pygame.init()
sc = pygame.display.set_mode([RES, RES]) #создаем окно с размерами
clock = pygame.time.Clock() #создаем переменную клок для регулирования скорости змейки

while True:
    sc.fill(pygame.Color('black')) #закрашиваем дисплей в черный цвет

    
    #рисуем змейку и яблоко
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake] #списковые включения для рисования змейки
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

#eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1

    #game over
    if x < 0 or x > RES or y < 0 or y > RES:
        break
    if len(snake) != len(set(snake)):
        break


    if dx == 0 and dy == -1:
        y -= SIZE
        snake.append((x, y))
        snake = snake[-length:]
    if dx == 0 and dy == 1:
        y += SIZE
        snake.append((x, y))
        snake = snake[-length:]
    if dx == 1 and dy == 0:
        x += SIZE
        snake.append((x, y))
        snake = snake[-length:]
    if dx == -1 and dy == 0:
        x -= SIZE
        snake.append((x, y))
        snake = snake[-length:]

    #делаем задержку в обновлении кадров
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
