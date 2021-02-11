weight = 41.5
premium_ground_shipping = 120
#Ground Shipping

if weight <= 2:
  print(1.50 * weight + 20)
elif weight <= 6:
    print(3 * weight + 20)
elif weight <= 10: 
      print(4 * weight + 20)
else:
    print(14.25 * weight + 20)

print(premium_ground_shipping)

# Drone Shipping
if weight <= 4.5:
  print(weight * 4.5)
elif weight <= 6:
  print(weight * 9)
elif weight <= 10:
  print(weight * 12)
else:
  print(weight * 14.25)
