db_username = '0headshot1'
db_password = '0headshot1'


# function for authorization
def auth(tries:int):
    count = 0
    while count < tries:
        username = input('Please input your username: ')
        password = input('Please input your password: ')
        if db_username == username and db_password == password:
            if 8 < len(username) < 40 and 8 < len(password) < 16 and not username.isalpha() and not username.isdigit():
                print(f'Welcome, {username}!')
                break
            else:
                print('Incorrect data:\n'
                      '1)Incorrect lenght for username or password!\n'
                      '2)Username and password should include letters and digits\n')
        else:
            print('Incorrect username or password!')
        count += 1

auth(3)


# this is dictionary for our catalogue of food
catalogue = {'hot-dog': 50, 'hamburger': 120, 'shaurma': 150, 'naggets': 130, 'pizza': 930,
                 'boso-lagman': 250, 'plov': 190, 'giro-lagman': 240, 'mantes': 160, 'rolls': 600,
                 'garnir': 100, 'grechka': 70, 'pelmeni': 130, 'french meat': 400, 'fish': 500,
                 't-bone': 870, 'Beijing duck': 5000, 'shashlyk assorti': 50000
                 }


# function for checking the amount of money of client and calculating the result
def give_me_my_money(money:int, price:int):
    if money < price:
        return 'no money'
    else:
        result = money - price
        return result


# fucntion for inputing food that client want to buy
def what_client_want():
    total_food = int(input('Please input how much food you want to buy: '))
    lst_catal = []
    for i in range(total_food):
        i_want = input('Please input what you want to buy: ')
        if i_want in catalogue:
            lst_catal.append(i_want)
    return lst_catal



# function for ordering the food and giving money back
def order():
    money = int(input('Please input how much money you have: '))
    list1 = what_client_want()
    for food in list1:
        price = catalogue[food]
        money = give_me_my_money(money, price)
        print(money)
order()

