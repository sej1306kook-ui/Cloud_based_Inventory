from db import collection_1, collection_2, collection_3, collection_4
from pymongo.errors import PyMongoError
import re
from bson.errors import InvalidId
import bcrypt
import traceback

def top():
    print("\n"+"*"*100)

def bottom():
    print("*"*100+"\n")     

def is_valid():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[A-Za-z]{2,}$'
    while True :
        email = input("Enter the email: ")
        if re.match(pattern, email):
            return email
        else :
            print("Invalid email! Please Try again!")

def top1():
    print("\n"+"="*100)
def bottom1():
    print("="*100+"\n")

def valid_quantity():
    while True:
        try: 
            value  = int(input("Enter the quantity: "))
            if value <= 0 :
                top1()
                print("quantity must be a positive integer!")
                bottom1()
                continue
            else :
                return value
        except ValueError as e :
            top()
            print(f"ValueError: {e}")
            bottom()

def valid_price():
    while True:
        user_input = input("Enter the price: ")
        try:
            price = float(user_input.replace(',', ''))
            if price <= 0 :
                top()
                print("Price must be greater than 0")
                bottom()
                continue
            else :
                return price
            
        except ValueError:
            top()
            print("Invalid input!")
            bottom()


def error_handling(err):
    if isinstance(err, InvalidId):
        top()
        print("Invalid Id! Please enter a valid Id")
        bottom()
    elif isinstance(err, PyMongoError):
        top()
        print(f"Database Error: {err}")
        bottom()
    else:
        top()
        print(f"unexpected Error: {err}")
        traceback.print_exc()
        bottom()


def unique_prod_id():
    while True:
        try :
            prod_id = input("Enter the product id: ")
            if collection_1.find_one({'product_id':prod_id}):
                top1()
                print("This product id is already existed!")
                bottom1()
                continue
            else :
                return prod_id
            
        except Exception as e :
            error_handling(e)


def valid_cust_id():
    while True:
        try:
            cust_id = input("Enter the customer id: ")
            if collection_2.find_one({"customer_id": cust_id}):
                top1()
                print("This customer already exists!")
                bottom1()
                continue
            else :
                return cust_id
            
        except Exception as e :
            error_handling(e)


def valid_name():
    while True:
        name = input("Enter the name: ")
        try :
            if name.isdigit():
                top1()
                print("name can't be a number!")
                bottom1()
                continue
            else :
                return name
        except Exception as e :
            error_handling(e)


def unique_sales_id():
    while True:
        try :
            sal_id = input("Enter the sales id: ")
            if collection_4.find_one({"sales_id": sal_id}):
                top1()
                print("This sales id is already existed!")
                bottom1()
                continue
            else :
                return sal_id
        
        except Exception as e :
            error_handling(e)


def matched_prod_id():
    while True :
        try :
            match_prod_id = input("Enter the product id: ")
            user1 = collection_1.find_one({"product_id": match_prod_id})
            if not user1:
                top()
                print("This product id doesn't exist!")
                bottom()
                continue
            else:
                return match_prod_id
        
        except Exception as e :
            error_handling(e)


def matched_cust_id():
    while True :
        try :
            match_cust_id = input("Enter the customer id: ")
            if not collection_2.find_one({"customer_id": match_cust_id}):
                top1()
                print("This customer doesn't exist!")
                bottom1()
                continue
            return match_cust_id
        
        except Exception as e :
            error_handling(e)


def input_username():
    while True :
        try :
            username = input("Enter username: ")

            if len(username) < 3:
                top()
                print("Minimum length is 3!")
                bottom()
                continue
            elif len(username) > 16:
                top()
                print("Maximum length is 16!")
                bottom()
                continue
            elif " " in username:
                top()
                print("Spaces are not allowed!")
                bottom()
                continue
            else :
                return username

        except Exception as e :
            error_handling(e)


def input_email():
    while True:
        try :
            email1 = is_valid()

            if email1:
                return email1
            
        except Exception as e :
            error_handling(e)


def input_password():
    while True :
        try :
            passw = input("Enter password: ")
            if len(passw) < 4:
                top()
                print("Password minimum length is 4 characters!")
                bottom()
            elif len(passw) > 12:
                top()
                print("Password maximum length is 12 characters!")
                bottom()
            else :
                password = passw.encode('utf-8')

                hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                return hashed

        except Exception as e :
            error_handling(e)


def input_role():
    while True:
        try :
            role = input("Enter role(admin/staff): ")
            if role != 'admin' and role != 'staff':
                top()
                print("please enter a valid role!")
                bottom()
                continue
            else :
                return role
            
        except Exception as e :
            error_handling(e)


def error_handling(err):
    if isinstance(err, InvalidId):
        top()
        print("Invalid Id! Please enter a valid Id")
        bottom()
    elif isinstance(err, PyMongoError):
        top()
        print(f"Database Error: {err}")
        bottom()
    else:
        top()
        print(f"unexpected Error: {err}")
        traceback.print_exc()
        bottom()


def unique_username():
    while True:
        username1 = input_username()
        if collection_3.find_one({"username": username1}):
            top()
            print("This username is already existed!")
            bottom()
            continue
        else: 
            return username1


def unique_emails():           
    while True:
        email2 = input_email()
        if collection_3.find_one({"email": email2}):
            top()
            print("This email already exists!")
            bottom()
            continue
        else :
            return email2

      
# checking usernames for update user
def check_username(target_id): 
    try: 
        
        while True:                  
            username_up = input_username()
            if collection_3.find_one({"username": username_up, "_id":{"$ne": target_id} }):
                top()
                print("This username is already taken!")
                bottom()
                continue
            else:
                return username_up
    except Exception as e :
        error_handling(e)
        

# checking emails for update user
def check_email(target_id):
    try:
        while True:
            email_up = input_email()
            if collection_3.find_one({"email": email_up, "_id":{"$ne": target_id}}):
                top()
                print("This email is already taken!")
                bottom()
                continue
            else:
                return email_up
    except Exception as e :
        error_handling(e)