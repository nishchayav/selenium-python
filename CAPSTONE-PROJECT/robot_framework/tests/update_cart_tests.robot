*** Settings ***
Resource    ../keywords/common_keywords.robot
Suite Setup     Open Browser To Application
Suite Teardown  Close Browser


*** Test Cases ***
Update Cart Quantity and Remove Item
    Search Product    HP
    Add Product To Cart
    Open Cart
    Update Cart Quantity    2
    Remove Item From Cart
