*** Settings ***
Documentation    Simple test to show a prerunmodifier capabilities

*** Test Cases ***
Simple cool test
    [Tags]    S1    S2    S3
    Log    Some cool test

*** Keywords ***
Precondition for S1
    Log    Precondition for S1

Precondition for S2
    Log    Precondition for S2

Precondition for S3
    Log    Precondition for S3
