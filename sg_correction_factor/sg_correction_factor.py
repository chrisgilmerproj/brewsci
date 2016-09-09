"""

Brew By the Numbers - Add Up What’s in Your Beer
ZYMURGY Summer 1995

    Corrected SG = density of wort at T / density of water at T

                 =   density of wort at T     density of water at 60F
                   ------------------------ x -----------------------
                   density of water at 60 F    density of water at T

                 = (Measured SG at T) (SG correction factor)

This correction factor is solely a function of the density of water at
various temperatures, which is well-known. I made a curve fit to some data from
a couple of sources (De Clerck, Weast) that yielded the SG correction factor as
a function of measuring temperature (T in Fahrenheit):

    SG correction factor = 1.00130346 – 1.34722124 x 10-4 T + 2.04052596 x 10-6 T2 – 2.32820948 x 10-9 T3

This equation is accurate over the entire region from 32 degrees F to 212
degrees F.
"""  # nopep8
