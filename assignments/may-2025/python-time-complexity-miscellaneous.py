# Question 1: What is the time complexity of the following code?
# n = 10
def function(n):
    i = 1
    s = 1

    # 1 < 10 => True
    # 2 < 10 => True
    # 4 < 10 => True
    # 7 < 10 => True
    # 11 < 10 => False: LOOP EXITS
    while (s < n):
        # s = 1 + 1 = 2
        # s = 2 + 2 = 4
        # s = 4 + 3 = 7
        # s = 7 + 4 = 11
        s = s + i

        # i = 1 + 1 = 2
        # i = 2 + 1 = 3
        # i = 3 + 1 = 4
        # i = 4 + 1 = 5
        i += 1


############ MATHEMATICAL EXPLANATION STARTS ############
'''
    Natural number: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + ...... + 100 = ?
    
    [ Not using formula: N(N+1)/2]: 
    
    [ Using this formula: N(N+1)/2]: 
        N=100
        N+1=101
        N(N+1)/2 = 50x101 = 5050
    

    When S>=n , then loop will stop at kth iterations,
    ⇒ S>=n ⇒ S=n
    ⇒ 2 + 2 + 3 + 4 + ……+ k = n
    => 1 + (1+1) + (1+1+1) + (1+1+1+1) + … + (1+1+1+1+1) + k = n
    => 1 + 1+ 2 + 3 + 4 + ...... + k = n [ Formula for the sum of the first N natural numbers = N(N+1)/2]
    ⇒ 1 + (k * (k + 1))/2  = n
    ⇒  1 + (k^2+k)/2 = n 
    => (k^2)/2 = n
    => k^2 = n
    => k = √n
    Hence, the time complexity is O(√n).
'''
############ MATHEMATICAL EXPLANATION ENDS ##############

# Answer: Time complexity = O(√n).
# Explanation:
# The sum of 's' is a series: S = S + i, where S = 2 + 2 + 3 + ... + k.
# When S >= n, the loop stops. The sum of the series can be expressed as (k * (k + 1)) / 2 = n, which results in k^2 = n.
# Hence, the time complexity is O(√n).

# Question 2: What is the time complexity of the following code?
def fun(n):
    if (n < 5):
        print("GeeksforGeeks", end ="")
    else:
        for i in range(n):
            print(i, end= " ")

# Answer: Time complexity = O(1) in best case and O(n) in worst case.
# Explanation:
# If n < 5, the program prints only "GeeksforGeeks", which is a constant time operation O(1).
# But if n >= 5, the for loop runs, making the time complexity O(n).

# Question 3: What is the time complexity of the following code?
def fun(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a

# Answer: Time complexity = O(1) in best case and O(max(a, b)) worst case.
# Explanation:
# If a == b, the while loop doesn't run, so the time complexity is O(1).
# Otherwise, the while loop reduces the larger value step by step. In the worst case, the time complexity is O(max(a, b)).

# Question 4: What is the time complexity of the following code?
def fun(n):
    i = 0
    while i * i < n:
        print("GeeksforGeeks")
        i += 1

# Answer: Time complexity = O(√n).
# Explanation:
# The loop continues until i * i >= n. This happens when i = √n. Hence, the number of iterations is O(√n).

# Question 5: What is the time complexity of the following code?
def fun(n, x):
    for i in range(1, n, i * x):
        print("GeeksforGeeks")

# Answer: Time complexity = O(log_x n).
# Explanation:
# The number of iterations depends on how the value of i increases exponentially by a factor of x each time.
# The number of iterations is log_x(n), so the time complexity is O(log_x n).

# Question 6: What is the time complexity of the following code?
import math
def fun(n):
    for i in range(0, math.floor(n/2)):
        for j in range(1, n - math.floor(n/2) + 1):
            k = 1
            for k in range(1, n + 1, 2 * k):
                print("GeeksforGeeks")

# Answer: Time complexity = O(n^2 log2 n).
# Explanation:
# The first and second for loops have time complexity O(n).
# The third for loop has time complexity O(log2 n) because k doubles each time.
# Therefore, the overall time complexity is O(n^2 log2 n).

# Question 7: What is the time complexity of the following code?
def fun(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1, i):
            print("GeeksforGeeks")

# Answer: Time complexity = O(n log n).
# Explanation:
# The first loop runs n times.
# The second loop runs n / i times for each value of i.
# The total time complexity is O(n log n), since the sum of 1/n + 1/2n + ... approaches log n.

# Question 8: What is the time complexity of the following code?
def fun(n):
    for i in range(n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("GeeksforGeeks")

# Answer: Time complexity = O(n^2).
# Explanation:
# The first loop runs n / 3 times, and the second loop runs n / 4 times.
# Hence, the overall time complexity is O(n^2).

# Question 9: What is the time complexity of the following code?
def fun(n):
    i = 1
    while (i < n):
        j = n
        while (j > 0):
            j = j // 2
        i = i * 2

# Answer: Time complexity = O(log2 n).
# Explanation:
# The outer loop doubles the value of i each time, so it runs log n times.
# The inner loop halves the value of j each time, so it also runs log n times.
# Therefore, the overall time complexity is O(log2 n).

# Question 10: Consider the following code, what is the number of comparisons made in the execution of the loop?
def fun(n):
    j = 1
    while (j <= n):
        j = j * 2

# Answer: ceil(log2 n) + 1 comparisons.
# Explanation:
# The value of j doubles each time, so the number of iterations is log2 n.
# We take the ceiling of log2 n since the number of comparisons is one more than the iterations.
# Thus, the total number of comparisons is ceil(log2 n) + 1.