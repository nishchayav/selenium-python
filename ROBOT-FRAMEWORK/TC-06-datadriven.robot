*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      Chrome


*** Keywords ***
open orangehrm
    open browser    ${url}     ${browser}
    maximize browser window
orangehrmlogin
    [Arguments]    ${username}    ${password}
    input text    name=username    ${username}
    input text    name=password    ${password}
    sleep           5s
     capture page screenshot    beforelogin.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep           5s
    capture page screenshot    afterlogin.png
    close browser


*** Test Cases ***
TC-06-datadriven.robot
    open orangehrm
    orangehrmlogin    Admin     admin123

