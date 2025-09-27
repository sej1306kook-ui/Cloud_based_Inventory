from db import collection_2, collection_3
import re
from bson import ObjectId
from utils import top, bottom, is_valid, top1, bottom1, valid_cust_id, valid_name, error_handling



# --------------------------------COLLECTION 2.---------------------------------------------------------
def valid_number():
    try :
        while True :
            number = input("Enter your phone number: ")
            if len(number) == 10 and number.isdigit() :
                return number
            else:
                top()
                print("Invalid number! Please try again!")
                bottom()

    except Exception as e :
        error_handling(e)


def add_customer(customer_id, name, email1, number1):
    try:
        details = {
            
            "customer_id": customer_id,
            "name": name,
            "email": email1,
            "phone_no" : number1
        }
        insert = collection_2.insert_one(details)

        if insert.acknowledged:
            top()
            print("Inserted succesfully")
            bottom()
        else:
            top()
            print("Insert operation unsuccessful!")
            bottom()

    except Exception as e :
        error_handling(e)

def update_customer(Id, name, email2, number2):
    try:
        
        update = collection_2.update_one({"_id":ObjectId(Id)},{
            "$set":{
                
                "name": name,
                "email": email2,
                "phone_no": number2
            }
        })

        if update.matched_count == 0:
            top1()
            print("No customer found!")
            bottom1()
            return 
            
        if update.modified_count > 0:
            top1()
            print("Updated successfully")
            bottom1()
        else:
            top1()
            print("Update operation unsuccessful!")
            bottom1()

    except Exception as e :
        error_handling(e)


def view_all_customers():
    try:
        if collection_2.count_documents({}) == 0:
            top1()
            print("No customer found!")
            bottom1()
            return 

        find = collection_2.find()
        for doc in find:
            top()
            print(f"ID: {doc['_id']}\nname: {doc['name']}\n email: {doc['email']}\n Phone no.: {doc['phone_no']}")
            bottom()
            
    except Exception as e :
        error_handling(e)

def delete_customer(delete):
    try:
        
        delete_id = collection_2.delete_one({"_id": ObjectId(delete)})

        if delete_id.deleted_count > 0:
            top1()
            print("Delete operation successful!")
            bottom1()
        else:
            top1()
            print("No customer found to be deleted!")
            bottom1()

    except Exception as e :
        error_handling(e)

def customers(current_user):
    while True:
        top()
        print("1. Add customer.")
        print("2. Update customer.")
        print("3. Delete customer.")
        print("4. View all customers.")
        print("5. Exit.")
        bottom()

        choice = input("Enter the choice: ")

        match choice:
            case '1':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can add customers.")
                    bottom1()
                    return None
                           
                customer_id = valid_cust_id()
                        
                name = valid_name()
                    
                email1 =  is_valid()
                if not collection_3.find_one({"email": email1}) :
                    top()
                    print("This email is not registered!")
                    bottom()
                    return None
                
                  
                number1 = valid_number()

                add_customer(customer_id, name, email1, number1)

            case '2':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can update customers")
                    bottom1()
                    return None 
                
                view_all_customers()

                Id = input("Enter the id: ")         
            
                name = valid_name()
                    
                email2 = is_valid()
                if not collection_3.find_one({"email": email2}):
                    top()
                    print("This email is not registered!")
                    bottom()
                    return None 
                
                number2 = valid_number()

                update_customer(Id, name, email2, number2)

            case '3':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can delete customers")
                    bottom1()
                    return None
                 
                view_all_customers()

                delete = input("Enter the id to delete the customer: ")
                
                delete_customer(delete)
                
            case '4':
                view_all_customers()
            case '5':
                break
            case _:
                top()
                print("Invalid option!")
                bottom()


          
