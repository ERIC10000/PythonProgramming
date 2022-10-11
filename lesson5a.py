# Sequencial
# Decisional
# Repetitions - > A block(group) of code is repeated based on conditions -> Loops
# for loop
# while loop

# for
# # strings
# name = "MODCOM"
# for check in name:
#     print(check)
#
# # a list
countries = ["South aafrica", "Somalia", "Uganda", " Tanzania", " Kenya"]
#
for country in countries:

    if country == "Uganda":
        continue
    print(country)
#
# break -> Terminates the loop if the condition is reached
# continue -> Skips the items

# loops using range function
# range -> start, limit, increament
#
for count in range(3,10, 2):
    print(count)


# Write a code that will loop through a list of 10 counties in Kenya, then adds counties with two names
# inside a nwe list
# print the new list

# counties = ["Nairobi", "Uasin Gishu", "Tana River", "Taita Taveta", "Mombasa", "Wajir", "Nyandarua", "Homa Bay",
#             "Nakuru", "Tharaka Nithi"]
# print(len(counties))
#
# newList = []
#
# # if " " in county:
# for county in counties:
#     if " " not in county:
#         newList.append(county)
#         print(newList)
