# What the project does:

This project reads monthly sales Excel files and checks if any salesperson exceeded $55,000 in sales. If someone hits the target, the system automatically sends an SMS with the salesperson's name and sales amount.

## Required libraries:

The project uses **`panda`** to read Excel files, **`openpyxl`** as the Excel engine, **`os`** to handle file paths, and **`twilio`** to send SMS messages.

## How to run:

To run the project, install the libraries with **`pip install pandas openpyxl twilio`**. Then, set your file paths and Twilio credentials, and run the Python script. It reads the files and sends SMS notifications for sales that hit the target.

