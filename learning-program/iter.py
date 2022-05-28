import sys

list = ["aofeng", "caizai", "laoma", "haha"]
it = iter(list)

# for x in it :
#     print(x, end = " ")
# print("\n" + str(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()