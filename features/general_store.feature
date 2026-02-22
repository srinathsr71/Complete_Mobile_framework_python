Feature: verify the shopping general store

@tc01case @store
Scenario Outline: Successful shopping general store
  Given user is on General Store home
  When user selects country "<country>"
  And user enters name "<name>"
  And user selects gender "<gender>"
  Then user proceeds to shop
Examples:
| country | name   | gender |
| Angola  | Raksha | female |


@tc02case @store
Scenario Outline: Successful shopping general store adding products
  Given user is on General Store home
  When user selects different country "<country>"
  And user enters name "<name>"
  And user selects gender "<gender>"
  Then user proceeds to shop
  And user added product to the cart
  And user click on add to cart
  Then user verify the cart total amount
  And user click on proceed button
  Then user navigating to web view
  And user verifies the title of the page
  Then user return to native app
Examples:
| country | name   | gender |
| India  | demo | female |
