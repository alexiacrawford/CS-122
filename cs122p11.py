'''
CS 122 Spring 2023 Project 1-1
Author(s): Alexia Crawforde
Credit: N/A
Description: Hello, Python – intro problems and code
'''
#1a
cost_t = 20
cost_green = cost_t * .75
cost_yellow = 20
ttl_shirts = 100
ttl_yellow = ttl_shirts // 2
ttl_green = ttl_shirts // 2
ttl_yellow_cost = ttl_yellow * cost_t
ttl_green_cost = cost_green * ttl_green
print(ttl_green, 'green t-shirts were purchased')
print(ttl_yellow, 'yellow t-shirts were purchased')
ttl_yellow_cost = ttl_yellow * cost_t
ttl_cost = ttl_green_cost + ttl_yellow_cost
print('the total cost is', ttl_cost)

#1b
cost_t = 20
cost_green = cost_t * .75
cost_yellow = 20
ttl_shirts = 101
ttl_yellow = ttl_shirts // 2
ttl_green = ttl_shirts - ttl_yellow # bug here is subtract not divide
ttl_yellow_cost = ttl_yellow * cost_t
ttl_green_cost = cost_green * ttl_green
print(ttl_green, 'green t-shirts were purchased')
print(ttl_yellow, 'yellow t-shirts were purchased')
ttl_yellow_cost = ttl_yellow * cost_t
ttl_cost = ttl_green_cost + ttl_yellow_cost
print('the total cost is', ttl_cost)
#expected outcome was a weird uneven number
#actual outcome was 51 green, 50 yellow, total cost is 1765.0

#2a
ttl_gummies = 100
ttl_orange = 7
ttl_green = ttl_orange * 3
ttl_purple = ttl_green + ttl_orange
ttl_red = ttl_purple * .5
ttl_yellow = ttl_gummies - ttl_orange - ttl_green - ttl_purple - ttl_red
print(ttl_orange, 'orange gummies')
print(ttl_green, 'green gummies')
print(ttl_purple, 'purple gummies')
print(ttl_red, 'red gummies')
print(ttl_yellow, 'yellow gummies')

#2b
ttl_gummies = 100
ttl_orange = 8
ttl_green = ttl_orange * 3
ttl_purple = ttl_green + ttl_orange
ttl_red = ttl_purple * .5
ttl_yellow = ttl_gummies - ttl_orange - ttl_green - ttl_purple - ttl_red
print(ttl_orange, 'orange gummies')
print(ttl_green, 'green gummies')
print(ttl_purple, 'purple gummies')
print(ttl_red, 'red gummies')
print(ttl_yellow, 'yellow gummies') 

#3
MPH = 60 # minutes per hour
ttl_mday = MPH * 24
ttl_dayyear = 365
print(ttl_mday * ttl_dayyear, 'minutes per year')



