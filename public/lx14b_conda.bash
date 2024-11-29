#!/bin/bash

# ~/lx/lx14/public/lx14b_conda.bash
# ooooooooooooooo oooooooooooo
# 2024-11-28
# port python env from d81:lc11 to hp88:dan/lx

# conda env remove -n lx14a
# bc python 3.13 is trouble for langchain

conda create -n lx14b python=3.11
# python  pkgs/main/linux-64::python-3.11.10-he870216_0

# conda activate  lx14b

# I need to ensure that imports in gen_summaries12.py will run:
# import bs4, datetime, glob, inspect, json, operator, os, re, shutil, sys, time, typing
# import langchain, langchain_core, langsmith, langchain_groq

conda install bs4
# beautifulsoup4-4.12.3

conda install langchain -c conda-forge
# langchain          conda-forge/noarch::langchain-0.3.9-pyhd8ed1ab_0 
# langchain-core     conda-forge/noarch::langchain-core-0.3.21-pyhd8ed1ab_0 
# langchain-text-sp~ conda-forge/noarch::langchain-text-splitters-0.3.2-pyhd8ed1ab_0 
# langsmith          conda-forge/noarch::langsmith-0.1.147-pyhd8ed1ab_0 

conda install langchain_groq -c conda-forge
# PackagesNotFoundError

pip install langchain_groq
# Successfully installed distro-1.9.0 groq-0.12.0 langchain_groq-0.2.1

