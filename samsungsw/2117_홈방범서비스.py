def find_max_at_point(map_vlg, N, M, cur_pos, size_rhombus):
    x = cur_pos[0]
    y = cur_pos[1]

    expense = (size_rhombus+1)**2 + (size_rhombus)**2
    profit = 0
    cnt_house = 0
    for du in range(-size_rhombus, size_rhombus+1, 2):
        for dv in range(-size_rhombus, size_rhombus+1, 2):
            dx = (du+dv)//2
            dy = (du - dv)//2
            cur_x = x+dx
            cur_y = y+dy
            if cur_x >= 0 and cur_x < N and cur_y >= 0 and cur_y < N and map_vlg[cur_y][cur_x]:
                profit += M
                cnt_house += 1
    for du in range(-size_rhombus+1, size_rhombus, 2):
        for dv in range(-size_rhombus+1, size_rhombus, 2):
            dx = (du+dv)//2
            dy = (du-dv)//2
            cur_x = x+dx
            cur_y = y+dy
            if cur_x >= 0 and cur_x < N and cur_y >= 0 and cur_y < N and map_vlg[cur_y][cur_x]:
                profit += M
                cnt_house += 1
    if profit - expense >= 0:
        return cnt_house
    else:
        return 0


def find_max(map_vlg, N, M):
    i_max = 0
    for size_rhombus in range(2*N-1, 0, -1):
        for x in range(N-(size_rhombus+1)//2+2):
            for y in range(N-(size_rhombus+1)//2+2):
                i_val = find_max_at_point(map_vlg, N, M, (x, y), size_rhombus)
                if i_val > i_max:
                    i_max = i_val
        if i_max > 0:
            break
    return i_max


def set_data(T):
    for _ in range(T):
        N, M = map(int, input().split())
        map_vlg = [list(map(int, input().split(' '))) for _ in range(N)]
        yield map_vlg, N, M


T = int(input())
i = 0
for map_vlg, N, M in set_data(T):
    ans = find_max(map_vlg, N, M)
    print("#%d %d" % (i+1, ans))
    i += 1