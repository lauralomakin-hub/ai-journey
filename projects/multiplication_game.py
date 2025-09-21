#b)
import tkinter as tk
import numpy as np

X,Y = 0, 0  #placeholder for current numbers
score = 0
tables = []         #placeholder


difficulties = {                    #dictionary with tables
    "Easy" : [0, 1, 2, 5, 10],
    "Medium" : [3, 4, 6],
    "Hard" : [7, 8, 9]
}

def choose_difficulty(level):
    global tables, score
    tables = difficulties[level]
    score = 0
    info_var.set(f"Now difficulty = {level}. Click start to begin!")  #replace print
    start_btn.pack(pady=6)                                          #button

def new_question():
   global X, Y
   X = int(np.random.choice(tables))
   Y = int(np.random.randint(1, 11))
   question_var.set(f"{X} * {Y} =   ")   # label instead of print question
   answer_var.set("")                    # entry instead of input
   feedback_var.set("")
   #activate feedback and hide YES/NO button
   answer_entry.config(state = "normal")
   try_again_frame.pack_forget()
   answer_entry.focus_set()
   submit_btn.config(state="normal")
   start_btn.pack_forget()

def check_answer():
    global score
    text = answer_var.get().strip()               #read from entry instead of input()
    if text.isdigit():
        answer = int(text)
        if answer == X * Y:
            feedback_var.set(f"{X} * {Y} = {X * Y} . You are Right!")  # replace print
            score += 1
            score_var.set(f"Score: {score}")
        else:
            feedback_var.set(f"I am sorry, {X} * {Y} is not {answer}. The right answer is {X * Y}")  #replace print
            score_var.set(f"Score: {score}")
            
    else: 
        feedback_var.set("please enter your answer as a number.")
        return
    answer_entry.config(state="disabled")
    submit_btn.config(state = "disabled")
    try_again_frame.pack(pady=8)
    root.unbind("<return>")

def try_again(choice: str):
    #hide YES/NO buttons
    try_again_frame.pack_forget()

    if choice == "yes":
        #continue game: unlock field and button, ask question
        answer_entry.config(state="normal")
        submit_btn.config(state="normal")
        new_question()
    
    else:  #"break" "thank you"
        feedback_var.set("Thank you!")
        question_var.set("")              #empty question
        info_var.set("Choose a level to play again.")
        answer_entry.config(state="disabled")
        submit_btn.config(state="disabled")
        root.bind("<Return>", lambda e: check_answer())

#UI
root=tk.Tk()
root.title("Multiplication game")
root.geometry("420x340")

# variables that labels and entry uses

info_var  = tk.StringVar(value="Choose your level to start!")
question_var = tk.StringVar(value="")
answer_var = tk.StringVar(value="")
feedback_var = tk.StringVar(value="")
score_var = tk.StringVar(value="Score: 0")

#level - instead of input "choose your level"

tk.Label(root, text= "Choose Your level: ", font=("segoe UI", 14)).pack(pady=8)
lvl_row = tk.Frame(root)
lvl_row.pack()
tk.Button(lvl_row, text="Easy", width=12, command=lambda: choose_difficulty("Easy")).pack(side= "left", padx = 5)
tk.Button(lvl_row, text="Medium", width=12, command=lambda: choose_difficulty("Medium")).pack(side="left", padx=5) 
tk.Button(lvl_row, text="Hard", width=12, command=lambda: choose_difficulty("Hard")).pack(side="left", padx=5)   

tk.Label(root, textvariable=info_var).pack(pady=6)

#start-button -concealed until lvl choosen.

start_btn = tk.Button(root, text="START", command=new_question)
start_btn.pack_forget()

#game surface

tk.Label(root, textvariable=question_var, font=("Segoe UI", 18)).pack(pady=6)
answer_entry = tk.Entry(root, textvariable=answer_var, font=("Segoe UI", 16), width=8, justify="center")
answer_entry.pack()
submit_btn = tk.Button(root, text="submit", command=check_answer)
submit_btn.pack(pady=6)
tk.Label(root, textvariable=feedback_var, font=("Segoe UI", 12)).pack(pady=6)
tk.Label(root, textvariable=score_var, font=("Segoe UI", 12, "bold")).pack()

# YES/NO buttons concealed until answer

try_again_frame = tk.Frame(root)
tk.Label(try_again_frame, text="Do you want to try again?").pack(side="left", padx=6)
tk.Button(try_again_frame, text="YES", width=6, command=lambda: try_again("yes")).pack(side="left", padx=4)
tk.Button(try_again_frame, text="NO", width=6, command=lambda: try_again("no")).pack(side="left", padx=4)       

#enter = submit

root.bind("<Return>", lambda e:check_answer())

root.mainloop()


# OLd version##
# while True:
#    X = (np.random.choice(tables))
#    Y = (np.random.randint(1, 11))
#    answer = int(input(f"{X} * {Y} =   "))
#    if answer == X * Y:
#        print(f"{X} * {Y} = {X * Y} . You are Right!")
#        score += 1
#    else:
#        print(f"I am sorry, {X} * {Y} is not {answer}. The right answer is {X * Y}")

#    choice = input(f"Do you want to try again? yes/no ").strip().lower()
#    if choice == "no":
#        print("Thank you!")
#        break
#    elif choice == "yes":
#        continue
#    else:
#        print("I am sorry, I did not understand. Quitting game")
#        break