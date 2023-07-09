from flipkart_db import DbModel

def find_mobile_detail(model):
    db_model = DbModel('mobiles.db')
    db_model.connect()
    mobile_details = db_model.get_mobile_detail(model)
    if mobile_details:
        mobile_format = f"""
        Model: {mobile_details[1]}
        Price: {mobile_details[2]}
        Rating: {mobile_details[3]}
        Image: {mobile_details[4]}
        Description: {mobile_details[5]}
        Reviews: {mobile_details[6]}
        Specifications: {mobile_details[7]}
        """
        db_model.close_db_connection()
        return mobile_format
    db_model.close_db_connection()
    return "Mobile not found"

if __name__ == "__main__":
    model = input("Enter model name: ")
    res = find_mobile_detail(model)
    print(res)
