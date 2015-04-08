def compare(item):
    return searchfor in item.lower()
with open("filmlist.txt", "r") as film:
    filmlist = film.read().splitlines()
searchfor = input("Enter part of the film \
name you are searching for: ").lower().strip()
foundlist = filter(compare, filmlist)
for name in foundlist:
    print(name)
    
