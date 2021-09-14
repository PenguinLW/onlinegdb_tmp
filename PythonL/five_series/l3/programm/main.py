def reset():
    global count;
    count = 0;
    #print(count);
def increment():
    global count;
    count += 1;
    #print(count);
def decrement():
    global count;
    count -= 1;
    #print(count);
def print_count():
    global count;
    print(count);
count = 0;
reset();
increment();
print_count();
increment();
print_count();
reset();
decrement();
decrement();
print_count();