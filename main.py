from product import product
from customers import customers
from users import users, login, admin_acc
from sales import sales
from utils import top, bottom 


def main(current_user):
    top()
    print("Welcome to Cloud Inventory & Sales Management")
    bottom()
    while True :
        top()
        print("1. User menu. ")
        print("2. Customer menu.")
        print("3. Product menu.")
        print("4. Sales menu.")
        print("5. Exit the app.")
        bottom()
        
        choice = input("Enter the choice: ")

        match choice :
            case '1':
                users(current_user)
            case '2':
                customers(current_user)
            case '3':
                product(current_user)
            case '4':
                sales(current_user)
            case '5':
                break 
            case _:
                top()
                print("Invalid option!!")
                bottom()


if __name__ == "__main__":
    top()
    print("Welcome to Cloud Inventory & Sales Management")
    bottom()
    
    admin_acc()
    top()
    print("============================== Login your account =============================================")
    bottom()

    
    current_user = login()
    if current_user :       
        main(current_user)
    else :
        top()
        print("Login failed!")
        bottom()
            
    




        