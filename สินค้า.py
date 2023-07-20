#คุณเป็นเจ้าของร้านขายสินค้าออนไลน์ และคุณต้องการคำนวณยอดขายรวมจากการขายสินค้าต่าง ๆ ที่มีราคาแตกต่างกัน 3 ชิ้น
def products_seles():
    products = {
        "gass" : 50,
        "coat" : 200,
        "shoe" : 150 
    }
    
    total_seles = 0

    for product, price in products.items():
        valid_quantity = False
        while not valid_quantity:
            quantity = (input(f"กรุณาใส่จำนวณสินค้า {product}:" ))
            if quantity.isdigit() and int(quantity) >= 0:
                valid_quantity = True
            else:
                print("โปรดป้อนจำนวณสินค้าเป็นจำนวนเต็มบวก")

        sales = int(quantity) * price
        total_seles += sales

    print("ยอดขายรวมทั้งหมด:", total_seles, "บาท")

products_seles()