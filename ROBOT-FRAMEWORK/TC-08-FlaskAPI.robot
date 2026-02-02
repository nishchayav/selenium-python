*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Create New User
    Create Session    api    ${BASE_URL}
    ${data}=    Create Dictionary    name=Nish
    ${response}=    POST On Session    api    /users    json=${data}
    Status Should Be    201    ${response}
    Log To Console    ${response.json()}

Update User
    ${data}=    Create Dictionary    name=Nishchaya
    ${response}=    PUT On Session    api    /users/1    json=${data}
    Status Should Be    200    ${response}
    Log To Console    ${response.json()}

Verify Get All Users
    ${response}=    GET On Session    api    /users
    Status Should Be    200    ${response}
    Log To Console    ${response.json()}

Verify Get Single User
    ${response}=    GET On Session    api    /users/1
    Status Should Be    200    ${response}
    Log To Console    ${response.json()}

Verify User Not Found
    ${response}=    GET On Session    api    /users/999
    Status Should Be    404    ${response}
    Log To Console    User not found as expected

Verify Delete User By ID
    ${response}=    DELETE On Session    api    /users/1
    Status Should Be    200    ${response}
    Log To Console    User deleted successfully
