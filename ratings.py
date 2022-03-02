"""Restaurant rating lister."""


# READS THE FILE AND SAVES IT VALUE AND KEY INTO EMPTY DICTIONARY
def read_file():
    file = open("scores.txt")
    restaurant_dict = {}

    for line in file:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        restaurant_dict[restaurant] = int(rating)

    return restaurant_dict


# print(read_file())

# USER CAN ADD THEIR REST & RATING, GETS ADDED INTO THE LIST
def user_input(restaurant_dict):

    print("Add one of your favorite restaurant and a rating..")
    restaurant_name = input("Add your Restaurant: ")

    restaurant_rating_correct = True
    while restaurant_rating_correct:
        restaurant_rating = input("Rating: ")

        if int(restaurant_rating) > 5 or int(restaurant_rating) <= 0:
            print("Choose a rating number from 1-5")
        else:
            restaurant_rating_correct = False

    restaurant_dict[restaurant_name] = restaurant_rating


# SORTS THE LIST ITEMS RESTAURANTS NAME ALPHABETICALLY
def print_sorted_scores(restaurant_dict):
    for restaurant_name, restaurant_rating in sorted(restaurant_dict.items()):
        print(f"{restaurant_name} is rated at {restaurant_rating}.")


# READ FROM FILE
restaurant_dict = read_file()

# ADD NEW REST & RATING
user_input(restaurant_dict)

print_sorted_scores(restaurant_dict)
