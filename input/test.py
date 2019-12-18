import name
from name import validate_display, validate, F_ERROR

print("THIRD")
d = second.validate_display("")
if F_ERROR in d:
    print(d[F_ERROR])

"""
d = validate("18")
print(d)
second.validate_display("Albert Einstein")

print(re.match("^[A-Za-z]+$", "Emmm34"))
exit(0)
"""
