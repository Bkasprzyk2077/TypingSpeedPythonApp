import tkinter, timer

window = tkinter.Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=300)

text_to_copy = tkinter.StringVar()
text_to_copy.set("lorem ipsum")
text_to_copy_label = tkinter.Label(textvariable=text_to_copy)
text_to_copy_label.pack()

text_area = tkinter.Text(window, height=5, width=20)
text_area.pack()

timer_label = tkinter.Label(text="00:00:00")
timer_label.pack()

timer = timer.Timer()


def on_key_pressed(e):
    area_text = text_area.get('1.0', tkinter.END).rstrip()
    # print(f"area: {area_text}, copy: {text_to_copy.get()}")
    if area_text == text_to_copy.get():
        print("test")
        timer.stop_timer()
    else:
        timer.start_timer()


def update_clock():
    elapsed_time = timer.get_time()
    timer_label.config(text=elapsed_time)
    window.after(10, update_clock)


update_clock()

window.bind('<KeyPress>', on_key_pressed)

window.mainloop()
