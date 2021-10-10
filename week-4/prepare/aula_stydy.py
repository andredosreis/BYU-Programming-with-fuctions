from tkinter import Scale, Tk, Canvas, Frame, BOTH

def main():
    root = Tk()
    
    #Scene()

    root.geometry("800x600")
    root.configure(background=('white'))
    #root.title("prove- week-04")
    root.mainloop()
    
"""
class Scene(Frame):

    def _init_ (self):

        super().__init__()
        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        draw_scene(canvas, 0, 0, 799, 599)
"""
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    
def draw_grid(canvas):
    canvas.create_line(0, 100, 799, 100)
    
main()