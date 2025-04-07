from pick import pick

user_input = int(input("Enter the value: "))

lengths = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Micrometer": 0.000001,
    "Nanometer": 0.000000001,
    "Inch": 0.0254,
    "Foot": 0.3048,
    "Yard": 0.9144,
    "Mile": 1609.34,
}

title = "Select the unit you want to convert from: "
options = [
    "Meter",
    "Kilometer",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Inch",
    "Foot",
    "Yard",
    "Mile",
]
option1, index = pick(options, title, indicator="=>", default_index=0)

title = "Select the unit you want to convert to: "
options = [
    "Meter",
    "Kilometer",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Inch",
    "Foot",
    "Yard",
    "Mile",
]
option2, index = pick(options, title, indicator="=>", default_index=0)

from_unit = lengths[option1]
to_unit = lengths[option2]
base_amount = user_input * from_unit
final_answer = int(base_amount / to_unit)

print(f"Your unit conversion of {user_input} from {option1} to {option2} is {final_answer}")