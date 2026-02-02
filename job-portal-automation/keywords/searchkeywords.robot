*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.robot

*** Keywords ***

Open Job Portal
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    ${SEARCH_INPUT}    15s

Search Job With Keyword And Location
    [Arguments]    ${keyword}    ${location}
    Input Text     ${SEARCH_INPUT}    ${keyword}
    Input Text     ${LOCATION_INPUT}  ${location}
    Click Button   ${SEARCH_BUTTON}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Validate Job Results Are Displayed
    ${count}=    Get Element Count    ${JOB_CARDS}
    Should Be True    ${count} > 0    No job results displayed

Validate Job Title Contains Keyword
    [Arguments]    ${keyword}
    ${title}=    Get Text    (${JOB_CARDS})[1]${JOB_TITLE}
    Should Contain    ${title}    ${keyword}

Search For Invalid Job
    [Arguments]    ${keyword}
    Input Text     ${SEARCH_INPUT}    ${keyword}
    Click Button   ${SEARCH_BUTTON}
    Wait Until Element Is Visible    ${NO_RESULTS_TEXT}    15s

Validate No Results Message
    Element Should Be Visible    ${NO_RESULTS_TEXT}

Open First Job Details
    Click Element    (${JOB_CARDS})[1]
    Wait Until Element Is Visible    ${JOB_DETAIL_TITLE}    15s

Validate Job Details Page
    Element Should Be Visible    ${JOB_DETAIL_TITLE}
    Element Should Be Visible    ${JOB_DETAIL_COMPANY}
    Element Should Be Visible    ${JOB_DETAIL_LOCATION}
    Element Should Be Visible    ${APPLY_BUTTON}

Close Browser Session
    Close Browser
