#!/bin/bash

# ~/lx/lx14/public/lx14a_conda.bash
# ooooooooooooooo oooooooooooo
# 2024-11-28
# port python env from d81:lc11 to hp88:dan/lx

conda create -n lx14a python
# python             pkgs/main/linux-64::python-3.13.0-hf623796_100_cp313
# conda activate  lx14a

# I need to ensure that imports in gen_summaries12.py will run:
# import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing
# import langchain, langchain_core, langsmith, langchain_groq

conda install bs4
# bs4-4.12.3 

conda install langchain -c conda-forge
echo is trouble bc python is 3.13, I think.
echo try python 3.11?
exit


