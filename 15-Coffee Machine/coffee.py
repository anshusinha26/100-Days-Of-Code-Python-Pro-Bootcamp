"""stores ascii art"""
logo = """
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--,
   |            (__  ;
   |             | )  )
   |             |/  /
   |             /  / 
   |            (  /
   \             y'
    `-.._____..-'
"""
"""stores the menu data"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk":  100
        },
        "cost": 3.0
    }
}
"""initial profit is set to 0"""
profit = 0
"""stores the initial resources"""
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}