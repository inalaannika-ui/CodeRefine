from flask import Flask ,request,jsonify
from utils import refine_code,check_code_quality
app=Flask(__name__)
def home():
    return "coderefine backend running"
def analyze_code():
    data=request.json
    code=data.grt("code")
if not code:
     return jsonify({"error":"NO code provieded" }), 400 
     refined=refine_code(code)
     quality=check_code_quality(code)
     return jsonify({"original_code":code,"refined_code":refined, "analysis":quality})
     if __name__=="__main__": app.run(debug=True)