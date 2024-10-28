#  File: Spiral.py

#  Description: A spiral is created based on an odd number read in from the file. This spiral is tested by checking if the adjacent numbers added equals to the given outputs.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 08/29/2022

#  Date Last Modified: 08/29/2022



#  Imports sys package to read in file
import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    #  converts str to int
    n = int(n)

    #  if n is an even number, it will increment n by 1
    if (n % 2 != 1):
        n += 1

    #  creates an empty array for spiral
    spiral = []

    #  makes 2D array with 0s
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(0)
        spiral.append(new_row)
        
    #  the highest number is determined
    num = pow(n, 2)

    #  indexes for the corners of the spiral are determined
    row_index_top = 0
    row_index_bottom = n - 1
    col_index_right = n - 1
    col_index_left = 0

    #  this tells us how many numbers will be added to each row and column
    num_of_horizontal_values = n
    num_of_vertical_values = n - 2

    #  the middle of the spiral is determined and 1 is assigned to that position
    spiral[n // 2][n // 2] = 1

    #  this loop will keep running until num == 1
    while (num > 1):

        #  the last number of the row is determined. Function is called to fill in the array horizontally to the left
        ending_number = num - num_of_horizontal_values
        spiral = left_horizontal(spiral, num, ending_number, row_index_top, col_index_right)

        #  index, starting number, and ending number are adjusted based on previous run. Function is called to fill the array vertically from top to bottom
        row_index_top += 1
        num = ending_number
        ending_number = num - num_of_vertical_values
        spiral = down_vertical(spiral, num, ending_number, row_index_top, col_index_left)

        #  starting number and ending number are adjusted based on previous run. Function is called to fill the array horizontally from left to right
        num = ending_number
        ending_number = num - num_of_horizontal_values
        spiral = right_horizontal(spiral, num, ending_number, row_index_bottom, col_index_left)

        #  #  index, starting number, and ending number are adjusted based on previous run. Function is called to fill the array vertically from bottom to top
        num = ending_number
        ending_number = num - num_of_vertical_values
        row_index_bottom -= 1
        spiral = up_vertical(spiral, num, ending_number, row_index_bottom, col_index_right)

        #  index, starting number, and ending number are adjusted based on previous run. The number of horizontal and vertical values are adjusted for the next set of functions
        col_index_right -= 1
        col_index_left += 1
        num = ending_number
        num_of_horizontal_values -= 2
        num_of_vertical_values -= 2
        
    return spiral

#  this function fills in the array from right to left
def left_horizontal(spiral, starting_number, ending_number, row, starting_index_col):
    num = starting_number
    c = starting_index_col
    range_nums = starting_number - ending_number
    for i in range(range_nums):
        if (num == ending_number):
            spiral[row][c] = num
            break
        else:
            spiral[row][c] = num
            num -= 1
            c -= 1
    return spiral

#  this function fills in teh array from top to bottom
def down_vertical(spiral, starting_number, ending_number, starting_index_row, col):
    num = starting_number
    r = starting_index_row
    range_nums = starting_number - ending_number
    for i in range(range_nums):
        if (num == ending_number):
            spiral[r][col] = num
            break
            
        else:
            spiral[r][col] = num
            num -= 1
            r += 1
    return spiral

#  this function fills in the array from left to right
def right_horizontal(spiral, starting_number, ending_number, row, starting_index_col):
    num = starting_number
    c = starting_index_col
    range_nums = starting_number - ending_number
    for i in range(range_nums):
        if (num == ending_number):
            spiral[row][c] = num
            break
        else:
            spiral[row][c] = num
            num -= 1
            c += 1
    return spiral

#  this function fills in the array from bottom to top
def up_vertical(spiral, starting_number, ending_number, starting_index_row, col):
    num = starting_number
    r = starting_index_row
    range_nums = starting_number - ending_number
    for i in range(range_nums):
        if (num == ending_number):
            spiral[r][col] = num
            break
            
        else:
            spiral[r][col] = num
            num -= 1
            r -= 1
    return spiral

    

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    #  converts str to int
    n = int(n)
    sum_adj = 0
    index_r = -1
    index_c = -1

    #  the index of the value is determined
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if (spiral[i][j] == n):
                index_r = i
                index_c = j
                break
        if (index_r != -1):
            break
    #  if the value does not exist, the program will return 0
    if (index_r == -1):
        return 0
    #  if else statements are written to determine the sum based on the position of the value

    #  bottom left corner
    if (index_r == len(spiral) - 1 and index_c == 0):
        sum_adj = spiral[index_r-1][index_c] + spiral[index_r-1][index_c+1] + spiral[index_r][index_c+1]

    #  bottom right corner
    elif (index_r == len(spiral) - 1 and index_c == len(spiral) - 1):
        sum_adj = spiral[index_r-1][index_c] + spiral[index_r-1][index_c-1] + spiral[index_r][index_c-1]

    #  top left corner
    elif (index_r == 0 and index_c == 0):
        sum_adj = spiral[index_r][index_c+1] + spiral[index_r+1][index_c+1] + spiral[index_r+1][index_c]

    #  top right corner
    elif (index_r == 0 and index_c == len(spiral) - 1):
        sum_adj = spiral[index_r][index_c-1] + spiral[index_r+1][index_c-1] + spiral[index_r+1][index_c]

    #  top row
    elif (index_r == 0):
        sum_adj = spiral[index_r][index_c+1] + spiral[index_r+1][index_c+1] + spiral[index_r+1][index_c] + spiral[index_r+1][index_c-1] + spiral[index_r][index_c-1]

    #  left most column
    elif (index_c == 0):
        sum_adj = spiral[index_r-1][index_c] + spiral[index_r-1][index_c+1] + spiral[index_r][index_c+1] + spiral[index_r+1][index_c+1] + spiral[index_r+1][index_c]

    #  bottom row
    elif (index_r == len(spiral) - 1):
        sum_adj = spiral[index_r][index_c-1] + spiral[index_r-1][index_c-1] + spiral[index_r-1][index_c] + spiral[index_r-1][index_c+1] + spiral[index_r][index_c+1]

    #  right most column
    elif (index_c == len(spiral) - 1):
        sum_adj = spiral[index_r+1][index_c] + spiral[index_r-1][index_c] + spiral[index_r+1][index_c-1] + spiral[index_r-1][index_c-1] + spiral[index_r][index_c-1]

    #  all numbers in the middle
    else:
        sum_adj = spiral[index_r][index_c+1] + spiral[index_r][index_c-1] + spiral[index_r+1][index_c+1] + spiral[index_r-1][index_c+1] + spiral[index_r+1][index_c-1] + spiral[index_r-1][index_c-1] + spiral[index_r+1][index_c] + spiral[index_r-1][index_c]

    return sum_adj
    
#  file is read in
def main():
    input_file = sys.stdin
    spiral = create_spiral(input_file.readline().strip())
    line = True

    #  Loops until we get to the end of the file
    while line:
        input_file_line = input_file.readline().strip()
        if input_file_line == '':
            break
        else:
            print(sum_adjacent_numbers(spiral, input_file_line))

if __name__ == "__main__":
  main()
