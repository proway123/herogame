from tkinter import Tk, ttk
from classes.main import GameAdmin

main_application = Tk()
main_application.title('The Hero Game')
main_application.geometry("500x800")

main_frame = ttk.Frame(main_application, padding=20)
main_frame.grid()

cell1 = GameAdmin(main_application, 50, 50)
cell1.draw_map()


main_application.mainloop()