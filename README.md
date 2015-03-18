#pixelpy
PixelPy is a tool that makes it easier to label pixel coordinates of areas in images. This was written 
specifically to label items within visual scenes for an eyetracking experiment. Basically, it lets you draw a rectangle 
or oval directly onto an image and outputs the coordinates of the shape to an output file. 

Hopefully it'll make your life easier. 

##Configuration
Before you can use PixelPy, you have to configure it to work the way you want.
This is super easy to do, and I've included a sample
configuration file that works with the included sample (cfg.py). You'll want to change the config file slightly
so that it uses the images and instructions that you want for your task.

##Usage

I've included a fully working sample to get you started:

```python pixelpy.py```

This will open up a separate GUI window. Instructions for each images are shown in the window header.

![Separate window](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample1.png)

By clicking and dragging, you can draw a rectangle or oval in whatever color you want (depending on your configuration). Coordinates won't be saved unless you
press Enter, so keep drawing until you draw around the area you want.

![Drag and click](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample2.png)

Press Enter to save the coordinates (upper left, bottom right) of the shape that you drew. Label it so you can remember what you labeled.

![Drag and click](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample3.png)

The program will automatically move on to the next image once you've labeled as many areas as specified in the config.

##Output Format
Output is appended to the output file in the format:
`filename|label|upper_left_x_coordinate|upper_left_y_coordinate|bottom_right_x_coordinate|bottom_right_y_coordinate`

##Features
- Label as many images as you want
- Label as many sections within the images as you want
- Label as rectangles or ovals
- Instructions can be different for each image
- Saves coordinate information in computer-readable format

##Disclaimer
Not sure how easy or difficult this would be to get working on a windows computer. 
There's also no memory component of this program -- it will NOT remember whether you have already labeled part or all of an image. If you stop halfway, you'll have to remember it yourself for now. 
