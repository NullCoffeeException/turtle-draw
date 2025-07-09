import tkinter as tk
import customtkinter as ctk
import turtle
import threading    # GUI 2개를 동시에 하기 위함


# turtle을 이용한 그리기 함수
def turtle_draw():
    try:
        turtle.TurtleScreen._RUNNING = True

        screen = turtle.Screen()
        screen.clearscreen
        screen.bgcolor("black")

        t = turtle.Turtle()
        t.speed(0)
        t.color("cyan")
        t.hideturtle()

        for _ in range(5):
            t.forward(100)
            t.right(90)

        screen.exitonclick()
        screen.bye()

    except:
        pass


# 버튼 클릭 시 turtle 실행 함수
def on_click():
    turtle_thread = threading.Thread(target=turtle_draw, daemon= True).start()


# 테마 설정
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 창 설정
root = ctk.CTk()
root.title("Turtle Draw")
root.geometry("1000x600")

button = ctk.CTkButton(root, text="실행", command=turtle_draw)
button.pack(pady=100)


root.mainloop()