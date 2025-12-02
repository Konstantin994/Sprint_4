import pytest

from main import BooksCollector

class TestBooksCollector:
    
    def test_genre_is_true(self,books_collector,genre):
        assert books_collector.genre[0] == genre[0] and books_collector.genre[1] == genre[1] and books_collector.genre[2] == genre[2] and books_collector.genre[3] == genre[3] and books_collector.genre[4] == genre[4] 
    
    def test_genre_age_rating_is_true(self,books_collector, genre_age_rating):
        assert books_collector.genre_age_rating[0] == genre_age_rating[0] and books_collector.genre_age_rating[1] == genre_age_rating[1]

    @pytest.mark.parametrize('name', ['И',
                                      'Иа',
                                      'mdqtbDshvckJoNLIWTnedIYGcUxyQfWRvLhIEhs',
                                      'CWWIcsubGsBwMrnykrmDditjtYQiLuzfDGSXkJWd'])
    def test_add_new_book_name_true(self, books_collector, name):
        books_collector.add_new_book(name)
        b_genre_k = books_collector.books_genre.keys()
        assert name in b_genre_k
    
    def test_set_book_genre(self, books_collector, genre):
        name = 'Дюна'
        expected_genre = 'Фантастика'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre[0])
        genre = books_collector.books_genre[name]
        assert genre == expected_genre
    
    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.set_book_genre("Дюна", "Фантастика")
        assert books_collector.get_books_genre() == {"Дюна": "Фантастика"}
    
    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.set_book_genre("Дюна", "Фантастика")
        assert books_collector.get_books_with_specific_genre("Фантастика") == ["Дюна"]

    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.set_book_genre("Дюна", "Фантастика")
        assert books_collector.get_books_genre() == {"Дюна": "Фантастика"}
    
    @pytest.mark.parametrize(('book', 'genre', 'book_false','genre_false'), [
                                            ["Дюна", "Фантастика","Сияние","Ужасы"],
                                            ["Белоснежка и 7 гномов", "Мультфильмы","Шерлок Холмс","Детективы"]
                                            ])
    def test_get_books_for_children(self, book, genre, book_false, genre_false, books_collector,):
        books_collector.add_new_book(book)
        books_collector.add_new_book(book_false)
        books_collector.set_book_genre(book, genre)
        books_collector.set_book_genre(book_false, genre_false)

        result = books_collector.get_books_for_children()

        assert book in result
        assert book_false  not in result
    
    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Книга")
        books_collector.add_book_in_favorites("Книга")
        assert books_collector.get_list_of_favorites_books() == ["Книга"]
    
    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Книга")
        books_collector.add_book_in_favorites("Книга")
        books_collector.delete_book_from_favorites("Книга")
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.add_book_in_favorites("Дюна")
        result = books_collector.get_list_of_favorites_books()
        assert result == ["Дюна"] 