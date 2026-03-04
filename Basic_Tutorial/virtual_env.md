Steps to create and activate a Python virtual environment (venv) on Windows:

1. Open your terminal in the project directory.
2. Run:
   ```
   python -m venv venv
   ```
   This creates a virtual environment named "venv".

3. Activate the environment:
   ```
   .\venv\Scripts\activate
   ```
   Your prompt will change to show the environment is active.

4. Install packages as needed (e.g., FastAPI):
   ```
   pip install fastapi
   ```