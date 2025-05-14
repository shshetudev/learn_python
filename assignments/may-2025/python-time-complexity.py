
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
for i in range(n // 2, n):  # Runs n/2 times O(n)
    j = 2
    while j < n:  # j doubles each time O(log n)
        k = k + n / 2
        j *= 2

# Answer: O(n log n)
# Explanation: Outer loop O(n), inner loop O(log n) so Total O(n log n)


# Answer: X will always be a better choice for large inputs
# Explanation: In asymptotic analysis, we consider the growth of the algorithm in terms of input size. An algorithm X 
# is said to be asymptotically better than Y if X takes smaller time than y for all input sizes n larger than a value 
# n0 where n0 > 0


a = 0
i = N
while i > 0:
    a += i
    i //= 2  # Dividing by 2 each time

# Answer: O(log N)
# Explanation: Number of times N can be divided by 2 until reaching 0 is log N

# Answer: Both time and memory
# Explanation: Time and space complexity both matter in determining algorithm efficiency.

# Answer: By counting the number of primitive operations performed by the algorithm on a given input size

# code
for i in range(n):
    modified_i = i * k

# Answer: O(logkn)
# Explanation: Complexity depends on how many multiplications until reaching n log base k of n


value = 0
for i in range(n):
    for j in range(i):
        value += 1

# Answer: n(n-1)/2
# Explanation: Sum of inner loop counts+ 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 => O(n^2)

# Answer: False
# Explanation: Big O is asymptotic. For small input sizes, O(n) may perform better than O(log n) depending on instance.