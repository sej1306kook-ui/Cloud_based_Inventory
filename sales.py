from db import collection_4, collection_1
from bson import ObjectId
from datetime import datetime
from utils import top, bottom, top1, bottom1, valid_price, valid_quantity, unique_sales_id, matched_prod_id, matched_cust_id, error_handling


# ------------------------------- COLLECTION 4. -----------------------------------------

def add_sales(sales_id, product_id, customer_id,  quantity, price, sales_date):
    try:
        details = {
            "sales_id":sales_id,
            "product_id": product_id,
            "customer_id": customer_id,
            "quantity": quantity,
            "price": price,
            "created_at":sales_date
        }
        result = collection_1.update_one(
            {"product_id": product_id, "quantity": {"$gte": quantity}},
            {"$inc":{"quantity": -quantity}}

        )
        if result.matched_count == 0:
            top()
            print("Not enough stock! Sales can't be added")
            bottom()
            return
            
        insert = collection_4.insert_one(details)
        if insert.acknowledged:
            top()
            print("Inserted successfully")
            bottom()
        else :
            top()
            print("Insert Operation Unsuccessful!")
            bottom()

        
    except Exception as e :
        error_handling(e)
    

def update_sales(id, quantity, price, sales_date):
    try:
        
        update = collection_4.update_one({"_id":ObjectId(id)},{
            "$set":{

                "quantity":quantity,
                "price":price ,
                "last_updated":sales_date  

                }
        })
        if update.matched_count == 0:
            top()
            print("No sales found!")
            bottom()
            return
        
        if update.modified_count > 0:
            top()
            print("Updated successfully")
            bottom()
        else :
            top()
            print("Update operation unsuccessful!")
            bottom()

    except Exception as e :
        error_handling(e)
    

def view_all_sales():
    try :

        if collection_4.count_documents({}) == 0:
            print("No sales found!")
            return

        view = collection_4.find()
        for doc in view:
            top()
            print(f"ID: {doc['_id']}\nsales id: {doc['sales_id']}\nproduct id: {doc['product_id']}\ncustomer id: {doc['customer_id']}\nquantity: {doc['quantity']}\nprice: {doc['price']}\ncreated_at: {doc['created_at']}\nlast updated: {doc.get('last_updated')}")
            bottom()

    except Exception as e :
        error_handling(e)
    
def delete_sales(delete):
    try :
    
        delete1 = collection_4.delete_one({'_id':ObjectId(delete)})

        if delete1.deleted_count > 0:
            top1()
            print("Deleted successfully")
            bottom1()
        else:
            top1()
            print("No sales found to be deleted!")
            bottom1()

    except Exception as e :
        error_handling(e)
    
def daily_sales_report():
    try :
        today = datetime.today().date()
        print(f"---Today sales report: {today}---")

        start = datetime.combine(today, datetime.min.time())
        end = datetime.combine(today, datetime.max.time())

        # 1. total sales of today
        total_sales = collection_4.aggregate([{
            "$match":{"created_at": {"$gte":start, "$lte":end}}},
            {"$group":{ "_id":0, "total":{"$sum": "$price"}}}
        ])
        total_sales1 = list(total_sales)

        if total_sales1:
            total_sales_value = total_sales1[0]["total"]
            top()
            print(f"Total sales: {total_sales_value}")
            bottom()
        else:
            top()
            print("No sales found for today!")
            bottom()

    except Exception as e :
        error_handling(e)
    

    # 2. best selling product
    try :
        best_selling = collection_4.aggregate([
            {"$match":{"created_at":{"$gte":start, "$lte":end}}},
            {"$group":{"_id":"$product_id", "total_qty":{"$sum":"$quantity"}}},
            {"$sort":{"total_qty":-1}},
            {"$limit":1}
        ]) 
        
        best_selling2 = list(best_selling)
        if best_selling2:
            product_id = best_selling2[0]["_id"]
            qty = best_selling2[0]["total_qty"]
            product4 = collection_1.find_one({"product_id":product_id})
            if product4 :   
                top()
                print(f"best selling product: {product4['product']},({qty}units) ")
                bottom()
            else:
                top()
                print("Best selling product not found in product collection! Data inconsistent.")
                bottom()
        else :
            top1()
            print("No sales today!")
            bottom1()
    
    except Exception as e :
        error_handling(e)
    


    # 3. low stock alert 

    try:
        low_stock1 = collection_1.find({"quantity":{"$lte":4}})

        low_stock = list(low_stock1)
        if low_stock: 
            for doc in low_stock:
                top1()
                print(f"low stock alert!\n- {doc['product']} {doc['quantity']} units are left!")
                bottom1()

        else:
            top1()
            print("There is no low stock!")
            bottom1()

    except Exception as e :
        error_handling(e)



def sales(current_user): 
    while True:
        top()
        print("1. Add new sale. ")
        print("2. Update sale.")
        print("3. View all sales.")
        print("4. Delete sales.") 
        print("5. Daily sales report.")
        print("6. Exit")
        bottom()

        choice = input("Enter the choice: ")

        match choice:
            case '1':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can add sales.")
                    bottom1()
                    return None 
                
                sales_id = unique_sales_id()
                        
                product_id = matched_prod_id()

                customer_id = matched_cust_id()
                    
                quantity = valid_quantity()

                       
                price = valid_price()
                    
                sales_date = datetime.today()

                add_sales(sales_id, product_id, customer_id, quantity, price, sales_date)

            case '2':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can update sales.")
                    bottom1()
                    return None 
                
                view_all_sales()

                id = input("Enter the id to update: ")

                quantity = valid_quantity()
                      
                price = valid_price()
                        
                sales_date = datetime.today()

                update_sales(id, quantity, price, sales_date)

            case '3':
                view_all_sales()

            case '4':
                if current_user["role"] != "admin":
                    top1()
                    print("Access Denied! Only admin can delete sales.")
                    bottom1()
                    return None 
                
                view_all_sales()

                delete = input("Enter the id to delete the sale: ")

                delete_sales(delete)
                
            case '5':
                daily_sales_report()
            case '6':
                break

            case _:
                top()
                print("Invalid option!")
                bottom()
            

        