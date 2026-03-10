import autopep8
import subprocess
import tempfile


def refine_code(code):
    # Improve formatting
    refined = autopep8.fix_code(code)
    return refined


def check_code_quality(code):
    # Run pylint on temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as temp:
        temp.write(code)
        filename = temp.name

    result = subprocess.run(
        ["pylint", filename],
        capture_output=True,
        text=True
    )

    output = result.stdout

    if output.strip() == "":
        return "No major issues detected."
    else:
        return output


def explain_code(code):
    # Simple explanation generator
    lines = code.split("\n")
    explanation = []

    for line in lines:
        line=line.strip()

        if line.startswith("def"):
            explanation.append("This defines a function.")

        elif "print" in line:
            explanation.append("This line prints output to the console.")

        elif "=" in line:
            explanation.append("This line assigns a value to a variable.")

    if not explanation:
        explanation.append("The code performs general operations.")

    return " ".join(explanation)
def score_code(code):
    score = 10
    if "print(" in code:
        score -= 1
    if "range(len" in code:
        score -= 1
    if "==" in code:
        score -= 0.5

    if score < 0:
        score = 0

    return round(score,1)


def suggest_improvements(code):
    suggestions = []

    if "range(len" in code:
        suggestions.append("Use direct iteration instead of range(len()).")

    if "print(" in code:
        suggestions.append("Remove debug print statements in production.")

    if "==" in code:
        suggestions.append("Consider using 'is' when comparing with None.")

    if not suggestions:
        suggestions.append("Your code follows good practices.")

    return suggestions


def detect_complexity(code):
    loops = code.count("for") + code.count("while")
    conditions = code.count("if")

    complexity = loops + conditions

    if complexity <= 2:
        return "Simple Code (Low Complexity)"
    elif complexity <= 5:
        return "Moderate Code (Medium Complexity)"
    else:
        return "Complex Code (High Complexity)"