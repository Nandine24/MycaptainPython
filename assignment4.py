#count of characters in a string in descending order of the count
from collections import Counter
def most_frequent():

    a_string =input("enter string:")
    count = Counter(a_string)
    print(count)
most_frequent()
