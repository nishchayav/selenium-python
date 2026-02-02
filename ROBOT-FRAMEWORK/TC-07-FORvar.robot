#️⃣ FOR loop with list variable
*** Variables ***
@{COLORS}    Red    Green    Blue
@{USERS}    admin    user
@{PWDS}     admin123    user123

*** Test Cases ***
FOR Loop With List
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END

FOR Loop Zip
    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PWDS}
        Log    ${u} / ${p}
    END