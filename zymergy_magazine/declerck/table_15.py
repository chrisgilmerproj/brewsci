#! /usr/bin/env python

"""
Balling's Table
From deClerck - A Textbook of Brewing 1958
Vol 2, p428, Table 15

p - % original extract
q - attenuation quotient
n - real extract
m - apparent extract
A%w - Alcohol percent by weight

TODO: Unclear how to get p-m
"""


def main():
    print("p\tq\t1/q\tA%w/(p-m)\tA%w/(p-n)\tA%w/(n-m)")
    for p in xrange(1, 21):
        q = 0.22 + 0.001 * p
        q_inv = 1 / q
        p_n = 1 / (2.0665 - 0.010665 * p)
        n_m = p_n * q_inv
        p_m = 0.0

        print("{}\t{:0.3f}\t{:0.3f}\t{:0.4f}\t\t{:0.4f}\t\t{:0.4f}".format(
            p, q, q_inv, p_m, p_n, n_m))


if __name__ == "__main__":
    main()
