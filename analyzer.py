from radon.complexity import cc_visit
def analyze_code(code):
    blocks=cc_visit(code)
    for block in blocks:
        result.append({"functions":block.name,"complexity":block.complexity})
        if "print(" in code :
            result.append({"warning":"Debug print statement found"})
            if "==" not in code and "if" in code:
                result.append({"warning":"possible logic issue in condition"})
                return result