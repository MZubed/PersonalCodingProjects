# zubed-mini-project

### **MINI PROJECT 1: SHOP MANAGEMENT SYSTEM**

Introduction: Hello, this is my first coding project which I have able to program over the course of 6 weeks thanks to the Data Engineering Bootcamp run by Generation UK. It is an application which uses a command line interface for a shop to keep track of customer orders, products and couriers.

### **INSTRUCTIONS TO ACCESSING MY PYTHON MINI PROJECT:**

Download and install the latest version of Python. Make sure to add Python to path during installation.  Once the download is finished, check if python has been installed by opening  your computer's terminal from the searchbar on your computer. For Windows, this is Windows Powershell and for Linux and Mac this is Terminal. Then for Mac and Linux users type 'python3 --version',  it should display something similar to 'Python 3.x.x'. For Windows users type 'python --version' and if that doesn't work type 'python3 --version' as before and it will display the same results. If not then this means Python has not been installed and you willl have to go through the installation process again.

Install Visual Studio Code and check if it has been installed by looking at your downloads. Once finished installing, open Visual Studio Code and go into the Extensions view by clicking the square icon on the left sidebar. Search for the Python extension and install Python.

Afterwards, make sure to download the week1 folders which contains the following: couriers.txt, orders.txt, products.txt, app.py, testapp.py, and products.py. Go to VSCode, click on File in the top left corner and click Open folder. Go to your downloads section and select the 'week1' folder. Click Open Folder to open it in VSCode which should now allow you to run the program by clicking the run icon in the top right corner.

### **FEATURES OF MY APP:**

###### MENU OPTIONS:

* Used **\n** to print menu options on separate lines for clarity and to organize **functions**.
* Created main menu options and submenus for products, couriers, and orders.
* Allows users to select options using **input()** combined with **if** and **else** statements to navigate defined functions.
* Implemented error handling using try and except to account for input errors.
  * Provided specific error messages, e.g., differentiating between selecting a number outside of the range of the function and entering a string input.
* Ensured the menu runs continuously using while loops until the user exits the app.

###### PRODUCTS, COURIERS AND ORDERS FUNCTIONS:

* Displayed items in a vertical list with their indexes using a **for** loop and **.index** function.
* Created Products, Couriers, and Orders using **dictionaries** and added them to lists with **append().**
* Updated items by showing the list along with their index for user selection and modifying dictionary keys based on input.
* Deleted items by displaying them in a list, allowing the user to select via index what items they wish to delete, and removing them using the **del** function.
* Implemented error handling using try and except to account for input errors.
  * Provided specific error messages, e.g., differentiating between string input for phone numbers and integer inputs for customer name.

###### PRODUCTS, COURIERS AND ORDERS CSV FILES:

* Created files for Products, Couriers and Orders to persist data from the program.
* Used the csv module, to store and load **dictionaries**.
* Can load data from the text files into dictionaries using **DictReader.**
* Ensured any changes made to lists is saved upon exiting the app.
* Able to save the dictionaries in the respective files using **DictWriter()** along with their keys as headings using **fieldnames** and separating the items using **newline**.

### MY MINI PROJECT CODING JOURNEY:

The below information details my progression of my mini project week by week which leads back to the current stage of my mini project.

* During week 1, we learnt about the fundamentals of lists. This week's requirements of our mini projects were to build a menu with options to print,create,update, and delete products in a products list. This week's implementations were the most satisfying as this marked the start of my coding journey and demonstrates the most progress of my coding knowledge.
* During week 2, we learnt about the fundamentals of dictionaries. This week's requirements were to build another menu with options to print,create,update, and delete orders within a dictionary and to append them to an orders list.
* During week 3, we learnt about storing our data into text files. This week's requirements were to save and load our data to and from the couriers and products text file. This also included the couriers list manipulation as according to above.
* During week 4, we learnt abour data persistence using the csv module. This week's requirements were to save and load data from the products, couriers and data text files into dictonaries. I am currently at this stage and refining this week's requirements.
* During week 5, we learnt about databases using SQL. This week's requirements were to save and load our couriers and products data to and from database tables. This is currently a work in progress.

### **PROJECT REFLECTIONS:**

This has been made possible because of the teachers at Generation UK who have been a massive help to me on meeting the project requirements as well as boosting me on my coding journey. If I had more time on my project, I would choose to add more error handling for even more situations as well as implementing the week 5 requirements. I would also like to add many more unit tests for separate functions in my programs as well as different files to import my functions from.
