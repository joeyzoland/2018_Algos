def ArrayManipulation():



# code copied from hackerRank; timing out for more complex problems, even though O^n complexity?
#
# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#
#     array = []
#     for _ in range (0, n):
#         array.append(0)
#
#     for a0 in range(m):
#         a, b, k = input().strip().split(' ')
#         a, b, k = [int(a), int(b), int(k)]
#         for i in range(a - 1, b):
#             array[i] += k
#
#     max = array[0]
#     for j in range(1, len(array)):
#         if (array[j] > max):
#             max = array[j]
#     print (max)
