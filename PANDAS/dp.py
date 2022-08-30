import pandas as pd  
import matplotlib.pyplot as plt

PROD = {'Product_ID':[10,20,30,40,50,60,70,80,90,100],'Product_Name':['ABC','PQR','XYZ','RWZ','HDJ','QWE','GSU','GAN','SDS','EAF'],
           'Price' :[10,2000,3000,40,5000,100,7000,8000,9000,10000],'Quantity':[2,1,5,7,8,3,7,98,4,10]}
           
PRODUCT = pd.DataFrame(data=PROD)



print(PRODUCT)

print("--------------------------------Last 5--------------------------------------------------------")
tails = PRODUCT.tail(5)

print(tails)

print("---------------------------------First 3------------------------------------------------------")
heads = PRODUCT.head(3)

print(heads)

print("---------------------------------Greater than 100---------------------------------------------")

great100 = PRODUCT.loc[PRODUCT["Price"] >100]
print(great100)


print("---------------------------------Product & Quantity--------------------------------------------")



pnq =  PRODUCT[["Product_Name","Quantity"]]
print(pnq)

print("---------------------------------Read CSV------------------------------------------------------")

ird = pd.read_csv("iris.data")
print(ird)




