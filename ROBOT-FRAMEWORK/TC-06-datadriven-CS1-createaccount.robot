*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Process
Suite Setup    Open Qafox
Suite Teardown    Close Qafox

*** Variables ***
${URL}       https://tutorialsninja.com/demo/
${BROWSER}   chrome

*** Keywords ***
Open Qafox
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Generate Random Email
    ${rand}=    Generate Random String    5    [LETTERS]
    ${email}=   Set Variable    user${rand}@test.com
    RETURN    ${email}

Create Demo Account
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a/span[1]
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[1]/a

    Wait Until Element Is Visible    name=firstname    10s

    ${email}=    Generate Random Email
    ${password}=    Set Variable    Test@123

    Input Text    name=firstname    Demo
    Input Text    name=lastname     User
    Input Text    name=email        ${email}
    Input Text    name=telephone    9999999999
    Input Text    name=password     ${password}
    Input Text    name=confirm      ${password}

    Click Element    name=agree
    Click Button    xpath=//input[@value='Continue']

    Wait Until Page Contains    Your Account Has Been Created    10s

    Save To Excel    ${email}    ${password}

    Logout From Qafox

Save To Excel
    [Arguments]    ${email}    ${password}
    Run Process    python    DDexcelwrite.py    ${email}    ${password}

Logout From Qafox
    # Logout from right panel
    Click Element    //*[@id="column-right"]/div/a[13]
    Click Element    //*[@id="content"]/div/div/a

    # Reset dropdown state safely
    Mouse Over    xpath=//*[@id="top-links"]/ul/li[2]/a/span[1]
    sleep        5s

Close Qafox
    Close Browser

*** Test Cases ***
Create 5 Demo Accounts
    FOR    ${i}    IN RANGE    5
        Create Demo Account
    END
