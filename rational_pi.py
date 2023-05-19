import math

PI = math.pi

best_log_dr = 1
best_p, best_q = None, None

for q in range(1, 100_000_000):
    p1 = int(q * PI)
    for p in [p1, p1 + 1]:
        r = p / q
        log_dr = math.log10(abs(r - PI))

        if log_dr < best_log_dr:
            best_log_dr = log_dr
            best_p, best_q = p, q
            print(f'{best_p}/{best_q} = {r} (log error: {best_log_dr:.1f})')
