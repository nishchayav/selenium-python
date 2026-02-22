*** Settings ***

Library    DataDriver    ../variables/register_data.csv

Resource   ../resources/common.robot
Resource   ../keywords/register_keywords.robot
Resource    ../keywords/login_keywords.robot

Suite Setup     Open Site
Suite Teardown  Close Site
Test Teardown   Capture Screenshot On Failure

Test Template   Registration


*** Test Cases ***

Register User With CSV for user ${firstname} ${lastname}

*** Keywords ***
Registration
    [Arguments]    ${firstname}    ${lastname}    ${phone}    ${password}

    Register New User
    input firstname    ${firstname}
    input lastname    ${lastname}
    input email    
    Input Phone    ${phone}
    input password    ${password}
    Click agree
    Click continue
    Click logout
    Login User Successfully    ${password}
    Click logout