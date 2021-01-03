def html_tag(tag):
    
    def wrap_text(msg):
        print(f'<{tag}>{msg}<{tag}>')
        
    return wrap_text

print_h1 = html_tag('h1')
print_h1('test another headline')
print_h1('another headline')

print_p = html_tag('p')
print_p('Test Paragraph1')


def logger(msg):
    
    def log_message():
        print('Log:', msg)
        
    return log_message

log_hi = logger('Hi!')
log_hi()


def square(x):
    return x * x


f = square

print(square)
print(f(5))


def my_map(func, nums):
    for i in range(len(nums)):
        nums[i] = func(nums[i])
        
    return nums

squares = my_map(square, [1,2,3,4,5])
print(squares)



def cube(x):
    return x * x * x