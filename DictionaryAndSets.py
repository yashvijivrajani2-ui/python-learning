dict={
    "key": "value",
    "name": "yashvi",
    "age": 20,
    "is student": True,
    "marks": [94.4, 88.5, 76.3, 92.1, 85.0]
}
print(dict)

# only tuples can be made keys because they are immutable
dict["surname"]="jivrajani"
print(dict)

student={
    "name":"yashvi",
    "score":{
        "phy": 90,
        "chem": 95,
        "maths": 85
    }
}
print(student)
print(student["score"]["phy"])

print(dict.keys())
print(dict.values())
print(dict.items())
print(len(dict))
print(dict.get("name"))
dict.update({"age": 21})
print(dict)
dict.update({"a": "b"})
print(dict)

print(list(dict.keys()))
print(len(list(dict.keys())))

# a["keys"]=value, similarly a.get("keys")=value, but a.get() will not throw an error if the key is not present, it will return None instead

# sets are unordered collection of unique elements. it is immutable
s1={1, 2, 2, 3}
print(s1)
print(type(s1))  

s1.add(4)
print(s1)

s1.remove(2)
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)

s2={1, 2, 3, 4, 5}
s3={4, 5, 6, 7, 8}

print(s2.union(s3))
print(s2.intersection(s3))
print(s2.difference(s3))
print(s2.symmetric_difference(s3))
print(s2.issubset(s3))
print(s2.issuperset(s3))
print(s2.isdisjoint(s3))

d={
    "table":["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

print(d)