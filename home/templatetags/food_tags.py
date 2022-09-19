from django import template
from math import floor

register = template.Library()

@register.simple_tag
def curren(food):
    after_discount=food.price - (food.price*food.discount / 100)
    after_discount=floor(after_discount)
    return after_discount




@register.simple_tag
def multiply(a , b):
    return a*b


@register.filter
def cal_total_payable_amount(cart):
    total =0
    for c in cart:
        discount = c.get('food').discount
        price = c.get('food').price
        sale_price = discount_cart(price , discount)
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product

    return total 


@register.filter
def cal_total_payable_amount_st(cart_st):
    total =0
    for c in cart_st:
        discount = c.get('stationary').discount
        price = c.get('stationary').price
        sale_price = discount_cart(price , discount)
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product

    return total 






@register.simple_tag
def discount_cart(price , discount):
    after_discount=price - (price*discount / 100)
    after_discount=floor(after_discount)
    return after_discount