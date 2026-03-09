def review_with_ai(code):
    if len(code) < 20:
        return "code is very small.consider adding comments."
        if "for"in code and "range" in code:
            return "Loop detected.Make sure complexity is optimized."
            return "code looks okay but could use better documentation."