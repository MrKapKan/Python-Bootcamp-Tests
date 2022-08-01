from read_note.crud_data import CRUD, GetRating


path = '../read_note/Note.csv'

print(CRUD.read(path))
# CRUD.add(path)
CRUD.read_to_console(path)
# CRUD.remove(path)
print(GetRating.get_highest_rating(path))
print(GetRating.get_avg_rating(path))
print(GetRating.get_lowest_rating(path))
