def filmyear(film):
    return film.rsplit('(',1)[1]
with open("filmlist.txt", "r") as file:
    filmlist = file.read().splitlines()
filmlist.sort()
filmlist.sort(key=filmyear)
for film in filmlist:
    print(film)
    
