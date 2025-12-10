@echo off
setlocal

:: Check if .venv exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

:: Activate virtual environment
call .venv\Scripts\activate

:: Install dependencies if not already installed (basic check)
if not exist .venv\Lib\site-packages\torch (
    echo Installing dependencies...
    pip install -r requirements.txt
)

:: Run the main script
python main.py %*

endlocal
pause
