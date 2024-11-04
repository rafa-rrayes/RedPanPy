from RedPanPy import RedPanPyApp

def main():
    # Initialize the GUI with the path to your HTML file
    app = RedPanPyApp("/Examples/Calculator/calculator.html", title="Calculator", width=300, height=500)
    expression = {'value': ''}  # Using a dict to allow inner functions to modify the variable

    # Function to update the calculator display
    def update_display():
        app.set_element_value("display", expression['value'])

    # Callback factory for number buttons
    def on_number_click(num):
        def callback():
            expression['value'] += str(num)
            update_display()
        return callback

    # Callback factory for operator buttons
    def on_operator_click(op):
        def callback():
            if expression['value'] and expression['value'][-1] not in '+-*/':
                expression['value'] += op
                update_display()
        return callback

    # Callback for the clear button
    @app.bind("btnClear", "click")
    def on_clear_click():
        expression['value'] = ''
        update_display()
    # Callback for the equal button
    @app.bind("btnEqual", "click")
    def on_equal_click():
        try:
            # Evaluate the expression safely
            result = str(eval(expression['value']))
            expression['value'] = result
        except Exception:
            expression['value'] = 'Error'
        update_display()        
    # Bind number buttons (0-9)
    for num in range(0, 10):
        app.bind_specific(f"btn{num}", "click", on_number_click(num))

    # Bind operator buttons
    app.bind_specific("btnAdd", "click", on_operator_click('+'))
    app.bind_specific("btnSub", "click", on_operator_click('-'))
    app.bind_specific("btnMul", "click", on_operator_click('*'))
    app.bind_specific("btnDiv", "click", on_operator_click('/'))
    app.bind_specific("btnDot", "click", on_operator_click('.'))


    # Initialize the display
    update_display()

    # Run the application
    app.run()

if __name__ == "__main__":
    main()
