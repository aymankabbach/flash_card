from tkinter import *
import pandas,time,random
window=Tk()
window.title("flash cards")
language="English"
is_going=True
clicked=False
def read_csv_file():
    global to_learn
    try:
        data=pandas.read_csv("words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("french_words.csv")
        to_learn=data.to_dict(orient="records")
    else:
        to_learn=data.to_dict(orient="records")
read_csv_file()
current_card=random.choice(to_learn)
def next_card():
    global current_card
    current_card=random.choice(to_learn)
def is_known():
    global clicked,current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
    clicked=True
def is_unkown():
    global clicked
    next_card()
    clicked=True
right_img=PhotoImage(file="right.png")
right_button=Button(image=right_img,highlightthickness=0,command=is_known)
wrong_img=PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=is_unkown)
canvas=Canvas(width=800,height=526)
window.config(padx=50,pady=50, background="#B1DDC6")
front_img=PhotoImage(file="card_front.png")
back_img=PhotoImage(file="card_back.png")
my_img=canvas.create_image(400,263, image=front_img)
canvas.config(bg="#B1DDC6",highlightthickness=0)
language_word=canvas.create_text(400,150,text=language,font=("Ariel",40,"italic"))
word=canvas.create_text(400,270,text=current_card["English"],font=("Ariel",60,"bold"))
def grid_canvas_and_button():
    canvas.grid(row=0,column=0,columnspan=2)
    wrong_button.grid(row=1, column=0)
    right_button.grid(row=1, column=1)
def start():
    global is_going,language,clicked
    grid_canvas_and_button()
    while is_going:
        window.update()
        if language=="English":
            time.sleep(3)
            canvas.itemconfig(my_img,image=back_img)
            language="French"
            canvas.itemconfig(word,text=current_card["French"])
            canvas.itemconfig(language_word,text=language)
        if language=="French":
            if clicked==False:
                pass
            else: 
                canvas.itemconfig(my_img,image=front_img)
                language="English"
                canvas.itemconfig(word,text=current_card["English"])
                canvas.itemconfig(language_word,text=language)
                clicked=False
start()
window.mainloop()