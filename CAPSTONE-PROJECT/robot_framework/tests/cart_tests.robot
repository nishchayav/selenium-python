*** Settings ***
Resource    ../keywords/common_keywords.robot
Suite Setup     Open Browser To Application
Suite Teardown  Close Browser


*** Test Cases ***
Add Product To Cart
    Search Product    iPhone
    Add Product To Cart
