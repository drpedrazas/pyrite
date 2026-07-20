# Pyrite

A basic machine learning module, built from scratch in Python.

## About this project

Pyrite is **not intended for production use**. It's a personal learning project, with two goals:

1. Refresh and practice Python programming after some time away from it.
2. Understand how classic ML algorithms actually work (linear regression, regularization, trees, etc.) by implementing them from scratch instead of relying on libraries like scikit-learn.

If you need a robust, tested, and maintained ML library, use [scikit-learn](https://scikit-learn.org) instead. This project exists purely for educational purposes.

## Design philosophy

- **Fully functional**: pure functions, no classes with internal state or inheritance.
- **No ML dependencies**: models are implemented from scratch, using only `numpy` for linear algebra. `scikit-learn` is used exclusively to load sample datasets (iris, wine, etc.).
- **Explicit typing**: all functions use type hints, enforced at runtime with [`beartype`](https://github.com/beartype/beartype).

## Current status

Work in progress. The structure and functions described here may change as development continues.

## Installation and usage

Section pending, to be added once the module has stable functionality worth documenting.
