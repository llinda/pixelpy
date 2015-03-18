#pixelpy
PixelPy is a tool to make it easier to label pixel coordinates of areas in images. This was written specifically to label 
the positions of items within visual scenes so that this data could then be used to configure an eyetracking experiment.

##Configuration
Before you can use PixelPy, you have to figure configure it to work with the directories you want. It's pretty easy to configure... I've included a sample
configuration file that works with the included sample.

##Usage

```python pixelpy.py```

This will open up a separate GUI window. Instructions for each images are shown in the window header.
![Separate window](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample1.png)

By clicking and dragging, you can draw a rectangle or oval in whatever color you want (depending on your configuration). Coordinates won't be saved unless you
press Enter, so keep drawing until you draw around the area you want.
![Drag and click](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample2.png)

Press Enter to save the coordinates (upper left, bottom right) of the shape that you drew. Label it so you can remember what you labeled.
![Drag and click](https://raw.githubusercontent.com/llinda/pixelpy/master/screenshots/pixelpy_sample3.png)

##Output
Output is appended to the output file in the format:
`filename|label|upper_left_x_coordinate|upper_left_y_coordinate|bottom_right_x_coordinate|bottom_right_y_coordinate`




