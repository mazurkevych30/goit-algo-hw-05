import timeit
from search_alg.kmp_search import kmp_search
from search_alg.boyer_moore_search import boyer_moore_search
from search_alg.rabin_karp_search import rabin_karp_search

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)

def main():
    article_one_text = load_file("data/text_1.txt")
    article_two_text = load_file("data/text_1.txt")

    test_cases = [
        ("Existing substring in file 1", article_one_text, "Усі алгоритми"),
        ("Existing substring at the beginning of the text in file 1", article_one_text, "АЛГОРИТМІВ"),
        ("Existing substring at the end of text in file 1", article_one_text, " Режим доступу до ресурсу"),

        ("Existing substring in the end file 2", article_two_text, "результати показала"),
        ("Existing substring at the beginning of the text in file 2", article_two_text, "структури даних для реалізації бази даних рекомендаційної"),
        ("Existing substring at the end of text in file 2", article_two_text, " Структуры данных и алгоритмы. М.: Вильямс, 2000"),

        ("Non-existing substring in file 1", article_one_text, "результати показала та Усі алгоритми"),
        ("Non-existing substring in file 2", article_two_text, "результати показала та Усі алгоритми"),
    ]

    search_algo = [
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Rabin-Karp", rabin_karp_search),
    ]
    for description, text, substring in test_cases:
        print(f"\n{description}:")
        results = {
            measure_time(algo[1], text, substring): algo[0] for algo in search_algo
        }
        for time_taken, algo_name in sorted(results.items()):
            print(f"{algo_name}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
