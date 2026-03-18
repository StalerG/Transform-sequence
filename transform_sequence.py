def transform_sequence(data: list, output_type: type = list, key: Callable = lambda obj: ' '.join(obj))-> list:
    """Универсальный преобразователь типов"""
    return output_type(map(key, data))
