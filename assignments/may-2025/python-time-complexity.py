import random

a = 0
b = 0
for i in range(N):  # O(N)
    a = a + random.random()

for i in range(M):  # O(M)
    b = b + random.random()

# Answer: O(N + M) time, O(1) space
# Explanation: Two independent loops so Time = O(N + M)
# Constant number of variables so Space = O(1)

a = 0
for i in range(N):  # Outer loop runs N times
    for j in reversed(range(i, N)):  # Inner loop runs (N - i) times
        a = a + i + j

# Answer: O(N^2)
# Explanation: Number of operations = N*(N+1)/2 = O(N^2)

k = 0
# n=10 , range(n//2,n): (5,9)
for i in range(n // 2, n):  # Runs n/2 times O(n)
    # i = 5, 6, 7, 8, 9
    j = 2
    # 2 < 10
    # 4 < 10
    # 8 < 10
    # 16 < 10 <NO>:<END WHILE LOOP>
    while j < n:  # j doubles each time O(log n)
        k = k + n / 2  # 5, 10, 15
        j *= 2  # 4, 8, 16 (j=j*2)

# Answer: O(n) * O(log n) = O(n log n)
# Explanation: Outer loop O(n), inner loop O(log n) so Total O(n log n)


# Answer: X will always be a better choice for large inputs
# Explanation: In asymptotic analysis, we consider the growth of the algorithm in terms of input size. An algorithm X 
# is said to be asymptotically better than Y if X takes smaller time than y for all input sizes n larger than a value 
# n0 where n0 > 0


# N=10
a = 0
# i = 10
i = N

# 10 > 0
# 5 > 0
# 2 > 0
# 1 > 0
# 0 > 0 = False
while i > 0:
    # a = a + i = 0 + 10 = 10
    # a = 10 + 5 = 15
    # a = 15 + 2 = 17
    # a = 17 + 1 = 18
    a += i

    # i = i/2 = 10/2 = 5
    # i = 5/2 = 2.5 = 2
    # i = 2/2 = 1
    # i = 1/2 = 0.5 = 0
    i //= 2  # Dividing by 2 each time

# Answer: O(log N)
# Explanation: Number of times N can be divided by 2 until reaching 0 is log N

# Answer: Both time and memory
# Explanation: Time and space complexity both matter in determining algorithm efficiency.

# Answer: By counting the number of primitive operations performed by the algorithm on a given input size

# code
# n = 10, range = (0,9)
# k = 2

'''
for(i=0;i<n;i++)
'''
# i = 0
# i++ = i+1 = 0 + 1 = 1, 1<10
# i = 2
# i = 3
# i = 4
# i = 5
# i = 7
# i = 8
# i++ = i+1 = 8+1 = 9, 9 < 10
# i++ = i+1 = 9+1 = 10, (10 < 10): ==== False, Loop breaks ========

for i in range(n):
    # modified_i = 0 * 2 = 0
    # modified_i = 1 * 2 = 2
    # modified_i = 2 * 2 = 4
    # modified_i = 3 * 2 = 6
    # modified_i = 4 * 2 = 8
    # modified_i = 5 * 2 = 10
    # modified_i = 6 * 2 = 12
    # modified_i = 7 * 2 = 14
    # modified_i = 8 * 2 = 16
    # modified_i = 9 * 2 = 18
    modified_i = i * k

# Answer: O(logkn)
# Explanation: Complexity depends on how many multiplications until reaching n log base k of n

# n = 10, i = (0,9)
value = 0

'''
    for(i=0;i<n;i++)
'''
# i = 0
#---------------------------------
# i = 0 + 1 = 1 < 10: True
#---------------------------------
# i = 1 + 1 = 2 < 10: True
#---------------------------------
# i = 2 + 1 = 3 < 10: True
#---------------------------------
for i in range(n):
    '''
        for(j=0;j<i,j++)
    '''
    # j = (0,0) = (0,-1): False, Loop breaks
    #---------------------------------
    # j = range(0,1) = 0
    # j = 0+1 = 1 < 0: False, Loop breaks
    #---------------------------------
    # j = range(0,2) = 0 , 1
    # j = 0: True
    # j = 0 + 1 = 1 < 2: True
    # j = 1+1 = 2 < 2: False, Loop breaks
    #---------------------------------
    # j = range(0,3) = 0 , 1, 2
    # j = 0: True
    # j = 0+1 = 1 < 2: True
    #---------------------------------
    for j in range(i):
        # ----------------------------
        # value = value + 1 = 0 + 1 = 1
        # ----------------------------
        # value = 1 + 1 = 2, j=0
        # value = 2 + 1 = 3, j=1
        # ----------------------------
        # value = 3 + 1 = 4, j=0
        value += 1

# Answer: n(n-1)/2
# Explanation: Sum of inner loop counts+ 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 => O(n^2)

# Answer: False
# Explanation: Big O is asymptotic. For small input sizes, O(n) may perform better than O(log n) depending on instance.
