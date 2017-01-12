Feature: A Game of 4 en linea

Scenario: Game starts
  Given Game started
  Then the board should be set and empty

Scenario: Yellow Player start
  Given Game started
  Then it should be Yellow Player's turn

Scenario: Player makes a move
  Given Game started
  When Yellow Player makes a move on column 4
  Then there should be a yellow element in column 4

Scenario: Yellow Player wins
  Given Game started
  When Yellow Player meets horizontal winning conditions
  Then Yellow Player is the winner