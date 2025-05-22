import pytest


class TestBooksCollector:

    def test_add_valid_book(self, collector):
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""

    def test_add_duplicate_book(self, collector):
        collector.add_new_book("1984")
        collector.add_new_book("1984")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("name, expected", [
        ("A" * 40, True),
        ("A" * 41, False),
        ("", False)
    ])
    def test_add_books_with_different_lengths(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    def test_set_valid_genre(self, collector):
        collector.books_genre["Ночной дозор"] = ""
        collector.set_book_genre("Ночной дозор", "Фантастика")
        assert collector.books_genre["Ночной дозор"] == "Фантастика"

    def test_set_invalid_genre(self, collector):
        collector.books_genre["Собачье сердце"] = ""
        collector.set_book_genre("Собачье сердце", "История")
        assert collector.books_genre["Собачье сердце"] == ""

    def test_get_book_genre_for_existing_book(self, collector):
        collector.books_genre = {"Преступление и наказание": "Детективы"}
        assert collector.get_book_genre("Преступление и наказание") == "Детективы"

    def test_get_book_genre_for_book_without_genre(self, collector):
        collector.books_genre = {"Война и мир": ""}
        assert collector.get_book_genre("Война и мир") == ""

    def test_get_nonexistent_book_genre(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_get_books_by_genre(self, collector):
        collector.books_genre = {
            "Книга1": "Детективы",
            "Книга2": "Детективы",
            "Книга3": "Фантастика"
        }
        result = collector.get_books_with_specific_genre("Детективы")
        assert result == ["Книга1", "Книга2"]

    def test_get_books_by_nonexistent_genre(self, collector):
        collector.books_genre = {"Книга1": "Детективы"}
        assert collector.get_books_with_specific_genre("История") == []

    def test_get_children_books(self, collector):
        collector.books_genre = {
            "Ну погоди!": "Мультфильмы",
            "Оно": "Ужасы",
            "Маугли": "Мультфильмы"
        }
        result = collector.get_books_for_children()
        assert result == ["Ну погоди!", "Маугли"]

    def test_add_to_favorites(self, collector):
        collector.books_genre = {"Мастер и Маргарита": ""}
        collector.add_book_in_favorites("Мастер и Маргарита")
        assert "Мастер и Маргарита" in collector.favorites

    def test_add_to_favorites_twice(self, collector):
        collector.books_genre = {"Преступление и наказание": ""}
        collector.add_book_in_favorites("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")
        assert len(collector.favorites) == 1

    def test_add_nonexistent_book_to_favorites(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert len(collector.favorites) == 0

    def test_remove_from_favorites(self, collector):
        collector.favorites = ["Анна Каренина"]
        collector.delete_book_from_favorites("Анна Каренина")
        assert "Анна Каренина" not in collector.favorites

    def test_remove_nonexistent_from_favorites(self, collector):
        collector.delete_book_from_favorites("Несуществующая книга")
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ["Книга1", "Книга2"]
        assert collector.get_list_of_favorites_books() == ["Книга1", "Книга2"]

    def test_get_empty_list_of_favorites(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_all_books(self, collector):
        collector.books_genre = {"Книга1": "", "Книга2": ""}
        assert collector.get_books_genre() == {"Книга1": "", "Книга2": ""}

    def test_get_empty_books_collection(self, collector):
        assert collector.get_books_genre() == {}

    def test_initial_state(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']