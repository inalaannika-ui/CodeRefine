from analyzer import analyze_code

snippets = [
    "def add(a,b): return a+b",
    "def multiply(x,y): print(x*y); return x*y"
]

for code in snippets:
    print(analyze_code(code))