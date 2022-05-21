def cats_and_mouse(a, b, c):
    if abs(a - c) == abs(b - c): return 'Mouse C'
    return 'Cat A' if abs(a - c) < abs(b - c) else 'Cat B'

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        c_A, c_B, m_C = map(int, input().strip().split())
        result = cats_and_mouse(c_A, c_B, m_C)
        print(result)
