import easygui

items = []
prices = []
amount = []
amounts = 0
finished = False
total_price = 0.00
list_num = -1


def take_item():
    global list_num, amounts, finished
    item = easygui.enterbox("What item is it?")
    if item == "done" or item == "None":
        finished = True
    else:
        how_many = easygui.integerbox("How many {0:} do you have?".format(item))
        amounts = how_many
        items.append(item)
        amount.append(how_many)
        list_num += 1


def pricing():
    global list_num, total_price
    if finished:
        pass
    else:
        try:
            price = easygui.enterbox("What is the price of 1 {0:}".format(items[list_num]))
        new_price = float(price)
        except ValueError:
            easygui.msgbox("Please enter a number.")
            pricing()
        else:
            total_price += float(price) * amounts
            prices.append(new_price)


def create_receipt():
    print "Item \t Amount \t Price \t Total Price"
    for i in range(0, list_num+1):
        print items[i], "\t\t", amount[i], "\t\t 3", prices[i]
    print "\t\t\t ", "$",total_price
    print "Thank you for using Tony's Receipt Maker!"
    print "-----------------------------------------------------------"


while 1:
    take_item()
    pricing()
    if finished:
        create_receipt()
    else:
        continue