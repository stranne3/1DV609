import sympy

# Tests all of what is inside sympy
sympy.test()

# Parts of sympy can also be tested using the following code
# The following code just tests what is contained within the basic.py file (part of the core)
sympy.test("sympy/core/tests/test_basic.py")
sympy.test("_basic")

# Results from first test 2021-12-13 https://www.toptal.com/developers/hastebin/ucexasucaq.sql
