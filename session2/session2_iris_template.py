"""Session 2: practice variables, basic arithmetic, comparisons, type conversions, and adding a second flower.
Note: Variable names must match exactly because later sessions import these names.
"""

# Task 1: Print Flower Summary
id = "flower1"  # Task 2: Change this to "flower_2x"
print("\n=== Flower Summary ===")
print("ID:", id)

# Task 2: Change this to "flower_2x"
id = "flower_2x"
print("\n=== Flower Summary ===")
print("ID:", id)

# Task 3: Define more variables for one Iris flower
id = "flower1"
sepal_length = 5.1
sepal_width = 3.5  # Uncomment me by click ctrl + / (Windows)
petal_length = 1.4  # Add appropriate value for petal_length
petal_width = 0.2
species = "setosa"

# Task 3a: Uncomment the print statements below to see the values of the variables you defined.
print("\n=== Flower Summary ===")
print("ID:", id)
print("Sepal Length:", sepal_length)
print("Sepal Width:", sepal_width)
print("Petal Length:", petal_length)
print("Petal Width:", petal_width)
print("Species:", species)

# Task 4: Compute petal area
petal_area = petal_length * petal_width
print("\nPetal Area:", petal_area)  #Uncomment the area

threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

# Task 5: Comparing with threshold
is_short_petal = petal_length < threshold
print("\n=== Comparison ===")
print("is_short_petal (petal_length < threshold):", is_short_petal)
print("\n=== Conversion ===")
print("petal_length_text:", str(petal_length), "| type: <class 'str>")
print("threshold_text:", str(threshold), "| type: <class 'str'>")
print("threshold_number:", float(threshold), "| type: <class 'float'>")

# Task 6: Comparing with species

sepal_length_2 = 4.9
sepal_width_2 = 3.0
petal_length_2 = 1.4
petal_width_2 = 0.2
species_2 = "setosa"
petal_area_2 = petal_length_2 * petal_width_2

print("\n=== Flower 2 ===")
print("Petal Area 2:", petal_area_2)


