import tkinter as tk
from tkinter import *

def  main():
    
    #create the Tk root object.
    root = tk.Tk()
    
    root.geometry("800x600")
    

    #Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    
    frame.pack(fill=tk.BOTH, expand=1)

    #Create a canvas object that will drw into the frame 

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)
    canvas.configure(background=("white"))
    
    draw_scene(canvas, 0, 0, 799, 599)

    root.mainloop()
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
   
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    #canvas.create_oval(200, 300, 400, 400, fill = "#ff0000")
  

def draw_grid(canvas, left, top, right, bottom, grid_spacing):

    #When I put this varible I said information my value of margin
    text_horizontal_margin = 20
    text_vertical_margin = 15

    #draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        #the value of "i" começa no canto da janela, left é a direção

        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")


    #draw vertical lines
    for f in range(left, right, grid_spacing):
        canvas.create_line(f, top, f, bottom)
        canvas.create_text(f, top + text_vertical_margin, text=f'{f}')


main()    