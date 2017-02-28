# Timmermans

Timmermans, Jean, The Physico-Chemical Constants of Binary
Systems in Concentrated Solutions, Vol. 4: Systems with Inorganic and Organic or Inorganic Compounds, Interscience Publishers, 1960.

## Equations

To convert back and forth between extract (E) in degrees Plato and specific
gravity (SG), you can use these equations:

Eq7
E = -668.962 + 1262.45 * SG - 776.43 * SG**2 + 182.94 * SG**3

Eq8
SG = 1.00001 + 0.0038661 * E + 1.3488 * 10**-5 * E**2 + 4.3074 * 10**-8 * E**3

These equations are accurate cubic fits that I did to Plato’s data (Timmermans)
over the range of 0 to 33  ̊P, which covers specific gravities between
1.000 and 1.144. 

It appears that he fit the data from the table at 15degC (which is
approximately 60degF.  This is helpful since we can look at only one column
of data from 0 to 33P.
