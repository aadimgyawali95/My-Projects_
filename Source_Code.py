'''
Made By: Aadim Gyawali
Publish : 1/16/2023
Date
'''


def main():
    # Make two pairs from the back. E.g 1234=["12","34"]
    def make_pairs(string):
        result = []

        if len(string) % 2 != 0:
            result.append(string[0])
            string = string[1:]

        for i in range(0, len(string), 2):
            result.append(string[i:i + 2])

        return result

  # Solve any value error
    try:
        inp = int(input("Enter a number: "))

    except:
        print("Enter A valid number !")
        main()


    list_of_numbers = make_pairs(str(inp))
    first = list_of_numbers.pop(0)

  # (side_num+x)*x now find the largest number closer to value
    def div(value, side_num):
        z = 0

        while (side_num + z) * z <= value:
            z = z + 1
        z = z - 1

        return side_num + z, z

  # find the closest square number. it is very similar to math.isqrt()
    def closest_qrt(n):
        x = n
        y = (x + n // x) // 2

        while y < x:
            x = y
            y = (x + n // x) // 2

        return x

  # Find the closest number that can multiply the first pair of the number
    def max_square_subtraction(num):
        num = int(num)
        square_number = closest_qrt(num)
        side_num = (square_number + square_number) * 10
        sub_value = num - square_number**2
        return side_num, sub_value, square_number

    side_num, sub_value, final = max_square_subtraction(first)

  #do this until the there is no pair left
    while len(list_of_numbers) != 0:

        first = list_of_numbers.pop(0)
        value = int((str(sub_value) + str(first)))
        side_num, final1 = div(value, side_num)
        final = (str(final) + str(final1))
        sub_value = value - side_num * final1
        side_num = (side_num + final1) * 10

    a = False
    i = 0
    if sub_value!=0:
        try:
            deci=int(input("Enter a No of Decimals: "))

        except:
            print("Enter a valid number !")
            main()

        if deci > 100:
            print("Enter number less than 100!")
            main()

        while i != deci:  #To give decimals as the user expected
        # Now if sub_value isn't 0 and len of list is 0 then it finds the decimals
            if sub_value != 0:
                value = int(str(sub_value) + str("00"))
                side_num, final1 = div(value, side_num)

            if not a:
                final = (str(final) + "." + str(final1))
                a = True

            else:
                final = (str(final) + str(final1))
            sub_value = value - side_num * final1
            side_num = (side_num + final1) * 10
            i = i + 1

    print(f"The square root of {inp} is {final}")
    main()

main()

