n = int(input())
students = [{'dohod': dohod, 'educ': educ, 'free': free} for dohod, educ, free in zip(
    map(int, input().split()), map(int, input().split()), map(int, input().split()))]

q = int(input())
test_cases = [{'dohod': dohod, 'educ': educ, 'free': free} for dohod, educ, free in zip(
    map(int, input().split()), map(int, input().split()), map(int, input().split()))]

country = [next((str(j+1) for j, student in enumerate(students) if (student['free'] == 1 and j+1 == test_case['free'])
                or (test_case['educ'] >= student['educ'] and test_case['dohod'] >= student['dohod'])), '0') for test_case in test_cases]

print(' '.join(country))
