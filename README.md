<!-- SpendWisePy - Expense Tracker Application -->

# SpendWisePy 📈💰
SpendWisePy is a simple expense tracker application that allows users to create and manage their expenses.

![Version](https://img.shields.io/github/release/felipealfonsog/SpendWisePy.svg?style=flat&color=blue)
![Main Language](https://img.shields.io/github/languages/top/felipealfonsog/SpendWisePy.svg?style=flat&color=blue)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<!--
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
-->

[![Vim Powered](https://img.shields.io/badge/Vim-Powered-%2311AB00.svg?logo=vim&logoColor=white)](https://www.vim.org)
[![VS Code Powered](https://img.shields.io/badge/VS%20Code-Powered-%23007ACC.svg?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

SpendWisePy is a simple and intuitive expense tracking application built in Python by Felipe Alfonso Gonzalez, a passionate Computer Science Engineer from Chile. 💻🚀
#### IMPORTANT NOTE
This open-source project comes with dual licensing options: MIT. In short words, feel free to use, modify, and distribute the software under these permissive licenses. However, if you utilize the source code or create a fork, please kindly attribute Felipe Alfonso Gonzalez as the original creator behind this expense management tool.

#### Features ✨🚀 

- Create, manage, and track your expenses effortlessly from the comfort of your terminal.
- Add expense details such as name, amount, description, and date.
- Update and delete expenses easily with a user-friendly interface.
- Filter expenses by date range to get better insights.
- Total expenses displayed for easy monitoring.
- User-friendly GUI powered by PyQt5.
- Supports multiple operating systems including Windows, macOS, and Linux.


#### Screenshot in macOS

<img src="./imgs/sshot-macos.jpg" alt="Screenshot" width="550" height="550">

#### Screenshot in Arch Linux

<img src="./imgs/sshot-arch.jpg" alt="Screenshot" width="550" height="550">


#### Prerequisites and notes

Before running SpendWisePy, make sure you have the following dependencies installed:

- Python 3
- Mysql
- "mysql-connector-python" for Python: Install using "pip install mysql-connector-python"
- To configure the credentials for Mysql, go to "models/database.py"
- PyQt5: Install PyQt5 library using pip:
- You can create an executable using "pyinstaller" (pip install pyinstaller): "pyinstaller --onefile spendwiseapp.py"

#### How to Use 🚀

1. Clone the repository using `git clone`.
2. Install the required dependencies with `pip install -r requirements.txt`.

   NOTE: If you are an Arch Linux user once you have installed Python and Pip, rename this file (Causes some ssues about pip's externally-managed-environment error):
   This is in:
   
   ```
   cd /usr/lib/python3.11/
   ```
   
   ```
   sudo mv EXTERNALLY-MANAGED EXTERNALLY-MANAGED.bak
   ```
   
4. Run the application using `python3 spendwiseapp.py`.
5. Start managing your expenses efficiently!

#### How to Run

1. Clone the SpendWisePy repository from GitHub.

2. Navigate to the project directory:

3. Run the main application script:

4. The SpendWisePy application will launch.

5. To exit the application, close the main window.

🛠️ Database
- SpendWisePy uses a custom database model. Make sure to include the appropriate model or adapt it for your needs.

#### Contributing

Contributions to this project are more than welcome! If you have any ideas, bug fixes, or new features to add, please feel free to open an issue or submit a pull request. Let's make SpendWisePy even better together! 🤝

🤝 If you'd like to contribute to SpendWisePy, please follow these steps:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

#### Contact

📧 For any questions or suggestions, feel free to contact the developer:
- Name: Felipe Alfonso Gonzalez
- Email: f.alfonso@res-ear.ch
- GitHub: [felipealfonsog](https://github.com/felipealfonsog)

#### Support

☕ If you find SpendWisePy helpful, consider supporting the project with a cup of coffee:

- [![Sponsor on Paypal](https://img.shields.io/badge/Sponsor%20on-Paypal-blue)](https://paypal.me/felipealfonsog)
- [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-orange)](https://www.buymeacoffee.com/felipealfonsog)
- [![Sponsor on GitHub](https://img.shields.io/badge/Sponsor%20on-GitHub-green)](https://github.com/sponsors/felipealfonsog)


🙏 Your support is greatly appreciated!

---

Happy expense tracking! 📊💸


