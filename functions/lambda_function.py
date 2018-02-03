my_list = range(16)
print(list(filter(lambda x: x % 3 == 0, my_list)))

threes_and_fives = range(1, 15)
print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, threes_and_fives)))

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = (filter(lambda x: x != "X", garbled))
print(list(message))
