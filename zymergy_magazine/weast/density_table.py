#! /usr/bin/env python


def f_to_c(temp):
    return (temp - 32.0) / 1.8


def c_to_f(temp):
    return (temp * 1.8) + 32.0


def sg_correction_factor_zymergy(t):
    """
    Equation 4 from Zymergy Magazine

    t - Temperature in Fahrenheit
    """
    density = (1.00130346 * t**0 -
               1.34722124 * 10**-4 * t**1 +
               2.04052596 * 10**-6 * t**2 -
               2.32820948 * 10**-9 * t**3)
    return density


def density_crc_1988(t):
    """
    CRC Handbook of Chemistry and Physics
    QD65.C88 1988 c.3
    F-4 to F-5

    For purposes of this table, ordinary water is that with a maximum density
    of 999.972 kg*m**-3.

    Reprinted with permission from Kell, G.S., J. Chem. Eng. Data,
    20(1), 97, 1975. Copyright by the American Chemical Society.

    t - Temperature in Celsius
    """
    if t < -30 or t > 150:
        raise Exception("Equation not valid outside -30C to 150C")

    num = (999.83952 * 10**0 * t**0 +
           16.945176 * 10**0 * t**1 -
           7.9870401 * 10**-3 * t**2 -
           46.170461 * 10**-6 * t**3 +
           105.56302 * 10**-9 * t**4 -
           280.54253 * 10**-12 * t**5)
    den = (1 + 16.879850 * 10**-3 * t**1)
    return round(num / den, 3)


def sg_correction_factor_crc_1988(t):
    return density_crc_1988(f_to_c(60)) / density_crc_1988(t)


def main_c():
    # Temp is in Celsius
    for t in range(-30, 151):
        ct = t
        ft = c_to_f(ct)

        print("{}\t{:0.2f}\t{:0.2f}".format(
            ct
            (sg_correction_factor_crc_1988(ct) - 1) * 1000,
            (sg_correction_factor_zymergy(ft) - 1) * 1000))


def main_f():
    for t in range(32, 213):
        ft = t
        ct = f_to_c(ft)

        print("{}\t{:0.2f}\t{:0.2f}".format(
            ft,
            (sg_correction_factor_crc_1988(ct) - 1) * 1000,
            (sg_correction_factor_zymergy(ft) - 1) * 1000))


if __name__ == "__main__":
    main_f()
