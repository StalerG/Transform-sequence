# 🔄 Transform-sequence

Универсальный преобразователь последовательностей, позволяющий гибко менять формат данных с помощью кастомных функций. Идеально подходит для обработки списков кортежей, например, для форматирования имен.

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## ✨ Возможности

- 🔄 **Универсальность** — работает с любыми последовательностями (списки, кортежи, множества)
- 🛠 **Гибкость** — можно передать любую функцию для преобразования данных
- 🛡 **Безопасность** — проверка входных данных на корректность
- 📝 **Типизированный код** — полная поддержка IDE и type hints
- 🎯 **Простота использования** — интуитивно понятный API

## 🚀 Установка

```bash
# Клонируем репозиторий
git clone https://github.com/StalerG/transform-sequence.git
cd transform-sequence

# Никаких зависимостей — чистый Python!
```

## 💡 Примеры использования

### 1. Базовое использование (склейка имён)
```python
from transform_sequence import transform_sequence

names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez')]

# По умолчанию — через пробел
result = transform_sequence(names)
print(result)
# ['Gerald Tucker', 'Tricia Johnson', 'Robert Mendez']
```

### 2. Разные разделители
```python
# Без разделителя
result = transform_sequence(names, key=lambda x: ''.join(x))
print(result)
# ['GeraldTucker', 'TriciaJohnson', 'RobertMendez']

# Через дефис
result = transform_sequence(names, key=lambda x: '-'.join(x))
print(result)
# ['Gerald-Tucker', 'Tricia-Johnson', 'Robert-Mendez']
```

### 3. Разные типы возврата
```python
# Кортеж вместо списка
result = transform_sequence(names, output_type=tuple)
print(result)
# ('Gerald Tucker', 'Tricia Johnson', 'Robert Mendez')
```

### 4. Работа с числами
```python
numbers = [1, 2, 3, 4, 5]

# Квадраты чисел
result = transform_sequence(numbers, key=lambda x: x**2)
print(result)
# [1, 4, 9, 16, 25]
```

### 5. Сложные преобразования
```python
# Фамилия, И. (инициалы)
result = transform_sequence(names, key=lambda x: f'{x[1]}, {x[0][0]}.')
print(result)
# ['Tucker, G.', 'Johnson, T.', 'Mendez, R.']
```

## 📦 API

```python
def transform_sequence(
    data: list, 
    output_type: type = list, 
    key: Callable = lambda obj: ' '.join(obj)
) -> list:
    """
    Универсальный преобразователь последовательностей.
    
    Args:
        data: Входная последовательность (список)
        output_type: Тип возвращаемого объекта (list, tuple, set и т.д.)
        key: Функция преобразования для каждого элемента
    
    Returns:
        Преобразованная последовательность указанного типа
    """
```

## 🧪 Тесты

```python
# Запуск тестов
python -m unittest test_transform_sequence.py
```

## 🤝 Как помочь проекту

Буду рад любым предложениям и улучшениям!
- 🐛 Создавайте [issue](https://github.com/StalerG/transform-sequence/issues) для багов
- 💡 Предлагайте новые фичи
- 🔧 Отправляйте pull request'ы

## 📜 Лицензия

Проект распространяется под лицензией MIT.  
Copyright (c) 2026 Vadim - StalerG

Подробнее в файле [LICENSE](LICENSE).

## 📫 Контакты

- GitHub: [@StalerG](https://github.com/StalerG)
- Telegram: [@S_ta_le_rG](https://t.me/S_ta_le_rG)

---

⭐ Если проект оказался полезным — поставьте звёздочку на GitHub!
