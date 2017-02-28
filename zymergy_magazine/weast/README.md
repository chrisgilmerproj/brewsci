# Weast 

The equation to reproduce is:

    SG Factor = 1.00130346 - 1.34722124 * 10**-4 * T + 2.04052596 * 10**-6 * T**2 - 2.32820948 * 10**-9 * T**3

I found the 1988 Version of this instead of the 1980 version.

The definition of the SG Correction Factor comes from this equation:

Corrected SG = (density of wort at T) / (density of water at T)

But this is further explained where:

Corrected SG = ((density of wort at T) / (density of water at 60F)) * ((density of water at 60F) / (density of water at T))

Corrected SG = (measured SG at T) * (SG correction factor)

so we can see:

SG Correction Factor = (density of water at 60F) / (density of water at T)
