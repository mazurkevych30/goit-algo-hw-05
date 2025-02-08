def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def build_good_suffix_table(pattern):
    """Створити таблицю добрих суфіксів для алгоритму Боєра-Мура."""
    length = len(pattern)
    good_suffix = [-1] * length
    border = length

    for i in range(length - 1, -1, -1):
        if i == length - 1 or pattern[i] != pattern[length - 1]:
            border = i + 1
        good_suffix[length - 1 - i] = border

    for i in range(1, length):
        if good_suffix[i] == -1:
            good_suffix[i] = good_suffix[i - 1]

    return good_suffix

def boyer_moore_search(text, pattern):
    """Здійснити пошук підрядка за допомогою алгоритму Боєра-Мура."""
    shift_table = build_shift_table(pattern)
    good_suffix = build_good_suffix_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів і добрих суфіксів
        char_shift = shift_table.get(text[i + len(pattern) - 1], len(pattern))
        suffix_shift = good_suffix[j] if j >= 0 else len(pattern)
        i += max(char_shift, suffix_shift)

    # Якщо підрядок не знайдено, повертаємо -1
    return -1
