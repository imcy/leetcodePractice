import sys

from functools import cmp_to_key
from itertools import permutations

class Solution:

    def rank_grades(self, grades):
        for i, g in enumerate(grades):
            g.append(i+1)

        def cmp(a, b):
            for i in range(len(a)-1):
                if a[i] > b[i]:
                    return -1
                elif a[i] < b[i]:
                    return 1
                else:
                    continue
            return 0

        result = sorted(grades, key=cmp_to_key(cmp))
        res = [result[i][-1] for i in range(len(result))]
        return res

    def mathematical_competition(self, n, students):
        s = {}
        classes = {}
        c = 1
        for student in students:
            if s.get(student[0]):
                s[student[1]] = s[student[0]]
                classes[s[student[0]]].append(student[1])
            elif s.get(student[1]):
                s[student[0]] = s[student[1]]
                classes[s[student[1]]].append(student[0])
            else:
                s[student[0]] = c
                s[student[1]] = c
                classes[c] = []
                classes[c].append(student[0])
                classes[c].append(student[1])
                c += 1

        for i in range(n):
            if not s.get(i):
                classes[c] = [i]
                c += 1

        if len(classes) == 1:
            return 0

        len_list = []
        for c in classes:
            len_list.append(len(classes[c]))

        sum = 0
        for i in range(len(len_list)):
            for j in range(i+1, len(len_list)):
                sum += len_list[i]*len_list[j]

        return sum

    def find_best_cut_position(self, weights, n):
        total = sum(weights)
        middle = total // n
        ans = []
        start = 0
        for i in range(1, len(weights)+1):
            print(weights[start:i])
            if sum(weights[start:i]) >= middle:
                ans.append(weights[start:i])
                start = i

        print(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.mathematical_competition(5, []))
