*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=DDtestdataCS2.xlsx
Test Template    Qafox Login With Excel
Suite Setup    Open Qafox
Suite Teardown    Close Qafox

*** Variables ***
${URL}       https://tutorialsninja.com/demo/
${BROWSER}   chrome

*** Keywords ***
Open Qafox
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Qafox Login With Excel
    [Arguments]    ${email}    ${password}
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a/span[1]
    sleep        5s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[2]/a
    Wait Until Element Is Visible    name=email    10s
    Input Text    name=email    ${email}
    Input Text    name=password    ${password}
    Capture Page Screenshot        afterloginCS1.png
    Click Button    xpath=//input[@value='Login']

    sleep        10s
    Logout From Qafox

Logout From Qafox
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a/span[1]
    Sleep        5s
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/ul/li[5]/a
    Capture Page Screenshot        afterloginCS2.png
    Sleep        5s

Close Qafox
    Close Browser

*** Test Cases ***
Login with user from Excel
    Log    Executed via DataDriver
