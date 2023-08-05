loggertools
===========
..
  pandoc -f rst -o README.html -t html README.rst

A Python port of the Control File Functions of the Logger Tools Software of Olaf
Kolle, MPI-BGC Jena, (c) 2012.

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5574388.svg
   :target: https://doi.org/10.5281/zenodo.5574388
   :alt: Zenodo DOI

.. image:: https://badge.fury.io/py/loggertools.svg
   :target: https://badge.fury.io/py/loggertools
   :alt: PyPI version

..
   .. image:: https://img.shields.io/conda/vn/conda-forge/loggertools.svg
      :target: https://anaconda.org/conda-forge/loggertools
      :alt: Conda version

.. image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/mcuntz/loggertools/blob/master/LICENSE
   :alt: License

.. image:: https://github.com/mcuntz/loggertools/workflows/Continuous%20Integration/badge.svg?branch=main
   :target: https://github.com/mcuntz/loggertools/actions
   :alt: Build status

..
   .. image:: https://coveralls.io/repos/github/mcuntz/loggertools/badge.svg?branch=main
      :target: https://coveralls.io/github/mcuntz/loggertools?branch=main
      :alt: Coverage status


About loggertools
-----------------

``loggertools`` is a Python port of the Control File Functions of the Logger
Tools Software of Olaf Kolle, MPI-BGC Jena, (c) 2012.

From the Logger Tools Software manual:
"The functions range from simple mathematic operations to more complex
and special procedures including functions for checking data. Most of
the functions have the following appearance: `y = f(x, p1, p2, ..., pn)`
where `y` is the variable in which the result of the function `f` is
stored, `x` is the input variable of the function and `p1` to `pn` are
parameters (numbers) of the function. An output variable (result of a
function) may be the same as an input variable. Some functions need
more than one input variable, some functions do not need any parameter
and some functions (`mean`, `mini`, `maxi`) may have a variable number
of input variables."

The complete documentation of ``loggertools`` is available at:

   https://mcuntz.github.io/loggertools/

Some functions are renamed compared to the original logger tools:

   `chs` -> `varchs`

   `add` -> `varadd`

   `sub` -> `varsub`

   `mul` -> `varmul`

   `div` -> `vardiv`

   `sqr` -> `varsqr` / `varsqrt`

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
elements are excluded from the calculations if any of the inputs equals `undef`.

Only bit_test and the if-statements `ifeq`, `ifne`, `ifle`, `ifge`, `iflt`, `igt`
do not have the `undef` keyword.


Logger Tool Functions
---------------------

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

         y = cubic(x, a0, a1, a2, a3) means `y = a0 + a1 * x + a2 * x**2 + a3 * x**3`,
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

         This function may be used to adjust small negative values of short wave
         radiation during nighttime to zero values.

         def setlow(dat, low, islow=None, undef=-9999.):


    17. Replacement of overflows by new value

         y = sethigh(x, lo, ln=None) means `IF (x < lo) THEN y = ln ELSE y = x`,
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

         `y = x * fl + sigma * (Tp + 273.16)**4`

         where `sigma = 5.67051 * 10**8` W m-2 K-4 is the
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

         `y = sqrt4(Rl / (sigma * epsilon)) - 273.16`

         where `sigma = 5.67051 * 10**8` W m-2 K-4 is the
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

         `y = (T + 273.16) * (1000/p)**0.286`

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

         `Tv = ((T + 273.16) * (1 + 0.000608 * sh)) - 273.16`

         `y = p * 100 / (287.05 * (Tv + 273.16))`

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


Installation
------------

The easiest way to install is via `pip`:

.. code-block:: bash

   pip install loggertools

Requirements
    * numpy_


License
-------

``loggertools`` is distributed under the MIT License. See the LICENSE_ file for
details.

Copyright (c) 2014-2022 Matthias Cuntz, Olaf Kolle

The project structure of ``loggertools`` has borrowed heavily from welltestpy_
by `Sebastian Müller`_.

.. _LICENSE: https://github.com/mcuntz/pyjams/blob/main/LICENSE
.. _Sebastian Müller: https://github.com/MuellerSeb
.. _numpy: https://numpy.org/
.. _welltestpy: https://github.com/GeoStat-Framework/welltestpy/
