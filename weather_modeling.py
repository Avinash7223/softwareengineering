# Define the quadratic equation for temperature modeling
def temperature_modeling(a, b, c, time):
  # Calculate temperature based on time using the quadratic equation
  temperature = a * time**2 + b * time + c
  return temperature


# Step 1: Hard-coded Variables for Weather Modeling
print("Step 1: Hard-coded Variables for Weather Modeling")
a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10
time_hardcoded = 5  # Example time value
result_hardcoded = temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded,
                                        time_hardcoded)
print(
    f"Temperature for hardcoded coefficients at time {time_hardcoded} hours: {result_hardcoded}"
)
print("\n")

# Step 2: Keyboard Input for Weather Modeling
print("Step 2: Keyboard Input for Weather Modeling")
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))
time_keyboard = float(input("Enter time in hours: "))
result_keyboard = temperature_modeling(a_keyboard, b_keyboard, c_keyboard,
                                       time_keyboard)
print(
    f"Temperature for keyboard input coefficients at time {time_keyboard} hours: {result_keyboard}"
)
print("\n")

# Step 3: Read from a File for Weather Modeling
print("Step 3: Read from a File for Weather Modeling")

with open('weather.txt', 'r') as file:
  lines = file.readlines()
  a_file, b_file, c_file, time_file = map(float, lines[0].split())

result_file = temperature_modeling(a_file, b_file, c_file, time_file)
print(
    f"Temperature for file input coefficients at time {time_file} hours: {result_file}"
)
print("\n")
