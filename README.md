# tri_bicolor_tiling

This is a solution to solve both the codewars tri bicolor tiling and the insane tri bicolor tiling:

------------------------------------------------------------------------------------------------------------------------------------------------------------------
You have a row of n square tiles, which are colored black and the side length is 1. You also have infinite supplies of three kinds of rectangular tiles:

    Red tiles of Length r
    Green tiles of Length g
    Blue tiles of Length b

All tiles have integer lengths and share the same height of 1.

Now, you want to replace some black square tiles with your colored tiles. However, you are quite picky, and you want to use exactly two types of colored tiles (RGB). You can leave black gaps as much as you want.

In how many ways can you replace black tiles with your colored tiles? Since your answer will be very large, please give your answer modulo 12345787.
Example

For n = 6 and (r, g, b) = (2, 3, 4), these are the eight possible arrangements using exactly two colors (R, G, B denote red, green, blue tiles respectively, and a dot is a black tile):
------------------------------------------------------------------------------------------------------------------------------------------------------------------


This is solvable by setting up an adjacency matrix a, with the tile length leading to the same tile length-1 ; 5->4, 4-> 3, 3->2, 2->1, and also 1->0 or another 1 block, which is 1->1, as well as the given lengths for the colours, and the n square tiles is equivalent to a path of length n, which can be represented by the matrix a^n, which always ends with a 1 block, so we take only the first row (the "1" row) by multiplying a^n by a 1X5 matrix in which the first element is 1 and the rest are zeroes, and taking the modulus of this as per the requirements of the question. This is done by creating an identity matrix res, and solving the the problem in a while loop while n>0; if n is even, then do a dot product of res with the matrix a and take the modulus. Equally, in the while loop, take the floor division of n by 2, and multiply a by itself and take the modulus. Repeat until the loop breaks at n=0. Finally, we multiply the matrix res by the 1x5 matrix aforementioned.

Given that the problem requires two colours, we must solve the function for any two combination of colours [a,b] for a,b in [r,g,b]. However, the function f(n,[a,b]) also contains tilings only containg a or b, so we must discard them by subtraction (via the principle of Inclusion-Exclusion) f(n, [a,b]) - f(n,[a]) - f(n,[b]) + 1. The + 1 term is for the union term |aUb|=1. Summate all combinations of these colours and take the modulus and you've solved the problem efficiently without resulting in timeout.
