#!/usr/bin/env python
import sys
import os
MY_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_DIR = os.path.dirname(MY_DIR)
sys.path.insert(0, REPO_DIR)

from moreblender import main

if __name__ == "__main__":
	sys.exit(main())
