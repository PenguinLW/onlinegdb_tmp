import math;
message = [32, 14, 5, 22, 17, 0, 14, 31, 19, 0, 10, 14];#я не храню тайн

'''
    20 -> 13, Usova
    n = 793, e = 79
    p = 13, q = 61, f(n) = 720, d = 319
'''
for el in message:
    print(pow(el, 79) % 793);
print("\n");
shifr = [761, 14, 229, 321, 173, 0, 14, 697, 280, 0, 166, 14];#[761, 292, 424, 559, 380, 0, 292, 268, 398, 0, 387, 292, 274, 0, 0, 0];
for el in shifr:
    print(pow(el, 319) % 793);

print("\n");
'''
    20 -> 13, Usova
    n = 793, e = 7
    p = 13, q = 61, f(n) = 720, d = 103
'''
for el in message:
    print(pow(el, 7) % 793);
print("\n");
shifr = [761, 14, 411, 178, 30, 0, 14, 112, 553, 0, 270, 14];
for el in shifr:
    print(pow(el, 103) % 793);

print("\n");



