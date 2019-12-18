# Test

from name import validate_display, validate
from year import validate_year
import unittest

"""
print("THIRD")
d = (input.name).validate_display("")
if F_ERROR in d:
    print(d[F_ERROR])

d = validate("18")
print(d)
(input.name).validate_display("Albert Einstein")

print(re.match("^[A-Za-z]+$", "Emmm34"))
exit(0)

x = validate_year("1950")
print(f"retour {x} type {type(x)}")
"""


class yearTestCase(unittest.TestCase):
    """Tests for year.py"""

    def testValidateYear(self):
        t1 = validate_year("gjrujg")
        self.assertEqual(t1, "None")
        t2 = validate_year(18)
        self.assertEqual(t2, 2018)
        t3 = validate_year(97)
        self.assertEqual(t3, 1997)


if __name__ == "__main__":
    unittest.main()
