from radon.complexity import cc_visit

def analyze_code(code):
    results = []

    blocks = cc_visit(code)
    for block in blocks:
        results.append({
            "function": block.name,
            "complexity": block.complexity
        })

    if "print(" in code:
        results.append({"warning": "Debug print statement found"})

    if len(code) > 300:
        results.append({"warning": "Code too long. Split functions"})

    if "#" not in code:
        results.append({"warning": "No comments found in code"})

    return results

# Optional test
if __name__ == "__main__":
    test_code = """
def add(a,b):
    print(a+b)
    return a+b
"""
    print(analyze_code(test_code))