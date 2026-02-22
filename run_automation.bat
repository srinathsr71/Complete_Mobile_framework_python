@echo off
setlocal EnableDelayedExpansion
title Python Web + Mobile Automation Runner

cls
echo ===============================================================
echo            PYTHON AUTOMATION EXECUTION PANEL
echo ===============================================================
echo.

:: ===============================================================
:: PLATFORM TYPE (WEB / MOBILE)
:: ===============================================================
echo Select Execution Platform
echo ----------------------------------
echo  1) Web (Selenium - Python)
echo  2) Mobile (Appium - Python)
echo ----------------------------------
set /p platformTypeChoice=Enter choice (1 or 2):

if "%platformTypeChoice%"=="1" set PLATFORM_TYPE=web
if "%platformTypeChoice%"=="2" set PLATFORM_TYPE=mobile

if "%PLATFORM_TYPE%"=="" (
    echo Invalid platform selection
    pause
    exit /b
)

:: ===============================================================
:: ENVIRONMENT SELECTION
:: ===============================================================
cls
echo ===============================================================
echo               SELECT ENVIRONMENT
echo ===============================================================
echo  1) Dev
echo  2) Test
echo  3) Stage
echo  4) Prod
echo ----------------------------------
set /p envChoice=Enter choice (1-4):

if "%envChoice%"=="1" set ENV=dev
if "%envChoice%"=="2" set ENV=test
if "%envChoice%"=="3" set ENV=stage
if "%envChoice%"=="4" set ENV=prod

if "%ENV%"=="" (
    echo Invalid environment selection
    pause
    exit /b
)

:: ===============================================================
:: WEB FLOW
:: ===============================================================
if "%PLATFORM_TYPE%"=="web" goto WEB_FLOW

:: ===============================================================
:: MOBILE FLOW
:: ===============================================================
if "%PLATFORM_TYPE%"=="mobile" goto MOBILE_FLOW


:: ===============================================================
:: WEB EXECUTION
:: ===============================================================
:WEB_FLOW
cls
echo ===============================================================
echo                 WEB AUTOMATION
echo ===============================================================

echo Select Browser
echo ----------------------------------
echo  1) Chrome
echo  2) Firefox
echo ----------------------------------
set /p browserChoice=Enter choice (1 or 2):

if "%browserChoice%"=="1" set BROWSER=chrome
if "%browserChoice%"=="2" set BROWSER=firefox

if "%BROWSER%"=="" (
    echo Invalid browser selection
    pause
    exit /b
)

echo.
echo Select Browser Mode
echo ----------------------------------
echo  1) Normal
echo  2) Headless
echo ----------------------------------
set /p modeChoice=Enter choice (1 or 2):

if "%modeChoice%"=="1" set HEADLESS=false
if "%modeChoice%"=="2" set HEADLESS=true

echo.
set /p TAGS=Enter pytest markers (example: smoke or regression):

cls
echo ===============================================================
echo                 EXECUTION SUMMARY
echo ===============================================================
echo PLATFORM TYPE : WEB
echo ENVIRONMENT   : %ENV%
echo BROWSER       : %BROWSER%
echo HEADLESS      : %HEADLESS%
echo TAGS          : %TAGS%
echo ===============================================================
echo.

pytest -v -m "%TAGS%" --alluredir=allure-results

goto END


:: ===============================================================
:: MOBILE EXECUTION
:: ===============================================================
:MOBILE_FLOW
cls
echo ===============================================================
echo                MOBILE AUTOMATION
echo ===============================================================

echo Select Mobile OS
echo ----------------------------------
echo  1) Android
echo  2) iOS
echo ----------------------------------
set /p osChoice=Enter choice (1 or 2):

if "%osChoice%"=="1" set PLATFORM=android
if "%osChoice%"=="2" set PLATFORM=ios

if "%PLATFORM%"=="" (
    echo Invalid mobile OS selection
    pause
    exit /b
)

cls
echo ===============================================================
echo                DEVICE TYPE
echo ===============================================================
echo  1) Real Device
echo  2) Emulator / Simulator
echo ----------------------------------
set /p deviceChoice=Enter choice (1 or 2):

if "%deviceChoice%"=="1" set DEVICE=mobile
if "%deviceChoice%"=="2" (
    if "%PLATFORM%"=="android" set DEVICE=emulator
    if "%PLATFORM%"=="ios" set DEVICE=simulator
)

if "%DEVICE%"=="" (
    echo Invalid device selection
    pause
    exit /b
)

cls
echo ===============================================================
echo              EXECUTION MODE
echo ===============================================================
echo  1) Local Appium
echo  2) Remote Cloud / Grid
echo ----------------------------------
set /p execChoice=Enter choice (1 or 2):

if "%execChoice%"=="1" (
    set EXEC_MODE=local
)

if "%execChoice%"=="2" (
    set EXEC_MODE=remote
    set REMOTE_SERVER_URL=https://hub.browserstack.com/wd/hub
)

if "%EXEC_MODE%"=="" (
    echo Invalid execution mode
    pause
    exit /b
)

cls
echo ===============================================================
echo                 TAG SELECTION
echo ===============================================================
set /p TAGS=Enter pytest markers (example: smoke or regression):

cls
echo ===============================================================
echo                 EXECUTION SUMMARY
echo ===============================================================
echo PLATFORM TYPE : MOBILE
echo ENVIRONMENT   : %ENV%
echo PLATFORM      : %PLATFORM%
echo DEVICE        : %DEVICE%
echo EXECUTION     : %EXEC_MODE%
echo TAGS          : %TAGS%
echo ===============================================================
echo.

set PYTHONUNBUFFERED=1
echo ===============================================================
echo                 CLEAN ALLURE RESULTS
echo ===============================================================
if exist allure-results (
    rmdir /s /q allure-results
)
mkdir allure-results

if "%EXEC_MODE%"=="local" (
    pytest -v -m "%TAGS%" --alluredir=allure-results
) else (
    pytest -v -m "%TAGS%" --alluredir=allure-results
)

goto END


:: ===============================================================
:: END
:: ===============================================================
:END
echo.
echo ===============================================================
echo                EXECUTION COMPLETED
echo ===============================================================
set REPORT_TS=%DATE:~-4%%DATE:~4,2%%DATE:~7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set REPORT_TS=%REPORT_TS: =0%

set REPORT_DIR=allure-report-%REPORT_TS%

echo Generating Allure Report...
allure generate allure-results -o %REPORT_DIR%
pause
exit /b
