# פונקציית המטרה שלנו
def f(x):
    return x**2

# נגזרת של הפונקציה (השיפוע)
def f_prime(x):
    return 2 * x

# פונקציה לחישוב Gradient Descent
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point  # נקודת ההתחלה שלנו
    for i in range(iterations):
        gradient = f_prime(x)  # חישוב השיפוע בנקודה הנוכחית
        x = x - learning_rate * gradient  # עדכון הערך של x לפי נוסחת Gradient Descent
        print(f"איטרציה {i + 1}: x = {x}, f(x) = {f(x)}")  # הצגת התוצאה בכל איטרציה
    return x

# הגדרות
starting_point = 3 # נקודת התחלה
learning_rate = 0.01  #  קצב הלמידה מומלץ 0.001
iterations = 510  # מספר האיטרציות

# הרצת Gradient Descent
final_x = gradient_descent(starting_point, learning_rate, iterations)
print(f"המינימום נמצא ב- x ≈ {final_x}")