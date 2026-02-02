# Automated Job Search & Filtering Validation for Job Portal

## Project Overview
This project automates the validation of job search, filtering, sorting, and job detail navigation features of a generic job portal using Robot Framework and Selenium.

The automation is strictly read-only and does not perform any job application or form submission.

## Tools Used
- Robot Framework
- SeleniumLibrary
- Chrome Browser
- XPath & CSS Selectors
- Explicit Waits
- Robot Framework Reports & Logs

## Folder Structure
job-portal-automation
│
├── tests              → Test cases
├── keywords           → Reusable custom keywords
├── resources          → Global variables
├── reports            → Execution reports
└── README.md

## Prerequisites
- Python 3.x installed
- Chrome browser installed
- ChromeDriver compatible with browser version
- Robot Framework installed
- SeleniumLibrary installed

## Install Dependencies
pip install robotframework
pip install robotframework-seleniumlibrary

## How to Execute Tests
Navigate to the project root directory and run

robot -d reports tests

## Sample Command
robot -d reports teststest_jobsearch.robot

## Output
- report.html
- log.html
- output.xml

All reports will be generated inside the `reports` folder.
