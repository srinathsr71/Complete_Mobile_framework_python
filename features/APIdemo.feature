Feature: Navigation in API Demos app
@tc01APIDemos
  Scenario: Navigate to App Activity Custom Title
    Given the API Demos app is launched
    When the user clicks on "App"
    And the user clicks on "Activity"
    And the user clicks on "Custom Title"
    Then the Custom Title screen should be displayed
