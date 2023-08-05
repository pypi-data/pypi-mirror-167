#!/usr/bin/env python
"""
loggertools is a Python port of the Control File Functions of
Logtools, the Logger Tools Software of Olaf Kolle, MPI-BGC Jena, (c) 2012.

Some functions are renamed compared to the original logger tools:

    `chs` -> `varchs`

    `add` -> `varadd`

    `sub` -> `varsub`

    `mul` -> `varmul`

    `div` -> `vardiv`

    `sqr` -> `varsqr`/`varsqrt`

    `exp` -> `varexp`

    `log` -> `varlog`

    `pot` -> `varpot`

Not all functions are implemented (yet). Missing functions are:

    `varset`

    `met_torad`

    `met_psy_rh`

    `met_dpt_rh`

    `write`

Some functions are slightly enhanced, which is reflected in the
documentation of the indidual functions.

All functions have an additional keyword `undef`, which defaults to -9999.:
elements are excluded from the calculations if any of the inputs equals
`undef`.

Only bit_test and the if-statements `ifeq`, `ifne`, `ifle`, `ifge`, `iflt`,
`igt` do not have the `undef` keyword.

.. autosummary::
   varchs
   varadd
   varsub
   varmul
   vardiv
   varsqr
   varsqrt
   varexp
   varlog
   varpot
   lin
   quad
   cubic
   hms
   bit_test
   setlow
   sethigh
   limits
   mean
   mini
   maxi
   met_lwrad
   met_trad
   met_alb
   met_albl
   met_vpmax
   met_vpact
   met_vpdef
   met_sh
   met_tpot
   met_rho
   met_dpt
   met_h2oc
   met_h2oc_rh
   met_wdrot
   met_urot
   met_vrot
   met_uv_wv
   met_uv_wd
   met_wvwd_u
   met_wvwd_v
   ifeq
   ifne
   ifle
   ifge
   iflt
   ifgt

The Looger Tools control functions are:

    1. Assignment

       # not implemented


    2. Change sign

        y = varchs(a) means `y = -a`, where a is a variable or a number.

        def varchs(var1, undef=-9999.):


    3. Addition

        y = varadd(a, b) means `y = a + b`, where a and b are ndarray or float.

        def varadd(var1, var2, undef=-9999.):


    4. Subtraction

        y = varsub(a, b) means `y = a - b`, where a and b are ndarray or float.

        def varsub(var1, var2, undef=-9999.):


    5. Multiplication

        y = varmul(a, b) means `y = a * b`, where a and b are ndarray or float.

        def varmul(var1, var2, undef=-9999.):


    6. Division

        y = vardiv(a, b) means `y = a / b`, where a and b are ndarray or float.

        def vardiv(var1, var2, undef=-9999.):


    7. Square root

        y = varsqr(a) means `y = sqrt(a)`, where a is a variable or a number.

        y = varsqrt(a) means `y = sqrt(a)`, where a is a variable or a number.

        def varsqr(var1, undef=-9999.):

        def varsqrt(var1, undef=-9999.):


    8. Exponentiation of e

        y = varexp(a) means `y = exp(a)`, where a is a variable or a number.

        def varexp(var1, undef=-9999.):


    9. Natural logarithm

        y = varlog(a) means `y = ln(a)`, where a is a variable or a number.

        def varlog(var1, undef=-9999.):


    10. Exponentiation

         y = varpot(a, b) means `y = a**b`, where a and b are ndarray or float.

         def varpot(var1, var2, undef=-9999.):


    11. Apply linear function

         y = lin(x, a0, a1) means `y = a0 + a1 * x`,
         where a0 and a1 are ndarray or float.

         def lin(var1, a, b, undef=-9999.):


    12. Apply 2nd order function

         y = quad(x, a0, a1, a2) means `y = a0 + a1 * x + a2 * x**2`,
         where a0, a1 and a2 are ndarray or float.

         def quad(var1, a, b, c, undef=-9999.):


    13. Apply 3rd order function

         y = cubic(x, a0, a1, a2, a3) means
         `y = a0 + a1 * x + a2 * x**2 + a3 * x**3`,
         where a0, a1, a2 and a3 are ndarray or float.

         def cubic(var1, a, b, c, d, undef=-9999.):


    14. Calculate fraction of day from hours, minutes and seconds

         y = hms(h, m, s) means `y = (h + m/60 + s/3600)/24`,
         where h, m and s (hours, minutes and seconds) are ndarray or float.

         def hms(h, m, s, undef=-9999.):


    15. Bitwise test

         y = bit_test(x, b, start=0) means `y = 1` if bit b is set in x
         otherwise `y = 0`.

         Returns a list of `b` is an array.

         Counting of `b` starts at start.

         For the behaviour of the original logger tools, set start=1.

         Negative `b` are not implemented.

         def bit_test(var1, var2, start=0):


    16. Replacement of underflows by new value

         y = setlow(x, lo, ln=None) means `IF (x > lo) THEN y = ln ELSE y = x`,
         where `lo` and `ln` are ndarray or float.

         `ln` is optional. If not given `lo` will be used.

         This function may be used to adjust small negative values of short
         wave radiation during nighttime to zero values.

         def setlow(dat, low, islow=None, undef=-9999.):


    17. Replacement of overflows by new value

         y = sethigh(x, lo, ln=None) means
         `IF (x < lo) THEN y = ln ELSE y = x`,
         where `lo` and `ln` are ndarray or float.

         `ln` is optional. If not given `lo` will be used.

         This function may be used to adjust relative humidity values of a
         little bit more than 100% to 100%.

         def sethigh(dat, high, ishigh=None, undef=-9999.):


    18. Replacement of underflows or overflows by the undef

         y = limits(x, ll, lh) means
         `IF (x > ll) OR (x < lh) THEN y = undef ELSE y = x`,
         where `ll` and `lh` are ndarray or float.

         This function may be used to check values lying in between certain
         limits. If one of the limits is exceeded the value is set to undef.

         def limits(dat, mini, maxi, undef=-9999.):


    19. Calculation of mean value

         y = mean(x1, x2, ..., xn) means `y = (x1 + x2 + ... + xn) / n`,
         where `x1`, `x2`, ..., `xn` are ndarray or float.

         def mean(var1, axis=None, undef=-9999.):


    20. Calculation of minimum value

         y = mini(x1, x2, ..., xn) means `y = min(x1, x2, ..., xn)`,
         where `x1`, `x2`, ..., `xn` are ndarray or float.

         def mini(var1, axis=None, undef=-9999.):


    21. Calculation of maximum value

         y = maxi(x1, x2, ..., xn) means `y = max(x1, x2, ..., xn)`,
         where `x1`, `x2`, ..., `xn` are ndarray or float.

         def maxi(var1, axis=None, undef=-9999.):


    22. Calculation of total radiation from net radiometer

        # no implemented


    23. Calculation of long wave radiation from net radiometer

         y = met_lwrad(x, Tp) where
         x is the output voltage of the net radiometer in mV,
         Tp is the temperature of the net radiometer body in degC.

         The total radiation in W m-2 is calculated according to the following
         formula:

         `y = x * fl + sigma * (Tp + 273.15)**4`

         where `sigma = 5.67 * 10**-8` W m-2 K-4 is the
         Stephan-Boltzmann-Constant and fl is the factor for long wave radiation
         (reciprocal value of sensitivity) in W m-2 per mV.

         The function assumes that fl was already applied before.

         All parameters may be ndarray or float.

         # assumes that dat was already multiplied with calibration factor
         def met_lwrad(dat, tpyr, undef=-9999.):


    24. Calculation of radiation temperature from long wave radiation

         y = met_trad(Rl, epsilon) where
         Rl is the long wave radiation in W m-2,
         epsilon is the long wave emissivity of the surface (between 0 and 1).

         The radiation temperature in degC is calculated according to the
         following formula:

         `y = sqrt4(Rl / (sigma * epsilon)) - 273.15`

         where `sigma = 5.67 * 10**-8` W m-2 K-4 is the
         Stephan-Boltzmann-Constant.

         Both parameters may be ndarray or float.

         def met_trad(dat, eps, undef=-9999.):


    25. Calculation of albedo from short wave downward and upward radiation

         y = met_alb(Rsd, Rsu) where
         Rsd is the short wave downward radiation in Wm-2, Rsu is the short
         wave upward radiation in Wm-2,

         The albedo in % is calculated according to the following formula:

         `y = 100 * ( Rsu / Rsd )`

         If Rsd > 50 W m-2 or Rsu > 10 W m-2 the result is undef.

         Both parameters may be ndarray or float.

         def met_alb(swd, swu, swdmin=50., swumin=10., undef=-9999.):


    26. Calculation of albedo from short wave downward and upward radiation
        with limits

         y = met_albl(Rsd, Rsu, Rsd_limit, Rsu_limit) where
         Rsd is the short wave downward radiation in Wm-2,
         Rsu is the short wave upward radiation in Wm-2,
         Rsd_limit is the short wave downward radiation limit in Wm-2,
         Rsu_limit is the short wave upward radiation limit in Wm-2,

         The albedo in % is calculated according to the following formula:

         `y = 100 * ( Rsu / Rsd )`

         If Rsd > Rsd_limit or Rsu > Rsu_limit the result is undef.

         All four parameters may be ndarray or float.

         def met_albl(swd, swu, swdmin, swumin, undef=-9999.):


    27. Calculation of saturation water vapour pressure

         y = met_vpmax(T) where
         T is the air temperature in degC.

         The saturation water vapour pressure in mbar (hPa) is calculated
         according to the following formula:

         `y = 6.1078 * exp(17.08085 * T / (234.175 + T))`

         The parameter may be a variable or a number.

         def met_vpmax(temp, undef=-9999.):


    28. Calculation of actual water vapour pressure

         y = met_vpact(T, rh) where T is the air temperature in degC,
         rh is the relative humidity in %.

         The actual water vapour pressure in mbar (hPa) is calculated
         according to the following formulas:

         `Es = 6.1078*exp(17.08085*T/ (234.175 + T))`

         `y = Es * rh/100`

         Both parameters may be ndarray or float.

         def met_vpact(temp, rh, undef=-9999.):


    29. Calculation of water vapour pressure deficit

         y = met_vpdef(T, rh) where T is the air temperature in degC,
         rh is the relative humidity in %.

         The water vapour pressure deficit in mbar (hPa) is calculated
         according to the following formulas:

         `Es = 6.1078*exp(17.08085*T/ (234.175 + T))`

         `E = Es * rh/100`

         `y = Es - E`

         Both parameters may be ndarray or float.

         def met_vpdef(temp, rh, undef=-9999.):


    30. Calculation of specific humidity

         y = met_sh(T, rh, p) where
         T is the air temperature in degC,
         rh is the relative humidity in %,
         p is the air pressure in mbar (hPa).

         The specific humidity in g kg-1 is calculated according to the
         following formulas:

         `Es = 6.1078*exp(17.08085*T/ (234.175 + T))`

         `E = Es * rh/100`

         `y = 622 * E/(p-0.378*E)`

         All parameters may be ndarray or float.

         def met_sh(temp, rh, p, undef=-9999.):


    31. Calculation of potential temperature

         y = met_tpot(T, p) where
         T is the air temperature in degC,
         p is the air pressure in mbar (hPa).

         The potential temperature in K is calculated according to
         the following formula:

         `y = (T + 273.15) * (1000/p)**0.286`

         Both parameters may be ndarray or float.

         def met_tpot(temp, p, undef=-9999.):


    32. Calculation of air density

         y = met_rho(T, rh, p) where
         T is the air temperature in degC,
         rh is the relative humidity in %,
         p is the air pressure in mbar (hPa).

         The air density in kg m-3 is calculated according to the
         following formulas:

         `Es = 6.1078*exp(17.08085*T/ (234.175 + T))`

         `E = Es * rh/100`

         `sh = 622 * E/(p-0.378*E)`

         `Tv = ((T + 273.15) * (1 + 0.000608 * sh)) - 273.15`

         `y = p * 100 / (287.05 * (Tv + 273.15))`

         All parameters may be ndarray or float.

         def met_rho(temp, rh, p, undef=-9999.):


    33. Calculation of dew point temperature

         y = met_dpt(T, rh) where
         T is the air temperature in degC, rh is the relative humidity in %.

         The dew point temperature in degC is calculated according to the
         following formulas:

         `Es = 6.1078*exp(17.08085*T/(234.175 + T))`

         `E = Es * rh/100`

         `y = 234.175 * ln(E/6.1078)/(17.08085 - ln(E/6.1078))`

         Both parameters may be ndarray or float.

         def met_dpt(temp, rh, undef=-9999.):


    34. Calculation of water vapour concentration

         y = met_h2oc(T, rh, p) where T is the air temperature in degC,
         rh is the relative humidity in %,
         p is the air pressure in mbar (hPa).

         The water vapour concentration in mmol mol-1 is calculated according
         to the following formulas:

         `Es = 6.1078*exp(17.08085*T/ (234.175 + T))`

         `E = Es * rh/100`

         `y = 0.1 * E /(0.001*p*100*0.001)`

         All parameters may be ndarray or float.

         def met_h2oc(temp, rh, p, undef=-9999.):


    35. Calculation of relative humidity from dry and wet bulb temperature

        # not implemented


    36. Calculation of relative humidity from dew point temperature

        # not implemented


    37. Calculation of relative humidity from water vapour concentration

         y = met_h2oc_rh(T, [H2O], p) where
         T is the air temperature in degC,
         [H2O] is the water vapour concentration in mmolmol-1,
         p is the air pressure in mbar (hPa).

         The relative humidity in % is calculated according to the
         following formulas:

         `Es = 6.1078*exp(17.08085*T/(234.175 + T))`

         `E = 10 * [H2O] * 0.001 * p * 100 * 0.001`

         `y = 100 * E / Es`

         All parameters may be ndarray or float.

         def met_h2oc_rh(temp, h, p, undef=-9999.):


    38. Rotation of wind direction

         y = met_wdrot(wd, a) where
         wd is the wind direction in degree,
         a is the rotation angle in degree (positive is clockwise).

         The rotated wind direction is calculated according to the
         following formulas:

         `y = wd + a`

         `IF y > 0 THEN y = y + 360`

         `IF y >= 360 THEN y = y - 360`

         Both parameters may be ndarray or float.

         def met_wdrot(wd, a, undef=-9999.):


    39. Rotation of u-component of wind vector

         y = met_urot(u, v, a) where
         u is the u-component of the wind vector,
         v is the v-component of the wind vector,
         a is the rotation angle in degree (positive is clockwise).

         The rotated u-component is calculated according to the
         following formula:

         `y = u * cos (a) + v * sin (a)`

         All three parameters may be ndarray or float.

         def met_urot(u, v, a, undef=-9999.):


    40. Rotation of v-component of wind vector

         y = met_vrot(u, v, a) where
         u is the u-component of the wind vector,
         v is the v-component of the wind vector,
         a is the rotation angle in degree (positive is clockwise).

         The rotated v-component is calculated according to the
         following formula:

         `y = -u * sin (a) + v * cos (a)`

         All three parameters may be ndarray or float.

         def met_vrot(u, v, a, undef=-9999.):


    41. Calculation of wind velocity from u- and v-component of wind vector

         y = met_uv_wv(u, v) where
         u is the u-component of the wind vector,
         v is the v-component of the wind vector.

         The horizontal wind velocity is calculated according to the
         following formula:

         `y = sqrt(u**2 + v**2)`

         Both parameters may be ndarray or float.

         def met_uv_wv(u, v, undef=-9999.):


    42. Calculation of wind direction from u- and v-component of wind vector

         y = met_uv_wd(u, v) where
         u is the u-component of the wind vector,
         v is the v-component of the wind vector.

         The horizontal wind velocity is calculated according to the
         following formulas:

         `IF u = 0 AND v = 0 THEN y = 0`

         `IF u = 0 AND v > 0 THEN y = 360`

         `IF u = 0 AND v < 0 THEN y = 180`

         `IF u < 0 THEN y = 270 - arctan(v/u)`

         `IF u > 0 THEN y = 90 - arctan(v/u)`

         Both parameters may be ndarray or float.

         def met_uv_wd(u, v, undef=-9999.):


    43. Calculation of u-component of wind vector from wind velocity and wind
        direction

         y = met_wvwd_u(wv, wd) where wv is the horizontal wind velocity,
         wd is the horizontal wind direction.

         The u-component of the wind vector is calculated according to the
         following formula:

         `y = -wv * sin (wd)`

         Both parameters may be ndarray or float.

         def met_wvwd_u(wv, wd, undef=-9999.):


    44. Calculation of v-component of wind vector from wind velocity and wind
        direction

         y = met_wvwd_v(wv, wd) where wv is the horizontal wind velocity,
         wd is the horizontal wind direction.

         The v-component of the wind vector is calculated according to the
         following formula:

         `y = -wv * cos (wd)`

         Both parameters may be ndarray or float.

         def met_wvwd_v(wv, wd, undef=-9999.):


    45. If-statements

         y = ifeq(x, a0, a1, a2) means `IF x == a0 THEN y = a1 ELSE y = a2`

         y = ifne(x, a0, a1, a2) means `IF x != a0 THEN y = a1 ELSE y = a2`

         y = ifle(x, a0, a1, a2) means `IF x <= a0 THEN y = a1 ELSE y = a2`

         y = ifge(x, a0, a1, a2) means `IF x >= a0 THEN y = a1 ELSE y = a2`

         y = iflt(x, a0, a1, a2) means `IF x > a0 THEN y = a1 ELSE y = a2`

         y = ifgt(x, a0, a1, a2) means `IF x < a0 THEN y = a1 ELSE y = a2`

         All parameters may be ndarray or float.

         def ifeq(var1, iif, ithen, ielse):

         def ifne(var1, iif, ithen, ielse):

         def ifle(var1, iif, ithen, ielse):

         def ifge(var1, iif, ithen, ielse):

         def iflt(var1, iif, ithen, ielse):

         def ifgt(var1, iif, ithen, ielse):


    46. Write variables to a file

        # not implemented


This module was written by Matthias Cuntz while at Department of
Computational Hydrosystems, Helmholtz Centre for Environmental
Research - UFZ, Leipzig, Germany, and continued while at Institut
National de Recherche pour l'Agriculture, l'Alimentation et
l'Environnement (INRAE), Nancy, France.

Copyright (c) 2014-2020 Matthias Cuntz - mc (at) macu (dot) de
Released under the MIT License; see LICENSE file for details.

.. moduleauthor:: Matthias Cuntz

History
    * Written Jun-Dec 2014 by Matthias Cuntz (mc (at) macu (dot) de)
    * Corrected type in met_tpot, Jun 2014, Corinna Rebmann
    * Changed to Sphinx docstring and numpydoc, May 2020, Matthias Cuntz
    * Made standalone package, Sep 2022, Matthias Cuntz

"""
import numpy as np
sigma = 5.67e-08  # Stefan-Boltzmann constant [W m^-2 K^-4]
T0 = 273.15       # Celcius <-> Kelvin [K]


__all__ = ['varchs', 'varadd', 'varsub', 'varmul', 'vardiv', 'varsqr',
           'varsqrt', 'varexp', 'varlog', 'varpot', 'lin', 'quad',
           'cubic', 'hms', 'bit_test', 'setlow', 'sethigh', 'limits',
           'mean', 'mini', 'maxi', 'met_lwrad', 'met_trad', 'met_alb',
           'met_albl', 'met_vpmax', 'met_vpact', 'met_vpdef', 'met_sh',
           'met_tpot', 'met_rho', 'met_dpt', 'met_h2oc', 'met_h2oc_rh',
           'met_wdrot', 'met_urot', 'met_vrot', 'met_uv_wv', 'met_uv_wd',
           'met_wvwd_u', 'met_wvwd_v', 'ifeq', 'ifne', 'ifle', 'ifge',
           'iflt', 'ifgt']


# Not implemented: varset


def varchs(a, undef=-9999.):
    """
    Change sign

        y = varchs(a) means `y = -a`, where `a` is ndarray or float.

    Parameters
    ----------
    a : ndarray
        input variable
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Changed sign

    """
    return np.where(a == undef, undef, -a)


def varadd(a, b, undef=-9999.):
    """
    Addition

        y = varadd(a, b) means `y = a + b`, where `a` and `b` are ndarray or
        float.

    Parameters
    ----------
    a : ndarray
        input variable 1
    b : ndarray
        input variable 2
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Addition

    """
    return np.where((a == undef) | (b == undef), undef, a + b)


def varsub(a, b, undef=-9999.):
    """
    Subtraction

        y = varsub(a, b) means `y = a - b`, where `a` and `b` are ndarray or
        float.

    Parameters
    ----------
    a : ndarray
        input variable 1
    b : ndarray
        input variable 2
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Subtraction

    """
    return np.where((a == undef) | (b == undef), undef, a - b)


def varmul(a, b, undef=-9999.):
    """
    Multiplication

        y = varmul(a, b) means `y = a * b`, where `a` and `b` are ndarray or
        float.

    Parameters
    ----------
    a : ndarray
        input variable 1
    b : ndarray
        input variable 2
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Multiplication

    """
    return np.where((a == undef) | (b == undef), undef, a * b)


def vardiv(a, b, undef=-9999.):
    """
    Division

        y = vardiv(a, b) means `y = a / b`, where `a` and `b` are ndarray or
        float.

    Parameters
    ----------
    a : ndarray
        dividend
    b : ndarray
        divisor
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Division

    """
    return np.where((a == undef) | (b == undef), undef, _div(a, b, undef))


def varsqr(a, undef=-9999.):
    """
    Square root

        y = varsqr(a) means `y = sqrt(a)`, where `a` is ndarray or float.

    Parameters
    ----------
    a : ndarray
        input variable
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Square root

    """
    return np.where((a == undef), undef, np.sqrt(a))


def varsqrt(a, undef=-9999.):
    """
    Square root

        y = varsqrt(a) means `y = sqrt(a)`, where `a` is ndarray or float.

    Parameters
    ----------
    a : ndarray
        input variable
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Square root

    """
    return np.where((a == undef), undef, np.sqrt(a))


def varexp(a, undef=-9999.):
    """
    Exponentiation of e

        y = varexp(a) means `y = exp(a)`, where `a` is ndarray or float.

    Parameters
    ----------
    a : ndarray
        exponent
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Exponentiation

    """
    return np.where((a == undef), undef, np.exp(a))


def varlog(a, undef=-9999.):
    """
    Natural logarithm

        y = varlog(a) means `y = ln(a)`, where `a` is ndarray or float.

    Parameters
    ----------
    a : ndarray
        input variable
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Natural logarithm

    """
    return np.where((a == undef), undef, np.log(a))


def varpot(a, b, undef=-9999.):
    """
    Exponentiation

        y = varpot(a, b) means `y = a**b`, where `a` and `b` are ndarray or
        float.

    Parameters
    ----------
    a : ndarray
        base
    b : ndarray
        exponent
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        Exponentiation

    """
    return np.where((a == undef) | (b == undef), undef, a**b)


def lin(x, a0, a1, undef=-9999.):
    """
    Apply linear function

        y = lin(x, a0, a1) means `y = a0 + a1 * x`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray or float
        parameter 1
    a1 : ndarray or float
        parameter 2
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        linear function

    """
    return np.where((x == undef), undef, a0 + a1 * x)


def quad(x, a0, a1, a2, undef=-9999.):
    """
    Apply 2nd order function

        y = quad(x, a0, a1, a2) means `y = a0 + a1 * x + a2 * x**2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray or float
        parameter 1
    a1 : ndarray or float
        parameter 1
    a2 : ndarray or float
        parameter 1
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        2nd order function

    """
    return np.where((x == undef), undef, a0 + a1 * x + a2 * x * x)


def cubic(x, a0, a1, a2, a3, undef=-9999.):
    """
    Apply 3rd order function

        y = cubic(x, a0, a1, a2, a3) means
        `y = a0 + a1 * x + a2 * x**2 + a3 * x**3`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray or float
        parameter 1
    a1 : ndarray or float
        parameter 2
    a2 : ndarray or float
        parameter 3
    a3 : ndarray or float
        parameter 4
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        3rd order function

    """
    return np.where((x == undef), undef,
                    a0 + a1 * x + a2 * x * x + a3 * x * x * x)


def hms(h, m, s, undef=-9999.):
    """
    Calculate fraction of day from hours, minutes and seconds

        y = hms(h, m, s) means `y = (h + m/60 + s/3600)/24`

    Parameters
    ----------
    h : ndarray
        hour
    m : ndarray
        minute
    s : ndarray
        second
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        fraction of day

    """
    return np.where((h == undef) | (m == undef) | (s == undef),
                    undef, (h + m / 60. + s / 3600.) / 24.)


def bit_test(x, b, start=0):
    """
    Bitwise test

        y = bit_test(x, b, start=0) means `y = 1` if bit `b` is set in `x`
        otherwise `y = 0`.

    Returns a list if `b` is an array.

    Counting of `b` starts at `start`.

    For the behaviour of the original logger tools, set `start=1`.

    Negative `b` are not implemented.

    Parameters
    ----------
    x : ndarray
        input variable 1
    b : int or ndarray
        input variable 2
    start : int, optional
        Counting of `b` starts at start (default: 0)

    Returns
    -------
    int or list
        Bitwise test

    """
    if np.size(b) > 1:
        return [ (x >> i+start) % 2 for i in b ]
    else:
        return (x >> b+start) % 2


def setlow(x, low, islow=None, undef=-9999.):
    """
    Replacement of underflows by new value

        y = setlow(x, low, islow) means
        `IF (x < low) THEN y = islow ELSE y = x`

    `islow` is optional. If not given `low` will be used.

    This function may be used to adjust small negative values of short wave
    radiation during nighttime to zero values.

    Parameters
    ----------
    x : ndarray
        input variable
    low : ndarray
        lower threshold
    islow : None or ndarray, optional
        if not None, use islow in case of y < low
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        underflows replaced by new value

    """
    if islow is None:
        out = np.maximum(x, low)
    else:
        out = np.where(x < low, islow, x)
    return np.where(x == undef, undef, out)


def sethigh(x, high, ishigh=None, undef=-9999.):
    """
    Replacement of overflows by new value

        t = sethigh(x, high, ishigh) means
        `IF (x > high) THEN y = ishigh ELSE y = x`

    `ishigh` is optional. If not given `high` will be used.

    This function may be used to adjust relative humidity values of a little
    bit more than 100% to 100%.

    Parameters
    ----------
    x : ndarray
        input variable
    high : ndarray
        upper threshold
    ishigh : None or ndarray, optional
        if not None, use ishigh in case of y > high
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        overflows replaced by new value

    """
    if ishigh is None:
        out = np.minimum(x, high)
    else:
        out = np.where(x > high, ishigh, x)
    return np.where(x == undef, undef, out)


def limits(x, mini, maxi, undef=-9999.):
    """
    Replacement of underflows or overflows by undef

        y = limits(x, mini, maxi) means
        `IF (x < mini) OR (x > maxi) THEN y = undef ELSE y = x`

    This function may be used to check values lying in between certain limits.

    If one of the limits is exceeded the value is set to `undef`.

    Parameters
    ----------
    x : ndarray
        input variable
    mini : ndarray
        lower threshold
    maxi : ndarray
        upper threshold
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        underflows or overflows replaced by `undef`

    """
    return np.where((x >= mini) & (x <= maxi), x, undef)


def mean(x, axis=None, undef=-9999.):
    """
    Calculation of mean value

        y = mean(x) means `y = (x[0] + x[1] + ... + x[n-1]) / n`

    Parameters
    ----------
    x : ndarray
        input variable
    axis : None or int or tuple of ints, optional
        Axis or axes along which the means are computed.
        The default is to compute the mean of the flattened array.

        If this is a tuple of ints, a mean is performed over multiple axes,
        instead of a single axis or all the axes as before.
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        mean value

    """
    return np.ma.mean(np.ma.array(x, mask=(x == undef)),
                      axis=axis).filled(undef)


def mini(x, axis=None, undef=-9999.):
    """
    Calculation of minimum value

        y = mini(x) means `y = min(x[0], x[1], ..., x[n-1])`

    Parameters
    ----------
    x : ndarray
        input variable
    axis : None or int or tuple of ints, optional
        Axis or axes along which the minimum are computed.
        The default is to compute the minimum of the flattened array.

        If this is a tuple of ints, a minimum is performed over multiple axes,
        instead of a single axis or all the axes as before.
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        minimum value

    """
    return np.ma.amin(np.ma.array(x, mask=(x == undef)),
                      axis=axis).filled(undef)


def maxi(x, axis=None, undef=-9999.):
    """
    Calculation of maximum value

        y = maxi(x) means `y = max(x[0], x[1], ..., x[n-1])`

    Parameters
    ----------
    x : ndarray
        input variable
    axis : None or int or tuple of ints, optional
        Axis or axes along which the maximum are computed.
        The default is to compute the maximum of the flattened array.

        If this is a tuple of ints, a maximum is performed over multiple axes,
        instead of a single axis or all the axes as before.
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        maximum value

    """
    return np.ma.amax(np.ma.array(x, mask=(x == undef)),
                      axis=axis).filled(undef)


# Not implemented: met_torad


# assumes that y was already multiplied with calibration factor
def met_lwrad(y, Tp, undef=-9999.):
    """
    Calculation of long wave radiation from net radiometer

        y = met_lwrad(x, Tp)

    The total radiation in W m-2 is calculated according to the following
    formula:

        `y = x * fl + sigma * (Tp + T0)**4`

    where `sigma = 5.67 * 10**-8` W m-2 K-4 is the Stephan-Boltzmann constant
    and `fl` is the factor for long wave radiation (reciprocal value of
    sensitivity) in W m-2 per mV.

    The function assumes that `fl` was already applied before.

    Parameters
    ----------
    y : ndarray
        output voltage of the net radiometer [mV]
    Tp : ndarray
        pyranometer temperature, i.e. the temperature of the net radiometer
        body [degC]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        total radiation in W m-2

    """
    return np.where((y == undef) | (Tp == undef),
                    undef, y + sigma * (Tp+T0)**4)


def met_trad(Rl, epsilon, undef=-9999.):
    """
    Calculation of radiation temperature from long wave radiation

        y = met_trad(Rl, epsilon)

    The radiation temperature in degC is calculated according to the following
    formula:

        `y = sqrt4(Rl / (sigma * epsilon)) - T0`

    where `sigma = 5.67 * 10**-8` W m-2 K-4 is the
    Stephan-Boltzmann constant.

    Parameters
    ----------
    Rl : ndarray
        longwave radiation [W m-2]
    epsilon : ndarray
        long wave emissivity of the surface [0-1]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        radiation temperature in degC

    """
    const = 1./(epsilon*sigma)
    trad = (np.ma.sqrt(np.ma.sqrt(const * np.ma.array(Rl, mask=(Rl == undef))))
            - T0)
    return trad.filled(undef)


def met_alb(swd, swu, swdmin=50., swumin=10., undef=-9999.):
    """
    Calculation of albedo from short wave downward and upward radiation

        y = met_alb(swd, swu)

    The albedo in % is calculated according to the following formula:

        `y = 100 * ( swu / swd )`

    If `swd < swdmin` (50 W m-2) or `swu < swumin` (10 W m-2),
    the result is undef.

    Parameters
    ----------
    swd : ndarray
        shortwave downward radiation [W m-2]
    swu : ndarray
        shortwave upward radiation [W m-2]
    swdmin : float, optional
        If `swd` < `swdmin` the result is undef (default: 50).
    swumin : float, optional
        If `swu` < `swumin` the result is undef (default: 10).
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        albedo in %

    """
    return np.where((swd == undef) | (swu == undef) | (swd < swdmin) |
                    (swu < swumin), undef, _div(swu * 100., swd, undef))


def met_albl(swd, swu, swdmin, swumin, undef=-9999.):
    """
    Calculation of albedo from short wave downward and upward radiation with
    limits

        x=met_albl(swd, swu, swdmin, swumin)

    The albedo in % is calculated according to the following formula:

        `y = 100 * ( swu / swd )`

    If `swd < swdmin` or `swu < swumin`, the result is `undef`.

    Parameters
    ----------
    swd : ndarray
        shortwave downward radiation [W m-2]
    swu : ndarray
        shortwave upward radiation [W m-2]
    swdmin : float
        If `swd` < `swdmin` the result is undef.
    swumin : float
        If `swu` < `swumin` the result is undef.
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        albedo in %

    """
    return np.where((swd == undef) | (swu == undef) | (swd < swdmin) |
                    (swu < swumin), undef, _div(swu * 100., swd, undef))


def met_vpmax(T, undef=-9999.):
    """
    Calculation of saturation water vapour pressure

        y = met_vpmax(T)

    The saturation water vapour pressure in mbar (hPa) is calculated according
    to the following formula:

        `y = 6.1078 * exp(17.08085 * T / (234.175 + T))`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        saturation water vapour pressure in mbar (hPa)

    """
    es = _esat(np.ma.array(T + T0, mask=(T == undef))) * 0.01
    return es.filled(undef)


def met_vpact(T, rh, undef=-9999.):
    """
    Calculation of actual water vapour pressure

        y = met_vpact(T, rh)

    The actual water vapour pressure in mbar (hPa) is calculated according to
    the following formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `y = Es * rh / 100`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        actual water vapour pressure in mbar (hPa)

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) | (rh == undef))))
          * 0.01)
    ea = es * rh * 0.01
    return ea.filled(undef)


def met_vpdef(T, rh, undef=-9999.):
    """
    Calculation of water vapour pressure deficit

        y = met_vpdef(T, rh)

    The water vapour pressure deficit in mbar (hPa) is calculated according to
    the following formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `E = Es * rh / 100`

        `y = Es - E`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        water vapour pressure deficit in mbar (hPa)

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) | (rh == undef))))
          * 0.01)
    ea = es * rh * 0.01
    vpd = es - ea
    return vpd.filled(undef)


def met_sh(T, rh, p, undef=-9999.):
    """
    Calculation of specific humidity

        y = met_sh(T, rh, p)

    The specific humidity in g kg-1 is calculated according to the following
    formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `E = Es * rh / 100`

        `y = 622 * E / (p - 0.378 * E)`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    p : ndarray
        air pressure [hPa = mbar]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        specific humidity in g kg-1

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) | (rh == undef) |
                                          (p == undef)))) * 0.01)
    ea = es*rh*0.01
    sh = _div(622.*ea, (p-0.378*ea), undef)
    return sh.filled(undef)


def met_tpot(T, p, undef=-9999.):
    """
    Calculation of potential temperature

        y = met_tpot(T, p)

    The potential temperature in K is calculated according to the following
    formula:

        `y = (T + T0) * (1000 / p)**0.286`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    p : ndarray
        air pressure [hPa = mbar]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        potential temperature in K

    """
    return np.where((T == undef) | (p == undef),
                    undef, (T + T0) * _div(1000., p)**0.286)


def met_rho(T, rh, p, undef=-9999.):
    """
    Calculation of air density

        y = met_rho(T, rh, p)

    The air density in kg m-3 is calculated according to the following
    formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `E = Es * rh / 100`

        `sh = 622 * E / (p - 0.378 * E)`

        `Tv = ((T + T0) * (1 + 0.000608 * sh)) - T0`

        `y = p * 100 / (287.05 * (Tv + T0))`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    p : ndarray
        air pressure [hPa = mbar]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        air density in kg m-3

    """
    es = (_esat(np.ma.array(T+T0, mask=((T == undef) | (rh == undef) |
                                        (p == undef)))) * 0.01)
    ea = es * rh * 0.01
    sh = _div(622. * ea, (p - 0.378 * ea), undef)
    Tv = ((T + T0) * (1. + 0.000608 * sh)) - T0
    rho = _div(p * 100., (287.05 * (Tv + T0)), undef)
    return rho.filled(undef)


def met_dpt(T, rh, undef=-9999.):
    """
    Calculation of dew point temperature

        y = met_dpt(T, rh)

    The dew point temperature in degC is calculated according to the following
    formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `E = Es * rh / 100`

        `y = 234.175 * ln(E / 6.1078) / (17.08085 - ln(E / 6.1078))`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        dew point temperature in degC

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) |
                                          (rh == undef)))) * 0.01)
    ea = es * rh * 0.01
    dpt = (234.175 * np.ma.log(ea / 6.1078) /
           (17.08085 - np.ma.log(ea / 6.1078)))
    return dpt.filled(undef)


def met_h2oc(T, rh, p, undef=-9999.):
    """
    Calculation of water vapour concentration

        y = met_h2oc(T, rh, p)

    The water vapour concentration in mmol mol-1 is calculated according to the
    following formulas:

        `Es = 6.1078 * exp(17.08085 * T/ (234.175 + T))`

        `E = Es * rh / 100`

        `y = 0.1 * E / (0.001 * p * 100 * 0.001)`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    rh : ndarray
        relative humidity [%]
    p : ndarray
        air pressure [hPa = mbar]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        water vapour concentration in mmol mol-1

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) | (rh == undef) |
                                          (p == undef)))) * 0.01)
    ea = es * rh * 0.01
    c = _div(1000. * ea, p, undef)
    return c.filled(undef)


# Not implemented: met_psy_rh


# Not implemented: met_dpt_rh


def met_h2oc_rh(T, h, p, undef=-9999.):
    """
    Calculation of relative humidity from water vapour concentration

        y = met_h2oc_rh(T, [H2O], p)

    The relative humidity in % is calculated according to the following
    formulas:

        `Es = 6.1078 * exp(17.08085 * T / (234.175 + T))`

        `E = 10 * [H2O] * 0.001 * p * 100 * 0.001`

        `y = 100 * E / Es`

    Parameters
    ----------
    T : ndarray
        air temperature [degC]
    h : ndarray
        water vapour concentration [mmol mol-1]
    p : ndarray
        air pressure [hPa = mbar]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        relative humidity in %

    """
    es = (_esat(np.ma.array(T + T0, mask=((T == undef) | (h == undef) |
                                          (p == undef)))) * 0.01)
    ea = 0.001 * h * p
    c = 100. * ea / es
    return c.filled(undef)


def met_wdrot(wd, a, undef=-9999.):
    """
    Rotation of wind direction

        y = met_wdrot(wd, a)

    The rotated wind direction is calculated according to the following
    formulas:

        `y = wd + a`

        `IF y < 0 THEN y = y + 360`

        `IF y <= 360 THEN y = y - 360`

    Parameters
    ----------
    wd : ndarray
        wind direction [degree]
    a : ndarray
        rotation angle (positive is clockwise) [degree]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        rotated wind direction

    """
    rot = np.ma.array(wd+a, mask=((wd == undef) | (a == undef)))
    rot = np.ma.where(rot < 0., rot + 360., rot)
    rot = np.ma.where(rot >= 360., rot - 360., rot)
    return rot.filled(undef)


def met_urot(u, v, a, undef=-9999.):
    """
    Rotation of u-component of wind vector

        y = met_urot(u, v, a)

    The rotated u-component is calculated according to the following formula:

        `y = u * cos (a) + v * sin (a)`

    Parameters
    ----------
    u : ndarray
        u-component of the wind vector
    v : ndarray
        v-component of the wind vector
    a : ndarray
        rotation angle (positive is clockwise) [degree]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        rotated u-component

    """
    return np.where((u == undef) | (v == undef) | (a == undef),
                    undef, u * np.cos(np.deg2rad(a)) +
                    v * np.sin(np.deg2rad(a)))


def met_vrot(u, v, a, undef=-9999.):
    """
    Rotation of v-component of wind vector

        y = met_vrot(u, v, a)

    The rotated v-component is calculated according to the following formula:

        `y = -u * sin (a) + v * cos (a)`

    Parameters
    ----------
    u : ndarray
        u-component of the wind vector
    v : ndarray
        v-component of the wind vector
    a : ndarray
        rotation angle (positive is clockwise) [degree]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        rotated v-component

    """
    return np.where((u == undef) | (v == undef) | (a == undef),
                    undef, -u * np.sin(np.deg2rad(a)) +
                    v * np.cos(np.deg2rad(a)))


def met_uv_wv(u, v, undef=-9999.):
    """
    Calculation of wind velocity from u- and v-component of wind vector

        y = met_uv_wv(u, v)

    The horizontal wind velocity is calculated according to the following
    formula:

        `y = sqrt(u**2 + v**2)`

    Parameters
    ----------
    u : ndarray
        u-component of the wind vector
    v : ndarray
        v-component of the wind vector
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        horizontal wind velocity

    """
    return np.where((u == undef) | (v == undef), undef, np.sqrt(u*u + v*v))


def met_uv_wd(u, v, undef=-9999.):
    """
    Calculation of wind direction from u- and v-component of wind vector

        y = met_uv_wd(u, v)

    The horizontal wind velocity is calculated according to the following
    formulas:

        `IF u = 0 AND v = 0 THEN y = 0`

        `IF u = 0 AND v < 0 THEN y = 360`

        `IF u = 0 AND v > 0 THEN y = 180`

        `IF u > 0 THEN y = 270 - arctan(v / u)`

        `IF u < 0 THEN y = 90 - arctan(v / u)`

    Parameters
    ----------
    u : ndarray
        u-component of the wind vector
    v : ndarray
        v-component of the wind vector
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        horizontal wind velocity

    """
    wd = np.ma.zeros(u.shape)
    wd.mask = (u == undef) | (v == undef)
    wd = np.ma.where((u == 0.) & (v == 0.), 0., wd)
    wd = np.ma.where((u == 0.) & (v < 0.), 360., wd)
    wd = np.ma.where((u == 0.) & (v > 0.), 180., wd)
    wd = np.ma.where((u > 0.), 270. - np.rad2deg(np.ma.arctan(v / u)), wd)
    wd = np.ma.where((u < 0.), 90. - np.rad2deg(np.ma.arctan(v / u)), wd)
    return wd.filled(undef)


def met_wvwd_u(wv, wd, undef=-9999.):
    """
    Calculation of u-component of wind vector from wind velocity and
    wind direction

        y = met_wvwd_u(wv, wd)

    The u-component of the wind vector is calculated according to the following
    formula:

        `y = -wv * sin(wd)`

    Parameters
    ----------
    wv : ndarray
        horizontal wind velocity [m s-1]
    wd : ndarray
        horizontal wind direction [degree]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        u-component of the wind vector

    """
    return np.where((wv == undef) | (wd == undef),
                    undef, -wv * np.sin(np.deg2rad(wd)))


def met_wvwd_v(wv, wd, undef=-9999.):
    """
    Calculation of v-component of wind vector from wind velocity and
    wind direction

        y = met_wvwd_v(wv, wd)

    The v-component of the wind vector is calculated according to the following
    formula:

        `y = -wv * cos(wd)`

    Parameters
    ----------
    wv : ndarray
        horizontal wind velocity [m s-1]
    wd : ndarray
        horizontal wind direction [degree]
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        v-component of the wind vector

    """
    return np.where((wv == undef) | (wd == undef),
                    undef, -wv * np.cos(np.deg2rad(wd)))


def ifeq(x, a0, a1, a2, undef=-9999.):
    """
    If-equal statement

        y = ifeq(x, a0, a1, a2) means `IF x == a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x == a0`
    a1 : ndarray
        result if `x == a0`
    a2 : ndarray
        result if `x != a0`
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF y == a0 THEN x = a1 ELSE x = a2

    """
    out = np.where(x == a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


def ifne(x, a0, a1, a2, undef=-9999.):
    """
    If-not-equal statements

        y = ifne(x, a0, a1, a2) means `IF x != a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x != a0`
    a1 : ndarray
        result if `x != a0`
    a2 : ndarray
        result if `x == a0`
    y : ndarray
    a0 : ndarray
    a1 : ndarray
    a2 : ndarray
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF y != a0 THEN x = a1 ELSE x = a2

    """
    out = np.where(x != a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


def ifle(x, a0, a1, a2, undef=-9999.):
    """
    If-lower-equal statement

        y = ifle(x, a0, a1, a2) means `IF x >= a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x <= a0`
    a1 : ndarray
        result if `x <= a0`
    a2 : ndarray
        result if `x > a0`
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF y >= a0 THEN x = a1 ELSE x = a2

    """
    out = np.where(x <= a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


def ifge(x, a0, a1, a2, undef=-9999.):
    """
    If-greater-equal statement

        y = ifge(x, a0, a1, a2) means `IF x <= a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x >= a0`
    a1 : ndarray
        result if `x >= a0`
    a2 : ndarray
        result if `x < a0`
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF y <= a0 THEN x = a1 ELSE x = a2

    """
    out = np.where(x <= a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


def iflt(x, a0, a1, a2, undef=-9999.):
    """
    If-lower-than statement

        y = iflt(x, a0, a1, a2) means `IF x < a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x < a0`
    a1 : ndarray
        result if `x < a0`
    a2 : ndarray
        result if `x >= a0`
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF x < a0 THEN y = a1 ELSE y = a2

    """
    out = np.where(x < a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


def ifgt(x, a0, a1, a2, undef=-9999.):
    """
    If-greater-than statement

        y = ifgt(x, a0, a1, a2) means `IF x > a0 THEN y = a1 ELSE y = a2`

    Parameters
    ----------
    x : ndarray
        input variable
    a0 : ndarray
        compare to input `x > a0`
    a1 : ndarray
        result if `x > a0`
    a2 : ndarray
        result if `x <= a0`
    undef : float, optional
        elements are excluded from the calculations if any of the inputs equals
        `undef` (default: -9999.)

    Returns
    -------
    ndarray
        IF y > a0 THEN x = a1 ELSE x = a2

    """
    out = np.where(x > a0, a1, a2)
    return np.where((x == undef) | (a0 == undef) | (a1 == undef) |
                    (a2 == undef), undef, out)


# Not implemented: write


#
# Local replacement functions if helper functions do not exist in library
#

def _div(a, b, otherwise=np.nan, prec=0.):
    """
    Divide two arrays, return `otherwise` if division by 0

    Parameters
    ----------
    a : array_like
        enumerator
    b : array_like
        denominator
    otherwise : float
        value to return if `b=0` (default: `np.nan`)
    prec : float
        if |b|<|prec| then `otherwise`

    Returns
    -------
    ndarray
        ratio : numpy array or masked array
        a/b        if |b| >  |prec|

        otherwise  if |b| <= |prec|

        Output is numpy array. It is a masked array if at least one
        of `a` or `b` is a masked array.
    """
    oldsettings = np.geterr()
    np.seterr(divide='ignore')

    if isinstance(a, np.ma.masked_array) or isinstance(b, np.ma.masked_array):
        out = np.ma.where(np.ma.abs(np.ma.array(b)) > np.abs(prec),
                          np.ma.array(a) / np.ma.array(b), otherwise)
    else:
        out = np.where(np.abs(np.array(b)) > np.abs(prec),
                       np.array(a) / np.array(b), otherwise)

    np.seterr(**oldsettings)

    return out


def _esat(T):
    """
    Calculates the saturation vapour pressure of water with the Goff-Gratch
    formula

    Parameters
    ----------
    T : ndarray
        Temperature [K]

    Returns
    -------
    ndarray
        Saturation water pressure at temperature T in Pascal [Pa].
    """
    # steam point temperature in K
    Ts = 373.16
    # saturation pressure at steam point temperature, normal atmosphere
    ews = 1013.246
    esat_liq = 10.**(-7.90298 * (Ts / T - 1.) +
                     5.02808 * np.ma.log10(Ts / T) -
                     1.3816e-7 * (10.**(11.344 * (1. - T/Ts)) - 1.) +
                     8.1328e-3 * (10.**(-3.49149 * (Ts / T - 1.)) - 1.) +
                     np.ma.log10(ews))  # [hPa]
    return esat_liq * 100.  # [Pa]


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
