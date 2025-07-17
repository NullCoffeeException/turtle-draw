import tkinter as tk
import customtkinter as ctk
import turtle
import colorsys
import math
import threading    # GUI 2개를 동시에 하기 위함
from PIL import Image


# 1번. 만다라
def draw_mandara():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    hue = 0
    n = 36

    for i in range(240):
        c = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(c)
        t.width(i / 100 + 1)

        t.forward(i)
        t.left(59)
        hue += 1 / n


# 2번. 스파이럴 플라워
def draw_spiral_flower():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    hue = 0

    for _ in range(60):
        c = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(c)

        t.circle(100)
        t.left(6)
        hue += 1 / 60


# 3번. 장미 곡선
def draw_rose_curve():
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()
    hue = 0

    for theta in range(210):
        c = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(c)
        angle = math.radians(theta)
        r = 200 * math.sin(13 * angle)
        x = r * math.cos(angle)
        y = r * math.sin(angle)

        t.goto(x, y)

        if theta == 0:
            t.penup()
        else:
            t.pendown()
        hue += 1 / 180


# 4번. 원 중첩
def draw_circle_overlap():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    hue = 0

    for i in range(80):
        c = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(c)
        t.circle(100 - i)
        t.left(45)
        hue += 1 / 100


# 선택된 그림 전역변수
func = draw_mandara


# turtle을 이용한 그리기 함수
def turtle_draw():
    try:
        turtle.TurtleScreen._RUNNING = True

        screen = turtle.Screen()
        screen.clearscreen
        screen.bgcolor("black")

        func()

        screen.exitonclick()
        screen.bye()

    except:
        pass


# 버튼 클릭 시 turtle 실행 함수
def on_click():
    turtle_thread = threading.Thread(target=turtle_draw, daemon= True)
    turtle_thread.start()


# 테마 설정
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 창 설정
root = ctk.CTk()
root.title("Turtle Draw")
root.geometry("1000x500+200+200")



# grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=7, minsize=420)
root.rowconfigure(1, weight=1, minsize=60)

# 레이아웃
top_frame = ctk.CTkFrame(root)
top_frame.grid(row=0, column=0, sticky="nsew")

bottom_frame = ctk.CTkFrame(root, fg_color="#444444")
bottom_frame.grid(row=1, column=0, sticky="nsew")


# top_frame 레이아웃
top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)
top_frame.columnconfigure(3, weight=1)
top_frame.rowconfigure(0, weight=1)


IMG_SIZE = 200

# 만다라 버튼
def click_mandara():
    global func
    func = draw_mandara

img_mandara = ctk.CTkImage(light_image=Image.open("./img/mandara.png"), size=(IMG_SIZE, IMG_SIZE))
btn_mandara = ctk.CTkButton(top_frame, image=img_mandara, text="", command=click_mandara)
btn_mandara.grid(row=0, column=0)


# 스파이럴 플라워 버튼
def click_spiral_flower():
    global func
    func = draw_spiral_flower

img_spiral_flower = ctk.CTkImage(light_image=Image.open("./img/spiral_flower.png"), size=(IMG_SIZE, IMG_SIZE))
btn_spiral_flower = ctk.CTkButton(top_frame, image=img_spiral_flower, text="", command=click_spiral_flower)
btn_spiral_flower.grid(row=0, column=1)


# 장미 곡선 버튼
def click_rose_curve():
    global func
    func = draw_rose_curve

img_rose_curve = ctk.CTkImage(light_image=Image.open("./img/rose_curve.png"), size=(IMG_SIZE, IMG_SIZE))
btn_rose_curve = ctk.CTkButton(top_frame, image=img_rose_curve, text="", command=click_rose_curve)
btn_rose_curve.grid(row=0, column=2)


# 원 중첩 버튼
def click_circle_overlap():
    global func
    func = draw_circle_overlap

img_wolf = ctk.CTkImage(light_image=Image.open('./img/circle_overlap.png'), size=(IMG_SIZE, IMG_SIZE))
btn_wolf = ctk.CTkButton(top_frame, image=img_wolf, text="", command=click_circle_overlap)
btn_wolf.grid(row=0, column=3)

# bottom_frame 레이아웃
btn_run = ctk.CTkButton(bottom_frame, text="실행", command=turtle_draw, width=150, height=40, font=("Arial", 18))
btn_run.pack(pady=30)


root.mainloop()