# main.py

from redpanpy import RedPanPyApp

def main():
    # Initialize the GUI with the path to your HTML file
    app = RedPanPyApp("/Users/Rafa/Python/RedPanPy/index.html")

    # Define a callback function for the button click
    def on_button_click():
        print("Button clicked!")
        app.set_element_text("text1", "Button was clicked!")
    def on_button_click2():
        app.get_element_text("text1")
        
    # Bind the click event of the button to the callback
    app.bind("myButton", "click", on_button_click)
    app.bind("myButton2", "click", on_button_click2)

    app.set_element_text('texto1', 'oiii')
    # Show the GUI window
    app.run()

if __name__ == "__main__":
    main()
