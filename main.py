import tkinter

# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# window.mainloop()

def add(*args):
    print(f'args: {args}')
    arg_sum = sum(args)
    print(f"arg_sum: {arg_sum}")

add(1,3,4, 9, 10, 12)
