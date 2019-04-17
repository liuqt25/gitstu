def F(**kwargs):
    print(kwargs)

li = {"k1":1,"k2":2}
F(k=li)
F(**li)

# {'k': {'k2': 2, 'k1': 1}}
# {'k2': 2, 'k1': 1}
