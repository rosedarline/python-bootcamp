def display_info(a, b, *args, instructor="James", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))

print(display_info(1, 2, 3, last_name="Stone", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "James"
# kwargs - {'last_name': "Stone", "job": "Instructor"}

[1, 2, (3,), 'James', {'last_name': 'Stone', 'job': 'Instructor'}]