from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import time

root = Tk()
root.geometry("1200x650+40+30")
root.title("GAME")
root.resizable(0, 0)
root.configure(bg="#fff")
choice = ['ROCK', 'PAPER', 'SCISSOR']
my_lbl = ""
player = 0
comp = 0

rock_i = Image.open("C:\game\image\_rock.png")
new = rock_i.resize((120, 70), Image.ANTIALIAS)
rock_ig = ImageTk.PhotoImage(new)

paper_i = Image.open("C:\game\image\paper.png")
new = paper_i.resize((120, 70), Image.ANTIALIAS)
paper_ig = ImageTk.PhotoImage(new)

scissor_i = Image.open("C:\game\image\scissor.png")
new = scissor_i.resize((120, 70), Image.ANTIALIAS)
scissor_ig = ImageTk.PhotoImage(new)

question_i = Image.open("C:\game\image\question.jpg")
new = question_i.resize((120, 70), Image.ANTIALIAS)
question_ig = ImageTk.PhotoImage(new)

order_i = Image.open("C:\game\image\order.jpg")
new = order_i.resize((170, 90), Image.ANTIALIAS)
order_ig = ImageTk.PhotoImage(new)

select_i = Image.open("C:\game\image\select.jpg")
new = select_i.resize((170, 90), Image.ANTIALIAS)
select_ig = ImageTk.PhotoImage(new)

computer_i = Image.open("C:\game\image\computer.png")
new = computer_i.resize((170, 90), Image.ANTIALIAS)
computer_ig = ImageTk.PhotoImage(new)

player_i = Image.open("C:\game\image\player.jpg")
new = player_i.resize((170, 90), Image.ANTIALIAS)
player_ig = ImageTk.PhotoImage(new)


def end_g():
    root.destroy()
    root1 = Tk()
    root1.geometry("1200x650+40+30")
    root1.title("GAME")
    root1.resizable(0, 0)
    root1.configure(bg="#fff")
    if comp == player:
        tie_i = Image.open("C:\game\image\_tie.png")
        new1 = tie_i.resize((250, 200), Image.ANTIALIAS)
        tie_ig = ImageTk.PhotoImage(new1)
        display_lbl = Label(root1, image=tie_ig)
        display_lbl.pack(pady=50)
    elif comp > player:
        lose_i = Image.open("C:\game\image\lose.jpg")
        new1 = lose_i.resize((250, 200), Image.ANTIALIAS)
        lose_ig = ImageTk.PhotoImage(new1)
        display_lbl = Label(root1, image=lose_ig, bg="#fff")
        display_lbl.pack()
    elif player > comp:
        win_i = Image.open("C:\game\image\win.jpg")
        new1 = win_i.resize((250, 200), Image.ANTIALIAS)
        win_ig = ImageTk.PhotoImage(new1)
        display_lbl = Label(root1, image=win_ig, bg="#fff")
        display_lbl.pack()
    thank = Label(root1, text="THANK YOU FOR PLAYING THE GAME \nHOPE YOU ENJOYED IT", font=("Helvetica", 14, "italic"),
                  bg="#fff")
    thank.pack(pady=10)
    word = Label(root1, text="GAME WILL AUTOMATICALLY CLOSE AFTER 5 SECOND", font=("Helvetica", 14, "italic"),
                 bg="#fff")
    word.pack()
    made = Label(root1, text="MADE BY: DHIRAJ AGARWAL", font=("Helvetica", 14, "italic"), bg="#fff")
    made.pack(pady=100)
    for i in range(4, -1, -1):
        time.sleep(1)
        word.configure(text="GAME WILL AUTOMATICALLY CLOSE AFTER " + str(i) + " SECOND")
        root1.update()
    root1.destroy()
    root1.mainloop()


def mine():
    global show
    if my_lbl == "D":
        show = Label(score_frame, text="DRAW", font=("Helvetica", 14, "italic"), bg="#fff")
        show.place(x=450, y=100, height=40, width=110)
    if my_lbl == "W":
        show = Label(score_frame, text="YOU WIN", font=("Helvetica", 14, "italic"), bg="#fff")
        show.place(x=450, y=100, height=40, width=110)
    if my_lbl == "L":
        show = Label(score_frame, text="YOU LOSE", font=("Helvetica", 14, "italic"), bg="#fff")
        show.place(x=450, y=100, height=40, width=110)
    player_score_1.configure(text=str(player))
    computer_score_1.configure(text=str(comp))
    root.update()


def reset():
    try:
        show.destroy()
    except:
        messagebox.showwarning("NOTHING", "PLAY THE GAME")
    finally:
        rock.configure(state=NORMAL)
        paper.configure(state=NORMAL)
        scissor.configure(state=NORMAL)
        question_lbl2.configure(image=question_ig)
        question_lbl1.configure(image=question_ig)


def g_rock():
    global my_lbl, player, comp
    computer = random.choice(choice)
    question_lbl2.configure(image=rock_ig)
    rock.configure(state=DISABLED)
    paper.configure(state=DISABLED)
    scissor.configure(state=DISABLED)
    if computer == "ROCK":
        question_lbl1.configure(image=rock_ig)
        my_lbl = "D"
    elif computer == "PAPER":
        question_lbl1.configure(image=paper_ig)
        my_lbl = "L"
        comp += 1
    elif computer == "SCISSOR":
        question_lbl1.configure(image=scissor_ig)
        my_lbl = "W"
        player += 1
    mine()


def g_paper():
    global my_lbl, player, comp
    computer = random.choice(choice)
    question_lbl2.configure(image=paper_ig)
    rock.configure(state=DISABLED)
    paper.configure(state=DISABLED)
    scissor.configure(state=DISABLED)
    if computer == "PAPER":
        question_lbl1.configure(image=paper_ig)
        my_lbl = "D"
    elif computer == "ROCK":
        question_lbl1.configure(image=rock_ig)
        my_lbl = "W"
        player += 1
    elif computer == "SCISSOR":
        question_lbl1.configure(image=scissor_ig)
        my_lbl = "L"
        comp += 1
    mine()


def g_scissor():
    global my_lbl, player, comp
    computer = random.choice(choice)
    question_lbl2.configure(image=scissor_ig)
    rock.configure(state=DISABLED)
    paper.configure(state=DISABLED)
    scissor.configure(state=DISABLED)
    if computer == "SCISSOR":
        question_lbl1.configure(image=scissor_ig)
        my_lbl = "D"
    elif computer == "PAPER":
        question_lbl1.configure(image=paper_ig)
        my_lbl = "W"
        player += 1
    elif computer == "ROCK":
        question_lbl1.configure(image=rock_ig)
        my_lbl = "L"
        comp += 1
    mine()


question_lbl1 = Label(root, image=question_ig, bg="#fff")
question_lbl1.place(x=530, y=190)
question_lbl2 = Label(root, image=question_ig, bg="#fff")
question_lbl2.place(x=530, y=310)
select = Label(root, image=select_ig, bg="#fff")
select.place(x=100, y=430)
computer_lbl = Label(root, image=computer_ig, bg="#fff")
computer_lbl.place(x=100, y=180)
player_lbl = Label(root, image=player_ig, bg="#fff")
player_lbl.place(x=100, y=300)
rock = Button(root, image=rock_ig, command=g_rock, bg="#fff")
rock.place(x=350, y=430)
paper = Button(root, image=paper_ig, command=g_paper, bg="#fff")
paper.place(x=550, y=430)
scissor = Button(root, image=scissor_ig, command=g_scissor, bg="#fff")
scissor.place(x=750, y=430)
order = Button(root, image=order_ig, command=reset, bg="#fff")
order.place(x=510, y=530)
score_frame = LabelFrame(root, text="SCORE", fg="brown", bg="#fff")
score_frame.pack(ipadx=500, ipady=85)
player_score = Label(score_frame, text="PLAYER", bg="black", fg="#fff", font=("Helvetica", 14, "italic"))
player_score.place(x=500, height=50, width=390)
player_score_1 = Label(score_frame, text="0", font=("Helvetica", 14, "bold"), bg="#fff")
player_score_1.place(x=670, y=60, height=40, width=40)
computer_score = Label(score_frame, text="COMPUTER", font=("Helvetica", 14, "italic"))
computer_score.place(x=100, height=50, width=390)
computer_score_1 = Label(score_frame, text="0", font=("Helvetica", 14, "bold"), bg="#fff")
computer_score_1.place(x=270, y=60, height=40, width=40)
end = Button(root, text="        E N D        ", bg="red", font=("Helvetica", 14, "bold"), command=end_g)
end.place(x=910, y=560, height=35, width=170)
root.mainloop()
