def main():
    pounds = pounds_to_float(input("How much was the meal in £? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    # TODO
    pounds_int = d.strip("£")       #stripping the £ sign from the input
    return float(pounds_int)        #coverting the stripped input into a float to account for decimals


def percent_to_float(p):
    # TODO
    percent_int = p.strip("%")          #stripping the % sign from the input
    return float(percent_int) / 100     #converting the stripped input into a float and dividing by 100 to get the decimal percentage


main()
