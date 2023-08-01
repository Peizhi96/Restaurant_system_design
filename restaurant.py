from Restaurant_data import *
from welcome import *
from Linked_list import Node, LinkedList

p_welcome()

def insert_food_types():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert_beginning(food_type)
    return food_type_list

def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in types:
        restaurant_list = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_type:
                restaurant_list.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_list)

    return restaurant_data_list

food_info_list = insert_food_types()
restaurant_info_list = insert_restaurant_data()


selected_food_type = ""

while len(selected_food_type) == 0:
    user_input = str(input("\nWhat type of food would like to eat?\nType the beginning of that food type and its's here.\n")).lower()
    
    finding_types = []
    types_list_head = food_info_list.get_head_node()
    while types_list_head is not None:
        if str(types_list_head.get_value()).startswith(user_input):
            finding_types.append(types_list_head.get_value())
        types_list_head = types_list_head.get_next_node()

    for food in finding_types:
        print(food)
    
    if len(finding_types) == 1:
        select_type = str(input("\nThe only matching type for the specified input is " + finding_types[0] + ". \nDo you want to look at " + finding_types[0] + " restaurants? Enter y for yes and n for no\n")).lower()



    if select_type == 'y':
        selected_food_type = finding_types[0]
        print("Selected Food Type: " + selected_food_type)
        restaurant_list_head = restaurant_info_list.get_head_node()
        while restaurant_list_head.get_next_node() is not None:
            sublist_head = restaurant_list_head.get_value().get_head_node()
            if sublist_head.get_value()[0] == selected_food_type:
                while sublist_head.get_next_node() is not None:
                    print("--------------------------")
                    print("Name: " + sublist_head.get_value()[1])
                    print("Price: " + sublist_head.get_value()[2] + "/5")
                    print("Rating: " + sublist_head.get_value()[3] + "/5")
                    print("Address: " + sublist_head.get_value()[4])
                    print("--------------------------\n")
                    sublist_head = sublist_head.get_next_node()
            restaurant_list_head = restaurant_list_head.get_next_node()
        select_again = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
        if select_again == 'y':
            selected_food_type = " "

