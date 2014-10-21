__author__ = 'jmasramon'

a, b, c = 1, 2, 'hola'

print(a,b,c)

######################## Vars

mystring, myfloat, myint = 'hello', 10.0, 20

print mystring, myfloat, myint

######################## Lists

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append('hello')
strings.append('world')



# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

even_numbers = [0,2,4]
odd_numbers = [1,3,5]

all_nums = even_numbers + odd_numbers

print all_nums
print all_nums * 3

##########


x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print big_list.count(x)

print "x_list contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d objects" % len(big_list)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print "Great!"

birds = ['canary']
cages = birds * 4
print birds
print cages
birds.append('parrot')
print birds
print cages

birds = ['canary']
cages = [birds] * 4
print birds
print cages
birds.append('parrot')
print birds
print cages

##### Formatting

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.2f."

print format_string % data

######### Strings

s = "Hey there! what should this string be?"

# Length should be 20
print "Length of s = %d" % len(s[:20])

# First occurrence of "a" should be at index 8
print s.index("a")
print s.index("a")-8
print s[(s.index("a")-8):s.index("a")+1]
print "The first occurrence of the letter a = %d" % s[(s.index("a")-8):s.index("a")+1].index('a')

# Number of a's should be 2
print "a occurs %d times" % (s+'a').count("a")

# Slicing the string into bits
print "The first five characters are '%s'" % s[:5] # Start to 5
print "The next five characters are '%s'" % s[5:10] # 5 to 10
print "The twelfth character is '%s'" % s[11] # Just number 12

print "The last five characters are '%s'" % s[-5:] # 5th-from-last to end

# Convert everything to uppercase
print "String in uppercase: %s" % s.upper()

# Convert everything to lowercase
print "String in lowercase: %s" % s.lower()

# Check how a string starts
if ('S' + s[s.index('str')+1:]).startswith("Str"):
    print "String starts with 'Str'. Good!"

# Check how a string ends
if s.endswith("ome!"):
    print "String ends with 'ome!'. Good!"
else:
    print  "String ends with '%s'. Good!" % s[-len("ome!"):]

# Split the string into three separate strings,
# each containing only a word
print "Split the words of the string: %s" % s.split(" ")[0:3]

############ Boolean logic

# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print "1"

if first_array:
    print "2"

if len(second_array) == 2:
    print "3"

if len(first_array) + len(second_array) == 5:
    print "4"

if first_array and first_array[0] == 1:
    print "5"

if not second_number:
    print "6"


########## Loops
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
first_result = []
for x in numbers:
    if x == 237:
        break
    if not x%2:
        first_result.append(x)

second_result = []
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    second_result.append(number)

print first_result
print second_result

if first_result == second_result:
    print "perfect"

############## Classes

class Vehicle:
    color, type = '', ''

    def toString(self):
        return self.color + ' ' + self.type + ' ' + self.name + ' ' + str(self.worth)


car1 = Vehicle()
car1.color = 'red'
car1.type = 'convertible'
car1.name = 'Fer'
car1.worth = 60000
car2 = Vehicle()
car2.color = 'blue'
car2.type = 'van'
car2.name = 'Jump'
car2.worth = 10000
print car1.toString()
print car2.toString()


