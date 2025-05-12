#The itertools module in the standard library offers powerful functions that work with and return iterators.
import itertools as it


cycler = it.cycle([1,2,3])#We can have an infinity iterator that starts at the beginning after reaching its end with cycle:
print("using cycle():")
next(cycler)
next(cycler)
c= next(cycler)
print(c)
c = next(cycler)# restarts from 1
print(c)


#The function counter provides an infinite counter with an optional start value (default is zero):
print("using count():")
counter = it.count(3)
c2 = next(counter)
print(c2)
c2 = next(counter)
print(c2)
c2 = next(counter)
print(c2)

#With repeat we can construct a new iterator that also can be infinite:
print("using repeat():")
l = list(it.repeat(4,2))
print(l)
endless  = it.repeat(3)
l = next(endless)
print(l)
l = next(endless)
l = next(endless)
print(l)

# We can use iszip to zip two or more iterables: ????

#Two or more iterables can be combine in one with chain:
print("using chain()")
lz = list(it.chain([1,2,3], [4,5,6,7,8]))
print(lz)

#To get only part of an iterable, we can use islice that works very similar to the slicing of sequences:
print("using islice()")
ls = list(it.islice(range(10), 5))
print(ls)
ls = list(it.islice(range(10), 5, None))
print(ls)
ls =  list(it.islice(range(10), 5, None, 3)) # 3 is step
print(ls)

'''
Exercises:
1. Write a generator that creates an endless stream of numbers starting from a value given as argument with a step size of 5.
Write one version without and one with itertools.
2. Extend this generator into an coroutine that allows the step size to be set from outside.
3. Stop the coroutine after it has produced 10 values (a) form outside and (b) from inside the coroutine.
4. Rewrite the following code snippets using itertools.
        x = 0
        while True:
            x += 1
        [1, 2, 3, 4, 5][2:]
        [1, 2, 3, 4, 5][:4]
        [1, 2, 3] + [4, 5, 6]
        zip('abc', [1, 2, 3])

'''
