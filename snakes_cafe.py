print(


'''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


Appetizers
----------
Wings
Cookies
Spring Rolls


Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden


Desserts
--------
Ice Cream
Cake
Pie


Drinks
------
Coffee
Tea
Unicorn Tears


***********************************
** What would you like to order? **
***********************************


'''


)


items = {} #dictionary storage


while True: #while True input data is added to the dictionary unless it is quit then it will break, otherwise it will add item to items starting at 0 with items.get
  item = input('> ')


  if item == 'quit':
    break


  items[item] = items.get(item, 0) + 1


  print(f'Item "{item}" has been added to your order.')


print('Final Order list:')
for item, count in items.items():
  print(f'{item}: {count}')