products = ['bear', 'milk', 'egg', 'egg', 'egg', 'egg']
products2 = []
for items in products:
    if items not in products2:
        products2.append(items)
print(products2)

# это я для себя разбираюсь как работать с for

product_list1 = ['bear', 'milk', 'egg', 'egg', 'egg', 'egg']
while 'egg' in product_list1:
    product_list1.remove('egg')
print(product_list1)


