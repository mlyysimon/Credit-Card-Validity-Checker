def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits: # sum of odd digits that are not multiplied by 2
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits: # sum of even digits that are multiplied by 2
        number = int(digit) * 2
        # if product is greater than or equal to 10, add the digits together
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    # sum of all digits
    total = sum_of_odd_digits + sum_of_even_digits
    # determine if the total can be evenly divided by 10 for validity
    return total % 10 == 0

def main():
    card_number = input('Enter a card number: ')
    card_translation = str.maketrans({'-': '', ' ': ''}) # remove hyphens and spaces
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('This card number is VALID!')
    else:
        print('This card number is INVALID!')

main()