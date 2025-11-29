<!-- @format -->

### API Query Features

**Filtering:**  
Filter books by title, author (ID), or publication year.

- `/api/books/?title=Hobbit`
- `/api/books/?author=2`
- `/api/books/?publication_year=1937`

**Searching:**  
Search books by their title or author name (case-insensitive, partial match).

- `/api/books/?search=tolkien`
- `/api/books/?search=ring`

**Ordering:**  
Order results by `title` or `publication_year` (add '-' for descending order).

- `/api/books/?ordering=publication_year`
- `/api/books/?ordering=-title`

You can combine filters:

- `/api/books/?search=tolkien&ordering=-publication_year`

**Implementation:**  
These features are provided by Django REST Framework’s filtering system, configured in `api/views.py`:

```python
filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author__name']
ordering_fields = ['title', 'publication_year']
```
