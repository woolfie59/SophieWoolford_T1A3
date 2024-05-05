#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install rich
python3 farm.py