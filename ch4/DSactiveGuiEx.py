# created by deepseek
#!/usr/bin/python3
"""
Simple Graphics Program using Tkinter.
Allows drawing rectangles with left-click and typing text at clicked positions.
"""

from tkinter import *

class SimpleGraphics:
    """A simple graphics application with rectangle and text capabilities."""
    
    def __init__(self, root, canvas):
        """Initialize the graphics application."""
        # State variables
        self.leftPoint = None      # First corner of rectangle
        self.rightPoint = None     # Second corner of rectangle
        self.mouseClick = None     # Position for text insertion
        
        # Setup GUI
        self.root = root
        self.canvas = canvas
        root.title("My Graphics")
        
        # Bind events
        canvas.bind("<Button-1>", self.handleLeftClick)
        canvas.bind("<Button-3>", self.drawRectangle)  # Right-click for rectangles
        canvas.pack()
        
        root.bind("<Key>", self.drawText)
    
    def handleLeftClick(self, event):
        """Handle left-click: set text position and optionally draw rectangle."""
        self.mouseClick = event
        # Uncomment below to also draw rectangle on left click
        # self.drawRectangle(event)
    
    def drawText(self, event):
        """Draw the pressed key at the last clicked position."""
        if self.mouseClick is not None:
            self.canvas.create_text(
                self.mouseClick.x, 
                self.mouseClick.y, 
                text=event.keysym
            )
            self.mouseClick.x += 6  # Move cursor for next letter
        else:
            # Default position if no click has been made
            self.canvas.create_text(100, 100, text=event.keysym)
    
    def drawRectangle(self, event):
        """Draw a rectangle using two clicks as opposite corners."""
        if self.leftPoint is None:
            self.leftPoint = event
        elif self.rightPoint is None:
            self.rightPoint = event
        
        # If both points are set, draw and reset
        if self.leftPoint is not None and self.rightPoint is not None:
            self.canvas.create_rectangle(
                self.leftPoint.x, self.leftPoint.y,
                self.rightPoint.x, self.rightPoint.y,
                outline="black",
                width=2
            )
            # Reset for next rectangle
            self.leftPoint = None
            self.rightPoint = None

# Main execution
""" my note: We use this and we basically ask ' am i being run directly or am i being imported?'
if ran directly, this file would do everything. if imported, it would do everything above the below.
This lets us test code that only runs when i run the file directly, and lets it be reusable. """
if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=600, height=400, bg="white")
    app = SimpleGraphics(root, canvas)
    root.mainloop() # sits and waits for events to happen until exit
