import Tkinter as tk 
from PIL import Image, ImageTk
import tkSimpleDialog
import cfg  #Personal config file

class LabelingApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.frame = tk.Frame(self, width=cfg.WINDOW_SIZE_WIDTH, height=cfg.WINDOW_SIZE_HEIGHT)
        self.canvas = tk.Canvas(self.frame, width=cfg.WINDOW_SIZE_WIDTH, height=cfg.WINDOW_SIZE_HEIGHT, scrollregion=(0,0,cfg.CANVAS_SIZE_WIDTH, cfg.CANVAS_SIZE_HEIGHT), cursor="cross")
        
        self.image_list = []
        self.completed = 0

        self.shape = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self._setup_scroll()
        self._bind_keys()
        self._read_list()
        self._draw_image()

    def _setup_scroll(self):
        self.frame.pack()
        hbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM,fill=tk.X)
        hbar.config(command=self.canvas.xview)
        vbar=tk.Scrollbar(self.frame,orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT,fill=tk.Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

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

    def _normalize_coordinates(self):
        '''Normalizes in case the user drags from bottom-right to top-left. Also prevents dragging to pixels outside the image.
        '''
        if self.start_x > self.end_x and self.start_y > self.end_y:
            ((self.start_x, self.start_y), (self.end_x, self.end_y)) = ((self.end_x, self.end_y), (self.start_x, self.start_y)) 
        if self.start_x < 0:
            self.start_x = 0
        if self.start_y < 0:
            self.start_y = 0
        if self.end_x > self.tk_im.width():
            self.end_x = self.tk_im.width()
        if self.end_y > self.tk_im.height():
            self.end_y = self.tk_im.height()

    def _draw_image(self):
        if self.image_list:
            try:
                self.im = Image.open(self.image_list[0][0])
                self.tk_im = ImageTk.PhotoImage(self.im)
                self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)
                self.wm_title("Instructions: {0}".format(" ".join(self.image_list[0][1:])))
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
        c = event.widget
        self.start_x = c.canvasx(event.x)
        self.start_y = c.canvasy(event.y)

        # create shape 
        if cfg.SHAPE == "rectangle":
            self.shape = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline=cfg.SHAPE_COLOR)
        else:
            if cfg.SHAPE == "oval":
                self.shape = self.canvas.create_oval(self.x, self.y, 1, 1, outline=cfg.SHAPE_COLOR)
            else:
                print "Check config. Shape must be rectangle or oval."
                quit()

    def on_mouse_move(self, event):
        #http://stackoverflow.com/questions/24135170/drawing-rectangle-using-mouse-events-in-tkinter for sections drag-drop behavior of shapes
        curX, curY = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
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
            self._normalize_coordinates()
            noun = tkSimpleDialog.askstring("Label Area", cfg.PROMPT)
            if noun: #user didn't hit cancel
                with open(cfg.OUTPUT_FILE, "a") as f:
                    f.write("{0}|{1}|{2}|{3}|{4}|{5}\n".format(self.image_list[0][0], noun, self.start_x, self.start_y, self.end_x, self.end_y))
                    print "{0}, {1}, {2}, {3} written to {4}".format(self.start_x, self.start_y, self.end_x, self.end_y, cfg.OUTPUT_FILE)
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
