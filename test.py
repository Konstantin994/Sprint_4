import pytest

from main import BooksCollector

class TestBooksCollector:
    
    def test_genre_is_true(self,books_collector):
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre == genre
    
    def test_genre_age_rating_is_true(self,books_collector):
        genre_age_rating = ['Ужасы', 'Детективы']
        assert books_collector.genre_age_rating == genre_age_rating

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
        books_collector.add_new_book("Сияние")
        books_collector.add_new_book("Шерлок Холмс")

        books_collector.set_book_genre("Дюна", "Фантастика")
        books_collector.set_book_genre("Сияние", "Ужасы")
        books_collector.set_book_genre("Шерлок Холмс", "Детективы")

        expected = {
        "Дюна": "Фантастика",
        "Сияние": "Ужасы",
        "Шерлок Холмс": "Детективы"
        }

        assert books_collector.get_books_genre() == expected
    
    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.add_new_book("Сияние")
        books_collector.add_new_book("Шерлок Холмс")

        books_collector.set_book_genre("Дюна", "Фантастика")
        books_collector.set_book_genre("Сияние", "Ужасы")
        books_collector.set_book_genre("Шерлок Холмс", "Фантастика")

        result = books_collector.get_books_with_specific_genre("Фантастика")

        assert "Дюна" in result
        assert "Шерлок Холмс" in result
        assert "Сияние" not in result

    def test_get_books_genre(self, books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.add_new_book("Сияние")
        books_collector.add_new_book("Шерлок Холмс")

        books_collector.set_book_genre("Дюна", "Фантастика")
        books_collector.set_book_genre("Сияние", "Ужасы")
        books_collector.set_book_genre("Шерлок Холмс", "Детективы")

        expected = {
        "Дюна": "Фантастика",
        "Сияние": "Ужасы",
        "Шерлок Холмс": "Детективы"
        }

        assert books_collector.get_books_genre() == expected
    
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