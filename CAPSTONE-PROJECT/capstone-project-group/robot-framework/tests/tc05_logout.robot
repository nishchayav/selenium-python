*** Settings ***

Library    DataDriver    ../variables/login_data.csv

Resource   ../resources/common.robot
Resource    ../keywords/logout_keywords.robot



Suite Setup     Open Site
Suite Teardown  Close Site
Test Teardown   Capture Screenshot On Failure

Test Template   Logout


*** Test Cases ***

Logout for email - ${email}

*** Keywords ***
Logout
    [Arguments]    ${email}    ${password}

    Login User
    input email for login    ${email}
    input password for login    ${password}
    click login 
    Logout User Successfully