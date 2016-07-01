
import numpy as np
import matplotlib.pyplot as plt


def mcu_srm(mcu):
    return mcu


def mosher(mcu):
    return (mcu * 0.3) + 4.7


def daniels(mcu):
    return (mcu * 0.2) + 8.4


def daniels_power(mcu):
    return 1.73 * (mcu ** 0.64) - 0.27


def noonan_power(mcu):
    return 15.03 * (mcu ** 0.27) - 15.53


def morey_hybrid(mcu):
    a_data = np.array([m for m in mcu if m < 10])
    b_data = np.array([m for m in mcu if 10 <= m < 37])
    c_data = np.array([m for m in mcu if 37 < m])
    return np.concatenate([a_data, daniels(b_data), mosher(c_data)])


def morey(mcu):
    return 1.4922 * (mcu ** 0.6859)


def main():

    mcu = np.linspace(0, 50, num=500)
    mc = mcu_srm(mcu)
    ms = mosher(mcu)
    ds = daniels(mcu)
    dp = daniels_power(mcu)
    no = noonan_power(mcu)
    mh = morey_hybrid(mcu)
    mo = morey(mcu)

    plt.plot(mcu, mc, '-',
             mcu, ms, '-',
             mcu, ds, '-',
             mcu, dp, '-',
             mcu, no, '-',
             mcu, mh, '.',
             mcu, mo, '.',
             )
    plt.legend(['mcu',
                'mosher',
                'daniels',
                'daniels power',
                'noonan power',
                'morey hybrid',
                'morey'], loc=2)
    plt.xlim(0, 50)
    plt.ylim(0, 30)
    plt.xlabel('mcu')
    plt.ylabel('srm', rotation='horizontal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
