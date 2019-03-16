# Exercise 1.1

import math

r = input("please enter a number:")
print (type(r))
r = float(r)

volume = (4/3)*math.pi*(r**3)
print('The volume is of a sphere of {} is {:.3f}.'.format(r,volume))

# Exercise 1.3

hour = 13
min = 2

print ("Current time is {:02}:{:02}.".format(hour,min))
print(1+2)

import datetime
print(datetime.datetime.now())
now = datetime.datetime
print(now)
print(now.hour, now.minute, now.second)


# exercise #2

NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60

seconds = 42 * NUMBER_OF_SECONDS_IN_ONE_MINUTE + 42

print("There are {} seconds....".format(seconds))

# Exercise 2.2

NUMBER_OF_KILOMETERES_IN_A_MILE = 1.61

miles = 10/NUMBER_OF_KILOMETERES_IN_A_MILE

print("There are {:.2f} miles in a ".format(miles))


