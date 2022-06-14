from tkinter import Canvas, Tk
from main import Main, VERY_EASY, EASY, MEDIUM

main = Main(MEDIUM)
main.resolve_kakuro()

grid = main.grid

N = len(grid)

root = Tk()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
X = WIDTH / N
Y = HEIGHT / N + 50
OFFSET = WIDTH / 4
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
root.title("Resolver")

canvas = Canvas(root, background="white", width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(OFFSET, 0, OFFSET + X * N / 2,  Y * N / 2, fill="black") # avoid creating black squares, creates one black square with the size of the puzzle
for i in range(N):
    for j in range(N):
        if len(grid[j][i]) == 1:
            canvas.create_rectangle(OFFSET + X * i / 2,  Y * j / 2, OFFSET + X * (i + 1) / 2,  Y * (j + 1) / 2, fill="white")
            text = grid[j][i]
            canvas.create_text(12 * OFFSET / 11 + X * i / 2, Y * j / 2 + Y / 8, text=text, fill="black", width="50", font=('Helvetica','20','bold'))
        elif len(grid[j][i]) > 2:
            text = grid[j][i].split('/')
            if text[0] != '0' and text[1] == '0': # down
                canvas.create_polygon(OFFSET + X * i / 2,  Y * j / 2, OFFSET + X * i / 2,  Y * (j + 1) / 2, OFFSET + X * (i + 1) / 2,  Y * (j + 1) / 2, fill="gray", outline="black")
                canvas.create_text(17 * OFFSET / 16 + X * i / 2, Y * j / 2 + Y / 3, text=text[0], fill="white", width="50", font=('Helvetica','15','bold'))
            elif text[0] == '0' and text[1] != '0': # right
                canvas.create_polygon(OFFSET + X * i / 2,  Y * j / 2, OFFSET + X * (i + 1) / 2,  Y * j / 2, OFFSET + X * (i + 1) / 2,  Y * (j + 1) / 2, fill="gray", outline="black")
                canvas.create_text(10 * OFFSET / 9 + X * i / 2, Y * j / 2 + Y / 6, text=text[1], fill="white", width="50", font=('Helvetica','15','bold'))
            elif text[0] != '0' and text[1] != '0': # down and right
                canvas.create_polygon(OFFSET + X * i / 2,  Y * j / 2, OFFSET + X * i / 2,  Y * (j + 1) / 2, OFFSET + X * (i + 1) / 2,  Y * (j + 1) / 2, fill="gray", outline="black")
                canvas.create_text(17 * OFFSET / 16 + X * i / 2, Y * j / 2 + Y / 3, text=text[0], fill="white", width="50", font=('Helvetica','15','bold'))
                canvas.create_polygon(OFFSET + X * i / 2,  Y * j / 2, OFFSET + X * (i + 1) / 2,  Y * j / 2, OFFSET + X * (i + 1) / 2,  Y * (j + 1) / 2, fill="gray", outline="black")
                canvas.create_text(10 * OFFSET / 9 + X * i / 2, Y * j / 2 + Y / 6, text=text[1], fill="white", width="50", font=('Helvetica','15','bold'))

root.mainloop()