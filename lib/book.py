class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count  # Encapsulating page_count attribute

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



# class TestBook:
#     '''Test class for Book in book.py'''

#     def test_has_title_and_page_count(self):
#         '''Tests if title and page_count are set correctly during initialization.'''
#         book = Book("And Then There Were None", 272)
#         assert book.page_count == 272
#         assert book.title == "And Then There Were None"

#     def test_requires_int_page_count(self):
#         '''Tests if "page_count must be an integer" is printed when page_count is not an integer.'''
#         book = Book("And Then There Were None", 272)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.page_count = "not an integer"
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "page_count must be an integer\n"

#     def test_can_turn_page(self):
#         '''Tests if "Flipping the page...wow, you read fast!" is output when turn_page() is called.'''
#         book = Book("The World According to Garp", 69)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.turn_page()
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
