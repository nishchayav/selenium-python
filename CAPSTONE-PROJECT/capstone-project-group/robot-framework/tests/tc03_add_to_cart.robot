*** Settings ***
Resource    ../resources/common.robot
Library    DataDriver    ../variables/search_data.csv
Resource    ../keywords/cart_keywords.robot
Resource   ../keywords/search_keywords.robot
Resource    ../keywords/product_keywords.robot

Suite Setup     Open Site
Suite Teardown  Close Site
Test Teardown   Capture Screenshot On Failure

Test Template   Search And View



*** Test Cases ***
add to cart for product- ${product}

*** Keywords ***
Search and View
    [Arguments]    ${product}
    Search Products
    input search    ${product}
    input enter
    validation
    Open First Product Details
    Add Product To Cart And Validate Success