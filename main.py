from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
NEON_GREEN = '#00ff08'
YELLOW = "#f7f5dd"
FONT_NAME = 'Eras Demi ITC'

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = ''


def reset():
    window.after_cancel(timer_count)
    canvas.itemconfig(timer, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    global reps
    reps = 0


def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='20\' Break', fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='5\' Break', fg=PINK)
    else:
        if reps == 1:
            checkmark['text'] = ''
            print(checkmark['text'])
        count_down(WORK_MIN * 60)
        timer_label.config(text='Working', fg=GREEN)


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer_count
        timer_count = window.after(1, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            checkmark['text'] += '✓'


window = Tk()
window.title('Pomodoro! 🍅')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text='', font=('', 14), bg=YELLOW, fg=NEON_GREEN)
checkmark.grid(column=1, row=3)
checkmark_num = Label(text='', font=('', 14), bg=YELLOW, fg=NEON_GREEN)
checkmark_num.grid(column=1, row=4)

window.mainloop()
