echo off
set ANACONDA_ROOT=C:\Anaconda3
@call "%ANACONDA_ROOT%\Scripts\activate.bat" %ANACONDA_ROOT%
python "%~dp0OctToDec.py"
pause >nul