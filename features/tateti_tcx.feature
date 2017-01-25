Feature: Tateti TXC

Scenario: Welcome screen
  Given Tateti app home
  Then Welcome screen message will display

Scenario: Welcome screen start game 
  Given Tateti app home
  When User start game
  Then game is started

Scenario: First game movement 
  Given Tateti app home
  And User start game
  When User click button 0 0
  Then button 0 0 change state
