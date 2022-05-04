"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = [{'India': ['Bangalore']}]
locations['Asia'].append({'China': ['Shanghai']})
locations['Africa'] = {'Egypt': ['Cairo']}
#locations.append({'Africa': {'Egypt': ['Cairo']}})
locations['North America']['USA'].append('Atlanta')

index = 1
for location in locations:
    if location == "North America":
        print(index)
        index += 1
        for usa_city in sorted(locations[location]['USA']):
            print(usa_city)
    if location == "Asia":
        print(index)
        index += 1
        for asian_country in locations[location]:
            for as_c, as_c_c in asian_country.items():
                for city in as_c_c:
                    print(city, "-", as_c)
    

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""