def CR7(a):
    try:
        return float(a)
    except ValueError:
        print("変換できません")

result = CR7("abc")
print(result)
