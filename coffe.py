# Define your functions

def coffee_bot(order_number):
  print("Welcome to the coffee shop!!")
  print_message(get_size(), get_drink_type(), order_number)
  

def print_message(size, coffee, order_number):
    print("You have ordered a " + size + " " + coffee + " your coffee will be out shortly!!!!!!!!!")
    print("Your order number is :>" + str(order_number))

def get_size():
  size = "nothing"
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    size = "Small"
  elif res == 'b':
    size = "Medium"
  elif res == 'c':
    size = "Large"
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_size()
  #print("You have choosen a " + size)
  return size

def order_latte():
  latte = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  milk = " "
  if latte == 'a':
    #print("you have choosen 2% milk")
    milk = "latte"
  elif latte == 'b':
    #print("you have choosen Non-fat milk")
    milk = "non-fat latte"
  elif latte == 'c':
    #print("you have choosen Soy milk")
    milk = "soy latte"
  else:
    #print("You did not choose a valid choice")
    return order_latte
  return milk

def get_drink_type():
  size = "Unkown"
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    size = "Brewed Coffee"
    #print("You have ordered a fresh Brew Coffee!")
  elif res == 'b':
    size = "Mocha"
    #print("You have ordered a Mocha")
  elif res == 'c':
    size = order_latte()
    #print("You have ordered a " + size)
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return get_drink_type() 

  #print("You chose a " + size)
  return size


# Call coffee_bot()!
count = 0
more_coffee = "yes"

print(count)
while more_coffee == "yes":
  print(count)
  coffee_bot(count)

  count += 1
  if count > 0:
    more_coffee = input("Would you like anouther cup of coffee?::(yes/no)::> ")

