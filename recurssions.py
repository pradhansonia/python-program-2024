def tri_recurssion(k):
    if (k > 0):
        result = k + tri_recurssion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\Recurssion Examle Results")
tri_recurssion(6)