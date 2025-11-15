# lib/MySet.py
class MySet:
    """A custom set implementation using a dictionary."""

    def __init__(self, iterable=None):
        """Initializes the set, using a dictionary to store elements."""
        self.dictionary = {}
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, element):
        """Adds an element to the set."""
        # Using the element as the key and a constant value (like True)
        # as the dictionary value, which is typical for set implementations.
        self.dictionary[element] = True

    def delete(self, element):
        """Removes an element from the set if it exists."""
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        """Checks if an element is present in the set."""
        return element in self.dictionary

    # The test `test_size` checks `len(test_set.dictionary)`, so no explicit
    # `size()` method is strictly needed for those tests to pass, but
    # providing a `__len__` method is idiomatic for Python collections.
    def __len__(self):
        """Returns the number of elements in the set."""
        return len(self.dictionary)

    # Implement the Bonus Tests if you uncomment them:

    def clear(self):
        """Removes all elements from the set."""
        self.dictionary.clear()

    def __str__(self):
        """Returns a string representation of the set."""
        # This implementation matches the required output: 'MySet: {1,2,3,4}'
        elements = ",".join(map(str, sorted(self.dictionary.keys())))
        return f"MySet: {{{elements}}}"