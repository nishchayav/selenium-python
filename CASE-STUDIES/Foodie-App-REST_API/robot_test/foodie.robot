*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           String
Suite Setup       Create Session    foodie    http://127.0.0.1:5000

*** Variables ***
${BASE}           /api/v1

*** Test Cases ***

1 Register Restaurant
    ${random}=    Generate Random String    5
    ${name}=    Set Variable    FoodHub_${random}
    ${body}=    Create Dictionary
    ...    name=${name}
    ...    category=Veg
    ...    location=Bhopal
    ...    images=["img1.jpg"]
    ...    contact=9876543210
    ${response}=    POST On Session    foodie    ${BASE}/restaurants    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${RESTAURANT_ID}    ${json['id']}

2 Update Restaurant
    ${body}=    Create Dictionary    location=Indore
    ${response}=    PUT On Session    foodie    ${BASE}/restaurants/${RESTAURANT_ID}    json=${body}
    Should Be Equal As Integers    ${response.status_code}    200

3 Disable Restaurant
    ${response}=    PUT On Session    foodie    ${BASE}/restaurants/${RESTAURANT_ID}/disable
    Should Be Equal As Integers    ${response.status_code}    200

4 View Restaurant
    ${response}=    GET On Session    foodie    ${BASE}/restaurants/${RESTAURANT_ID}
    Should Be Equal As Integers    ${response.status_code}    200

5 Add Dish
    ${body}=    Create Dictionary
    ...    name=Paneer
    ...    type=Veg
    ...    price=250
    ...    available_time=10AM-10PM
    ...    image=paneer.jpg
    ${response}=    POST On Session    foodie    ${BASE}/restaurants/${RESTAURANT_ID}/dishes    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${DISH_ID}    ${json['id']}

6 Update Dish
    ${body}=    Create Dictionary    price=300
    ${response}=    PUT On Session    foodie    ${BASE}/dishes/${DISH_ID}    json=${body}
    Should Be Equal As Integers    ${response.status_code}    200

7 Enable Disable Dish
    ${body}=    Create Dictionary    enabled=False
    ${response}=    PUT On Session    foodie    ${BASE}/dishes/${DISH_ID}/status    json=${body}
    Should Be Equal As Integers    ${response.status_code}    200

8 Delete Dish
    ${response}=    DELETE On Session    foodie    ${BASE}/dishes/${DISH_ID}
    Should Be Equal As Integers    ${response.status_code}    200

9 Approve Restaurant
    ${response}=    PUT On Session    foodie    ${BASE}/admin/restaurants/${RESTAURANT_ID}/approve
    Should Be Equal As Integers    ${response.status_code}    200

10 Admin Disable Restaurant
    ${response}=    PUT On Session    foodie    ${BASE}/admin/restaurants/${RESTAURANT_ID}/disable
    Should Be Equal As Integers    ${response.status_code}    200

11 View Feedback
    ${response}=    GET On Session    foodie    ${BASE}/admin/feedback
    Should Be Equal As Integers    ${response.status_code}    200

12 View Orders (Admin)
    ${response}=    GET On Session    foodie    ${BASE}/admin/orders
    Should Be Equal As Integers    ${response.status_code}    200

13 User Registration
    ${random}=    Generate Random String    5
    ${email}=    Set Variable    user_${random}@mail.com
    ${body}=    Create Dictionary
    ...    name=TestUser
    ...    email=${email}
    ...    password=123456
    ${response}=    POST On Session    foodie    ${BASE}/users/register    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${USER_ID}    ${json['id']}

14 Search Restaurants
    ${response}=    GET On Session    foodie    ${BASE}/restaurants/search    params=name=Food
    Should Be Equal As Integers    ${response.status_code}    200

15 Place Order
    ${body}=    Create Dictionary
    ...    user_id=${USER_ID}
    ...    restaurant_id=${RESTAURANT_ID}
    ...    dishes=["Paneer"]
    ${response}=    POST On Session    foodie    ${BASE}/orders    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    Set Suite Variable    ${ORDER_ID}    ${json['id']}

16 Give Rating
    ${body}=    Create Dictionary
    ...    order_id=${ORDER_ID}
    ...    rating=5
    ...    comment=Excellent
    ${response}=    POST On Session    foodie    ${BASE}/ratings    json=${body}
    Should Be Equal As Integers    ${response.status_code}    201

17 View Orders By Restaurant
    ${response}=    GET On Session    foodie    ${BASE}/restaurants/${RESTAURANT_ID}/orders
    Should Be Equal As Integers    ${response.status_code}    200

18 View Orders By User
    ${response}=    GET On Session    foodie    ${BASE}/users/${USER_ID}/orders
    Should Be Equal As Integers    ${response.status_code}    200
