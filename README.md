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
- db.py
- product.py
- customers.py
- users.py
- sales.py
- utils.py
- main.py
- README.md
- requirements.txt
  
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
      - Generate daily sales report and check best-selling products
    - **Staff can:**
        - View products, customers, sales
- Exit app from main menu


## License
MIT License

## Author
Sejal
