# # Program to print the name "pashupati" using star patterns



def print_P():
    return [
        " *********  ",
        " *        * ",
        " *        * ",
        " *        * ",
        " *        * ",
        " ********** ",
        " *          ",
        " *          ",
        " *          ",
        " *          ",
        " *          "
    ]

def print_A():
    return [
        "  *********  ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *********** ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * "
    ]

def print_S():
    return [
        "  ********* ",
        " *          ",
        " *          ",
        " *          ",
        " *          ",
        " ********** ",
        "          * ",
        "          * ",
        "          * ",        
        "          * ",                 
        "  ********* "
    ]

def print_H():
    return [
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *********** ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * "
    ]

def print_U():
    return [
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        " *         * ",
        "  ********* "
    ]

def print_T():
    return [
        " *********** ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       "
    ]

def print_I():
    return [
        " *********** ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        "     *       ",
        " *********** "
    ]

# # Mapping
letter_patterns = {
    'P': print_P(),
    'A': print_A(),
    'S': print_S(),
    'H': print_H(),
    'U': print_U(),
    'p': print_P(),
    'A': print_A(),
    'T': print_T(),
    'I': print_I()
}

def print_name(name):
    letters = list(name.upper())
    patterns = [letter_patterns[letter] for letter in letters]

    for i in range(len(patterns[0])):
        for pattern in patterns:
            print(pattern[i], end="  ")
        print()


print_name("PASHUPATI")

    

