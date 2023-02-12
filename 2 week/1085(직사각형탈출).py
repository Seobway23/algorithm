x, y, w, h = map(int, input().split())
ans = 0
# x,y는 한수의 좌표

# w, h 는 직사각형의 좌표

x_cmp = abs(x - w)  # 한수와 직사각형의 x축 거리
y_cmp = abs(y - h)  # 한수와 직사각형의 y축 거리

if x_cmp > x: #x가 더 작다면 갱신
    x_cmp = x

if y_cmp > y: #y가 더 작다면 갱신
    y_cmp = y

if x_cmp >= y_cmp:
    ans = y_cmp

else:
    ans = x_cmp

print(ans)