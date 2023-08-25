# List Operations

Instructions: You are given a 2D matrix, which represents the number of people in a room, grouped by their eye color and gender.
The first row represents the male gender, while the second row represents females.
The columns are the eye colors, in the following order: brown, blue, green, black:

data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

The data shows that, for example, there are 20 green eyed females in the room (2nd row, 3rd column).

Our program needs to take eye color as input and output the percentage of people with that eye color in the room.

Sample Input:
blue

Sample Output:
36

Explanation: There are 11+32=43 people with blue eyes, which is 36% of the total.


Pseudocode:





            BEGIN
              DECLARE data = [
                              [23, 11, 5, 14],
                              [8, 32, 20, 5]
                            ]
              DECLARE color_data = ['brown', 'blue', 'green', 'black']
              DECLARE total equals to zero for now
              DECLARE totalpercentage equals to zero for now
              DECLARE total_color equals to zero for now
              DECLRARE index_color equals to negative one (-1)


              INPUT choose_your_color "Choose your color (brown/blue/green/black): "

              IF choose_your_color not in color_data:
                PRINT "Invalid eye color choice."
              ELSE:
                IF choose_your_color is equals to brown
                  index_color plus 1
                IF choose_your_color is equals to blue
                  index_color plus 2
                IF choose_your_color is equals to green
                  index_color plus 3
                IF choose_your_color is equals to black
                  index_color plus 4
                ENDIF

                FOR i each ROW in data

                  FOR each COLUMN in i
                    total plus each of the i is currently holding
                  ENDFOR

                  FOR each COLUMN 
                    total_color plus COLUMN[index_color] # for example 3 - it gets the 14 and 5 equals to 19
                  ENDFOR

                ENDFOR

                totalpercentage equals to (total_color divided by total) times 100

                PRINT make_it_an_integer(totalpercentage)
              ENDIF



            END