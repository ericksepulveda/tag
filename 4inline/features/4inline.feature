Feature: A Game of 4 en linea

Scenario: Game starts
  Given Game started
  Then hint should be ????

Scenario: Player makes a guess
  Given Game started
  When Player sends a 2345
  Then hint should be ???-
