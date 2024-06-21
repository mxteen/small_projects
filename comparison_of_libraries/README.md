# Polynomial Approximation Comparison

This project aims to compare the performance of `numpy.polyfit` and `scipy.optimize.curve_fit` functions for polynomial data approximation. The goal is to determine whether `scipy.optimize.curve_fit` can replace `numpy.polyfit` to reduce the number of dependencies and simplify the transition to C++.

## Objective

Determine if `scipy.optimize.curve_fit` can be used as a replacement for `numpy.polyfit` for polynomial approximations in terms of performance and accuracy.

## Tasks

1. Verify if the polynomial coefficients obtained using `scipy.optimize.curve_fit` and `numpy.polyfit` are equal.
2. Check the closeness of approximations obtained using `scipy.optimize.curve_fit` and `numpy.polyfit` to the original polynomial.
3. Assess the closeness of approximations obtained using `scipy.optimize.curve_fit` and `numpy.polyfit` to each other.

## Conclusions

1. The coefficients of the third-degree polynomials obtained using `scipy.optimize.curve_fit` and `numpy.polyfit` are different.
2. The coefficients of the second-degree polynomials obtained using `scipy.optimize.curve_fit` and `numpy.polyfit` are nearly identical.
3. Both functions provide equally good approximations to the original polynomial in the vicinity of the \( X \) values where noisy data was provided.
4. The approximations provided by `scipy.optimize.curve_fit` and `numpy.polyfit` are closer to each other than to the original polynomial.
5. The use of these functions is equivalent in terms of the result. Therefore, for polynomial data approximation, `numpy.polyfit` can be replaced with `scipy.optimize.curve_fit`.

## Dependencies

- Python 3.x
- numpy
- scipy
- matplotlib


## Author

Maksim Terentev
