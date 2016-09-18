# This is a Makefile for the "make" utility.
#
# It automates a set of common steps that I (your kindly instructor) run on
# the files in this repo.
#
# You will probably find yourself using "make" and Makefiles, but this is not
# part of the exercises for class, it is for me to automate building the
# exercises.
PYTHON ?= python3

check:
	$(PYTHON) lab-tools/proc_solutions.py check

write:
	$(PYTHON) lab-tools/proc_solutions.py write
