# nansen-microservices-core dummy public package

## Summary

This is a dummy public package that was created to mitigate risk of fetching malicious code from public PyPI repository.

## Problem

Turns out that at the moment there is no way to set install priority order when specifying `extra-index-url` for `pip` 
(there is [a GitHub issue](https://github.com/pypa/pip/issues/8606) open for this case).
This means if someone creates a package with same name as this private package, `pip` may choose to fetch public
package instead of private package if public package has higher version, tag match (ABI tag, python version tag,
platform tag).

## Solution

Although, it is possible to fix this issue using `poetry`, `pipenv` and etc, there are some cases where we cannot use
such tools, for example Google Composer.

To mitigate this risk for all the cases we register a dummy public package with same name as the private one.
In this case public package version is under our control.

## Build

Make sure you have the latest versions of setuptools and wheel installed:
```
pip install --upgrade setuptools wheel
```

Run this command in the same directory where setup.py is located:
```
python3 setup.py sdist bdist_wheel
```

## Publish

For publishing we need to use `twine`:
```
pip install --upgrade twine
```

And upload:
```
twine upload dist/*
```
This command will ask PyPI username and password, they are stored in 1Password (search for `PyPI SRE`).
