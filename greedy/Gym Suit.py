

def solution(n, lost, reserve):
    set_res = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)

    for i in set_res:

        if i - 1 in set_lost:
            print(i-1)
            set_lost.remove(i-1)

        elif i + 1 in set_lost:
            print(i + 1)
            set_lost.remove(i+1)


    answer = n-len(set_lost)

    return answer


solution(5, [2, 4], [1, 3, 5])