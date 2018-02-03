import sys

message = "Hello World!"

print (sys.argv[0])
print (message)
print ("hi, " + sys.argv[1])
print ("how are you " + sys.argv[2] + "?")


#_____________________________
# sys.argv[0] is the name of the script
# sys.argv[1] and sys.argv[2] need to be called out when running the script:
#
# python3 hello.py Eric today
#
#[root@ep~]# python3 hello.py Eric today
#hello.py
#Hello World!
#hi, Eric
#how are you today?
