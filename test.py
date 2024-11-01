def is_even(num):
    return num % 2 == 0

def divide(a, b):
    return a / b

# Тесты
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(-2) == True
    assert is_even(0) == True

def test_divide():
    try:
        divide(10, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

# Запуск тестов
if __name__ == "__main__":
    test_is_even()
    test_divide()
    print("All tests passed!")
