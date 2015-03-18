#Controls the size of the window. Should be at least as large as your largest image.
WINDOW_SIZE_WIDTH = 700
WINDOW_SIZE_HEIGHT = 500
CANVAS_SIZE_WIDTH = 1024
CANVAS_SIZE_HEIGHT = 768

#Input file - each line should be image_location|Instructions
#Instruction will show up in header of window
INPUT_FILE = "sample/image_list.txt"
DELIM = "|"

LABELS_PER_IMG = 2 #How many areas will be labeled in each image?
SHAPE = "rectangle" #What shapes are we drawing? Can be rectangle or oval
SHAPE_COLOR = "blue"

#Output 
OUTPUT_FILE = "sample/output.txt"

#Prompt to show up after an image is labeled
PROMPT = "What did you just label?"
