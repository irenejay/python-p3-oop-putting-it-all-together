class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size  # Encapsulating size attribute
        self.condition = "New"  # Adding condition attribute with default value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
#         self.condition = "New"


# class TestShoe:
#     '''Test class for Shoe in shoe.py'''

#     def test_has_brand_and_size(self):
#         '''Tests if brand and size are set correctly during initialization.'''
#         stan_smith = Shoe("Adidas", 9)
#         assert stan_smith.brand == "Adidas"
#         assert stan_smith.size == 9

#     def test_requires_int_size(self):
#         '''Tests if "size must be an integer" is printed when size is not an integer.'''
#         stan_smith = Shoe("Adidas", 9)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         stan_smith.size = "not an integer"
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "size must be an integer\n"

#     def test_can_cobble(self):
#         '''Tests if "Your shoe is as good as new!" is output when cobble() is called.'''
#         stan_smith = Shoe("Adidas", 9)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         stan_smith.cobble()
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "Your shoe is as good as new!\n"

#     def test_cobble_makes_new(self):
#         '''Tests if cobble() creates an attribute called 'condition' and sets it to 'New'.'''
#         stan_smith = Shoe("Adidas", 9)
#         stan_smith.cobble()
#         assert stan_smith.condition == "New"
