if __name__ == "__main__":
    from os import system
    from sys import argv
    arg = argv[1:]
    if arg:
        system("bash make {arg[0]}")

