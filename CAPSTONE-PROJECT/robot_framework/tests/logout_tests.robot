*** Settings ***
Resource    ../keywords/common_keywords.robot
Suite Setup     Open Browser To Application
Suite Teardown  Close Browser
Test Teardown   Capture Page Screenshot

*** Test Cases ***
Logout and Session Validation
    Click My Account
    Click Login
    Login User    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Logout User
