#!/usr/bin/env bash

rm pairs_trading.db
python3 schema.py
python3 controller.py
