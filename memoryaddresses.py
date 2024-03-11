a = [1, 2, 3, 4, 5,]
print(id(a))

from ctypes import c_wchar_p, addressof

a = 44
print(addressof(c_wchar_p(a)))