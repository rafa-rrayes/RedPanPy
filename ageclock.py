from redpanpy import RedPanPyApp
from PyQt5.QtCore import QTimer
from datetime import datetime

def main():
    app = RedPanPyApp("/Users/Rafa/Python/RedPanPy/ageclock.html")

    def get_age_in_years(birthdate):
        now = datetime.now()

        years_difference = now.year - birthdate.year
        birthday_this_year = datetime(now.year, birthdate.month, birthdate.day)

        if now < birthday_this_year:
            age = years_difference - 1
        else:
            age = years_difference

        milliseconds_in_year = 31557600000  # Average milliseconds in a year (including leap years)

        if now < birthday_this_year:
            last_birthday = datetime(now.year - 1, birthdate.month, birthdate.day)
        else:
            last_birthday = birthday_this_year

        milliseconds_since_last_birthday = (now - last_birthday).total_seconds() * 1000
        fractional_year = milliseconds_since_last_birthday / milliseconds_in_year

        return age + fractional_year

    def update_age_display():
        def callback(birthdate_value):
            if birthdate_value:
                try:
                    birthdate_obj = datetime.strptime(birthdate_value, '%Y-%m-%d')
                    age = get_age_in_years(birthdate_obj)
                    age_str = f"You are exactly <br> {age:.9f} <br> Years old"
                    app.set_element_text('age', age_str)
                except ValueError:
                    app.set_element_text('age', 'Invalid birthdate')
            else:
                app.set_element_text('age', 'Please enter birthdate')
        app.get_element_value('birthdate', callback)

    def on_birthdate_input():
        update_age_display()
        # Start a timer to update every 50 milliseconds
        if not hasattr(app, 'age_timer_started') or not app.age_timer_started:
            app.age_timer_started = True
            app.age_timer = QTimer()
            app.age_timer.timeout.connect(update_age_display)
            app.age_timer.start(50)

    # Bind the 'input' event of the 'birthdate' element
    app.bind('birthdate', 'input', on_birthdate_input)

    # Run the application
    app.run()

if __name__ == "__main__":
    main()