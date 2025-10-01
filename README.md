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
**cloud_based_inventory**
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

1. ### Clone the repository
  - **Github repository:** https://github.com/sej1306kook-ui/Cloud_based_Inventory
    
    -  **Or via terminal**
      
  - `git clone: https://github.com/sej1306kook-ui/Cloud_based_Inventory.git`
2.  ### Install dependencies:
  - `pip install -r requirements.txt`
3.  ### Run project:
  - `python main.py`
 
## Usage
1. Run the project: `python main.py`
2. when running for the first time, create an Admin account (required to manage the system).
3. **Admin can:**
      - Add, update, delete, and view users, products, customers, and sales
      - Generate daily sales reports
      - Check low stock alerts
      - View best-selling products
4. **Staff can:**
      - View products, customers, and sales
      - Logout/Exit from the main menu

## Real-World Applications
**This project demonstrates how an inventory management system can be used in real business scenarios:**

- **Retail Shops / Kirana stores :** Manage daily sales, track low-stock items, and identify best-selling products.
  
- **Pharmacies / Medical Store :** Keep records of medicines, monitor expiry/low stock, and generate daily reports.
 
- **Restaurants / Cafes:** Track menu items, sales, and ingredients stock levels.
 
- **Wholesale Businesses / Warehouses:** Manage large inventories, suppliers, and customer sales records.
 
- **E-commerce Sellers:** Maintain product listings, sales data, and ensure timely stock replenishment.

- **Event Management Companies:** Track inventory of event materials (decorations, equipment), manage clients (customers), and record sales of services/items.
  
## License
 **MIT License**

## Author
 **Sejal**
