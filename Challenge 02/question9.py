#9.	La pente est (m = y2-y1/x2-x1). Trouvez la pente et la distance euclidienne 
#entre le point (2, 2) et le point (6, 10).
import math

x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La pente m est : {m}")
print(f"La distance euclidienne est : {d}")