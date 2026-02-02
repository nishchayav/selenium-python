*** Settings ***
Library    SeleniumLibrary
Resource   ../keywords/searchkeywords.robot
Resource   ../keywords/filterkeywords.robot

Suite Setup     Open Job Portal
Suite Teardown  Close Browser Session

*** Test Cases ***

Validate Job Filters Functionality
    Search Job With Keyword And Location    Software Tester    Bangalore
    Apply Experience Filter 0 To 2 Years
    Apply Job Type Full Time
    Apply Location Filter
    Apply Date Posted Filter
    Validate Experience Range

Validate Sorting Functionality
    Search Job With Keyword And Location    Software Tester    Bangalore
    Sort Jobs By Relevance
    Sort Jobs By Date
