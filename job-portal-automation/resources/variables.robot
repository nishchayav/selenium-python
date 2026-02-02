*** Variables ***
${BROWSER}              Chrome
${BASE_URL}             https://example-job-portal.com

${SEARCH_INPUT}         xpath=//input[@placeholder='Search jobs']
${LOCATION_INPUT}       xpath=//input[@placeholder='Location']
${SEARCH_BUTTON}        xpath=//button[contains(text(),'Search')]

${JOB_CARDS}            xpath=//div[contains(@class,'job-card')]
${JOB_TITLE}            xpath=.//h2[contains(@class,'job-title')]
${JOB_EXPERIENCE}       xpath=.//span[contains(@class,'experience')]

${NO_RESULTS_TEXT}      xpath=//div[contains(text(),'No jobs found')]

${FILTER_EXP_0_2}       xpath=//label[contains(text(),'0-2')]/preceding-sibling::input
${FILTER_FULLTIME}      xpath=//label[contains(text(),'Full-time')]/preceding-sibling::input
${FILTER_LOCATION}      xpath=//label[contains(text(),'Bangalore')]/preceding-sibling::input
${FILTER_DATE_POSTED}   xpath=//label[contains(text(),'Last 7 days')]/preceding-sibling::input

${SORT_DROPDOWN}        xpath=//select[@id='sort']
${SORT_RELEVANCE}       Relevance
${SORT_DATE}            Date

${JOB_DETAIL_TITLE}     xpath=//h1[contains(@class,'job-title')]
${JOB_DETAIL_COMPANY}   xpath=//div[contains(@class,'company-name')]
${JOB_DETAIL_LOCATION}  xpath=//div[contains(@class,'job-location')]
${APPLY_BUTTON}         xpath=//button[contains(text(),'Apply')]
