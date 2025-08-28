"""Nested Ternary Operator"""

condition = 10 == 10
condition_2 = 100 == 99
var = "value" if condition else "another value"
var_2 = "value" if condition_2 else "another value"
print(var)
print(var_2)

print("VALUE" if False else "ANOTHER VALUE" if False else "END")
