'''
CS 122 Spring 2023 Project 1-2
Author(s): Alexia Crawford
Credit: N/A
Description: Calculate number of watermelons needed for reunion
'''

#a

ttl_people = 50
ttl_child = 15
ttl_adult = ttl_people - ttl_child
watermelon_child = ttl_child * 3 # each child needs 3 slices
child_extra = watermelon_child * .1 # extra 10 percent = *.1
watermelon_adult = ttl_adult * 2 # each adult needs 2 slices
ttl_child_slices = watermelon_child + child_extra
ttl_watermelon = (ttl_child_slices + watermelon_adult) / 10
print('total watermelons needed', round (ttl_watermelon)) # round because extra 10 percent needed


#b

ttl_people = 60 # Changed from 50 to 60 becasue 10 extra kids
ttl_child = 25 # changed from 15 to 25 becasue 10 extra kids
ttl_adult = ttl_people - ttl_child
watermelon_child = ttl_child * 3
child_extra = watermelon_child * .1
watermelon_adult = ttl_adult * 2
ttl_child_slices = watermelon_child + child_extra
ttl_watermelon = (ttl_child_slices + watermelon_adult) / 10
print('total watermelons needed', round (ttl_watermelon))
