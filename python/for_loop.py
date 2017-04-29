numbers = [1, 2, 3]
count = len(numbers)
# Basic
for i in xrange(count):
    print 'index:', i

# Iterate on sequences
scores = [0.2, 0.5]
for score in scores:
    print 'score:', score

# Iterate on dictionaries
data = {'name': 'DSW', 'type': 'camp'}
for key in data:
    value = data[key]
    print key, ':', value
