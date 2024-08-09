import pandas
import sklearn
import seleniumbase
import selenium
import tensorflow
import keras
import regex as re
import matplotlib
import seaborn
import random
from seleniumbase import BaseCase
from seleniumbase import Driver

class myCode():
    def humza(self):
        print("I love Pakistan!")

# A = myCode()
# A.humza()

class my_code(BaseCase):
    def in_the_code(self):
        with Driver() as driver:
            driver.open("https://www.google.com")
            driver.save_screenshot("ss.png")
            print("successfull")

# B = my_code()
# B.in_the_code()

fx = lambda x: x*x
def Uses(fun, value):
    print(fun*value)
# Uses(fx(5), 10)