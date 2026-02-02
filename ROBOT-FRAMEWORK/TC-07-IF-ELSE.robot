1️⃣ IF condition (basic)
*** Test Cases ***
IF Condition Example
    ${age}=    Set Variable    17
    IF    ${age} >= 18
        Log    Eligible to vote
    END


IF ELSE Example
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log    Greater than 10
    ELSE
        Log    Less than or equal to 10
    END


IF ELSE IF Example
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log    Grade A
    ELSE IF    ${marks} >= 75
        Log    Grade B
    ELSE
        Log    Grade C
    END


Inline IF Example
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log    Test Passed
