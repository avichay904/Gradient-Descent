import numpy as np
import matplotlib.pyplot as plt

# פונקציית המטרה שלנו
def f(x):
    return x**2

# נגזרת של הפונקציה (השיפוע)
def f_prime(x):
    return 2 * x

# פונקציה לחישוב Gradient Descent
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point  # נקודת ההתחלה שלנו
    positions = []  # רשימה לשמור את הערכים של x בכל איטרציה
    for i in range(iterations):
        gradient = f_prime(x)  # חישוב השיפוע בנקודה הנוכחית
        x = x - learning_rate * gradient  # עדכון הערך של x לפי נוסחת Gradient Descent
        positions.append(x)  # שמירת הערך הנוכחי של x
        print(f"איטרציה {i + 1}: x = {x}, f(x) = {f(x)}")  # הצגת התוצאה בכל איטרציה
    return x, positions


starting_point = 3  # נקודת התחלה
learning_rate = 0.01  # קצב הלמידה
iterations = 510  # מספר האיטרציות

# הרצת Gradient Descent
final_x, positions = gradient_descent(starting_point, learning_rate, iterations)
print(f"המינימום נמצא ב- x ≈ {final_x}")





# ציור הפונקציה f(x)
x_values = np.linspace(-5, 5, 100)  # טווח x ליצירת גרף
y_values = f(x_values)  # חישוב ערכי y

plt.figure(figsize=(8, 6))  # גודל הגרף
plt.plot(x_values, y_values, label='f(x) = x^2', color='blue')  # ציור הפונקציה
plt.scatter(positions, f(np.array(positions)), color='red', label='Gradient Descent Steps')  # ציור הנקודות שנמצאות במהלך GD
plt.title('Gradient Descent on f(x) = x^2')  # כותרת
plt.xlabel('x')  # תווית ציר x
plt.ylabel('f(x)')  # תווית ציר y
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # קו אופקי על ה-y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # קו אנכי על ה-x=0
plt.legend()  # הצגת המדריך
plt.grid()  # רשת
plt.show()  # הצגת הגרף