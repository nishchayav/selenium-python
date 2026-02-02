*** Test Cases ***
Print names using FOR loop
    FOR    ${name}    IN    Ram Ravi Taj
        Log To Console    ${name}

    END

FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END

FOR Loop Range
    FOR    ${i}    IN RANGE    1    6
        Log    Number: ${i}
    END

FOR Loop With Step
    FOR    ${i}    IN RANGE    0    10    2
        Log    Value: ${i}
    END

FOR Loop Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log    ${index} = ${value}
    END

FOR Loop With IF
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log    Found 3
        END
    END

Nested FOR Loop
    FOR    ${i}    IN RANGE    1    4
        FOR    ${j}    IN RANGE    1    3
            Log    i=${i}, j=${j}
        END
    END









