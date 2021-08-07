1. XXXX ^ 0000 = XXXX
2. XXXX ^ 1111 = ~XXXX
3. XXXX ^ XXXX = 0000
4. XXXX & 0000 = 0000
5. XXXX & 1111 = XXXX
6. XXXX & XXXX = XXXX
7. XXXX | 0000 = XXXX
8. XXXX | 1111 = 1111
9. XXXX | XXXX = XXXX
10. logical right shift(>>>) vs arithmetic right shift(>>)

11. getBit (index : 3)
    9 -> 1001 -> 1000 (1001 & 1000) -> check wether 0 or not

12. setBit (index : 3)
    5 -> 0101 -> 1101 (0101 | 1000)

13. clearBit (index : 3)
    9 -> 1001 -> 0001 (1001 & 0111) : 0111 = ~(1000)

14. clearLeftBits (index : 3)
    169 -> 1010 1001 -> 0000 0001 (1010 1001 & 0111)

15. clearRightBits (index : 3)
    169 -> 1010 1001 -> 1111 0000 (1010 1001 & 1111 0000)

16. updateBit (index : 3, boolean : False)
    169 -> 1010 1001 -> 1010 0001 ((1010 1001 & 1111 0111) | 0000)
