import turtle
import time

# 建立畫面
win = turtle.Screen()
win.title("打磚塊遊戲")
win.bgcolor("black")
win.setup(width=600, height=800)
win.tracer(0)

# 建立球
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -300)
ball.dy = -5
ball.dx = -5

# 建立板子
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# 建立磚塊
bricks = []

# 磚塊的初始位置
brick_x = -280
brick_y = 250

# 磚塊的行數
num_rows = 5

# 磚塊的列數
num_cols = 10

# 磚塊的寬度
brick_width = 50

# 磚塊的高度
brick_height = 20

# 磚塊的間隔
brick_spacing = 5

# 磚塊的顏色
colors = ["red", "orange", "yellow", "green", "blue"]

# 建立磚塊
for i in range(num_rows):
    for j in range(num_cols):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        x_pos = brick_x + j * (brick_width + brick_spacing)
        y_pos = brick_y - i * (brick_height + brick_spacing)
        brick.goto(x_pos, y_pos)
        bricks.append(brick)

# 定義移動板子的函數
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -280:
        x = -280
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 280:
        x = 280
    paddle.setx(x)

# 設定鍵盤事件
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# 主遊戲迴圈
while True:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.move_left()
            elif event.key == pygame.K_RIGHT:
                paddle.move_right()

    # 更新球的位置
    ball.move()

    # 檢查球是否碰到磚塊
    for brick in bricks:
        if ball.hit_brick(brick):
            bricks.remove(brick)
            ball.bounce()

    # 檢查球是否碰到牆壁
    ball.check_wall_collision()

    # 檢查球是否碰到球拍
    if ball.hit_paddle(paddle):
        ball.bounce()

    # 清除畫面
    screen.fill(BLACK)

    # 繪製磚塊
    for brick in bricks:
        brick.draw(screen)

    # 繪製球拍
    paddle.draw(screen)

    # 繪製球
    ball.draw(screen)

    # 更新畫面
    pygame.display.update()

    # 設定遊戲速度
    clock.tick(60)

