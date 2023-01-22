"""My Doc String"""


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favoriute color is {color}")


fav_colors(craig='purple', elma='read', gabriel="blue", angelica='teal')
