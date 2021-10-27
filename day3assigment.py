'''You all are pilots, you have to land a plane,
the altitude required for landing a plane is 1000ft,
if it is less than that tell pilot to land the plane,
or it is more than that but less than 5000 ft
ask the pilot to “come down to 1000 ft”,
else if it is more than 5000ft ask the pilot to“go around and try later”'''
altitude=int(input("ft:"))
if(altitude<=1000):
  print("Land the plane")
elif(altitude>1000 and altitude<5000):
  print("Come down to 1000ft")
elif(altitude>5000):
  print("Go around and try later")
