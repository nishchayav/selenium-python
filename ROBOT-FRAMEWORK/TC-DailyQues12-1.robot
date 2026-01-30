*** Settings ***
Library    BuiltIn


*** Variables ***
${NAME}        Nishchaya
${COURSE}      Automation Testing
@{NUMBERS}     1    2    3    4    5


*** Test Cases ***
Test Case 1 - Logging Messages
    Log    This is a log message using BuiltIn Log keyword
    Log To Console    Hello ${NAME}, welcome to ${COURSE}
    Log    List of numbers is: ${NUMBERS}


Test Case 2 - Variable Demonstration
    Log    Scalar variable NAME value is ${NAME}
    Log    First number from list is ${NUMBERS}[0]
    Log To Console    Robot Framework execution successful
