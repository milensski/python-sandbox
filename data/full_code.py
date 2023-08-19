

class ToyStore:
    def __init__(self):
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def add_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] == toy_name:
            raise Exception("Toy is already in shelf!")
        if self.toy_shelf[shelf] is not None:
            raise Exception("Shelf is already taken!")
        self.toy_shelf[shelf] = toy_name
        return f"Toy:{toy_name} placed successfully!"

    def remove_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] != toy_name:
            raise Exception("Toy in that shelf doesn't exists!")
        self.toy_shelf[shelf] = None
        return f"Remove toy:{toy_name} successfully!"



from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_initialization(self):
        shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(shelf, self.store.toy_shelf)

    def test_add_not_existing_shelf_exception(self):
        with self.assertRaises(Exception) as e:
            self.store.add_toy('H', 'abc')

        self.assertEqual("Shelf doesn't exist!", str(e.exception))

    def test_add_toy_already_existing_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.add_toy('A', 'abc')
        self.assertEqual("Toy is already in shelf!", str(e.exception))

    def test_add_toy_to_not_none_shelf_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.add_toy('A', 'dfg')
        self.assertEqual("Shelf is already taken!", str(e.exception))

    def test_add_toy_success(self):
        result = self.store.add_toy('A', 'abc')
        expect = "Toy:abc placed successfully!"
        self.assertEqual(result, expect)
        self.assertEqual('abc', self.store.toy_shelf['A'])

    def test_remove_toy_from_not_existing_shelf_exception(self):
        with self.assertRaises(Exception) as e:
            self.store.remove_toy('H', 'abc')

        self.assertEqual("Shelf doesn't exist!", str(e.exception))

    def test_remove_toy_not_existing_exception(self):
        self.store.toy_shelf['A'] = 'abc'
        with self.assertRaises(Exception) as e:
            self.store.remove_toy('A', 'abv')

        self.assertEqual("Toy in that shelf doesn't exists!", str(e.exception))

    def test_remove_toy_success(self):
        shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.store.toy_shelf['A'] = 'abc'
        result = self.store.remove_toy('A', 'abc')
        expect = "Remove toy:abc successfully!"
        self.assertEqual(result, expect)
        self.assertEqual(shelf, self.store.toy_shelf)


if __name__ == "__main__":
    main()
