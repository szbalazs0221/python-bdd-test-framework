Feature: Error handling on the cucumber.io login page

    Scenario: Log in with an invalid email address
        
        Given Cucumber.io login page
        When The user is trying to log in with invalid credentials: (email: "test_user_invalid@testde.com", password: "myvalidpassword")
        Then An error message shows up

    Scenario: Log in with an invalid password
    
        Given Cucumber.io login page
        When The user is trying to log in with invalid credentials: (email: "test_user_valid@testde.com", password: "myinvalidpassword")
        Then An error message shows up

    Scenario: Log in with an invalid password and email address
        
        Given Cucumber.io login page
        When The user is trying to log in with invalid credentials: (email: "test_user_invalid@testde.com", password: "myinvalidpassword")
        Then An error message shows up

    
    Scenario Outline: Invalid Log in

        Given Cucumber.io login page
        When The user is trying to log in with invalid credentials: (email: "<email>", password: "<password>")
        Then An error message shows up

        Examples: Data
        | email                               | password          |
        | test_user_invalid@testde.com        | myvalidpassword   |
        | test_user_invalid@testde.com        | myvalidpassword   |
        | test_user_valid@testde.com          | myinvalidpassword |

