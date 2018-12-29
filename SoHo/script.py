from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()
print(len(types))
print(len(restaurant_data))

#Write code to insert food types into a data structure here. The data is in data.py
food_types = LinkedList()

for type in types:
  food_types.insert_beginning(type)

#Write code to insert restaurant data into a data structure here. The data is in data.py
restaurants = HashMap(len(types))

for i in range(len(restaurant_data)):
  restaurant_type = restaurant_data[i][0]
  restaurant_info = [[restaurant_data[i][j] for j in [1,2,3,4]]]

  if restaurants.retrieve(restaurant_type) == None:
    restaurants.assign(restaurant_type, restaurant_info)
  else:
    #add restaurant to existing list (if it's already exist)
    x = restaurants.retrieve(restaurant_type) + restaurant_info
    restaurants.assign(restaurant_type, x)

#Write code for user interaction here
final_choice = True

while final_choice:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()

    #Search for user_input in food types data structure here
    type_result = []
    current_node = food_types.get_head_node()

    while current_node.value != None:
      if current_node.value.startswith(user_input):
      	type_result.append(current_node.value)
      current_node = current_node.get_next_node()

    if len(type_result) != 1:
    	print("\nwith those beginning letters, your choices are {0}.".format(type_result))
    else:
      user_input2 = str(input("\nThe only option with those beginning letters is {0}. Do you want to look at {0} restaurants? Enter 'y' for yes and 'n' for no.\n".format(type_result[0]))).lower()
      if user_input2 == "y":

        #After finding food type write code for retrieving restaurant data here
        print("\nThe {0} restaurants in SoHo are...".format(type_result[0]))
        for restaurant in restaurants.retrieve(type_result[0]):
          print("\n--------------------------")
          print("\nName: {0}\nPrice: {1}\nRating: {2}\nAddres: {3}".format(restaurant[0], restaurant[1], restaurant[2], restaurant[3]))

        user_input3 = str(input("\n\nDo you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()
        if user_input3 == "n":
          final_choice = False

      elif user_input2 == "n":
        final_choice = False
