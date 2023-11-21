# d = {
#     'Songs': {
#         '__fields__': ['Title']
#     }
# }

d = {}

group_name = 'Songs'

fields = ['Title', 'Artist']



d[group_name] = {
    '__fields__': fields,
    '__data__': [

    ]
}

#print(d['Songs']['__fields__'])
#print(len(d['Songs']['__fields__']))

print(d['Songs']['__data__'])

song = {
    fields[0]: input(f"Enter {fields[0]}: "),
    fields[1]: input(f"Enter {fields[1]}: ")
} 

print(song)

d['Songs']['__data__'].append(song)

print()

for i, value in enumerate(d['Songs']['__data__']):
    print(i, value)
print(d['Songs']['__data__'])
print(d)



# nums = [2, 3, 4]

# target = 6

# def twoSum(nums, target):
#     seen = {}
#     for i, value in enumerate(nums):
#         print(value)


# twoSum(nums, target)