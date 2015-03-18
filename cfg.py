#Controls the size of the window. Should be at least as large as your largest image.
CANVAS_SIZE_WIDTH = 1024
CANVAS_SIZE_HEIGHT = 768

#Input file - each line should be image_location|Instructions
#Instruction will show up in header of window
INPUT_FILE = "sample/image_list.txt"
DELIM = "|"

LABELS_PER_IMG = 2 #How many areas will be labeled in each image?
SHAPE = "rectangle" #What shapes are we drawing?
SHAPE_COLOR = "blue"

#Output 
OUTPUT_FILE = "sample/output.txt"

#Prompt to show up after an image is labeled
PROMPT = "What did you just label?"
