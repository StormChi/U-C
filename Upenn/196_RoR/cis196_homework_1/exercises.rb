# Homework 1
#
# Numerous methods are defined below but are incomplete. For this homework
# assignment, you will have to implement the methods so that they pass the
# tests. Please don't change the method names as doing so will make the
# autograder give you a zero for the method.

# 1. In the find_evens method, you will return an array of all elements of
# the array that are even numbers in the same order. If an element is not an
# integer, it should not be included in the final array. For example,
# find_evens([2, 3, 4, 'foo']) should return `[2, 4]`.

def find_evens(elements)
#   elements.select {|num| num % 2 == 0}
  element.each do |num|
    if num % 2 == 0
      p num 
end

# 2. In the product method, you will find the product of all elements in
# the array. If an element is not a number, just ignore it. The method should
# return 0 if it doesn't contain any numbers. For example, product([1, 2, 3])
# should return 6.
def product(elements)

end

# 3. In the uniq method, you will return an array of distinct elements from the
# original array passed into the method in the same order. If a duplicate
# element is found, it should be removed (e.g. uniq([1, 2, 1]) should return
# [1, 2]). The uniq and uniq! methods built into the Array class will be
# disabled.
def uniq(array)
end

# 4. In the parse_phone_number method, you will parse a string of numbers into
# the format (123) 456-7890. Because users like to put in all kinds of input,
# this string of numbers may also contain extraneous spaces and dashes.
# For example, parse_phone_number('123-456-7890') should return (123) 456-7890,
# and 1 2 3 4 5 6 7 8 9 0 should be parsed into (123) 456-7890. All input
# will be a string with 10 numbers and maybe extraneous spaces and dashes.
def parse_phone_number(phone_number)
end

# 5. In the invert method, you will invert a hash so that the values become the
# keys, and the keys become the corresponding values. For example,
# invert({ 1 => 'foo', 2 => 'bar' }) will return {'foo' => 1, 'bar' => 2}. If
# there are duplicate values, the most recent key-value pair should be used, so
# invert({ 1 => 'foo', 2 => 'bar', 3 => 'foo' }) will return
# {'foo' => 3, 'bar' => 2}. The built-in invert method in the Hash class will be
# disabled.
def invert(hash)
end

# 6. In the fetch method, you will implement something similar to Hash's
# built-in fetch method (And of course, do not use the built-in method).
# This method should return the value corresponding to the key (the second
# argument) in the hash (the first argument). If the key is not found in the
# hash, then the string 'missing' should be returned unless an optional third
# argument is passed in. If a third argument is passed in, and the key is not
# found in the hash, then that third argument should be returned.
# Hint: While you may not change the method name, you may
# change the arguments as long as the method can accept the same number of
# arguments.
def fetch(hash, key, default)
end
