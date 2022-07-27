# STEP 1: Let Nook or the Nooklings enter the items and prices
nooks_cranny = { }
redds_corner = { }

print("~WELCOME TO NOOK'S CRANNY CATALOG~\
        \n\nEnter your items and prices here!\
        \nOnce you're done, just hit enter.\n")
print("-" * 3)
nook_item_name = input("\nEnter the item: ")

while nook_item_name != ' ' and nook_item_name != '':
    nook_item_price = int(input("What's the item's bell price?: "))
    
    nooks_cranny[nook_item_name] = nook_item_price
    redds_corner[nook_item_name] = 0
    nook_item_name = input("Enter the item: ")




# STEP 2: Print the most and least expensive items, and the
#           average price (have 3 decimal points)

avg_price = 0  
for key in nooks_cranny:
    avg_price += nooks_cranny[key]
avg_price /= len(nooks_cranny)

print("\nAVERAGE PRICE: {:.3f} bells".format(avg_price))
print("\nMOST EXPENSIVE ITEM:", max(nooks_cranny, key=nooks_cranny.get))
print("LEAST EXPENSIVE ITEM:", min(nooks_cranny, key=nooks_cranny.get))




# STEP 3: Name Redd's store, then make a copy of your dictionary and let the user edit the prices
#   If there are any items copied over that are brought up, we leave it alone and let the randomizer
#   determine how to mark it up or down.
#   Else, we ask the user what this new item's price is
import random

print("\n")
print("~" * 60)
print("\n-REDD'S CORNER CATALOG-\
        \n\nOh no, Redd's back, and he's selling more than just art - \
        \nhe's selling the exact same items as you and other rare items!\
    \n\n1.) Enter the items he has and we will find out what prices he has for them.\
    \n2.) Enter any items you're not selling as well as the prices.\
    \nOnce you're done, hit enter!\n")

print("-" * 5)

#This is to determine if an item was ever brought up or not. If it isn't, 
items_brought_up = []

redd_item_name = input("\nEnter the item: ")

while redd_item_name != ' ' and redd_item_name != '':
    #If the user inputs an item that isn't already in the dictionary, we treat it like it's a new entry.
    #       As far as rules go, I don't think it said anything about Redd changing prices of items
    #       Nook doesn't have.
    items_brought_up += [redd_item_name]
    if redd_item_name not in redds_corner:
        print("This item is not in the catalog.")
        redd_item_price = int(input("What's the new item's bell price?: "))
        redds_corner[redd_item_name] = redd_item_price
        redd_item_name = input("Enter the item: ")

    #But if it is in, if I understand directions correctly, it takes the original price Nook had his at
        #and randomly decides to subtract 20 bells (discount) or to add 35 bells (add on)
    elif redd_item_name in redds_corner:
        print("This item is in the catalog!")
        redds_corner[redd_item_name] += random.randint(-20, 35) #This determines how much is added or taken off

        #The bell price can NEVER be less than 1. So if this incident happens, while it's true, it
        #       should reassign the price over and over until it's > 1
        if redds_corner[redd_item_name] < 2:
            while redds_corner[redd_item_name] < 2:
                redds_corner[redd_item_name] += random.randint(-20, 35)
        redd_item_name = input("Enter the item: ")

#Looking through it again to see if there's any items in the dictionary Nook knows isn't being sold there
for key in list(redds_corner):
    if key not in items_brought_up:
        redds_corner.pop(str(key))

#prints the completed version of the dictionary
print(redds_corner)







# STEP 3.5 (BONUS): Compare the items in each dictionary. Show which ones Nook is also selling
#               and what different items Redd has

#Turning them into sets because it'd be the easiest way instead of doing constant loops
print("\n")
print("~" * 60)
print("\n*COMPARING ITEMS AND PRICES*\n")
print("-" * 5)
nook_key_set = set(nooks_cranny.keys())
redd_key_set = set(redds_corner.keys())
same_items = (nook_key_set.intersection(redd_key_set))
diff_items = redd_key_set - nook_key_set

print("\n\nThese are the same items he is selling as you:", same_items)
print("These are the differences in prices in respective order:", end = ' ')
for i in (same_items):
    print(str(abs(redds_corner[i] - nooks_cranny[i])) + " bells", end = ' ')

print("\n\nThese are items Redd is selling, but you're not:", diff_items)
print("These are their prices in respective order:", end = ' ')
for j in diff_items:
    if j in redds_corner: 
        print(str(redds_corner[j]) + " bells", end = ' ')



# STEP 4: Ask for how many items the shopper would like to get, in total.
#           Put the keys of the dictionaries into a list and use random.choice to put however
#           many items into the cart.
#               NOTE: Do it at each store, don't do a fair game by just having the randomizer choose
#               items that both stores have
#           Once you're done, use a loop to figure out the totals for the carts at each store,
#           then say whether Nook earned more than Redd, vice versa, or if they both made the same amount
print("\n")
print("~" * 60)
print("\n=SHOPPER'S CART= \
\n\nNow it's time to determine what shop is best for what items! There is one shopper at each\
 store, looking for number of items, in general. They do not care what items they are, they\
 just want to know which one would be best to go to, price-wise!\n")
print("-" * 5)

import random #Randomly determines what kind of items will go in the cart

nook_keys = nooks_cranny.keys()
redd_keys = redds_corner.keys()

num_of_items = int(input("\nHow many items would you, the shopper, like in your cart?: "))
nook_shoppers_cart = []
redd_shoppers_cart = []

i = 1
while i <= num_of_items:
    nook_random_item = random.choice(list(nook_key_set))
    nook_shoppers_cart.append(nook_random_item)
    redd_random_item = random.choice(list(redd_key_set))
    redd_shoppers_cart.append(redd_random_item)
    i += 1

print("\nThese are the items in the shopper's cart at Nook's:", nook_shoppers_cart)
print("These are the items in the shopper's cart at Redd's:", redd_shoppers_cart)

i = 0
while i < len(nook_shoppers_cart) and i < len(redd_shoppers_cart):
    nook_total = 0
    redd_total = 0
    
    for item in nook_shoppers_cart:
        nook_total += int(nooks_cranny[item])

    for item in redd_shoppers_cart:
        redd_total += int(redds_corner[item])
        
    i += 1
if nook_total > redd_total:
    print("\nNook's Cranny made more with this purchase.")
    print("Total at Nook's: " + str(nook_total) + " bells")
    print("Total at Redd's: " + str(redd_total) + " bells")
elif redd_total > nook_total:
    print("\nRedd's Corner made more with this purchase.")
    print("Total at Redd's: " + str(redd_total) + " bells")
    print("Total at Nook's: " + str(nook_total) + " bells")
else:
    print("\nIt doesn't matter where you go.")
    print("Total either way: " + str(((nook_total + redd_total) / 2)) + " bells")
