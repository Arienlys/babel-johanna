from django.test import TestCase
from .utils import get_century


def test_get_century():
    yeartotest = [1701, 19, 1700, 2011, 1200, 403]
    for y in yeartotest:
        century = get_century(y)
        print(f"Année {y} siècle {century}")

    print("- " * 30)
    year_to_test = [(1701, 18), (19, 1), (1700, 17), (2011, 21), (1200, 12), (403, 5)]
    for testy in year_to_test:
        century = get_century(testy[0])
        if century == testy[1]:
            print(f"Année {testy[0]} siècle {century} : PASSED")
        else:
            print(f"Année {testy[0]} siècle {century} expected {testy[1]} : FAILED")
            raise Exception(f"TEST FAILED with {testy[0]}")


test_get_century()
