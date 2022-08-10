# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H, X, Y):
    # write your code in Python 3.6
    n=len(H)
    total_cars=n
    cars_under_x=0
    cars_under_y=0
    total_time=0
    cars_counted=0
    #H.sort()
    for i in range(0,n):
        if H[i]==X:
            cars_under_x=cars_under_x+1
        elif H[i]==Y:
            cars_under_y=cars_under_y+1
        else:
            total_time=total_time+H[i]
            cars_counted=cars_counted+1
            if total_time==X:
                cars_under_x=cars_under_x+cars_counted
                cars_counted=0
                total_time=0
            elif total_time==Y:
                cars_under_y=cars_under_y+cars_counted
                cars_counted=0
                total_time=0
            else:
                continue
    ind_x=-1
    if cars_under_x==0:
        for i in range(0,n):
            temp=X-H[i]
            if temp in H:
                if H.index(temp)!=i:
                    cars_under_x=2
                    ind_x = i
            else:
                if cars_under_x==0:
                    if H[i]<X:
                        cars_under_x=1
                        ind_x=i

    if cars_under_y==0:
        for i in range(0,n):
            temp=Y-H[i]
            if temp in H and ind_x!=i:
                if H.index(temp)!=i:
                    cars_under_y=2
            else:
                if cars_under_y==0:
                    if H[i]<Y and ind_x!=i :
                        cars_under_y=1

    return cars_under_x+cars_under_y
    pass


if __name__ == '__main__':
    H = [6, 5, 5, 4, 3]
    x = 8
    y = 9
    print(str(solution(H, x, y)))
