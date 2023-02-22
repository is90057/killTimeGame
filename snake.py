import pygame
import random

# 遊戲區域尺寸
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# 定義貪食蛇的方塊尺寸
BLOCK_SIZE = 10

# 定義貪食蛇的顏色
SNAKE_COLOR = (0, 255, 0)

# 定義食物的顏色
FOOD_COLOR = (255, 0, 0)

# 初始化 Pygame
pygame.init()

# 創建遊戲區域
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 設置遊戲標題
pygame.display.set_caption('Snake Game')

# 創建時鐘對象
clock = pygame.time.Clock()

# 定義遊戲結束函數
def game_over():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Over! Your Score: " + str(score), True, (255, 0, 0))
    screen.blit(text, [SCREEN_WIDTH/3, SCREEN_HEIGHT/3])
    pygame.display.update()
    pygame.time.wait(2000)

# 定義繪製貪食蛇函數
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, SNAKE_COLOR, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# 生成食物
def generate_food():
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    return [food_x, food_y]

# 初始化貪食蛇的位置和長度
snake_head = [250, 250]
snake_list = [snake_head]
snake_length = 1

# 初始化貪食蛇的移動方向
direction = "right"

# 生成食物的初始位置
food_position = generate_food()

# 定義分數
score = 0

# 遊戲循環
game_over_flag = False
while not game_over_flag:

    # 處理遊戲事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # 根據方向移動貪食蛇
    if direction == "right":
        snake_head[0] += BLOCK_SIZE
    elif direction == "left":
        snake_head[0] -= BLOCK_SIZE
    elif direction == "up":
        snake_head[1] -= BLOCK_SIZE
    elif direction == "down":
        snake_head[1] += BLOCK_SIZE

    # 判斷貪食蛇是否吃到了食物
    if snake_head == food_position:
        # 生成新的食物位置
        food_position = [random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
        # 增加貪食蛇長度
        snake_length += 1

    # 將新的貪食蛇頭部添加到貪食蛇列表中
    snake_list.append(list(snake_head))

    # 如果貪食蛇長度大於指定長度，則刪除貪食蛇尾部
    if len(snake_list) > snake_length:
        del snake_list[0]

    # 判斷貪食蛇是否碰到邊界或自身
    if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
        game_over()
        game_over_flag = True
    for block in snake_list[:-1]:
        if block == snake_head:
            game_over()
            game_over_flag = True

    # 繪製遊戲界面
    screen.fill((255, 255, 255))
    draw_snake(snake_list)
    pygame.draw.rect(screen, FOOD_COLOR, [food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE])
    pygame.display.update()

    # 控制遊戲速度
    clock.tick(15)
pygame.quit()