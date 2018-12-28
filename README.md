berikut penjeasan dari sola upscale go-jek,
inti dari soal ini adalah : "mencari sebuat kata baik secara vertical,horisontal,diagonal dalam suatu balok(matrix)"

Skills Test

Basic Programming Aptitude

4 / Questions answered

There is a well-known puzzle called Word Search that involves looking for words in a grid of letters.The words are given in a list and can appear in the grid horizontally, vertically, or diagonally in any direction.In this task, you should implement a solver for word search.You will be given grids and a word to search for, and you have to find how many times that word comes out in the grid.Words that are spelled the same backwards and forwards, also known as palindromes, will not be given, so you don’t need to worry about words that match in the exact same spot in two different directions.

Input:

The first line is the number of test cases T. Each test case will have two numbers N and M, each on their own line given in that order.Following that is N lines of M lowercase letters each representing the grid of letters.Lastly, a word W is given that you must look for.

Output:

For each test case, output one line of the form “Case C: X” (without the quotes), where C is the case number (starting from 1), and X is how many times the word W appeared in the grid.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ M ≤ 100
1 ≤ length(W) ≤ 100

Sample Input:

3
3
4
catt
aata
tatc
cat
5
5
gogog
ooooo
godog
ooooo
gogog
dog
2
8
bananana
kalibrrr
nana

Output :
Case 1: 4
Case 2: 8
Case 3: 4