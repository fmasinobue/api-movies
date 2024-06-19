

from review import Review
from movie import Movie

print("Hola ....")


# revAll = Review.get_all()

# for rev in revAll:
#     print(rev)

# revOne = Review.get_by_id(40)
# print(revOne)



todasPelis=Movie.get_all()

print("ANTES: ",len(todasPelis))


unaPeli = Movie(5, "TESThola23",False,2025,"")
unaPeli2 = Movie(None, "HARRYTEST",False,2025,"")

unaPeli2.save()

print(unaPeli)


todasPelis=Movie.get_all()

print("DESPUES: ",len(todasPelis))