import csv

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


def fitfunc(p, x):
    return p[0] + p[1] * (x ** p[2])


def errfunc(p, x, y):
    return y - fitfunc(p, x)


def get_equation(xdata, ydata):

    qout, cov, infodict, mesg, ier = optimize.leastsq(errfunc,
                                                      [max(ydata), -1, -0.5],
                                                      args=(xdata, ydata),
                                                      maxfev=3000,
                                                      full_output=True)

    out = qout[:]
    out[0] = qout[0]
    out[1] = qout[1]
    out[2] = qout[2]

    print("{:0.6f} + {:0.6f} * x ^ {:0.6f}".format(out[0], out[1], out[2]))

    ss_err = (infodict['fvec'] ** 2).sum()
    ss_tot = ((ydata - ydata.mean()) ** 2).sum()
    rsquared = 1 - (ss_err / ss_tot)
    print(rsquared)
    return qout


def main():
    x, y = [], []

    with open('inoculation.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    xdata = np.array(x)
    ydata = np.array(y)

    qout = get_equation(xdata, ydata)
    # get_equation(ydata, xdata)

    xp = np.linspace(0, 250, num=1500)
    pxp = fitfunc(qout, xp)

    plt.plot(xdata, ydata, '.', xp, pxp, '-')
    plt.xlim(0, 250)
    plt.ylim(0, 6)
    plt.xlabel('x')
    plt.ylabel('y', rotation='horizontal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
