from textwrap import dedent

menu_items = {
    'Wings' : 0,
    'Cookies' : 0,
    'Spring Rolls' : 0,
    'Salmon' : 0,
    'Steak' : 0,
    'Meat Tornado' : 0,
    'A Literal Garden' : 0,
    'Ice Cream' : 0,
    'Cake' : 0,
    'Pie' : 0,
    'Coffee' : 0,
    'Tea' : 0,
    'Unicorn Tears' : 0,
}

def welcome_screen():
    message = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    print(dedent(message))


def menu_listing():
    cafe_menu = """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
    print(dedent(cafe_menu))


def order_prompt():
    prompt = """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
    print(dedent(prompt))

    while True:
        order = input()
        if order == "quit":
            break

        if order in menu_items:
            menu_items[order] += 1
            amount = menu_items[order]
            if amount == 1:
                print(f"\n** {amount} order of {order} have been added to your meal **\n")
            elif amount > 1:
                print(f"\n** {amount} orders of {order} have been added to your meal **\n")


def main():
    welcome_screen()
    menu_listing()
    order_prompt()


if __name__ == "__main__":
    main()
