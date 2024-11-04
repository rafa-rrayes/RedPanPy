from RedPanPy import RedPanPyApp

def main():
    app = RedPanPyApp("/Users/Rafa/Python/RedPanPy/plotter.html")

    tasks = []

    def add_task():
        def handle_input(task_text):
            if task_text.strip() == "":
                return  # Do not add empty tasks
            tasks.append({'text': task_text, 'completed': False})
            update_task_list()
            # Clear the input field
            app.set_element_value("taskInput", "")
        app.get_element_value("taskInput", handle_input)

    def update_task_list():
        # Generate HTML for the task list
        html = ""
        for index, task in enumerate(tasks):
            task_id = f"task_{index}"
            remove_button_id = f"remove_{index}"
            task_class = "completed" if task['completed'] else ""
            html += f'''
            <li id="{task_id}" class="{task_class}">
                <span>{task["text"]}</span>
                <span>
                    <button id="{remove_button_id}" class="removeButton">Remove</button>
                </span>
            </li>
            '''
        app.set_element_text("taskList", html)
        # Bind events to the new tasks and remove buttons
        for index, task in enumerate(tasks):
            task_id = f"task_{index}"
            remove_button_id = f"remove_{index}"
            # Bind click event to toggle task completion
            app.bind(task_id, "click", lambda idx=index: toggle_task(idx))
            # Bind click event to remove button
            app.bind(remove_button_id, "click", lambda idx=index: remove_task(idx))

    def toggle_task(index):
        tasks[index]['completed'] = not tasks[index]['completed']
        update_task_list()

    def remove_task(index):
        del tasks[index]
        update_task_list()

    # Bind the add button click event
    app.bind("addButton", "click", add_task)

    app.run()

if __name__ == "__main__":
    main()
