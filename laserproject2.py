import math
import tkinter as tk

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Stationary Laser Throw Distance Calculator")
# Set geometry(widthxheight)
root.geometry('800x400')

# Disable resizing of the window
root.resizable(False, False)

# Description of the application
# Long description text
description_text = """The purpose of this application is to be used for Track and Field throwing events to make measuring the distances of throws easier and faster. The application will be able to calculate the distance of the throw from where the laser is stationed, instead of going into the ring to measure it.

Follow these instructions to accurately measure the distance of a throw using your laser and this application:

1). Using the laser, shoot the distance from where the laser is stationed, to where the throw is released from, (Ex: the Discus Ring).

2). Enter the angle between where the throw is being released from (the throws ring), and where the throw landed in the field.

3). Using the laser, shoot the distance of where the implement landed in the field.

As soon as you use the laser to get the distance, the result will be displayed, and the entry field will reset.

The program is now ready to measure the next distance, and the distance to the ring will not change.
"""

# Create a text widget to display the long description
description_label = tk.Label(root, text=description_text, wraplength=425, justify="left")
description_label.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.NW)

entrys_frame = tk.Frame(root)
entrys_frame.pack(side=tk.TOP, padx=10)

# third label to third entry field
lbl3 = tk.Label(entrys_frame, text="1. Distance from laser to ring:")
lbl3.pack(anchor=tk.W)
# third entry third to first label
txt3 = tk.Entry(entrys_frame, width=15)
txt3.pack()
txt3.focus_set()

# second label to second entry field
lbl2 = tk.Label(entrys_frame, text="2. Enter angle:")
lbl2.pack(anchor=tk.W)
# second entry field to second label
txt2 = tk.Entry(entrys_frame, width=15)
txt2.pack()

# first label to first entry field
lbl1 = tk.Label(entrys_frame, text="3. Distance of throw:")
lbl1.pack(anchor=tk.W)
# first entry field to first label
txt1 = tk.Entry(entrys_frame, width=15)
txt1.pack()


# Text Displaying the results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# function to calculate total distance from three entry fields 
# button is clicked
def calculate(event=None):
    try:
        side1 = float(txt1.get())
        angle_degrees = float(txt2.get())
        side2 = float(txt3.get())

        # Convert side lengths from meters to unitless
        side1 /= 100
        side2 /= 100
        
        # Convert angle from degrees to radians
        angle_radians = math.radians(angle_degrees)
        
        # Law of cosines to find the third side
        side3_squared = side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle_radians)
        side3 = math.sqrt(side3_squared)
        
        # Law of sines to find angles
        angle1_radians = math.asin(side1 * math.sin(angle_radians) / side3)
        angle2_radians = math.asin(side2 * math.sin(angle_radians) / side3)
        angle3_radians = math.pi - angle1_radians - angle2_radians
        
        # Convert angles from radians to degrees
        angle1_degrees = math.degrees(angle1_radians)
        angle2_degrees = math.degrees(angle2_radians)
        angle3_degrees = math.degrees(angle3_radians)
        
        # Display results in meters
        result_text.set(f"Angle 1: {angle1_degrees:.2f} degrees\nAngle 2: {angle2_degrees:.2f} degrees\nAngle 3: {angle3_degrees:.2f} degrees\nDistance: {side3 * 100:.2f} meters")
        
        # Clear the first entry field
        txt1.delete(0, tk.END)
        # Set Entry Focus
        txt1.focus_set()
    except ValueError:
        result_text.set("Please enter valid numbers")

# Bind the <Return> key event to the root window
root.bind("<Return>", calculate)

# Execute Tkinter
root.mainloop()
