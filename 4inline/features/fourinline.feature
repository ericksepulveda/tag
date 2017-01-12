Feature: A Game of 4 en linea

Scenario: Game starts
  Given Game started
  Then the board should be set and empty

Scenario: Player_1 start
  Given Game started
  Then it should be Player_yellow's turn
