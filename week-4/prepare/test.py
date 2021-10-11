import tkinter as tk
from tkinter import *
import math

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
    canvas.configure(background=("#9ACBFC"))
    
    draw_scene(canvas, 0, 0, 799, 599)
   
   # draw_pine_tree(canvas, 400, 300, 150)
    #draw_pine_tree(canvas, 700, 300, 150)


    root.mainloop()
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
   
    draw_cloud(canvas, 200, 100)
    draw_cloud(canvas, 55, 100)
    draw_cloud(canvas, 70, 50)

    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    
    tree_center = scene_left + 500
    tree_top = scene_top + 100 
    tree_height = 300
    draw_pine_tree (canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 700
    tree_top = scene_top + 100 
    tree_height = 300
    draw_pine_tree (canvas, tree_center, tree_top, tree_height)


    draw_sun(canvas, 100, 100)
    draw_pine_tree(canvas, 550, 300, 150)
    draw_pine_tree(canvas, 730, 300, 150)
    draw_lawn(canvas,500, 450)
    draw_lawn(canvas,600, 450)
    draw_lawn(canvas,700, 450)
    
    #canvas.create_oval(200, 250, 350, 100, fill = "white")
    
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

def draw_sun(canvas, sun_left, sun_top, scale=1):
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_lenght = 100 * scale
    ray_width = 3 * scale
    #I will use this argument to use in the range
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)



    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#fff7b4", width=False)
    
    for i in range(ray_count):
        """para dar toda a volta no circulo que é 360 graus, vamos 
        usar um Formula matematica onde ele vai dar a volta 
        multlicando o numero por ray_count,
        logo em seguida vai ser usada os algulos sen e con para completar
        a volta no circulo
        """
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_lenght
        ray_y = sun_center_y + math.sin(angle) * ray_lenght

        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y,  width =ray_width, fill="#FFF7BF")




def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

   

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom, trunk_right, trunk_bottom, outline = "gray20", width=1, fill="tan3")

    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_cloud(canvas, cloud_left, cloud_top):
    cloud_width = 300 
    cloud_height = 150
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height
   
    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, outline ="ghostWhite", fill="ghostWhite" )

def draw_lawn(canvas, lawn_left, lawn_top):
    lawn_width = 50
    lawn_higth = 5
    lawn_right =  lawn_left + lawn_width
    lawn_bottom = lawn_top + lawn_higth

    canvas.create_line(lawn_left, lawn_top, lawn_bottom, lawn_top,  fill="green")
main()    