# ddunkleyCS333FInal
made by davis dunkley

Project functionality: 
  this is a project that will play a poker game.
  it will ask the user how many hands to play and it will return the best hand
   
  to run the code you will input into the terminal 
  
  pyhton3 driver.py

to run game: you will enter into the terminal: 
**pyhton3 driver.py**
then enter a number between 2 and 6.
the game will then tell you who won from the 4 to 6 players.
   
testing:
  there is 17 unit tests and 5 intergration tests.
  inter_test.py holds the intergration tests 
  test.py holds the unit test and intergration tests too.
  
  to check for coverage 
  run: 
  **python -m coverage run -m test  **
  
  then enter a number for the input

  **python -m coverage report  **
 
 the report states: 
 Name        Stmts   Miss  Cover
-------------------------------
driver.py     252     20    92%
test.py        77      0   100%
-------------------------------
TOTAL         329     20    94%

  
technology:
  python, coverage, vs code 
  
driver.py 
  plays the poker game 
  
docker file holds the image the will be uploaded to docker. 
