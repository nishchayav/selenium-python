*** Settings ***
Library         DataDriver    file=../testdata/registration_data.csv
Resource        ../keywords/common_keywords.robot
Test Template   Register New User
Suite Setup     Open Browser To Application
Suite Teardown  Close Browser
Test Teardown   Capture Page Screenshot

*** Test Cases ***
Registration With Multiple Users
    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

*** Keywords ***
Register New User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}
    Click My Account
    Click Register
    Register User    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}
