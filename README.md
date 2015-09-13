[![Build Status](https://travis-ci.org/0x07Ltd/django-generic-counter.svg?branch=master)](https://travis-ci.org/0x07Ltd/django-generic-counter)
django-generic-counter
======================

This small Django app provides a simple "Counter" model which consists of a `name` and an integer
`count`. It can be used any time you need to keep a tally of something, or store an arbitrary number
in the database.

Usage
-----

Include `django_generic_counter` in your `INSTALLED_APPS`, then use the Counter like so:

```python
from django_generic_counter import Counter

c = Counter(name="Green bottles hanging on the wall", count=10)
assert int(c) == 10, "Ten green bottles hanging on the wall"
assert c.count == 10, "Ten green bottles hanging on the wall"
c -= 1  # And if one green bottle should accidentally fall
assert int(c) == 9, "There'll be nine green bottles hanging on the wall"
```

The following are features of the Counter object:
- Assignment addition `c += 10`
- Assignment subtraction `c -= 10`
- Cast to int `int(c)`

Usage with South
----------------

The migrations for this project in the `migrations` directory have been made using Django 1.8. This means that if you're using South you must tell it to look in the `south_migrations` directory for its migrations by putting the following in your settings file:

```python
SOUTH_MIGRATION_MODULES = {
    'django_generic_counter': 'django_generic_counter.south_migrations'
}
```
