num_map = [1, 5, 8, 0, 6, 2, 4, 9, 3, 7]
color_cnt = [174, 135, 134, 174, 117, 164, 143, 141, 140, 128]

ans = 0
for i in range(10):
    ans += num_map[i] * color_cnt[i]

print(ans)