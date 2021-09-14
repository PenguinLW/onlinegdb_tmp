import math as m;
def get_len_of_polyline(v):
    print(v);
    l = 0;
    for i in range(len(v)-1, 0, -1):
        for j in range(len(v[i])-1, -1, -2):
            l += m.sqrt(pow(v[i][j-1]-v[i-1][j-1],2)+pow(v[i][j]-v[i-1][j],2));
    return l;
print(get_len_of_polyline([list(range(1,3)),list(range(3,5)),list(range(5,7)),list(range(7,9))]));
print(get_len_of_polyline(
        [
            [4,5],
            [1,2],
            [7,8],
            [4,4]
        ]
    )
);

