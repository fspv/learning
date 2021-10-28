import logging
import random
import sys
from functools import lru_cache
from typing import List, Tuple, Union

"""
Ниже приведены два подхода к решению задачи. Сначала я объясню top-down решение, так как оно более интуитивно понятное, после объясню, как получить bottom-up решение.

Эта задача - задача на динамическое программирование (DP). Но в любых DP задачах лучше всего начинать думать о задаче не как о задаче на DP, а сначала придумать брутфорс решение.

В условии нам явно сказано, что надо расставить скобки оптимальным образом. В качестве брутфорс решения тут мы можем попробовать расставить скобки всеми возможными способами, а потом выбрать из них самый оптимальный.

Давайте предположим, что у нас есть некоторое количество матриц:

A B C D E F G

Теперь давайте попробуем поставить скобки где-нибудь. Например, мы можем разделить матрицы скобками на 2 части вот так

(A B C) (D E F G)

Теперь у нас есть 2 произведения слева и справа, которые мы можем перемножить друг с другом, после их вычисления.

Теперь мы можем рекурсивно пойти в левую и правую часть и также поставить там скобки. Например, для левой части, вот так

((A B) C)

Или вот так

(A (B C))

Таким образом мы видимо, что у нас много опций как расставить скобки и мы можем перебрать их все, ставя скобку в произвольном месте, рекурсивно спускаясь в левую и правую часть выражения и повторяя операцию там.

Впоследствие мы можем написать что-то вроде вот такого рекурсивного выражения (не забывая про базовый случай, когда нечего больше делить, то есть остались всего 2 матрицы)

    def backtrack(left: int, right: int) -> int:
        if left >= right:
            return 0

        min_ops = float("+inf")

        for middle in range(left, right):
            ops_left = backtrack(left, middle)
            ops_right = backtrack(middle + 1, right)

            n_left, m_left = matrices[left][0], matrices[middle][1]
            n_right = matrices[right][1]

            ops = ops_left + ops_right + n_left * m_left * n_right
            min_ops = min(min_ops, ops)

        return int(min_ops)

С помощью этой рекурсии мы получаем брутфорс решение, перебирая все возможные опции.
Тут добавляется лишь немного математики, для вычисления непосредственно количества операций. Фактически, когда мы делим все произведение посередине, нас интересуют только размеры крайних матриц и матриц около точки раздела. Потому что все, что внутри в любом случае схлопнется в одну матрицу при перемножении. Оставлю объяснение этого на суд читателя, так как это имеет мало отношения непосредственно к алгоритму.

Теперь возвращаемся к тому факту, что это DP задача. Посмотрев на нашу рекурсию, мы видимо, что у каждого вызова рекурсии всего 2 параметра - указатели left и right. Каждый из этих указателей может принимать N значений. А значит, возможно всего N^2 комбинаций этих параметров. Мы же создаем дерево рекурсии, в котором делаем намного больше вызовов. Это значит, что часть из этих вызовов будет повторяться. И нет никаких предпосылок к тому, чтобы эти вызовы возвращали разные результаты, так как они не зависят ни от каких внешних переменных. Следовательно, мы можем легко закешировать эти вызовы, сводя полную сложность алгоритма к O(N^2) как по времени, так и по памяти. Таким образом мы получили top down DP решение.

Для получение bottom up (нерекурсивного) решения, нам нужно лишь сделать одно небольшое наблюдение. Мы кешируем значения вызовов рекурсивной функции в кеше размерности N x N, где перебираем все возможные значения left и right.  Это значит, что мы можем просто перебирать все значения left и right в цикле и вместо вызовов рекурсивной функции dp обращаться к аналогичной таблице. Таким образом, переписывая наше top down решение строчка за строчкой, и применяя вышеуказанные трансформации, мы получим bottom up решение, которое будет более выгодно в том плане, что мы не упремся в лимит размера стека рекурсии.
"""


def optimal_parentheses_top_down(matrices: List[Tuple[int, int]]) -> int:
    @lru_cache(None)
    def dp(left: int, right: int) -> int:
        if left >= right:
            return 0

        min_ops = float("+inf")

        for middle in range(left, right):
            ops_left = dp(left, middle)
            ops_right = dp(middle + 1, right)

            n_left, m_left = matrices[left][0], matrices[middle][1]
            n_right = matrices[right][1]

            ops = ops_left + ops_right + n_left * m_left * n_right
            min_ops = min(min_ops, ops)

        return int(min_ops)

    return dp(0, len(matrices) - 1)


def optimal_parentheses_bottom_up(matrices: List[Tuple[int, int]]) -> int:
    dp: List[List[Union[int, float]]] = [
        [float("+inf")] * len(matrices) for _ in matrices
    ]

    for pos in range(len(matrices)):
        dp[pos][pos] = 0

    for left in reversed(range(len(matrices))):
        for right in range(left, len(matrices)):
            for middle in range(left, right):
                ops_left = dp[left][middle]
                ops_right = dp[middle + 1][right]

                n_left, m_left = matrices[left][0], matrices[middle][1]
                n_right = matrices[right][1]

                ops = ops_left + ops_right + n_left * m_left * n_right

                dp[left][right] = min(dp[left][right], ops)

    return int(dp[0][len(matrices) - 1]) if matrices else 0


def get_number_of_matrices() -> int:
    line = sys.stdin.readline()

    try:
        number_of_matrices = int(line)
    except ValueError:
        logging.exception(f"Can't parse: {line}")

    return number_of_matrices


def get_matrix() -> Tuple[int, int]:
    line = sys.stdin.readline()

    try:
        n_str, m_str = line.strip().split(" ")
        output = int(n_str), int(m_str)
    except ValueError:
        logging.exception(f"Can't parse: {line}")

    return output


def main() -> None:
    matrices: List[Tuple[int, int]] = []
    for _ in range(get_number_of_matrices()):
        matrices.append(get_matrix())

    print(optimal_parentheses_bottom_up(matrices))


if __name__ == "__main__":
    main()


class TestOptimalParenthesesTopDown:
    def test_empty(self) -> None:
        assert optimal_parentheses_top_down([]) == 0

    def test_case1(self) -> None:
        assert optimal_parentheses_top_down([(1, 2), (2, 8), (8, 4)]) == 48

    def test_case2(self) -> None:
        assert optimal_parentheses_top_down([(10, 100)]) == 0

    def test_case3(self) -> None:
        assert optimal_parentheses_top_down([(3, 2), (2, 4), (4, 1), (1, 5)]) == 29


class TestOptimalParenthesesBottomUp:
    def test_empty(self) -> None:
        assert optimal_parentheses_bottom_up([]) == 0

    def test_case1(self) -> None:
        assert optimal_parentheses_bottom_up([(1, 2), (2, 8), (8, 4)]) == 48

    def test_case2(self) -> None:
        assert optimal_parentheses_bottom_up([(10, 100)]) == 0

    def test_case3(self) -> None:
        assert optimal_parentheses_bottom_up([(3, 2), (2, 4), (4, 1), (1, 5)]) == 29

    def test_large1(self) -> None:
        matrices: List[Tuple[int, int]] = [(10, 30)]

        prev_m = 30

        for _ in range(299):
            this_n = random.randint(1, 100)
            matrices.append((prev_m, this_n))

        optimal_parentheses_bottom_up(matrices)

    def test_large2(self) -> None:
        matrices: List[Tuple[int, int]] = [(10, 30)]

        prev_m = 30

        for _ in range(500):
            this_n = random.randint(1, 100)
            matrices.append((prev_m, this_n))

        optimal_parentheses_bottom_up(matrices)
