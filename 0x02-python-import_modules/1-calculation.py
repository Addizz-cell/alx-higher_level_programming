#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    add_ = add(a, b)
    sub_ = sub(a, b)
    div_ = div(a, b)
    mul_ = mul(a, b)
    print("{} + {} = {}".format(a, b, add_))
    print("{} - {} = {}".format(a, b, sub_))
    print("{} * {} = {}".format(a, b, mul_))
    print("{} / {} = {}".format(a, b, div_))
