*** Settings ***
Resource    ../keywords/common_keywords.robot
Suite Setup     Open Browser To Application
Suite Teardown  Close Browser


*** Test Cases ***
Search Product and View Details
    Search Product    iPhone
