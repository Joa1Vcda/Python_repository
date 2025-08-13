"""id"""

v1 = "a"
v2 = "b"
print(id(v1))
print(id(v2))

"""Flags,is,is not,none"""

condition = True
passed_if = None

if condition:
    passed_if = True
    print("condition is true")
else:
    print("condition is false")

print(passed_if, passed_if is None)
print(passed_if, passed_if is not None)

if passed_if is None:
    print("did not pass in if")
elif passed_if is not None:
    print("passed in if")
