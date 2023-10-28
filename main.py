#!/usr/bin/python

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true', default=False, \
                        help='Activate verbose mode for more information')
    
    