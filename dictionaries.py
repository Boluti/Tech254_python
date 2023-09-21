# What is a dictionary?

# uses key/value pairs
# key = the reference to the object
# value = the data storage mechanism u want to use (variable, list, dictionary etc)

# making a dictionary

student_1 = {
 "name": "Bolutife",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "operators"]
}
print(student_1)
#accessing data using the key(s)
print(student_1[ "stream"])
print(student_1["completed_lesson_names"][0])
# changing a value in a dictionary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
student_1["completed_lesson_names"]. remove("data_types")
print(student_1["completed_lesson_names"])

#getting the keys
print(student_1.keys())

# sets and frozen sets
# no order and cannot have duplicates in dictionary

car_parts = {"wheels", "doors", "exhaust", "windows"}
print(car_parts)
car_parts. add("steering_wheel")
print(car_parts)

car_parts. discard("windows")
print(car_parts)
# frozen sets - immutable set
x = frozenset([1,2,3,4,5])





