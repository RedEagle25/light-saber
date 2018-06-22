formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("earth", "fire", "wind", "water")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"There was an idea",
"To bring together, a group of remarkable people",
"So when we needed them,",
"They could fight the battles, that we never could."
)
