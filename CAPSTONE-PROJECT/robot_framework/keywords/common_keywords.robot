*** Settings ***
Library    SeleniumLibrary    timeout=10
Variables  ../variables/variables.py
Resource   ../resources/locators.robot

*** Keywords ***

Open Browser To Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Handle Cookie Popup
    Log    Browser Launched Successfully

Click My Account
    Wait Until Element Is Visible    ${MY_ACCOUNT}    20s
    Scroll Element Into View         ${MY_ACCOUNT}
    Click Element                    ${MY_ACCOUNT}

Click Register
    Wait Until Element Is Visible    ${REGISTER}
    Click Element    ${REGISTER}

Click Login
    Wait Until Element Is Visible    ${LOGIN}
    Click Element    ${LOGIN}

Register User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}
    Input Text    ${FIRST_NAME}    ${firstname}
    Input Text    ${LAST_NAME}     ${lastname}
    Input Text    ${EMAIL}         ${email}
    Input Text    ${TELEPHONE}     ${telephone}
    Input Text    ${PASSWORD}      ${password}
    Input Text    ${CONFIRM_PASSWORD}    ${password}
    Click Element    ${PRIVACY_POLICY}
    Click Button     ${CONTINUE_BTN}
    Capture Page Screenshot

Login User
    [Arguments]    ${email}    ${password}
    Input Text    ${LOGIN_EMAIL}    ${email}
    Input Text    ${LOGIN_PASSWORD}    ${password}
    Click Button    ${LOGIN_BTN}
    Wait Until Page Contains    My Account
    Capture Page Screenshot

Handle Cookie Popup
    Run Keyword And Ignore Error    Wait Until Element Is Visible    ${COOKIE_ACCEPT}    5s
    Run Keyword And Ignore Error    Click Element    ${COOKIE_ACCEPT}

Search Product
    [Arguments]    ${product}
    Wait Until Element Is Visible    ${SEARCH_BOX}    15s
    Input Text    ${SEARCH_BOX}    ${product}
    Click Button  ${SEARCH_BUTTON}

    # Wait for product list
    Wait Until Element Is Visible    xpath=(//div[@class='product-thumb'])[1]    15s

    # Click first product image/title
    Click Element    xpath=(//div[@class='product-thumb'])[1]//a

    # Ensure product page loaded
    Wait Until Element Is Visible    ${ADD_TO_CART}    15s
    Capture Page Screenshot


Add Product To Cart
    Wait Until Element Is Visible    ${ADD_TO_CART}    15s
    Scroll Element Into View         ${ADD_TO_CART}
    Click Button                     ${ADD_TO_CART}
    Wait Until Element Is Visible    ${CART_TOTAL}    15s
    Capture Page Screenshot


Open Cart
    Click Element    ${CART_TOTAL}
    Click Element    ${VIEW_CART}

Update Cart Quantity
    [Arguments]    ${qty}
    Wait Until Element Is Visible    ${QUANTITY_INPUT}
    Clear Element Text    ${QUANTITY_INPUT}
    Input Text    ${QUANTITY_INPUT}    ${qty}
    Click Element    ${UPDATE_CART_BTN}
    Capture Page Screenshot

Remove Item From Cart
    Click Element    ${REMOVE_ITEM_BTN}
    Capture Page Screenshot

Logout User
    Click My Account
    Wait Until Element Is Visible    ${LOGOUT}
    Click Element    ${LOGOUT}
    Wait Until Page Contains    Account Logout
    Capture Page Screenshot
