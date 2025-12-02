import pytest

from main import BooksCollector

@pytest.fixture
def books_collector():
    books_collector = BooksCollector()

    return books_collector

@pytest.fixture
def genre():
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    return genre

@pytest.fixture
def genre_age_rating():
    genre_age_rating = ['Ужасы', 'Детективы']

    return genre_age_rating