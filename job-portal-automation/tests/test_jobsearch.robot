*** Settings ***
Library    SeleniumLibrary
Resource   ../keywords/searchkeywords.robot

Suite Setup     Open Job Portal
Suite Teardown  Close Browser Session

*** Test Cases ***

Validate Job Search Functionality
    Search Job With Keyword And Location    Software Tester    Bangalore
    Validate Job Results Are Displayed
    Validate Job Title Contains Keyword    Software

Validate No Results Scenario
    Search For Invalid Job    Astronaut Python Ninja
    Validate No Results Message

Validate Job Details Page
    Search Job With Keyword And Location    Software Tester    Bangalore
    Open First Job Details
    Validate Job Details Page
