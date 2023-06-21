<h1>Part-1</h1>

<h1>Part-2</h1>

<h3>My implementation of Reed-Solomons</h3>

-I first converted the binary data to hexadecimal (base-16) data. I.e. one packet of data.(Can be converted into base-n data and the algorithm will work.

-Then clubbed four (arbitrary number) packets of data together (let them be a,b,c,d) and applied lagrange interpolation to get a function f(x) such that f(0)=a f(1)=b f(2)=c and f(3)=d

-Then find e and f such that f(4)=e and f(5)=f.

-Next update e and f such that they are less than 16 (n in general case) by applying mod 16 (n in general case).

-Pass a b c d e and f as the encoded package.

-Now if any packets go missing, they can be recovered, if number of packets lost is less or equal to 2 for that particular packet by applying lagrange interpolation on the remaining packets.

-Also apply mod 16 (n in general case) to get the final values.

-The Mod is applied to keep the values of e and f bounded.

-This algorithm works well when we know if any data has been lost and the data cannot get jumbled.

-For example a CD where data in one position cannot be moved to another position (could happen in other cases if data is lost in between and the “reciever” reads it instead of the lost data). [Not sure if this happens in practice, just an intuition based on the algorithm].

-Another possible problem would be when e and f are decimals where only the integer would get passed.
