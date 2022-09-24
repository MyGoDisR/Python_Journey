from statistics import mean, median

the_list = []

# Issue if user writes floats
number_of_objects = int(input("Specifies number of objects in the list: "))

# Solution for including negative numbers and zero
while number_of_objects <= 0:
    number_of_objects = int(input("Please put neutral positive number: "))

while number_of_objects != len(the_list):
    the_list.append(int(input("Enter a number: ")))

the_mean = mean(the_list)
the_median = median(the_list)
the_min = min(the_list)
the_max = max(the_list)

print(f'Mean: {the_mean}, Median: {the_median}, Min: {the_min}, Max: {the_max}')
the_list.clear()