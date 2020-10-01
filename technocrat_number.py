number = int(input())
n = number*number
n_len = len(str(n))
s: int
reversed_digits = []
digits = []

if number > 1 and number < 300:
    while n > 0:
        s = n%10
        n = int(n/10)
        reversed_digits.append(s)

    for i in range(len(reversed_digits)-1, -1,-1):
        digits.append(reversed_digits[i])

    half_digits_len = int(len(digits)/2)

    if n_len%2==0:
        x = digits[:half_digits_len]
        y = digits[half_digits_len:]

        p = ""
        q = ""

        for i in range(0, len(x)):
            p += str(x[i])

        for i in range(0, len(y)):
            q += str(y[i])

        if int(p) + int(q) == number:
            print("IT IS A TECHNOCRAT NUMBER")
        else:
            print("IT IS NOT A TECHNOCRAT NUMBER")

    else:
        half_digits_len += 1
        x = digits[:half_digits_len]
        y = digits[half_digits_len:]

        p = ""
        q = ""

        for i in range(0, len(x)):
            p += str(x[i])

        for i in range(0, len(y)):
            q += str(y[i])
        
        x = digits[:half_digits_len-1]
        y = digits[half_digits_len-1:]

        a = ""
        b = ""
        for i in range(0, len(x)):
            a += str(x[i])

        for i in range(0, len(y)):
            b += str(y[i])
        
        if (int(p) + int(q)) == number or (int(a) + int(b)) == number:
            print("IT IS A TECHNOCRAT NUMBER")
        else:
            print("IT IS NOT A TECHNOCRAT NUMBER")