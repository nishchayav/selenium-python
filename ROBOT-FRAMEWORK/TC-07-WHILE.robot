*** Test Cases ***

Print names using WHILE loop
    ${count} =    Set Variable    1
    WHILE        ${count}<=5
        Log To Console    ${count}
        ${count} =    Evaluate    ${count} + 1
    END


WHILE Loop Example
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END


WHILE Loop With BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log    ${i}
        ${i}=    Evaluate    ${i} + 1
    END
