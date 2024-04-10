# Вариант 1.
# Создайте класс, который имитирует дорожное движение.

# Правила:
# 1. Класс принимает дорогу road и время n.
# 2. Дорога является строкой типа ""C...R.....G....G.."
# 3. Время является числом.
# 4. На каждой итерации автомобиль "C" движется по дороге на 1 единицу вперед согласно сигналам светофора.
# 5. Сигнал светофора меняется следующим образом: G - 5 единиц времени --> O - 1 единица --> R - 5 единиц. Цикл повторяется.
# 6. Класс возвращает список строк каждой итерации

#разобраться со сфетофорами 
#если зеленый едем и тд
#4 коммита минимум с каждого по 1му
# Пример
# road = ""C...R...R.R..G....G"
# n = 15

# Результат:
# [   
#   "C...R...R.R..G....G", // 0   Стартовая позиция
#   ".C..R...R.R..G....G", // 1
#   "..C.R...R.R..G....G", // 2
#   "...CR...R.R..G....G", // 3
#   "...CR...R.R..G....G", // 4
#   "....C...G.G..O....O", // 5   C вместо G
#   "....GC..G.G..R....R", // 6
#   "....G.C.G.G..R....R", // 7
#   "....G..CG.G..R....R", // 8
#   "....G...C.G..R....R",  // 9
#   "....O...OCO..G....G",  // 10
#   "....R...RCR..G....G",  // 11
#   "....R...RCR..G....G",  // 12
#   "....R...RCR..G....G",  // 13
#   "....R...RCR..G....G",  // 14
#   "....R...RCR..G....G",  // 15

from pprint import pprint
class traffic:
  def __init__(self, road, n):
    self.road = road
    self.result = list(self.road)
    self.n = n

    self.light_time = {"G": 5, "O": 1, "R": 5}  # Время для каждого цвета светофора
    self.lights = {}  # Словарь для хранения светофоров
    self.car_index = self.result.index("C")  # Индекс машины на дороге
    self.pred = ""  # Предыдущее состояние светофора

    for i in range(len(self.result)):
      x = self.road[i]
      if x in self.light_time:
          self.lights[i] = (x, self.light_time[x])  # Запись светофора в словарь

  def change_light(self):
    # if light == "G":
    #   return "O"
    # elif light == "O":
    #   return "R"
    # else:
    #   return "G"
    # # Изменение состояния светофоров
    # for key in self.lights:
    #     if key == self.car_index:
    #         continue

    #     color, n = self.lights[key]  # Получение текущего цвета и оставшегося времени
    #     n -= 1  # Уменьшение времени на один шаг

    #     self.result[key] = color  # Обновление цвета на дороге

    #     if n < 1:
    #         color = change_light(color)  # Смена цвета светофора
    #         self.lights[key] = color, self.light_time[color]  # Обновление времени и цвета
    #     else:
    #         self.lights[key] = color, n  # Обновление оставшегося времени
    pass

  def begin(self):
    count = 0  # Счетчик времени
    traffic_road = [road]
  #print(f"{''.join(result)} - {count}")
  # Начало движения
    while count < self.n:

        count += 1
        self.__change_light()
        self.__move_car()
        traffic_road.append("".join(self.result))
    return traffic_road