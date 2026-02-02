*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.robot

*** Keywords ***

Apply Experience Filter 0 To 2 Years
    Click Element    ${FILTER_EXP_0_2}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Apply Job Type Full Time
    Click Element    ${FILTER_FULLTIME}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Apply Location Filter
    Click Element    ${FILTER_LOCATION}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Apply Date Posted Filter
    Click Element    ${FILTER_DATE_POSTED}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Validate Experience Range
    ${experience}=    Get Text    (${JOB_CARDS})[1]${JOB_EXPERIENCE}
    Should Contain Any    ${experience}    0-2    Fresher

Sort Jobs By Relevance
    Select From List By Label    ${SORT_DROPDOWN}    ${SORT_RELEVANCE}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s

Sort Jobs By Date
    Select From List By Label    ${SORT_DROPDOWN}    ${SORT_DATE}
    Wait Until Element Is Visible    ${JOB_CARDS}    15s
