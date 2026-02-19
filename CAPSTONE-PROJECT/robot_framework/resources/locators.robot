*** Variables ***

${MY_ACCOUNT}              xpath=//span[text()='My account']
${REGISTER}                xpath=//a[text()='Register']
${LOGIN}                   xpath=//a[text()='Login']
${LOGOUT}                  xpath=//a[text()='Logout']

${FIRST_NAME}              id=input-firstname
${LAST_NAME}               id=input-lastname
${EMAIL}                   id=input-email
${TELEPHONE}               id=input-telephone
${PASSWORD}                id=input-password
${CONFIRM_PASSWORD}        id=input-confirm
${PRIVACY_POLICY}          name=agree
${CONTINUE_BTN}            xpath=//input[@value='Continue']

${LOGIN_EMAIL}             id=input-email
${LOGIN_PASSWORD}          id=input-password
${LOGIN_BTN}               xpath=//input[@value='Login']

${SEARCH_BOX}              name=search
${SEARCH_BUTTON}           xpath=//button[@type='submit']
${PRODUCT_TITLE}           xpath=//h1

${COOKIE_ACCEPT}    xpath=//button[contains(text(),'Accept')]

${ADD_TO_CART}             id=button-cart
${CART_TOTAL}              id=cart-total
${VIEW_CART}               xpath=//strong[text()=' View Cart']

${QUANTITY_INPUT}          xpath=//input[contains(@name,'quantity')]
${UPDATE_CART_BTN}         xpath=//button[@data-original-title='Update']
${REMOVE_ITEM_BTN}         xpath=//button[@data-original-title='Remove']
