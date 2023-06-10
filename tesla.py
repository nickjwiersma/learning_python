def check_driver_age(age=0):
    if int(age) < 18:
        print('You are too young to drive this car.')
    elif int(age) > 18:
        print('Powering on. Enjoy the ride!')
    elif int(age) == 18:
        print('Congratulations on your first year of driving. Enjoy the ride!')

print(check_driver_age(input("What is your age? ")))