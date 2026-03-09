from fastapi import FastAPI
from pydantic import BaseModel
from ai_review import review_with_ai
app = FastAPI()
class codeRequest(BaseModel):
    code:str
    def review_code(data:codeRequest):
        code=data.code
        analysis=analyze_code(code)
        ai_feedback=review_with_ai(code)
        return{"analysis":analysis,"ai_review":ai_}