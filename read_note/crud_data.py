import pandas as pd


class CRUD:
    """Class implements reading, creating, and deleting methods from a csv file"""

    @classmethod
    def read(cls, path):
        """Method returns data from csv file"""

        try:
            notes = pd.read_csv(path)
        except FileNotFoundError:
            print('FileNotFoundError, check file path')
            return None

        return notes

    @classmethod
    def add(cls, path):
        """Method adds row to csv file. User enters data"""
        try:
            name = input('write film name: ')
            note = input('write note: ')
            rate = int(input('write rating: '))
        except ValueError:
            print('Value Error, check entry data')
            return None
        new_note = pd.DataFrame({'film_name': [name], 'note': [note], 'rating': [rate]})
        new_note.to_csv(path, mode='a', index=False, header=False)

    @classmethod
    def remove(cls, path):
        """Method remove row from table by its name. User enters name"""
        notes = cls.read(path)
        name = input('write film name: ')
        notes.drop(notes[notes['film_name'] == name].index, inplace=True)
        notes.to_csv(path)

    @classmethod
    def read_to_console(cls, path):
        """Method print notes to console"""
        notes = cls.read(path)
        for i in notes.values:
            print(f'Film name: {i[0]}, Note: {i[1]}, Rating: {i[2]}')


class GetRating(CRUD):
    """Class returns movies based on their rating.
    Class is inherited from CRUD to use the read method"""

    @classmethod
    def get_highest_rating(cls, path):
        """Method returns the movies with the highest rating"""
        notes = cls.read(path)
        filter = notes[notes['rating'] == notes['rating'].max()]
        return [i[0] for i in filter.values]

    @classmethod
    def get_lowest_rating(cls, path):
        """Method returns the movies with the lowest rating"""
        notes = cls.read(path)
        filter = notes[notes['rating'] == notes['rating'].min()]
        return [i[0] for i in filter.values]

    @classmethod
    def get_avg_rating(cls, path):
        """Method returns average movie rating"""
        notes = cls.read(path)
        return notes['rating'].mean()
