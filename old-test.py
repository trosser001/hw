import sys
def main():
    # Use sum() with a generator expression to process batch arguments
    total = sum(
        int(clean) 
        for arg in sys.argv[1:] 
        # 1. Clean commas, underscores, and surrounding whitespace
        if (clean := arg.replace(",", "").replace("_", "").strip()) 
        # 2. Ignore anything with a decimal point (floats)
        and "." not in clean 
        # 3. Only keep it if it's numeric (handles negative sign via lstrip)
        and clean.lstrip("-").isdigit()
    )

    print(f"Total Sum: {total}")