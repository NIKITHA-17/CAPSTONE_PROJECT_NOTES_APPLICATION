# Notes Application - UI + API Hybrid Automation Framework 

This project is a Selenium Python Pytest automation framework for the ExpandTesting Notes Application.We should use pytest framework for automation of both UI nad API testing.Also genrate rports,logs,allure_results.

It covers:
- UI Automation
- API Automation
- Hybrid UI + API E2E Testing
- Negative Testing
- Logging
- Screenshot Capture
- HTML Reporting
- Allure Reporting
- Parallel Execution
- Selenium Grid
- Jenkins CI/CD Pipeline

## Tech Stack that used to do this project
- Python
- Selenium WebDriver
- Pytest
- Requests Library
- Pytest-xdist
- Pytest-rerunfailures
- Pytest-html
- Allure Reports
- Docker
- Selenium Grid
- Jenkins

## Application that is given for testing of both UI and API:

UI:
https://practice.expandtesting.com/notes/app

API:
https://practice.expandtesting.com/notes/api/api-docs/

## To Run Tests Locally thae commands that used are:

python -m pytest tests -v

## To run Tests in Parallel Execution

python -m pytest tests -n 2 -v

## To generate HTML Report the commands are:

python -m pytest tests -n 2 -v --html=reports/final_report.html --self-contained-html

## To generate Allure Report the commands are;

python -m pytest tests -v --alluredir=allure-results
allure serve allure-results

## To run the Selenium Grid using Docker:
commands are:

Start Grid:

-> docker-compose up -d

Run tests on Grid:

-> set GRID=true
-> python -m pytest tests/test_login.py -v

Stop Grid:

-> docker-compose down


Agentic Automation

## Agentic Automation / Self-Healing Locator Concept

The framework supports the concept of self-healing locators by trying alternate locator strategies when the primary locator fails.

Example:
- Primary locator: data-testid
- Fallback locator: ID
- Final fallback locator: XPath text match

This improves stability when UI attributes change slightly.

## Project Structure


project/
│── config/
│   ├── config.yaml
│   └── environment.py
│
├── tests
│   ├── api/
├── tests/
│   ├── ui/
│   ├── api/
│   └── e2e/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── home_page.py
│
├── services/
│   ├── auth_service.py
│   └── notes_service.py
│   ├── api_client.py
├── utils/
│   └── logger.py
│   └── self_healing.py 
├── conftest.py
│   
│
├── fixtures/
│   ├── browser_fixture.py
│
├── reports/
├── output/
├── logs/
├── screenshots/
├── allure-results/
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
└── README.md

## Key Achievements

-> Enterprise-style automation framework
-> Hybrid UI + API validation
-> Selenium Grid implementation
-> Dockerized execution environment
-> CI/CD integration using Jenkins
->Allure Reports 
->Parallel execution support
->Intelligent wait and retry handling
->Reporting and logging integration
->screenshorts captures if testcases failed

## Setup Instructions

=> Generate HTML Report

pytest tests -v --html=reports/final_report.html --self-contained-html

=>Generate Allure Report

pytest tests -v --alluredir=allure-results

=>Open Allure report:

allure serve allure-results