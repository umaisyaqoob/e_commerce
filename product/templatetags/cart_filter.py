from django import template

register  = template.Library()

@register.filter("is_in_cart")
def is_in_cart(product, cart):
   keys =  cart.keys()
   for id in keys:
      if int(id) == product.id:
            return True
   return False
      

@register.filter("cart_count")
def cart_count(product, cart):
   keys =  cart.keys()
   for id in keys:
      if int(id) == product.id:
            return cart.get(id)
   return 0

@register.filter("price_total")
def price_total(product, cart):
  return product.price * cart_count(product, cart)


@register.filter("total_cart_price")
def total_cart_price(products, cart):
  sum = 0
  for p in products:
      sum += price_total(p, cart)

  return sum


@register.filter("currency")
def currency(number):
 return "Rs."+ str(number)

@register.filter("multiply")
def multiply(number, number1):
 return number * number1