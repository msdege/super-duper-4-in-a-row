# super-duper-4-in-a-row
Interactive single-player board game against the computer where you try to link 4 bubbles together for points in an increasingly smaller zone.

Instructions: Run the program to see a window with an empty grid and a reset button. Click anywhere in the grid to place a bubble. When you place a bubble, the computer will place a gray square to block a part of the grid (you will no longer be able to place a bubble where the computer blocked). Keep playing until you can no longer create links of 4 or more. Then, hit the reset button to empty the grid and restart.

How to get points: Try to link 4 or more bubbles in a row horizontally, veritcally, or diagonally to score points. When you link 4 or more, the bubbles will "pop", and you will receive a point for each bubble that pops (except when a multiplier is used).

Score multiplier: A multiplier is created if you link and pop 2 or more lines with a single bubble. The multiplier is determined by an exponential function based on the number of lines you pop at once. For example, if you pop two lines, then the multiplier will be 2^2 or 4. If you pop three lines, the multiplier will be 2^3 or 8 and so on. The multiplier is multiplied by the total bubbles popped to get your score. For example, if you pop two lines of 4 at the same time (7 total bubbles), then you will receive 28 points added to your total score.
