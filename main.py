import tkinter, timer as tm
import difflib
from wonderwords import RandomSentence


def change_sentence():
    text_to_copy.set(str(RandomSentence().sentence()))


def start_timer(e):
    timer.start_timer()


def check_user_text(e):
    user_text = text_area.get('1.0', tkinter.END).strip()
    # print(f"area: {area_text}, copy: {text_to_copy.get()}")
    if user_text == text_to_copy.get():
        timer.stop_timer()
        text_area.config(state=tkinter.DISABLED)


def update_labels():
    elapsed_time = timer.get_time(format=True)
    timer_label.config(text=elapsed_time)
    if timer.get_time(format=False) is not None:
        cmp = round(len(text_area.get('1.0', tkinter.END).strip()) / timer.get_time(format=False), 2)
        speed_label.config(text=f"Characters per second: {cmp}")
    accuracy = round(difflib.SequenceMatcher(None, text_area.get('1.0', tkinter.END).strip(),
                                             text_to_copy.get()).ratio() * 100, 2)
    accuracy_label.config(text=f"Accuracy: {accuracy}%")
    window.after(10, update_labels)


def reset():
    text_area.config(state=tkinter.NORMAL)
    text_area.delete('1.0', tkinter.END)
    accuracy_label.config(text="Accuracy: 0%")
    speed_label.config(text="Speed: 0")
    timer.reset()
    timer_label.config(text="Time: 00:00:00")
    change_sentence()


window = tkinter.Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=300)

tkinter.Label(text="Try to copy text below as fast as you can:").pack()

text_to_copy = tkinter.StringVar()
change_sentence()
text_to_copy_label = tkinter.Label(textvariable=text_to_copy, font='Helvetica 18 bold')
text_to_copy_label.pack()

text_area = tkinter.Text(window, height=10, width=60)
text_area.pack()

timer_label = tkinter.Label(text="Time: 00:00:00")
timer_label.pack()

accuracy_label = tkinter.Label(text="Accuracy: 0%")
accuracy_label.pack()

speed_label = tkinter.Label(text="Characters per second: 0")
speed_label.pack()

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.pack()

timer = tm.Timer()

text_area.bind('<KeyPress>', start_timer)
window.bind('<KeyPress>', check_user_text)

update_labels()

window.mainloop()
