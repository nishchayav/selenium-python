*** Test Cases ***
BREAK Example
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log    ${i}
    END

CONTINUE Example
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log    ${i}
    END
