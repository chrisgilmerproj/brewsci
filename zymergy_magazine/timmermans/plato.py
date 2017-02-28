

def sg_to_plato_zymergy(sg):
    plato = (-668.962 * sg**0 +
             1262.45 * sg**1 -
             776.43 * sg**2 +
             182.94 * sg**3)
    return plato


def plato_to_sg_zymergy(plato):
    sg = (1.00001 * plato ** 0 +
          0.0038661 * plato ** 1 +
          1.3488 * 10**-5 * plato**2 +
          4.3074 * 10**-8 * plato**3)
    return sg


def sg_to_plato(sg):
    """
    Timmermans
    Physico-Chemical Constants of Binary Systems
    Volume 4
    QD 453 T56 v.4
    p302 - p303
    """


def main():
    pass


if __name__ == "__main__":
    main()
