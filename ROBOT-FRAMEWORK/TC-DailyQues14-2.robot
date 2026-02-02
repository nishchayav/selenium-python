*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn


*** Variables ***
${URL}        https://www.selenium.dev/selenium/web/web-form.html
${BROWSER}    Chrome


*** Test Cases ***
Browser Automation With BuiltIn Keywords
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Text Box
    Input Text    name=my-text    RobotFramework
    Log To Console    Text entered in text box

    # Radio Button
    Click Element    id=my-radio-1
    Log To Console    Radio button selected

    # Check Box
    Click Element    id=my-check-1
    Log To Console    Check box selected

    # Drop-down
    Select From List By Label    name=my-select    Two
    Log To Console    Dropdown value selected

    # BuiltIn Keyword - Run Keyword If
    ${title}=    Get Title
    Run Keyword If    '${title}' != ''    Log To Console    Page title is available

    Sleep    5s
    Close Browser
