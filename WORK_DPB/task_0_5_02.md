## Use Python to find the remainder of 2304811 divided by 47 without using the modulo operator `%`

    In [1]: a = 2304811

    In [2]: b = 47

    In [3]: round((a / b - a // b) * b)
    Out[3]: 25

Is there a simpler way than this?

[end]
