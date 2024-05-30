# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # string format using f-string 
    return f"Hello, my name is {name} and I am {age} years old."

# Review 3
class Counter:
    # count = 0

    # def __init__(self):
    #     self.count += 1

    # def get_count(self):
    #     return self.count
    
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

# Review 4
import threading

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    # reorder the following statement
    # t.start()
    # threads.append(t)
    threads.append(t)
    t.start()

 

for t in threads:
    t.join()


# Review 5
import time
def count_occurrences(lst):
    # increment operation should be "+="
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def test_passing():
    # Review 1
    assert add_to_list("aa") == ["aa"]
    
    # Review 2
    c = Counter()
    assert c.get_count() == 0
    c.increment()
    assert c.get_count() == 1
    
    # Review 3
    assert format_greeting("Peter", "27") == "Hello, my name is Peter and I am 27 years old."
    
    # Review 4
    counter = SafeCounter()
    assert counter.get_count() == 0
    start = time.time()
    threads = []

    for _ in range(10):
        t = threading.Thread(target=worker, args=(counter,))
        # reorder the following statement
        # t.start()
        # threads.append(t)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()
    assert counter.get_count() == 10000
    print(end - start)
    
    # Review 5
    assert count_occurrences(["a","a","a","b","c"]) == dict(a=3, b=1, c=1)

if __name__ == "__main__":
    # Review 1
    print(add_to_list("aa"))
    
    # Review 2
    c = Counter()
    print(c.get_count())
    c.increment()
    print(c.get_count())
    
    # Review 3
    print(format_greeting("peter", "27"))
    
    # Review 4
    counter = SafeCounter()
    print(counter.get_count())
    start = time.time()
    threads = []

    for _ in range(10):
        t = threading.Thread(target=worker, args=(counter,))
        # reorder the following statement
        # t.start()
        # threads.append(t)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()
    print(counter.get_count())
    print(end - start)
    
    # Review 5
    dict_count = count_occurrences([1,1,1,5,6])
    print(dict_count)