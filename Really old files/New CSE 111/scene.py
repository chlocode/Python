# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_oval(canvas, 100,100, 300, 200, fill="white")


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4, scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height ):
    draw_rectangle( canvas, 0, 0, scene_width, scene_height / 4, width=0, fill="tan4" )

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # Draw another pine tree.
    tree_center_x = 250
    tree_bottom = 70
    tree_height = 220
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # right side middle pine tree.
    tree_center_x = 665
    tree_bottom = 90
    tree_height = 200
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # right side first pine tree.
    tree_center_x = 600
    tree_bottom = 70
    tree_height = 220
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # right side left pine tree.
    tree_center_x = 730
    tree_bottom = 70
    tree_height = 220
    draw_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_tree(canvas, center_x, bottom, height):
    trunk_width= height / 10
    trunk_height= height / 8
    trunk_left= center_x - trunk_width / 2
    trunk_right= center_x + trunk_width / 2
    trunk_top= bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

#def draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill=""):
    

# Call the main function so that
# this program will start executing.
main()