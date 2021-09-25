##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-209poll-tom.hermann
## File description:
## error
##

from src.constante import FAILURE, SUCCESS

def printUsage():
    print("USAGE\n\t./209poll pSize sSize p\n")
    print("DESCRIPTION\n")
    print("\tpSize\tsize of the population")
    print("\tsSize\tsize of the sample (supposed to be representative)")
    print("\tp\tpercentage of voting intentions for a specific candidate")

def error(argv):
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)
    if (len(argv) != 3):
        exit(FAILURE)
    try:
        if (int(argv[0]) <= 0):
            exit(FAILURE)
        elif (int(argv[1]) >= int(argv[0]) or int(argv[1]) <= 0):
            exit(FAILURE)
        elif (float(argv[2]) < 0 or float(argv[2]) > 100):
            exit(FAILURE)
        elif (int(argv[0])- 1 < 0):
            exit(FAILURE)
    except:
        exit(FAILURE)