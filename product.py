from db import collection_1
from bson import ObjectId
from utils import top, bottom, top1, bottom1, valid_quantity, valid_price, unique_prod_id, error_handling


# ---------------------------COLLECTION 1------------------------------------------------------

def add_product(product_id, product, category, price, quantity, supplier):
    try :
        details = {
            "product_id": product_id,
            "product":product,
            "category": category,
            "price": price,
            "quantity": quantity,
            "supplier": supplier
        }
    
        
        insert = collection_1.insert_one(details)
       
        if insert.acknowledged:
            top()
            print("Inserted successfully")
            bottom()
        else :
            top()
            print("Insert Operation Unsuccessfull!")
            bottom()
    
    except Exception as e :
        error_handling(e)

def update_product(up_id,up_product, up_category, up_price, up_quantity, up_supplier):
    try:
        
        update = collection_1.update_one({"_id": ObjectId(up_id)},
                                         {"$set":{
                    
                                            "product":up_product,
                                            "category":up_category,
                                            "price":up_price,
                                            "quantity":up_quantity,
                                            "supplier":up_supplier
                                        }})

        if update.matched_count == 0:
            top1()
            print("No product found!")
            bottom1()
            return  

        if update.modified_count>0:
            top()
            print("Updated successfully")
            bottom()
        else:
            top()
            print("Update operation unsuccessfull!")
            bottom()
        
    except Exception as e :
        error_handling(e)
    

def view_all_product():
    try:
        if collection_1.count_documents({}) == 0:
            print("No product found!")
            return 

        find = collection_1.find()
        for doc in find :
            top()
            print(f"ID: {doc['_id']}\n product id: {doc['product_id']}\n product: {doc['product']}\n price: {doc['price']}\n quantity: {doc['quantity']}\n supplier: {doc['supplier']}")
            bottom()

    except Exception as e :
        error_handling(e)            
    

def delete_product(delete):
    try:
        delete1 =  collection_1.delete_one({'_id':ObjectId(delete)})

        if delete1.deleted_count > 0:
            top()
            print("Deleted succesfully")
            bottom()
        else:
            top()
            print("No product found to be deleted!")
            bottom()
        
    except Exception as e :
        error_handling(e)  


def product(current_user):
    while True:
        top()
        print("1. Add a new product.")
        print("2. update the product info.")
        print("3. View all product.")
        print("4. Delete a product.")
        print("5. Exit.")
        bottom()

        choice = input("Enter the choice: ")
        match choice:
            case '1':
                if current_user['role'] != 'admin':
                    top1()
                    print("Access Denied! Only admin can add products.")
                    bottom1()
                    return None 
                
                product_id = unique_prod_id()
                    
                product = input("Enter the product name: ")

                category = input("Enter the product category: ")
                
                quantity = valid_quantity()

                price = valid_price()
                    

                supplier = input("Enter the supplier: ")
                add_product(product_id, product, category, price, quantity, supplier)
            
            case '2':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can update products.")
                    bottom1()
                    return None 
                
                view_all_product()

                up_id = input("Enter the id to update the product info: ")
                
                up_product = input("Enter the product name: ")

                up_category = input("Enter the product category: ")

                up_price = valid_price()

                up_quantity = valid_quantity()
                    
                up_supplier = input("Enter the supplier: ")

                update_product(up_id, up_product, up_category, up_price, up_quantity, up_supplier)

            case '3':
                view_all_product()

            case '4':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can delete products.")
                    bottom1()
                    return None 
                
                view_all_product()

                delete = input("Enter the id to delete the product info: ")
                
                delete_product(delete)

            case '5':
                break

            case _:
                top()
                print("Invalid option!")
                bottom()




       
           