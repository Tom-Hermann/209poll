#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-209poll-tom.hermann
## File description:
## main
##

from sys import argv
from src.constante import SUCCESS
from src.error import error
from math import sqrt

def poll(totalSize, SampleSize, p):
    variance = ((p / 100 * (1 - p / 100)) / SampleSize) * ((totalSize - SampleSize) / (totalSize - 1))
    p1 = (2 * 1.96 * sqrt(variance)) / 2 * 100
    p2 = (2 * 2.58 * sqrt(variance)) / 2 * 100
    print("Population size:\t\t{}".format(totalSize))
    print("Sample size:\t\t\t{}".format(SampleSize))
    print("Voting intentions:\t\t{:.2f}%".format(p))
    print("Variance:\t\t\t{:.6f}".format(variance))
    print("95% confidence interval:\t[{:.2f}%; {:.2f}%]".format(p - p1, p + p1))
    print("99% confidence interval:\t[{:.2f}%; {:.2f}%]".format(p - p2, p + p2))

def main():
    error(argv[1:])
    totalSize = int(argv[1])
    SampleSize = int(argv[2])
    p = float(argv[3])
    poll(totalSize, SampleSize, p)
    exit(SUCCESS)

if __name__ == "__main__":
    main()
