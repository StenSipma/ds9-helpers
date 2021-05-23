#!/usr/bin/env python3
from pyds9 import DS9
from pprint import pprint


def format_widths(x, y):
    return min(x, y) // 2


def convert(regions):
    # Wroks only for the box regions,
    values = [
        tuple(map(float, vals[4:-1].split(","))) for vals in regions.split(";")
    ]
    formatted_values = [
        ((x, y), format_widths(w_x, w_y)) for x, y, w_x, w_y, rot in values
    ]
    return formatted_values


if __name__ == "__main__":
    d = DS9()  # establish connection
    # r = d.get(b"regions -format ciao")  # get regions
    r = d.get("regions -format ds9 -strip yes")  # get regions
    # pprint(to_list(r))  # format regions
    for reg in r.split(";")[1:]:
        try:
            start = reg.index("(")
        except Exception:
            pass
        else:
            inner = reg[start + 1 : -1]
            reg_type = reg[:start]
            values = [float(val) for val in inner.split(",")]
            print(f"{reg_type:8} : {values}")
