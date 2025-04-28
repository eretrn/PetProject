import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.model_selection import train_test_split

# Синтетические данные
np.random.seed(0)
X = np.random.randn(100, 10)
true_coef = np.array([1.5, -2, 0, 0, 3, 0, 0, 0, 0, 0])
y = X @ true_coef + np.random.randn(100) * 0.5

# Делим на обучение и тест
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# LassoCV: L1-регуляризация с подбором alpha
lasso_cv = LassoCV(alphas=np.logspace(-3, 1, 50), cv=5)  # 5-кратная кросс-валидация
lasso_cv.fit(X_train, y_train)

# RidgeCV: L2-регуляризация с подбором alpha
ridge_cv = RidgeCV(alphas=np.logspace(-3, 1, 50), cv=5)
ridge_cv.fit(X_train, y_train)

# Выводим лучшие alpha
print(f"Лучший alpha для Lasso (L1): {lasso_cv.alpha_:.4f}")
print(f"Лучший alpha для Ridge (L2): {ridge_cv.alpha_:.4f}")

# Проверяем качество на тесте
print(f"\nLasso R2 score на тесте: {lasso_cv.score(X_test, y_test):.4f}")
print(f"Ridge R2 score на тесте: {ridge_cv.score(X_test, y_test):.4f}")

# Визуализация коэффициентов
plt.figure(figsize=(10, 6))
plt.plot(true_coef, 'ko', label='Истинные коэффициенты')
plt.plot(lasso_cv.coef_, 'rs', label='Lasso (подобранный alpha)')
plt.plot(ridge_cv.coef_, 'g+', label='Ridge (подобранный alpha)')
plt.legend()
plt.title('Коэффициенты моделей с подобранным alpha')
plt.xlabel('Номер признака')
plt.ylabel('Значение коэффициента')
plt.grid(True)
plt.show()
