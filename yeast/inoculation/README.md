# Inoculation Rate

Several websites use data compiled by Chris White and Jamil Zainasheff in a
book they wrote about yeast:

White, Chris, and Jamil Zainasheff.
Yeast: The Practical Guide to Beer Fermentation.
Boulder, CO: Brewers Publications, 2010. 139-44. Print.

The data for Inoculation Rate (B/L) vs Yeast Growth Rate was placed into a file
named `inoculation.csv`.  Using this data and the script in `fit_data.py` I
was able to confirm the equation given by Brewer's Friend:

    G = (12.54793776 * x^-0.4594858324) - 0.9994994906
    R2 = 0.999990

Where x is the inoculation rate and G is the growth rate.

This is ok if you already have the inoculation rate but not so helpful if you
only have the growth rate and need to get the inoculation rate. Here is the
reverse equation:

    a = - 0.9994994906
    b = 12.54793776 
    c = -0.4594858324

    x = 10 ** log10( b / (G - a) / c)

To interact with this data you can open up the notebook `inoculation.ipynb` and
graph the results.

```sh
$ jupyter notebook inoculation.ipynb
```

Source:
- http://www.brewersfriend.com/yeast-pitch-rate-and-starter-calculator/
- http://beersmith.com/blog/2011/01/10/yeast-starters-for-home-brewing-beer-part-2/
