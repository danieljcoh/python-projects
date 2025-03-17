# Project 6: Temperature Converter (Tkinter Version)

**Objective**: Create a graphical application that converts temperatures between Celsius and Fahrenheit, with input fields, buttons, and a result display.

## Basic Knowledge Needed
- **Programming Language**: Python
  - Version: Python 3.x (e.g., 3.11 as of March 2025)
- **Concepts**:
  - Variables: Store temperature values and conversion results
  - GUI Basics: Create windows, widgets (labels, entries, buttons), and handle events
  - Conditionals: Determine conversion direction (C to F or F to C)
  - Arithmetic: Apply conversion formulas
  - Numbers: Use floats for temperature values
  - Event-Driven Programming: Respond to button clicks

## Stack
- **Environment**:
  - Text editor (e.g., VS Code) or Python IDE (e.g., PyCharm, IDLE)
  - Python interpreter with Tkinter installed (comes with standard Python)
- **Runtime**: Graphical window (not a console)

## Modules/Packages
- **Built-in Python Modules**:
  - `tkinter`: Python’s standard GUI library
- **Tkinter Components**:
  - `Tk()`: Creates the main window
    - Returns: Root window object
  - `Label`: Displays static text (e.g., "Enter Temperature")
    - Args: Parent (window), `text` (string)
  - `Entry`: Text input field for the temperature
    - Args: Parent (window); use `.get()` to retrieve input as string
  - `Button`: Clickable button to trigger conversion
    - Args: Parent (window), `text` (label), `command` (function to call)
  - `StringVar` (optional): Links a variable to a widget for dynamic updates
    - Methods: `.set()` (update value), `.get()` (retrieve value)
- **Functions**:
  - `float()`: Convert Entry input (string) to a number
    - Args: String (e.g., "25.5")
  - `round()` (optional): Control decimal places in output
    - Args: Number, places (e.g., `round(32.56, 1)` → 32.6)
  - `.mainloop()`: Runs the Tkinter event loop (called on the root window)

## Logic
- **Flow**:
  - Create a window with:
    - Label: "Enter Temperature"
    - Entry field: For user to type temperature
    - Two buttons: "C to F" and "F to C"
    - Label: To display the result (e.g., "Result: 77.0°F")
  - When a button is clicked:
    - Get the temperature from the Entry field
    - Apply the formula based on the button:
      - C to F: °F = (°C × 9/5) + 32
      - F to C: °C = (°F - 32) × 5/9
    - Update the result label with the converted value
- **Structure**:
  - Main window with widget layout (e.g., grid or pack system)
  - Two functions: One for C-to-F, one for F-to-C, triggered by buttons
  - Event-driven: Code runs when buttons are clicked, not sequentially
- **Key Ideas**:
  - GUI Layout: Arrange widgets visually (e.g., using `.grid(row, column)`)
  - Input Handling: Convert Entry text to float for calculation
  - Output Display: Update a Label or StringVar with the result
  - Event Binding: Link buttons to conversion logic

## Example Interface
- Window titled "Temperature Converter"
- Layout:
  - "Enter Temperature" [Entry field]
  - [C to F Button] [F to C Button]
  - "Result: [converted value]"
- Behavior: Type "25" in the Entry, click "C to F", see "Result: 77.0°F"