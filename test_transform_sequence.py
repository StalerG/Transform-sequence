import unittest
from transform_sequence import transform_sequence

class TestTransformSequence(unittest.TestCase):
    
    def setUp(self):
        """Подготовка тестовых данных"""
        self.names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez')]
        self.numbers = [1, 2, 3, 4, 5]
    
    def test_default_behavior(self):
        """Тест поведения по умолчанию (список, через пробел)"""
        result = transform_sequence(self.names)
        expected = ['Gerald Tucker', 'Tricia Johnson', 'Robert Mendez']
        self.assertEqual(result, expected)
    
    def test_different_separator(self):
        """Тест с другим разделителем"""
        result = transform_sequence(self.names, key=lambda x: '-'.join(x))
        expected = ['Gerald-Tucker', 'Tricia-Johnson', 'Robert-Mendez']
        self.assertEqual(result, expected)
    
    def test_no_separator(self):
        """Тест без разделителя"""
        result = transform_sequence(self.names, key=lambda x: ''.join(x))
        expected = ['GeraldTucker', 'TriciaJohnson', 'RobertMendez']
        self.assertEqual(result, expected)
    
    def test_output_type_tuple(self):
        """Тест с возвратом кортежа"""
        result = transform_sequence(self.names, output_type=tuple)
        expected = ('Gerald Tucker', 'Tricia Johnson', 'Robert Mendez')
        self.assertEqual(result, expected)
    
    def test_with_numbers(self):
        """Тест с числами (квадраты)"""
        result = transform_sequence(self.numbers, key=lambda x: x**2)
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(result, expected)
    
    def test_empty_input(self):
        """Тест с пустым списком"""
        result = transform_sequence([])
        self.assertEqual(result, [])
    
    def test_complex_transformation(self):
        """Тест сложного преобразования (Фамилия, И.)"""
        result = transform_sequence(self.names, key=lambda x: f'{x[1]}, {x[0][0]}.')
        expected = ['Tucker, G.', 'Johnson, T.', 'Mendez, R.']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
