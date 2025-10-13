#!/usr/bin/env python3
#
# Copyright (C) 2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import os
import sys

# Stop immediately if imported (mimics the sourcing check in bash)
if __name__ != "__main__":
    sys.exit(0)

# Required device metadata
DEVICE = "RMX2061"
DEVICE_COMMON = "sm7125-common"
VENDOR = "realme"
DEVICE_BRINGUP_YEAR = "2020"

# Path to the common setup-makefiles.py
COMMON_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    "..", "..", VENDOR, DEVICE_COMMON, "setup-makefiles.py"
)

# Check if the common script exists
if not os.path.exists(COMMON_SCRIPT):
    sys.stderr.write(f"Error: Cannot find common script at {COMMON_SCRIPT}\n")
    sys.exit(1)

# Add the common script’s directory to the Python import path
sys.path.insert(0, os.path.dirname(COMMON_SCRIPT))

# Try importing and executing its main function
try:
    from setup_makefiles import main as common_main
except ImportError as e:
    sys.stderr.write(f"Failed to import common setup_makefiles: {e}\n")
    sys.exit(1)

# Forward CLI arguments (equivalent to "$@")
if __name__ == "__main__":
    sys.exit(common_main(sys.argv[1:]))
