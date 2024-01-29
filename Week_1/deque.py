#Deque

#As an extension to a typlical Python list we can also iport a 'Deque'
#All pop and push operations take O(1) runtime. A Deque is a double-ended LinkedList 
#Where you can pop and push from both the left and the right


from collections import deque
d = deque('ghi')
for e in d:
    print(e.upper())

d.append('j');
d.appendleft('f');
print(d);

#Return and remove the rightmost item
print(d.pop())

#return and remove leftmost item
print(d.popleft());

#To show the full deque 
print(d)
#Peeking at the leftmost item
print(d[0]);

#Peeking at the rightmost item
print(d[-1]);

#list the content of a deque in reverse
list(reversed(d));

#Check if 'h' is in the deque. This takes O(n) time.
print('h' in d) #True

d.extend('jkl') # This add multiple elements at once
print(d);
d.rotate(1) #Right rotation
print(d);
d.rotate(-1) #Left rotation
print(d);


#Make a new deque in reverse order
print(deque(reversed(d)))

d.clear(); #Empty the deque
# d.pop(); #Cannot pop from an empty deque
print(d);

d.extendleft('abc');
d.extend('dsa')
print(d)