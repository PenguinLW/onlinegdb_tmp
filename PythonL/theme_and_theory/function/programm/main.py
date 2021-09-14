import programm as p;
# def triangle_area(base, height):
#     """
#         Функия вычисляет площадь треугольника
#         по стороне и высоте, проведённой к ней.
#     """
#     area = 1/2 * base * height;
#     return area;
# #print(triangle_area(3,8));
# def farengeit2celsius(farengeit):
#     '''
#         Функция возвращает температуру в цельсиях
#         заданную по известной в фаренгейтах
#     '''
#     celsius = 5/9 * (farengeit - 32);
#     return celsius;
# #c1 = farengeit2celsius(32);
# #c2 = farengeit2celsius(212);
# #print("{0:f} {1:f}".format(c1, c2));
# #print(farengeit2celsius(451));
# def farengeit2kelvin(farengeit):
#     '''
#         Функция возвращает температуру в кельвинах
#         заданную по известной в фаренгейтах
#     '''
#     cel = farengeit2celsius(farengeit);
#     kelvin = cel + 273.15;
#     return kelvin;
# #k1 = farengeit2kelvin(32);
# #k2 = farengeit2kelvin(212);
# #print("{0:f} {1:f}".format(k1, k2));
# def hello():
#     print("Hola Mundo!!");
# #print(hello());
# #n = hello();
# #print(n);

print(p.hello());

print(p.farengeit2kelvin(212));