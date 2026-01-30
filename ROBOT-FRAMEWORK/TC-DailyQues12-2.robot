*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary


*** Test Cases ***
Verify Automation Environment Setup
    Log To Console    ===== Verifying Automation Environment =====

    Verify Python Installation
    Print Robot Framework Version
    Verify SeleniumLibrary Import

    Log To Console    ===== Environment Verification Completed Successfully =====


*** Keywords ***
Verify Python Installation
    Log    Checking Python installation
    ${result}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${result.rc} != 0    Fail    Python is not installed
    Log To Console    Python Installed: ${result.stdout}



Print Robot Framework Version
    ${result}=    Run Process    python    -m    robot    --version    stdout=PIPE
    Log    Robot Framework Version: ${result.stdout}
    Log To Console    Robot Framework Version: ${result.stdout}


Verify SeleniumLibrary Import
    Log    Verifying SeleniumLibrary import
    Run Keyword And Continue On Failure    Import Library    SeleniumLibrary
    Log To Console    SeleniumLibrary Imported Successfully
