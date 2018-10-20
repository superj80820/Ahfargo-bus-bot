l = [{'a': 123, 'b': 1234},
    {'a': 3222, 'b': 1234},
    {'a': 123, 'b': 12334}]
# seen = set()
# new_l = []
# for d in l:
#     t = tuple(d.items())
#     if t not in seen:
#         seen.add(t)
#         new_l.append(d)
new_l = {tuple(d.items()) for d in l}
# new_l = [dict(t) for t in {tuple(d.items()) for d in l}]

print(new_l)