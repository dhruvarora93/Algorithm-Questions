def product(ar):
    product_of_numbers_before_index=[]
    product_of_numbers_before_index.append(1)
    product=1
    for i in range(1,len(ar)):
        product*=ar[i-1]
        product_of_numbers_before_index.append(product)

    product=1
    for i in range(len(ar)-1,-1,-1):
        product_of_numbers_before_index[i]*=product
        product*=ar[i]
    print(product_of_numbers_before_index)


product([2,7,3,4])


