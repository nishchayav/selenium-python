⚠️ ERROR HANDLING (Control Structure)
1️⃣7️⃣ TRY / EXCEPT / FINALLY
*** Test Cases ***
Try Except Example
    TRY
        Fail    Something went wrong
    EXCEPT
        Log    Error handled
    FINALLY
        Log    Always executed
    END

#CONDITIONAL KEYWORD EXECUTION

Run Keyword If Example
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log    Test Passed

Run Keyword Unless Example
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log    Test Failed

