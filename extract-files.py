#!/usr/bin/env python3
#
# Copyright (C) 2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import os
import sys

# Stop here if being imported (mimics "if sourced" in bash)
if __name__ != "__main__":
    sys.exit(0)

# Required
DEVICE = "RMX2061"
DEVICE_COMMON = "sm7125-common"
VENDOR = "realme"

DEVICE_BRINGUP_YEAR = "2020"

# Path to the common extract-files.py
COMMON_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..", VENDOR, DEVICE_COMMON, "extract-files.py"
)

# Ensure the common script exists
if not os.path.exists(COMMON_SCRIPT):
    sys.stderr.write(f"Error: Cannot find common script at {COMMON_SCRIPT}\n")
    sys.exit(1)

# Add common script’s directory to Python path and import its main function
sys.path.insert(0, os.path.dirname(COMMON_SCRIPT))

try:
    from extract_files import main as common_main
except ImportError as e:
    sys.stderr.write(f"Failed to import common extract_files: {e}\n")
    sys.exit(1)

# Call the common extract logic with current script’s arguments
if __name__ == "__main__":
    sys.exit(common_main(sys.argv[1:]))
