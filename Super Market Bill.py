# import date and time
from datetime  import datetime
# Take user
name=input("Enter your name :")
# shows list of items
list='''
Apple       Rs 100/kg
Kiwi        Rs 100/kg
Watermelon  Rs 80/kg
Pomogranate Rs 90/kg
Banana      Rs 50/kg
Milk        Rs 35/l
Waterbottle Rs 20/l
'''
# print(list)

# declaration
price=0
totalPrice=0
FinalPrice=0
Plist=[]
Ilist=[]
Qlist=[]
pricelist=[]

# rates of items
items={"Apple":100,'Kiwi':100,'Watermelon':80,'Pomogranate':90,'Banana':50,'Milk':35,'Waterbottle':20} #dictionary
option=int(input('For list of items press 1 :')) #input()
if option==1: # if condition
    print(list)
else: # else condition
    print('sorry your are enter the wrong key')
for i in range(len(items)): # range of length of  items
    op1=int(input('if you want to buy press 1 for exit press 2 : ')) # input()
    if op1==2:
        break
    if op1==1:
        item=input("Enter the product name :")    
        quantity=int(input('Enter the quantity:'))
        if item in items.keys():
            price=quantity*(items[item]) # calculate the price of quantity
            pricelist.append((item,quantity,items,price)) # adding all in pricelist
            totalPrice+=price # adding all prices in Totalpricelist
            Ilist.append(item)
            Qlist.append(quantity)
            Plist.append(price)
            Gst=(totalPrice*18)/100
            FinalPrice=totalPrice+Gst
        else:
            print("sorry you enetered item is not available")
    else:
        print("you enetered wrong number")
    op2=input('can i bill press yes or no:')
    if op2=="yes":
        pass
    if FinalPrice!=0:
        print(25*"@","Reliance Smart Point",25*"@") # show bill presentation
        print(24*" ","Secunderabad,Hyderabad")
        print("Name",name,30*" ","Date :",datetime.now())
        print(75*"-") # middle line
        print("S No",8*" ",'Item',8*' ',"Quantity",3*" ","Price")
        for i in range(len(pricelist)): # for loop using range
            print(i,8*" ",Ilist[i],17*" ",Qlist[i],10*" ",Plist[i])
        print(75*"-")
        print(50*" ","Total Price :","Rs",totalPrice)
        print(50*" ","GST :",Gst)
        print(50*" ","Finalprice :",FinalPrice)
        print(75*"*")
        print(24*" ","Thank for Visiting") # finally thank you shows in the middle



            






