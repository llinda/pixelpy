import Tkinter as tk 
from PIL import Image, ImageTk
import tkSimpleDialog
import cfg

class LabelingApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=cfg.CANVAS_SIZE_WIDTH, height=cfg.CANVAS_SIZE_HEIGHT, cursor="cross")
        
        self.image_list = []
        self.completed = 0

        self.shape = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self._bind_keys()
        self._read_list()
        self._draw_image()

    def _bind_keys(self):
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        self.canvas.bind("<Return>", self.on_finish)

    def _read_list(self):
        try:
            with open(cfg.INPUT_FILE, 'r') as f:
                for line in f:
                    items = line.strip().split(cfg.DELIM)
                    self.image_list.append(items)
        except IOError:
            print "Input file {0} not found. Did you set up cfg.py properly?".format(cfg.INPUT_FILE)
            quit()

    def _draw_image(self):
        if self.image_list:
            try:
                self.im = Image.open(self.image_list[0][0])
                self.tk_im = ImageTk.PhotoImage(self.im)
                self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)
                self.wm_title("Label List: {0}".format(" ".join(self.image_list[0][1:])))
            except IOError:
                print "Image {0} not found. Aborting.".format(self.image_list[0][0])
                quit()
        else:
            print "Reached end of images. Exiting program."
            quit()

    def on_mouse_press(self, event):
        if self.shape:
            self.canvas.delete(self.shape)
        # save mouse drag start position
        self.end_x = None
        self.end_y = None
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle
        if cfg.SHAPE == "rectangle":
            self.shape = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline=cfg.SHAPE_COLOR)
        else:
            if cfg.SHAPE == "oval":
                self.shape = self.canvas.create_oval(self.x, self.y, 1, 1, outline=cfg.SHAPE_COLOR)
            else:
                print "Check config. Shape must be rectangle or oval."
                quit()

    def on_mouse_move(self, event):
        curX, curY = (event.x, event.y)
        self.end_x = curX
        self.end_y = curY
        # expand as you drag the mouse
        self.canvas.coords(self.shape, self.start_x, self.start_y, curX, curY)

    def on_mouse_release(self, event):
        self.canvas.focus_set()
        pass

    def on_finish(self, event):
        #A shape has been found
        if self.start_x and self.start_y and self.end_x and self.end_y:
            noun = tkSimpleDialog.askstring("Label Area", cfg.PROMPT)
            if noun: #user didn't hit cancel
                with open(cfg.OUTPUT_FILE, "a") as f:
                    f.write("{0}|{1}|{2}|{3}|{4}|{5}\n".format(self.image_list[0][0], noun, self.start_x, self.start_y, self.end_x, self.end_y))
                self.completed += 1
                if self.shape:
                    self.canvas.delete(self.shape)
        else:
            print "Nothing here to label..."
        if self.completed >= cfg.LABELS_PER_IMG:
            del(self.image_list[0])
            self.completed = 0
            self._draw_image()
            print "Success! Image labeled. Moving on."

if __name__ == "__main__":
    app = LabelingApp()
    app.mainloop()
