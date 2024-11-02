# main.py

from pyhtmlgui2 import PyHtmlGuiApp

def main():
    # Initialize the GUI with the path to your HTML file
    app = PyHtmlGuiApp("/Users/Rafa/Python/RedPanPy/old/index.html")

    # Define a callback function for the button click
    def on_button_click():
        print("Button clicked!")
        app.set_element_text("text1", "Button was clicked!")
    def on_button_click2():
        print("Button 2 clicked!")
        app.set_element_text("text1", "Button 2 was clicked!")
    # Bind the click event of the button to the callback
    app.bind("myButton", "click", on_button_click)
    app.bind("myButton2", "click", on_button_click2)

    app.set_element_text('texto1', 'oiii')
    # Show the GUI window
    app.run()

if __name__ == "__main__":
    main()
