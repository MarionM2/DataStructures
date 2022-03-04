"""finding the minimum value of an item in an array with a time complexity of bigO(n)"""

# store the list in a variable; list1.
list1 = [67, 2, 98, 100, 10]
# loop through the all the items in the list
for i in range(len(list1)):
    # in this condition if there is an item in the list that is smaller than the item holding position zero
    # in the unsorted list
    if list1[i] < list1[0]:
        # the smallest item in the list replaces the item holding position zero
        list1[0] = list1[i]
# print out the item in position zero to find the item with the minimum value in the list
print(list1[0])



""""Using a method to tackle the same problem"""
# have a method and pass in a constant variable for the list


def minimum(z):
    # looping through the list to check the items given the variable p
    for p in range(len(z)):
        # checking if all the items in the list are smaller than the item holding
        # position index zero in the unsorted list
        if z[p] < z[0]:
            # the item with the minimum value is then placed at index zero
            z[0] = z[p]
    # return the item at index zero
    return z[0]


# have a list of items that you need to parse in the method
list4 = [78, 90, 1, 98, -3]
# call the method and parse in the list
print(minimum(list4))