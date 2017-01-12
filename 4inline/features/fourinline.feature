Feature: A Game of 4 en linea

Scenario: Game starts
  Given Game started
  Then the board should be set and empty
  Then the board should be set and empty

Scenario: Player_1 start
  Given Game started
  Then it should be Player_yellow's turn

Scenario: Player makes a move
  Given Game started
  When player makes a move on column 4
  Then there should be a yellow element in column 4
