from tkinter import PhotoImage, Label, Scale, HORIZONTAL
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from fuzzy_logic import suggest_gift  # Importing fuzzy logic function
from tkinter import ttk  # Import ttk for better dropdown appearance

# Initialize the Tkinter app
root = tk.Tk()
root.title("Giftanator")
root.geometry("800x800")  # Initial size

# Load Giftanator images
giftanator_img = PhotoImage(file="assets/giftanator.png")
giftanator_thinking_img = PhotoImage(file="assets/giftanator_thinking.png")
giftanator_thinking_rotated_img = PhotoImage(file="assets/giftanator_thinking_rotated.png")

# Load the mystery box images
box_stage1_img = PhotoImage(file="assets/box_stage1.png")
box_stage2_img = PhotoImage(file="assets/box_stage2.png")
box_stage3_img = PhotoImage(file="assets/box_stage3.png")
box_open_img = PhotoImage(file="assets/box_open.png")

# Style configuration for buttons
button_style = {
    "bg": "#FFCE00",  # Light yellow/golden background
    "fg": "black",  # Text color
    "font": ("Arial", 18, "bold"),
    "relief": "solid",
    "bd": 3,
    "highlightthickness": 2,
    "highlightbackground": "#FF8C00",
    "activebackground": "#FFA500",
    "padx": 20,
    "pady": 10,
}

# Function to add both the 'Back' and 'Next' buttons side by side
def add_back_and_next_buttons(row, back_command, next_command, next_text="Next", col_offset=0):
    """Adds Back and Next buttons with optional column offset for right alignment."""
    back_button = tk.Button(root, text="Back", command=back_command, **button_style)
    back_button.grid(row=row, column=col_offset, sticky="e", padx=5, pady=10)
    
    next_button = tk.Button(root, text=next_text, command=next_command, **button_style)
    next_button.grid(row=row, column=col_offset+1, sticky="w", padx=5, pady=10)

# Function to show the main game screen
def main_game_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Giftanator")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    label_img = tk.Label(root, image=giftanator_img)
    label_img.image = giftanator_img
    label_img.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

    btn_gift_ideas = tk.Button(root, text="I need gift ideas, Mr. Giftanator!", command=suggest_gifts, **button_style)
    btn_guess_game = tk.Button(root, text="Guess the gift", command=guess_game, **button_style)

    btn_gift_ideas.grid(row=2, column=0, sticky="e", padx=10, pady=20)
    btn_guess_game.grid(row=2, column=1, sticky="w", padx=10, pady=20)

# Function to show the home screen
def show_home_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Giftanator")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    label_img = tk.Label(root, image=giftanator_img)
    label_img.image = giftanator_img
    label_img.grid(row=0, column=0, sticky="nsew")
    
    enter_button = tk.Button(root, text="Play as a Guest", command=main_game_screen, **button_style)
    enter_button.grid(row=1, column=0, pady=20, sticky="s")

# Function to handle gift suggestions step by step
def suggest_gifts():
    for widget in root.winfo_children():
        widget.destroy()
    ask_relationship_type()

# Function to show relationship question (Image on the right, text on the left)
def ask_relationship_type():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="What type of relationship do you have with the person?", font=("Arial Bold", 20), fg="black").grid(row=0, column=0, columnspan=2, pady=2)

    relationship_var = tk.StringVar(root)
    relationship_combobox = ttk.Combobox(root, textvariable=relationship_var, font=("Arial", 14), state='readonly', height=13)
    relationship_combobox['values'] = ["Select an option", "Colleague", "Friend", "Friend of a friend", "Mother", "Father", 
                                       "Brother", "Sister", "Son", "Daughter", 
                                       "Grandpa", "Grandma", "Husband", "Wife"]
    relationship_combobox.current(0)
    relationship_combobox.grid(row=1, column=0, columnspan=2, pady=5)

    image_label = tk.Label(root, image=giftanator_thinking_img)
    image_label.image = giftanator_thinking_img
    image_label.grid(row=0, column=2, rowspan=3, sticky="e", padx=15)  # Reduced padding for closer alignment
     
    def validate_selection():
        if relationship_var.get() == "Select an option":
            messagebox.showerror("Input Error", "Please select a relationship type.")
        else:
            ask_closeness_level(relationship_var.get())

    add_back_and_next_buttons(row=2, back_command=main_game_screen, next_command=validate_selection, col_offset=0)

# Function to show closeness question (Image on the left, text on the right)
def ask_closeness_level(relationship):
    for widget in root.winfo_children():
        widget.destroy()

    image_label = tk.Label(root, image=giftanator_thinking_rotated_img)
    image_label.image = giftanator_thinking_rotated_img
    image_label.grid(row=0, column=0, rowspan=3, sticky="w", padx=15)  # Reduced padding for closer alignment

    tk.Label(root, text=f"How close are you to your {relationship}?", font=("Arial Bold", 20), fg="black").grid(row=0, column=1, columnspan=2, pady=2)

    closeness_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=400, tickinterval=25, font=("Arial", 14))
    closeness_slider.grid(row=1, column=1, columnspan=2, pady=5)

    add_back_and_next_buttons(row=2, back_command=lambda: ask_relationship_type(), next_command=lambda: ask_occasion(relationship, closeness_slider.get()), col_offset=0)

# Function to show occasion question (Image on the right, text on the left)
def ask_occasion(relationship, closeness_level):
    for widget in root.winfo_children():
        widget.destroy()

    image_label = tk.Label(root, image=giftanator_thinking_img)
    image_label.image = giftanator_thinking_img
    image_label.grid(row=0, column=2, rowspan=3, sticky="e", padx=15)  # Reduced padding for closer alignment

    tk.Label(root, text="What is the occasion?", font=("Arial Bold", 20), fg="black").grid(row=0, column=0, columnspan=2, pady=2)

    occasion_var = tk.StringVar(root)
    occasion_combobox = ttk.Combobox(root, textvariable=occasion_var, font=("Arial", 14), state='readonly', height=5)
    occasion_combobox['values'] = ["Select an option", "Birthday", "Anniversary", "Holiday", "Diploma celebration"]
    occasion_combobox.current(0)
    occasion_combobox.grid(row=1, column=0, columnspan=2, pady=5)

    def validate_occasion():
        if occasion_var.get() == "Select an option":
            messagebox.showerror("Input Error", "Please select an occasion.")
        else:
            ask_occasion_excitement(relationship, closeness_level, occasion_var.get())

    add_back_and_next_buttons(row=2, back_command=lambda: ask_closeness_level(relationship), next_command=validate_occasion, col_offset=0)

# Function to show excitement question (Image on the left, text on the right)
def ask_occasion_excitement(relationship, closeness_level, occasion):
    for widget in root.winfo_children():
        widget.destroy()

    image_label = tk.Label(root, image=giftanator_thinking_rotated_img)
    image_label.image = giftanator_thinking_rotated_img
    image_label.grid(row=0, column=0, rowspan=3, sticky="w", padx=15)  # Reduced padding for closer alignment

    tk.Label(root, text=f"How important is this {occasion} to you?", font=("Arial Bold", 20), fg="black").grid(row=0, column=1, columnspan=2, pady=2)

    excitement_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=400, tickinterval=25, font=("Arial", 14))
    excitement_slider.grid(row=1, column=1, columnspan=2, pady=5)

    add_back_and_next_buttons(
        row=2, 
        back_command=lambda: ask_occasion(relationship, closeness_level), 
        next_command=lambda: ask_budget(relationship, closeness_level, occasion),
        col_offset=0
    )

# Function to show budget question (Image on the right, text on the left)
def ask_budget(relationship, closeness_level, occasion):
    for widget in root.winfo_children():
        widget.destroy()

    image_label = tk.Label(root, image=giftanator_thinking_img)
    image_label.image = giftanator_thinking_img
    image_label.grid(row=0, column=2, rowspan=3, sticky="e", padx=15)  # Reduced padding for closer alignment

    tk.Label(root, text="Select your budget (low, medium, high):", font=("Arial Bold", 20), fg="black").grid(row=0, column=0, columnspan=2, pady=5)

    budget_var = tk.StringVar(root)
    budget_combobox = ttk.Combobox(root, textvariable=budget_var, font=("Arial", 14), state='readonly', height=4)
    budget_combobox['values'] = ["Select an option", "Low", "Medium", "High"]
    budget_combobox.current(0)
    budget_combobox.grid(row=1, column=0, columnspan=2, pady=5)

    def validate_budget():
        if budget_var.get() == "Select an option":
            messagebox.showerror("Input Error", "Please select a budget.")
        else:
            show_suggestions(relationship, closeness_level, occasion, budget_var.get())

    add_back_and_next_buttons(
        row=2, 
        back_command=lambda: ask_occasion_excitement(relationship, closeness_level, occasion), 
        next_command=validate_budget,
        col_offset=0
    )

# Function to show gift suggestions
def show_suggestions(relationship, closeness_level, occasion, budget):
    for widget in root.winfo_children():
        widget.destroy()

    # Display gift suggestions using grid
    tk.Label(root, text=f"1. Gift Suggestion: {suggest_gift(relationship, occasion, budget)}", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(root, text=f"2. Gift Suggestion: {suggest_gift(relationship, occasion, budget)}", font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=5)
    tk.Label(root, text=f"3. Gift Suggestion: {suggest_gift(relationship, occasion, budget)}", font=("Arial", 14)).grid(row=2, column=0, columnspan=2, pady=5)

    # Add 'Back' and 'Next' buttons
    add_back_and_next_buttons(
        row=3, 
        back_command=lambda: ask_budget(relationship, closeness_level, occasion), 
        next_command=main_game_screen, 
        next_text="Back to Main"
    )

# Function to handle the guessing game
def guess_game():
    for widget in root.winfo_children():
        widget.destroy()

    label_box = tk.Label(root, image=box_stage1_img)
    label_box.image = box_stage1_img
    label_box.grid(row=0, column=0, columnspan=2, pady=10)

    hints = ["The gift is something you can read.", "It is often enjoyed with a cup of tea.", "It's filled with stories."]
    correct_answers = ["book", "novel", "storybook"]
    attempts = [False, False, False]

    # Label and hint for guessing the gift
    title_label = tk.Label(root, text="Guess the gift in the Mystery Box!", font=("Arial", 16), fg="black")
    title_label.grid(row=1, column=0, columnspan=2)
    hint_label = tk.Label(root, text="Hint: " + hints[0], font=("Arial", 14), fg="black")
    hint_label.grid(row=2, column=0, columnspan=2, pady=5)

    guess_entry = tk.Entry(root, font=("Arial", 14))
    guess_entry.grid(row=3, column=0, columnspan=2, pady=5)

    def process_guess():
        guess = guess_entry.get().lower()
        current_attempt = sum(attempts)

        if guess in correct_answers and current_attempt < 3:
            attempts[current_attempt] = True
            if current_attempt == 0:
                label_box.config(image=box_stage2_img)
                hint_label.config(text="Hint: " + hints[1])
            elif current_attempt == 1:
                label_box.config(image=box_stage3_img)
                hint_label.config(text="Hint: " + hints[2])
            elif current_attempt == 2:
                label_box.config(image=box_open_img)
                # Hide the guessing interface and show the "Congratulations" message
                title_label.grid_forget()
                hint_label.grid_forget()
                guess_entry.grid_forget()
                submit_button.grid_forget()

                tk.Label(root, text="Congratulations - You have guessed correctly!", font=("Arial", 18), fg="black").grid(row=1, column=0, columnspan=2, pady=10)
                main_game_button = tk.Button(root, text="Back to Main Menu", command=main_game_screen, **button_style)
                main_game_button.grid(row=4, column=0, columnspan=2, pady=20)
        else:
            messagebox.showwarning("Try Again", "Incorrect guess. Try again!")

    submit_button = tk.Button(root, text="Submit Guess", command=process_guess, **button_style)
    submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start the app with the home screen
show_home_screen()  # Display the home screen initially
root.mainloop()  # Start the Tkinter event loop
