import sys
import argparse

def useSysFunc():
    try: 
       for arg in sys.argv:
        print(arg)
    except:
        print("error occurred") 

def useArgParse():
    parser = argparse.ArgumentParser()
    parser.parse_args()
        

useSysFunc()
#useArgParse()

