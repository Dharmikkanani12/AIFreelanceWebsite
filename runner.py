from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.runner import run_snippet_docker

router = APIRouter(prefix="/runner")

class ExecReq(BaseModel):
    language_image: str  # e.g., "python:3.11-slim"
    code: str
    timeout: int = 6

@router.post("/exec")
def exec_code(req: ExecReq):
    try:
        res = run_snippet_docker(req.language_image, req.code, timeout=req.timeout)
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Runner error: " + str(e))