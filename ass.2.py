g_earth=9.81
g_moon=1.62

mass=float(input("Enter the mass of object: "))
weight_onEarth=mass*g_earth
weight_onMoon=mass*g_moon

print("weight in earth is: ",weight_onEarth,"kg")
print("weight on moon is: ",weight_onMoon,"kg")
