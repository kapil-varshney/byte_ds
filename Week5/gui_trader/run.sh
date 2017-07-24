#!/usr/bin/env bash

rm terminal_trading.db
python3 schema.py
python3 controller.py
