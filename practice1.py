#There are two ways to make a #Python object convertible to a dictionary:
#1) Define .keys() and .__getitem__()
#2) Make it iterable producing key/value pairs
from typing import List


class Dictable1:
    def keys(self):
        return ["x", "y", "z"]

    def __getitem__(self, n):
        return n + n + n

xyz = Dictable1()
dict(xyz)

class Dictable2:
    def __iter__(self):
        return iter([("p","ppp"),
                     ("q","qqq"),
                     ("R","rrr")])
pdq = Dictable2()
print(dict(pdq))

numbers = [2,4,5,6,7]
def square_num(x):
    return x**2

num2 = map(square_num, numbers)
type(square_num)
for num in num2:
    print(num)

x_coord = [1.3,2.5,-1.7, 4.8]
y_coord = [-3.2,1.7,3.4,3]
from math import sqrt
distance = map(lambda x, y: sqrt(x**2 + y**2), x_coord,y_coord)
print(sqrt(1.3**2 + (-3.2)**2))
for num in distance:
    print(num)

# Bad
#if (foo)
#  return 1
#else
  #return 2

# Good
#if (foo)
  #return 1
#return 2

#return 1 if foo else 2
#manipulting strings with map()
raw_words = ["now ", " men", " de eer ", "bucket"]
clean_words = list(map(str.strip, raw_words))
print(clean_words)
#list comprehensions for for loop
print([word.strip() for word in raw_words])
print([])
print(str.strip(raw_words[0]))

quote = """"On a visit to the NASA space center, President Kennedy spoke to a man sweeping \
up in one of the buildings.  "What's your job here?" asked Kennedy.  "Well Mr. President," \
the janitor replied, "I'm helping to put a man on the moon"."""
words = quote.split()
print(words[0:10])

def remove_punct(word):
    return word.strip(",.;:\"'?/")
correct = list(map(remove_punct,words))
print(correct[0:10])

remove = lambda w: w.strip(",.;:\"'? /")
corr = map(remove, words)
#or
"".join(map(remove, words))





