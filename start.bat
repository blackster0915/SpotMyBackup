@echo off
rem Starts the local server and opens SpotMyBackup in the default browser.
if not exist "%~dp0config.json" (
    copy "%~dp0config.example.json" "%~dp0config.json" >nul
    echo Created config.json - put the Client ID of your Spotify app into it, then reload the page.
)
start "" cmd /c "timeout /t 2 >nul & start http://127.0.0.1:8888"
python "%~dp0serve.py"
