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

Also by placing the packets at different positions on the “disc” we can prevent burst errors.


<h2>Reed Solomons</h2>
Time complexity is O(n log n) for encoding and decoding, and space complexity is O(n)
Maximum error correction capability is typically (n-k)/2, where n is the block size and k is the number of data symbols.
Introduces a higher redundancy overhead, with the number of additional parity symbols typically equal to the desired error correction capability.
Performs well with burst errors and random errors, widely used in applications such as data storage, satellite communication, and digital broadcasting.

<h2>Hamming  Code</h2>
Time complexity is O(n) for encoding and decoding, and space complexity is O(n) 
Designed for single-bit error correction. Can detect but not correct multiple errors.
Adds a smaller redundancy overhead, requiring only a few parity bits.
More suitable for applications with a higher likelihood of single-bit errors, such as computer memory systems and communication channels with relatively low error rates.

<h2>Cyclic Redundancy Check (CRC)</h2>

CRC methodology: Divide code to be sent by another number that will be known by the receiver side and append the remainder to the code.
If the received message gives zero remainder when divided by the above referenced number it has no errors/

CRC has low computational complexity with a time complexity of O(n) for encoding and decoding. The space complexity is minimal as it requires a small amount of additional storage for the CRC bits.
CRC is not an error correction algorithm but a method for error detection.
CRC has a minimal redundancy overhead as it appends a fixed-size checksum (CRC bits) to the data.

<h2>Turbo Codes</h2>
Turbo codes have higher computational complexity than Reed-Solomon and Hamming codes, with time complexity depending on the specific implementation. Space complexity can be higher than O(n).
Turbo codes can handle a higher number of errors compared to Reed-Solomon and Hamming codes, achieving near-Shannon limit performance.
Excel in scenarios with higher error rates and various error patterns. Commonly used in wireless communication systems and data transmission over noisy channels.

<h4>Final use cases</h4>

Reed-Solomon codes are commonly used in storage systems such as hard drives, solid-state drives (SSDs), and optical media and digital broadcasting.

Hamming codes are widely used in computer memory systems, such as RAM (random access memory) and ECC (error-correcting code) modules and low-error-rate communication channels, such as LANs.

Turbo codes have been employed in deep space missions by space agencies like NASA and ESA and  in wireless communication systems, including cellular networks (3G, 4G, and 5G).

CRC is often used for file integrity checks.

