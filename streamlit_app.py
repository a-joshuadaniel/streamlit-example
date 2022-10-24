
# joshua Daniel
# version 1 with front end
# CS50 Problem Set 0
#Problem link :https://cs50.harvard.edu/python/2022/psets/0/einstein
# step 1: Start
# Step 2: Prompt User For input bill amt in $
# Step 3: prompt user for tip perecntage in %
# Step 4: remove $
# Step 5: remove %
# Step 6: calculate tip
# Step 7: print tip amt

import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title('tip calculator')
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace('$',''))


def percent_to_float(p):
    p=float(p.replace('%',''))
    p1 = p/100
    return p1

main()
