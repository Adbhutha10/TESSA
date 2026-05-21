import sys
from lark import Lark

def main():
    # Read the grammar from the file
    try:
        with open("grammar.lark", "r") as f:
            grammar = f.read()
    except FileNotFoundError:
        print("Error: grammar.lark not found. Make sure you are running this from the BioSimLang directory.")
        sys.exit(1)

    # Create the parser
    parser = Lark(grammar, start='start', parser='lalr')

    # If a file is passed as an argument, read from it
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, "r") as f:
                code = f.read()
            print(f"Parsing {filename}...\n")
        except FileNotFoundError:
            print(f"Error: Could not find file {filename}")
            sys.exit(1)
    else:
        # Otherwise, accept dynamic multiline input from the terminal
        print("Interactive Mode: Enter your BioSimLang code below.")
        print("When you are finished typing, press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) on a new line and press Enter.")
        print("-" * 40)
        code = sys.stdin.read()
        print("\nParsing your input...\n")

    print("-" * 40)
    
    try:
        # Parse the code into an AST
        tree = parser.parse(code)
        print("AST Generated Successfully!\n")
        print(tree.pretty())
    except Exception as e:
        print("\n[!] Syntax Error parsing code:")
        print(e)

if __name__ == "__main__":
    main()
