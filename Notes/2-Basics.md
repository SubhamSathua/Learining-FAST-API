# How to Create and Run a FastAPI App

## 1. Create FastAPI App
- Import FastAPI: `from fastapi import FastAPI`
- Create app instance: `app = FastAPI()`
- Define routes using Python functions and decorators.

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
		return {"message": "Hello World"}
```

## 2. Run the App
- Use one of the following commands:
	- `uvicorn main:app --reload`  
		(Runs Uvicorn server, reloads on code changes)
	- `fastapi dev main.py`  
		(Developer-friendly, auto-reloads)
- Open browser at: `http://127.0.0.1:8000`
