import sys
from lark import Lark
from semantic.transformer import TESSATransformer
from runtime.engine import SimulationEngine

def load_compiler():
    try:
        with open("grammar.lark", "r") as f:
            grammar = f.read()
    except FileNotFoundError:
        print("Error: grammar.lark not found.")
        sys.exit(1)
        
    parser = Lark(grammar, start='start', parser='lalr')
    transformer = TESSATransformer()
    return parser, transformer

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file.bsl>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

    print(f"=== TESSA Compiler: Processing {filename} ===")
    parser, transformer = load_compiler()
    
    try:
        raw_tree = parser.parse(code)
        simulation_node = transformer.transform(raw_tree)
        print("[SUCCESS] Compilation complete. Starting runtime engine...\n")
        
        # Initialize and run the simulation engine
        engine = SimulationEngine(simulation_node, width=50, height=50)
        engine.run(max_ticks=24) # Run for 24 "hours" (ticks)
        
    except Exception as e:
        print(f"Compilation Error: {e}")

if __name__ == "__main__":
    main()
