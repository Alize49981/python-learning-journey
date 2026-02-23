
children = ["Ali", "Adan", "Issa"]
print(children[0])
print(children[1])
print(children[2])
children[1] = "Amad"
print(children)
children.append("Husen")
print(children)
children.insert(2, "Yusuf")
print(children)
children.remove("Amad")
children.pop()
children.pop(2)
print(children)
print(len(children))