Feature: Navigation in API Demos app

@tc01ADemos @APIDemos
  Scenario: Navigate to App Activity Custom Title
    Given the API Demos app is launched
    When  the user clicks on App
    Then the user clicks on Activity
    Then the user clicks on Custom Title
    Then the Custom Title screen should be displayed


@tc02ADemos @APIDemos
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



@tc03ADemos @APIDemos
  Scenario: Select and verify checkbox
    Given the API Demos app is launched
    When the user clicks on Views
    Then user clicks on Controls
    Then user clicks on Light Theme
    Then the user selects the Checkbox
    Then the checkbox should be checked


@tc04ADemos @APIDemos
Scenario: Select RadioButton2
  Given the API Demos app is launched
  When the user clicks on Views
  Then user clicks on Controls
  Then user clicks on Dark Theme
  Then the user selects RadioButton2
  Then RadioButton2 should be selected

@tc05ADemos @APIDemos
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

@tc06ADemos @APIDemos
Scenario: Handle OK Cancel dialog
    Given the API Demos app is launched
    When user clicks on App
    Then user clicks on alert dialogs
    Then the user clicks OK Cancel dialog with a message
    Then the user clicks OK
    Then the dialog should close successfully

@tc07ADemos @APIDemos
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

@tc08ADemos @APIDemos
 Scenario Outline: Choose specific time
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Date Widgets
    Then  user clicks on Dialog
    Then  the user clicks CHANGE THE TIME
    Then  the user selects hour "<hour>" and "<minute>"
    Then  the selected time should be displayed

  Examples:-
  |hour|minute|
  |10|30|

 @tc09ADemos @APIDemos
 Scenario: Scroll to find element
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  the user scrolls down the screen and click webview option
    Then  verify the title of the page



@tc10ADemos @APIDemos
 Scenario: Perform drag and drop
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Drag and Drop
    Then  the user drags the first dot to the second dot
    Then  verify the dropped text is visible


@tc11ADemos @APIDemos
 Scenario: Open context menu
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Expandable Lists
    Then  user clicks on custom adapter
    Then  the user long presses on People Names
    Then  verify the toast message by clicking sample action
#
@tc12ADemos @APIDemos
  Scenario: Display toast
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Popupmenu
    Then  the user clicks Make a Popup!
    Then  the user selects an option
    Then  a toast message should appear

@tc13ADemos @APIDemos
 Scenario: Interact with WebView content
     Given the API Demos app is launched
    When  the user clicks on Views
    Then  the user scrolls down the screen and click webview option
    Then  user click on link in the webview
    Then  the text should be displayed

 @tc14ADemos @APIDemos
 Scenario: Rotate device
    Given the API Demos app is launched
    When the device orientation changes to landscape
    Then the application should adjust to landscape mode


@tc15ADemos @APIDemos
 Scenario: Perform pinch gesture
    Given the API Demos app is launched
    When  the user clicks on Views
    Then  user clicks on Gallery
    Then the user performs a pinch gesture on the image
    Then the image should zoom out


