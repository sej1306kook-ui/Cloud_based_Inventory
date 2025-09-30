# Cloud Inventory & Sales Management 
Python + MongoDB CLI project for managing products, customers, users, and sales.

## Features
- Manage products: add, update, delete, view
- Manage customers: add, update, delete, view
- Manage sales: add, update, delete, view
- Manage users: add, update, delete, view
- User authentication (Admin & Staff)
- Sales tracking & reporting
- Low-stock alerts
- Total sales calculation for today
- Best-selling product identification
- Error handling for invalid IDs and database issues
- Formatted CLI output for readability

## Tech Stack
- **Language:** Python 3.12.10
- **Database:** MongoDB Atlas
- **Libraries/Modules:** 
  - `pymongo`
  - `bcrypt`
  - `bson`
  - `datetime`
  - `traceback`
  - `re`

## Project Structure
cloud_based_inventory
- **db.py** : MongoDB connection setup
- **product.py** : Functions to manage products
- **customers.py** : Functions to manage customers
- **users.py** : Functions to manage user accounts & authentication
- **sales.py** : Functions to manage sales and reports
- **utils.py** : Helper functions 
- **main.py** : Main CLI interface to run the app
- **README.md** : Project documentation
- **requirements.txt** : List of dependencies to install
  
## Setup
- Clone repo
   **git clone:** https://github.com/sej1306kook-ui/Cloud_based_Inventory/tree/main
- **Install dependencies:**
   `pip install -r requirements.txt`
- **Run project:**
   `python main.py`
 
## Usage
- Run the project: `python main.py`
- Login as admin (create first admin account if not exists)
    - **Admin can:**
      - Add/update/delete/view users, products, customers, sales
      - Generate daily sales report, check low stocks and best-selling products
    - **Staff can:**
        - View products, customers, sales
- Exit app from main menu


## License
 **MIT License**

## Author
 **Sejal**
