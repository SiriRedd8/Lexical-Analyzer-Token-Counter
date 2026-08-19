import re

# Keywords
keywords = {
    "int", "float", "double", "char", "if", "else",
    "for", "while", "do", "return", "void",
    "break", "continue", "switch", "case",
    "default", "long", "short"
}

# Operators
operators = {
    "+", "-", "*", "/", "%", "=", "==",
    "!=", ">", "<", ">=", "<=", "++", "--",
    "+=", "-=", "*=", "/=", "&&", "||", "!"
}

# Separators / Delimiters
separators = {
    "(", ")", "{", "}", "[", "]", ";", ","
}

# Special symbols
special_symbols = {
    ".", ":", "?", "#", "&", "|", "^", "~"
}


def lexical_analysis(filename):
    with open(filename, "r") as file:
        source = file.read()

    tokens = []

    # Remove single-line comments
    source = re.sub(r'//.*', '', source)

    # Remove multi-line comments
    source = re.sub(r'/\*.*?\*/', '', source, flags=re.DOTALL)

    # Token pattern
    pattern = r'''
        "(?:\\.|[^"\\])*"             |  # String literal
        '(?:\\.|[^'\\])*'             |  # Character literal
        \d+\.\d+                      |  # Decimal constant
        \d+                            |  # Integer constant
        [A-Za-z_][A-Za-z0-9_]*         |  # Identifier/Keyword
        ==|!=|>=|<=|\+\+|--|\+=|-=|\*=|/=|&&|\|\| |
        [+\-*/%=><!]                  |  # Operators
        [(){}\[\];,]                  |  # Separators
        [.:?#&|^~]                       # Special symbols
    '''

    matches = re.findall(pattern, source, re.VERBOSE)

    counts = {
        "Keywords": 0,
        "Identifiers": 0,
        "Operators": 0,
        "Constants": 0,
        "String Literals": 0,
        "Character Literals": 0,
        "Separators": 0,
        "Special Symbols": 0,
        "Comments": 0
    }

    print("TOKEN TYPE")
    print("-" * 50)

    for token in matches:

        if token in keywords:
            token_type = "Keyword"
            counts["Keywords"] += 1

        elif token in operators:
            token_type = "Operator"
            counts["Operators"] += 1

        elif token in separators:
            token_type = "Separator"
            counts["Separators"] += 1

        elif token.startswith('"'):
            token_type = "String Literal"
            counts["String Literals"] += 1

        elif token.startswith("'"):
            token_type = "Character Literal"
            counts["Character Literals"] += 1

        elif re.fullmatch(r'\d+(\.\d+)?', token):
            token_type = "Constant"
            counts["Constants"] += 1

        elif token in special_symbols:
            token_type = "Special Symbol"
            counts["Special Symbols"] += 1

        else:
            token_type = "Identifier"
            counts["Identifiers"] += 1

        tokens.append((token, token_type))
        print(f"{token:<20} {token_type}")

    print("\n" + "-" * 50)
    print("TOKEN COUNT")
    print("-" * 50)

    for key, value in counts.items():
        if value > 0:
            print(f"{key:<20}: {value}")

    return tokens, counts


# Main program
if __name__ == "__main__":
    lexical_analysis("input.txt")