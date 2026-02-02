*** Settings ***
Library    BuiltIn

Suite Setup       Suite Level Setup
Suite Teardown    Suite Level Teardown
Test Setup        Test Level Setup
Test Teardown     Test Level Teardown


*** Test Cases ***
Tagged Test Case - Login Check
    [Tags]    smoke
    Log To Console    Executing tagged smoke test
    Log    Smoke test executed successfully

Regular Test Case - Sanity Check
    Log To Console    Executing regular sanity test
    Log    Sanity test executed successfully


*** Keywords ***
Suite Level Setup
    Log To Console    ===== Suite Setup: Initializing test suite =====
    Log    Suite setup completed

Suite Level Teardown
    Log To Console    ===== Suite Teardown: Cleaning up test suite =====
    Log    Suite teardown completed

Test Level Setup
    Log To Console    ---- Test Setup: Preparing test ----
    Log    Test setup completed

Test Level Teardown
    Log To Console    ---- Test Teardown: Finishing test ----
    Log    Test teardown completed
