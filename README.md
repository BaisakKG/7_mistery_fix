# Решатель квадратных уравнений

Решает квадратное уравнение, получает три параметра и выдает есть корень или нет.

# Как использовать

Надо импортировать функцию get_roots из модуля quadratic_equation.
Пример:

```
from quadratic_equation import get_roots

root1, root2 = get_roots(2,4,-1)
print(root)
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
