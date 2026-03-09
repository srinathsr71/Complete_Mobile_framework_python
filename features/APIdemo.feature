Feature: Navigation in API Demos app

@tc01APIDemos @APIDemos
  Scenario: Navigate to App Activity Custom Title
    Given the API Demos app is launched
    When  the user clicks on App
    Then the user clicks on Activity
    Then the user clicks on Custom Title
    Then the Custom Title screen should be displayed


@tc02ADemos  @APIDemos
  Scenario Outline: Enter text in Custom Title
    Given the API Demos app is launched
    When  the user clicks on App
    Then the user clicks on Activity
    Then the user clicks on Custom Title
    Then the user enters "<lefttextbox>" in Left Text Box
    Then the user enters "<righttextbox>" in Right Text Box
    Then the user clicks on Change Left Title
    Then the left title should display as "<lefttextbox>"

  Examples:
  |lefttextbox|righttextbox|
  |Hello Appium|Python Automation|



@tc03ADemos   @APIDemos
  Scenario: Select and verify checkbox
    Given the API Demos app is launched
    When the user clicks on Views
    Then user clicks on Controls
    Then user clicks on Light Theme
    Then the user selects the Checkbox
    Then the checkbox should be checked


@tc04ADemos  @APIDemos
Scenario: Select RadioButton2
  Given the API Demos app is launched
  When the user clicks on Views
  Then user clicks on Controls
  Then user clicks on Dark Theme
  Then the user selects RadioButton2
  Then RadioButton2 should be selected

@tc05ADemos  @APIDemos
  Scenario Outline: Select planet from dropdown
    Given the API Demos app is launched
    When the user clicks on Views
    Then user clicks on Controls
    Then user clicks on Dark Theme
    Then the user clicks the Spinner dropdown
    Then the user selects "<selection>"
    Then "<selection>" should be displayed as selected option
  Examples:
  |selection|
  |Earth|

@tc06ADemos  @APIDemos
Scenario: Handle OK Cancel dialog
    Given the API Demos app is launched
    When user clicks on App
    Then user clicks on alert dialogs
    Then the user clicks OK Cancel dialog with a message
    Then the user clicks OK
    Then the dialog should close successfully

@tc07ADemos   @APIDemos
  Scenario Outline: Choose a specific date
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Date Widgets
    Then user clicks on Dialog
    Then the user clicks CHANGE THE DATE
    Then the user selects date "<date>"
    Then the selected "<date>" should be displayed
  Examples:
  |date|
  |15|


