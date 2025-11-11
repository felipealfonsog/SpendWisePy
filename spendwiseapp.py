# spendwiseapp.py
'''


▒█▀▀▀█ █▀▀█ █▀▀ █▀▀▄ █▀▀▄ ▒█░░▒█ ░▀░ █▀▀ █▀▀ ▒█▀▀█ █░░█ 
░▀▀▀▄▄ █░░█ █▀▀ █░░█ █░░█ ▒█▒█▒█ ▀█▀ ▀▀█ █▀▀ ▒█▄▄█ █▄▄█ 
▒█▄▄▄█ █▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▒█░░░ ▄▄▄█


*************************************************
SpendWisePy Expense Tracker Application
*************************************************
*  Simple: An expense tracking application to create and manage expenses.
*************************************************
* Developed and engineered by:
* Felipe Alfonso Gonzalez <f.alfonso@res-ear.ch>
* Computer Science Engineer
* Chile
*************************************************
* Prerequisites:
* - Python 3: Make sure you have Python 3 installed on your system.
* - PyQt5: Install PyQt5 library for the graphical user interface.
*   You can install it using pip: pip install pyqt5
* - Database model: The application uses a custom database model.
*   Make sure to include the appropriate model or adapt it for your needs.
*************************************************
* How to run the SpendWisePy application:
*
* 1. Clone the SpendWisePy repository from GitHub.
*
* 2. Navigate to the project directory:
*    cd SpendWisePy
*
* 3. Run the main application script:
*    python spendwiseapp.py
*
* 4. The SpendWisePy application will launch, allowing you to:
*    - Add expenses with name, amount, description, and date.
*    - Update and delete existing expenses.
*    - Filter expenses based on a specific date range.
*
* 5. To exit the application, close the main window.
*
*************************************************
* Important Notes:
* - The application has been tested on Linux and macOS.
* - For Windows, additional configurations may be required.
* - Make sure to fulfill the prerequisites before running the application.
* - The database model may need to be adjusted to match your database setup.
* - For more information, please refer to the project documentation.
*************************************************
'''

import sys
from PyQt5.QtWidgets import QApplication
from views.gui import SpendWiseApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpendWiseApp()
    window.show()
    sys.exit(app.exec_())
