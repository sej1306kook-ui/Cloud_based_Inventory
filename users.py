from db import collection_3
from utils import top, bottom, top1, bottom1, input_password, input_role, error_handling, check_username, check_email, unique_emails, unique_username
import bcrypt
from bson import ObjectId



# ---------------------------COLLECTION 3.-------------------------------------------------------
def admin_acc():
    if not collection_3.find_one({"role": "admin"}) :
        top1()
        print("No admin found! Create first admin account.")
        bottom1()
        
        username1 = unique_username()

        email = unique_emails()

        hashed = input_password()

        role = "admin"

        try: 
            details = collection_3.insert_one({
                "username": username1,
                "email": email,
                "password": hashed,
                "role": role 
            })
            if details.acknowledged:
                top1()
                print("Admin account created successfully. Please login to continue.....")
                bottom1()
            else :
                top1()
                print("Registration failed!")
                bottom1()

        except Exception as e :
            error_handling(e) 
        
    
def add_user(username, email1, hashed, role):
    try :
        
        details = collection_3.insert_one({
            "username": username,
            "email": email1,
            "password": hashed, 
            "role": role
        })
        if details.acknowledged:
            top1()
            print("Inserted successfully")
            bottom1()
        else :
            top1()
            print("Insert Operation Unsuccessfull!")
            bottom1()
    
    except Exception as e :
            error_handling(e) 
        

def update_user(id, username_up, email_up, passwd_up, role_up):
    try :
        update = collection_3.update_one({"_id":ObjectId(id)}, {
            "$set":{
                "username": username_up, 
                "email": email_up,
                "password": passwd_up,
                "role": role_up
            }
        })

        if update.matched_count == 0:
            top1()
            print("No user found!")
            bottom1()
            return 
        if update.modified_count > 0:
            top1()
            print("Updated Successfully")
            bottom1()
        else:
            top1()
            print("Update Operation Unsuccessfull!")
            bottom1()
    
    except Exception as e :
        error_handling(e)
        

def delete_user(id_del):
    try :
        delete = collection_3.delete_one({"_id": ObjectId(id_del)})
        if delete.deleted_count > 0 :
            top1()
            print("Deleted Successfully")
            bottom1()

        else : 
            top1()
            print("Delete Operation Unsuccessfull!")
            bottom1()

    except Exception as e :
        error_handling(e)
        


def login():
    try:
        email_attempts = 0
        while email_attempts < 3:

            email3 = input("Enter email: ")
            user = collection_3.find_one({"email": email3})
            if not user:
                top1()
                print("User not found! This email is not existed!")
                bottom1()
                email_attempts += 1
                continue
            else:
                break
        else :
            print("Too many invalid email attempts. Login blocked!")
            return None
        
            
        passwd_attempts = 0

        while passwd_attempts < 3:
            password2 = input("Enter password: ")
            stored_hashed = user["password"]
            if bcrypt.checkpw(password2.encode('utf-8'),stored_hashed):
                    top()
                    print("Password matched. Login Successfull...")
                    bottom()
                    return user 

            else :
                    top()
                    print("Invalid password! Please try again!")
                    bottom()
                    passwd_attempts += 1
                    continue
        else:
            print("Too many invalid password attempts. Login blocked!")
            return None   

    except Exception as e :
        error_handling(e)
        

def view_all_user():
    if collection_3.count_documents({}) == 0:
        top()
        print("No user found!")
        bottom()
        return 
    user  = collection_3.find()

    for doc in user:
        top()
        print(f"Id: {doc['_id']}\n username: {doc['username']}\nemail: {doc['email']}\nrole: {doc['role']}")
        bottom()

def role_check():
    try:
        username1 = input("Enter username: ")
        user = collection_3.find_one({"username": username1})
        if not user :
            top()
            print("This username doesn't exist!")
            bottom()
        else:
            role = user["role"]
            top()
            print(f"Role is {role}")
            bottom()
                
    except Exception as e :
        error_handling(e)
        

def users(current_user):
    while True :
        top()
        print("1. Register")
        print("2. Login ")
        print("3. Role based ")
        print("4. View all user")
        print("5. Update user")
        print("6. Delete user")
        print("7. Exit.")
        bottom()

        choice = input("Enter the choice: ")

        match choice :
            case '1':
        
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can add new user.")
                    bottom1()
                    continue 
                try : 
                    
                    username = unique_username()
                      
                    email1 = unique_emails()
                        
                    hashed = input_password()

                    role = input_role()

                    add_user(username, email1, hashed, role)

                except Exception as e :
                    error_handling(e)
                    
            case '2':
                
                new_user = login()
                if new_user:
                    current_user = new_user
            
            case '3':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can access roles.")
                    bottom1()
                    continue 
                
                role_check()

            case '4':
                view_all_user()

            case '5':
                
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can update user.")
                    bottom1()
                    continue
                try :
                    view_all_user()

                    id = input("Enter the id to update the user info: ")

                    target_id = ObjectId(id)

                    username_up = check_username(target_id)
                    
                    email_up = check_email(target_id)
                    
                    passwd_up = input_password()

                    role_up = input_role()

                    update_user(id, username_up, email_up, passwd_up, role_up)
                
                except Exception as e :
                    error_handling(e)
                    

            case '6':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can delete the user.")
                    bottom1()
                    continue
                
                view_all_user()

                id_del = input("Enter the id to delete the user: ")

                delete_user(id_del)
                
            case '7':
                break

            case _:
                top()
                print("Invalid option! Please try again!")
                bottom()
