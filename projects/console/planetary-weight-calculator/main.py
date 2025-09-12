def planetary_weight_calculator():
  print("Welcome to Planetary Weight Calculator!")
  weight_on_earth = int(input("\nEnter the weight on earth: "))
  planet_name = input("Enter the name of the planet you want to calculate your weight on: ").title()

  planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
  gravity_percentages = [37.6, 88.9, 37.8, 236.0, 108.1, 81.5, 114.0]

  if planet_name in planets:
    weight_on_other_planet = (weight_on_earth / 100) * gravity_percentages[planets.index(planet_name)]
    rounded_weight = round(weight_on_other_planet, 2)

    print(f"\nYour weight on Earth is: {weight_on_earth} kg \nYour weight on {planet_name} is: {rounded_weight} kg")

  else:
    print(f'\n"{planet_name}" is not recognized as a planet in our solar system.')

if __name__ == "__main__":
  planetary_weight_calculator()