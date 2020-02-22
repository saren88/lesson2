def get_summ(num_one, num_two):
    try:
        final_summ = int(num_one) + int(num_two)
        return final_summ

    except ValueError:
        print('Please enter a number!')


if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
