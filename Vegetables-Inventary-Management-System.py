# Vegetables Inventary Management

own = Owner_Secret_Code = 12345
veg = Vegetables = ['tomato','brinjal','carrot','beans','cucumber']
qty = Quantity_in_Kgs = [100,150,200,250,300]
cppr = Cost_Price_per_Kg = [25,30,35,40,45]
sppr = Sell_Price_per_Kg = [40,45,50,55,60]
cart_veg = []
qty_veg = []
user = 0
total_revenue = 0
total_itemized_profit = 0
while True:
    r = Role = input("Enter your Role 'Owner/Customer': ")
    if r == 'owner':
        pin_a = Pin_Attempts = 1
        max_attempts = 3
        while pin_a <= max_attempts:
            Pin = int(input('Enter Owner Secret Code: '))
            if Pin == own:
                print('Login Sucessful')
                break
        else:
            print('Entered Pin is Wrong')            
            pin_a = pin_a + 1
        if Pin != own:
            print('Tempararily, Your Profile is Blocked')
        else:
            print('1. Add Items to Inventary','2. Remove Item','3. Update Item',\
                    '4. View Inventry','5. View User Details','6. View Report',\
                    '7. Total Revenue','8. Total Revenue Itemized Profit','9. Exit',sep = '\n')
            choose = int(input('Choose an Option: '))
            while True:
                if choose == 1:
                    ask_veg_name = input('Enter what Vegetable you want to add: ')
                    if ask_veg_name not in veg:
                        veg.append(ask_veg_name)
                        ask_veg_qty = int(input('Enter Vegetables Quantity: '))
                        qty.append(ask_veg_qty)
                        ask_veg_cost_price = int(input('Enter Vegetable Cost Price/Kg: '))
                        cppr.append(ask_veg_cost_price)
                        ask_veg_sell_price = int(input('Enter Vegetable Sell Price/Kg: '))
                        sppr.append(ask_veg_sell_price)
                        print('Updated Vegetables',veg)
                    else:
                        print(ask_veg_name,'is already in Stock')
                elif choose == 2:
                    rem = input('Enter what Vegetable you want to Remove: ')
                    if rem in veg:
                        idx = veg.index(rem)
                        veg.pop(idx)
                        qty.pop(idx)
                        cppr.pop(idx)
                        sppr.pop(idx)
                        print('Updated Vegetables',veg)
                    else:
                        print('Vegtable not found')
                elif choose == 3:
                    upd = input('Enter what Vegetable you want to Update: ')
                    if upd in veg:
                        idx = veg.index(upd)
                        upd_qty = int(input('Enter Quantity of Vegetable: '))
                        upd_cost_price = int(input('Enter Cost Price/Kg of Vegetable: '))
                        upd_sell_price = int(input('Enter Price/Kg of Vegtable: '))
                        qty[idx] = upd_qty
                        cppr[idx] = upd_cost_price
                        sppr[idx] = upd_sell_price
                        print(veg)
                elif choose == 4:
                    print('Avaible Vegetables')
                    for i in range(len(veg)):
                        print('Vegetable Name:',veg[i])
                        print('Quantity:',qty[i])
                        print('Cost_Price/Kg:',cppr[i])
                        print('Sell_Price/Kg:',sppr[i])
                    
                elif choose == 5:
                    print(user)
                elif choose == 6:
                    print('View Report')
                    for i in range(len(veg)):
                        print('Vegetable :', veg[i])
                        print('Available Qty :', qty[i], 'Kgs')
                        print('Cost Price/Kg :', cppr[i])
                        print('Sell Price/Kg :', sppr[i])
                elif choose == 7:
                    print('Total Revenue is',total_revenue)
                elif choose == 8:
                    print('Total Itemized Profit',total_itemized_profit)
                elif choose == 9:
                    print('Exiting')
                    break
                else:
                    print('Invalid Option')
                stay = input("ENter 'Yes/No', if you want to do other programs: ")
                if stay != 'yes':
                    print('Thanks for Auditting')
                    break
                else:
                    print('1. Add Items to Inventary','2. Remove Item','3. Update Item',\
                        '4. View Inventry','5. View User Details','6. View Report',\
                        '7. Total Revenue','8. Total Revenue Itemized Profit','9. Exit',sep = '\n')
                
    elif r == 'customer':
        if r == 'customer':
            user = user + 1
        else:
            print('Nobody Visited our Mart Today')
        print('Welcome')
        while True:
            mob = input('Enter Your Mobile Number: ')
            if len(mob) == 10:
                print('Avaible Vegetables')
                for i in range(len(veg)):
                    print('Vegetable Name:',veg[i])
                    print('Price/Kg:',sppr[i])
                break
            else:
                print('Invalid Mobile Number')
        while True:
            print('1. Add Cart','2. Remove Cart','3. Modify Cart',\
                    '4. View Cart','5. Billing','6. Exit',sep = '\n')
            choose = int(input('Choose an Option: '))
            if choose == 1:
                w = What_do_you_need = input('Enter What Vegetables You Need:')
                if w in veg:
                    index= veg.index(w)
                    kgs = float(input('How many Kgs you need: '))
                    if kgs <= qty[index]:
                        cart_veg.append(w)
                        qty_veg.append(kgs)
                        qty[index] = qty[index] - kgs
                    else:
                        print('Entered',kgs,'is out of stock')
                else:
                    print(w,'is out of stock')
            elif choose == 2:
                rem = input('Enter what Vegetable you want to Remove: ')
                if rem in cart_veg:
                    idx = cart_veg.index(rem)
                    v_idx = veg.index(rem)
                    qty[v_idx] = qty[v_idx] + qty_veg[idx]
                    cart_veg.pop(idx)
                    qty_veg.pop(idx)
                    print(rem,'is removed from cart')

            elif choose == 3:
                mod = input('Enter what Vegetables you want to Modify: ')
                if mod in cart_veg:
                    idx_c = cart_veg.index(mod)
                    idx_v = veg.index(mod)
                    qty[idx_v] = qty[idx_v] + qty_veg[idx_c]
                    print(qty_veg[idx_c], 'Kgs')
                    new_qty = float(input('Enter How Much Quantity You Want To Modify: '))
                    if new_qty <= qty[idx_v]:
                        qty_veg[idx_c] = new_qty
                        qty[idx_v] = qty[idx_v] - new_qty
                        print('Quantity Modified Sucessfully')
                    else:
                        qty[idx_v] = qty[idx_v] - qty_veg[idx_c]
                        print('Stock is not avaible')
                else:
                    print(mod,' is not in cart')
            elif choose == 4:
                if len(cart_veg) == 0:
                    print('Your Cart is Empty')
                else:
                    print('Your Cart')
                    for i in range(len(cart_veg)):
                        print(cart_veg[i],'-',qty_veg[i],'Kgs')
            elif choose == 5:
                total = 0
                if len(cart_veg) == 0:
                    print('Your Cart is Empty')
                else:
                    for i in range(len(cart_veg)):
                        v_idx = veg.index(cart_veg[i])
                        item_price = sppr[v_idx]*qty_veg[i]
                        cost_price = cppr[v_idx]*qty_veg[i]
                        print(cart_veg[i],'-',qty_veg[i],'-',item_price)
                        total = total + item_price
                        total_revenue = total_revenue + item_price
                        total_itemized_profit = total_itemized_profit + (item_price - cost_price)
                    print('Total Bill is',total)
                    print('Thanks For Shopping, Have a Nice Day')
                    cart_veg = []
                    qty_veg = []
                    
            elif choose == 6:
                print('Thanks For Shopping')
                cart_veg = []
                qty_veg = []
                break
            else:
                print('Choose Correct Option')
            stay = input("Enter 'Yes/No', if you want to do other programs: ")
            if stay == 'yes':
                print('Avaible Vegetables')
                for i in range(len(veg)):
                    print('Vegetable Name:',veg[i])
                    print('Price/Kg:',sppr[i])
                continue
            else:
                print('Thanks for Shopping')
                break
                
    else:
        print('Select Correct Role')
