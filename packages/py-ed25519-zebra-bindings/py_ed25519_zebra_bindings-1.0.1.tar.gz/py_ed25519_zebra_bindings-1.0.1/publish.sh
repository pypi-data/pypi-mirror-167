#!/bin/sh
maturin publish -i python3.8 --no-sdist
maturin publish -i python3.7 --no-sdist
