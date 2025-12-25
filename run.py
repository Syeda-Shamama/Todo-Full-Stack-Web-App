import sys
import os
import uvicorn

if __name__ == "__main__":
    # Add the Backend directory to the Python path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Backend')))
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
