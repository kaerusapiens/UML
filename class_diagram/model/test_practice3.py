import unittest
from practice3 import Rectangle, Square, Client, Shape

class TestShapes(unittest.TestCase):

    def setUp(self):
        """Create instances of Rectangle and Square for testing."""
        self.rectangle = Rectangle(width=4, height=5)
        self.square = Square(length=3)
        self.client_rectangle = Client(shape=self.rectangle)
        self.client_square = Client(shape=self.square)

    def test_rectangle_area(self):
        """Test the area calculation for Rectangle."""
        self.assertEqual(self.rectangle.calc_area(), 20)  # 4 * 5 = 20

    def test_square_area(self):
        """Test the area calculation for Square."""
        self.assertEqual(self.square.calc_area(), 9)  # 3 * 3 = 9

    def test_client_rectangle_shape(self):
        """Test the Client with Rectangle."""
        self.assertIsInstance(self.client_rectangle._Client__shape, Shape)  # Verify it's a Shape

    def test_client_square_shape(self):
        """Test the Client with Square."""
        self.assertIsInstance(self.client_square._Client__shape, Shape)  # Verify it's a Shape

if __name__ == '__main__':
    unittest.main()