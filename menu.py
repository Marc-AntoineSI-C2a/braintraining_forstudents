"""
Author : Marc-Antoine Romao
Classe : SI-C2a
theme : MA-PROJ-PY
"""

import tkinter as tk
import geo01
import info02
import info05
import database

database.open_dbconnection()

# exercises array
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # label (with images) array
a_image = [None, None, None]  # images array
a_title = [None, None, None]  # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02,
              "info05": info05.open_window_info_05}


# call other windows (exercices)
def exercise(event, exer):
    dict_games[exer](window)


# call display_results
def display_result(event):
    global window_display_result, hex_color, canvas

    def update_table(name=""):
        for child in canvas.winfo_children():
            if child.grid_info()["row"] != 0:
                child.destroy()
        table_scores = database.getresults(name)
        for line in range(len(table_scores)):
            # Search students name in this row
            student_name = database.get_playername(table_scores[line][0])
            # Search exercise name in this row
            exercise_name = database.get_exercisename(table_scores[line][3])[0]
            # Show this rows and the written column values
            lbl_player = tk.Label(canvas, text=student_name[0], font=("Arial", 10), width=18, bg="white")
            lbl_player.grid(row=line + 1, column=0, ipady=5, padx=0, pady=5)
            lbl_date_heure = tk.Label(canvas, text=table_scores[line][1], font=("Arial", 10), width=18,
                                      bg="white")
            lbl_date_heure.grid(row=line + 1, column=1, ipady=5, padx=0, pady=5)
            lbl_duration = tk.Label(canvas, text=table_scores[line][2], font=("Arial", 10), width=18, bg="white")
            lbl_duration.grid(row=line + 1, column=2, ipady=5, padx=0, pady=5)
            lbl_exercise = tk.Label(canvas, text=exercise_name, font=("Arial", 10), width=18, bg="white")
            lbl_exercise.grid(row=line + 1, column=3, ipady=5, padx=0, pady=5)
            lbl_nb_success = tk.Label(canvas, text=table_scores[line][4], font=("Arial", 10), width=18, bg="white")
            lbl_nb_success.grid(row=line + 1, column=4, ipady=5, padx=0, pady=5)
            lbl_nb_tries = tk.Label(canvas, text=table_scores[line][3], font=("Arial", 10), width=18,
                                    bg="white")
            lbl_nb_tries.grid(row=line + 1, column=5, ipady=5, padx=0, pady=5)
            # To prevent errors, we are going to check if the value is 0 (can't divide by 0)
            if table_scores[line][3] == 0:
                print("Division by 0, value skipped")
            else:
                success_percentage = 100 * table_scores[line][4] / table_scores[line][3]
                success_percentage = round(success_percentage, 2)
                # Calculate the percent of success and then write it in the window
                lbl_success_percentage = tk.Label(canvas, text=f"{success_percentage}%", font=("Arial", 10), width=15,
                                                  bg="white")
                lbl_success_percentage.grid(row=line + 1, column=6, ipady=5, padx=0, pady=5)

    window_display_result = tk.Toplevel(window)
    window_display_result.title("Résultats")
    window_display_result.geometry("1100x900")
    window_display_result.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=50, weight=1)
    window_display_result.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), minsize=50,
                                            weight=1)

    # Title création
    lbl_title_training = tk.Label(window_display_result, text="TRAINING : AFFICHAGE", font=("Arial", 15))
    lbl_title_training.grid(row=0, column=4, ipady=5, padx=40, pady=40)
    # Main frame creation
    canvas = tk.Canvas(window_display_result, width=2000, height=500, bg="white")
    canvas.grid(row=1, column=0, padx=5, pady=5, columnspan=8, rowspan=13)
    canvas.columnconfigure((0, 1, 2, 3, 4, 5, 6), minsize=50, weight=1)
    canvas.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), minsize=50, weight=1)
    # Label for students name in score creation
    lbl_player = tk.Label(canvas, text="Eleve", font=("Arial", 10), width=20)
    lbl_player.grid(row=0, column=0, ipady=5, padx=0, pady=5)
    # Label for date and hour in score creation
    lbl_date_heure = tk.Label(canvas, text="Date Heure", font=("Arial", 10), width=20)
    lbl_date_heure.grid(row=0, column=1, ipady=5, padx=0, pady=5)
    # Label for time in score creation
    lbl_duration = tk.Label(canvas, text="Temps", font=("Arial", 10), width=20)
    lbl_duration.grid(row=0, column=2, ipady=5, padx=0, pady=5)
    # Label for exercises name in score creation
    lbl_exercise = tk.Label(canvas, text="Exercise", font=("Arial", 10), width=20)
    lbl_exercise.grid(row=0, column=3, ipady=5, padx=0, pady=5)
    # Label for number of successes in score creation
    lbl_nb_success = tk.Label(canvas, text="nb OK", font=("Arial", 10), width=20)
    lbl_nb_success.grid(row=0, column=4, ipady=5, padx=0, pady=5)
    # Label for number of total tries in score creation
    lbl_nb_tries = tk.Label(canvas, text="nb Total", font=("Arial", 10), width=20)
    lbl_nb_tries.grid(row=0, column=5, ipady=5, padx=0, pady=5)
    # Label for the success-in-pourcentage in score creation
    lbl_success_percentage = tk.Label(canvas, text="% réussi", font=("Arial", 10), width=20)
    lbl_success_percentage.grid(row=0, column=6, ipady=5, padx=0, pady=5)

    lbl_title_total = tk.Label(window_display_result, text="Total", font=("Arial", 15))
    lbl_title_total.grid(row=14, column=4, ipady=5, padx=40, pady=40)

    btn_results = tk.Button(window_display_result, text="Display results", font=("Arial", 15),
                            command=lambda: update_table(entry_pseudo.get()))
    btn_results.grid(row=15, column=2)

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window_display_result.configure(bg=hex_color)
    entry_pseudo = tk.Entry(window_display_result, font=("Arial", 15))
    entry_pseudo.grid(row=69, column=0)
    update_table()
    # main loop
    window_display_result.mainloop()


# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

# Title création
lbl_title_training = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title_training.grid(row=0, column=1, ipady=5, padx=40, pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex] = tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif")  # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex])  # put image on label
    albl_image[ex].grid(row=2 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 label per row
    albl_image[ex].bind("<Button-1>",
                        lambda event, ex=ex: exercise(event=None, exer=a_exercise[ex]))  # link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
btn_display.bind("<Button-1>", lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()

database.close_dbconnection()
