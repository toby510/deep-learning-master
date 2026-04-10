# show_pkl.py
import pickle

# 打开 pkl 文件
with open("sample_weight.pkl", "rb") as f:
    params = pickle.load(f)

# 打印里面有哪些键
print("文件里包含的键：")
print(list(params.keys()))

# 打印每个参数的形状
print("\n各参数形状：")
for key, val in params.items():
    print(f"{key}: {val.shape}")

#想看具体数值可以打印
print("\nW1 前5行：")
print(params['W1'][:5])

#