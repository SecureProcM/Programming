# Creted a list of 5 movies
Movies = ["Avatar","Black Panther","Cars","jumanji","spiderman into the spider verse"]
print(Movies)
# add the movie grinch after as the first movie listed
Movies.insert(1,"The Grinch")
print(Movies)
# print the movie in the number 1 position
print(Movies[1])
# then i added another movie to list called jingle all the way
Movies[-1] = "Jingle all the way"
print(Movies)
# then added santa paws at the end of the list
Movies.append("Santa  Paws")
print(Movies)

# check if the grinch is in the movie list and if it Christmas is coming
if "The Grinch" in Movies: 
    print("Christmas is coming")
