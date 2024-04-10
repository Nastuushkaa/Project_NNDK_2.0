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



class traffic:
  def __init__(self, road, n):
      self.road = road
      self.n = n

  def change_light(self, light):
      if light == "G":
        return "O"
      elif light == "O":
        return "R"
      else:
        return "G"

  def begin(self):
      result = list(self.road)  # Преобразование дороги в список символов

      light_time = {"G": 5, "O": 1, "R": 5}  # Время для каждого цвета светофора
      lights = {}  # Словарь для хранения светофоров
      car_index = result.index("C")  # Индекс машины на дороге
      pred = ""  # Предыдущее состояние светофора

      # Поиск светофоров и их времени
      for i in range(len(result)):
          x = self.road[i]
          if x in light_time:
              lights[i] = (x, light_time[x])  # Запись светофора в словарь

      count = 0  # Счетчик времени
      print(f"{''.join(result)} - {count}")

      # Начало движения
      for i in range(self.n):
          count += 1

          # Изменение состояния светофоров
          for key in lights:
              if key == car_index:
                  continue

              color, n = lights[key]  # Получение текущего цвета и оставшегося времени
              n -= 1  # Уменьшение времени на один шаг

              result[key] = color  # Обновление цвета на дороге

              if n < 1:
                  color = self.change_light(color)  # Смена цвета светофора
                  lights[key] = color, light_time[color]  # Обновление времени и цвета
              else:
                  lights[key] = color, n  # Обновление оставшегося времени

          # Движение машины
          if car_index + 1 < len(self.road) - 1:
              if result[car_index + 1] == ".":  # Если следующая ячейка свободна, машина движется вперед
                  result[car_index], result[car_index + 1] = result[car_index + 1], result[car_index]
                  if pred == "G":
                      result[car_index] = pred
                      pred = "."

                  car_index += 1
              elif result[car_index + 1] == "R":  # Если перед машиной красный свет, машина останавливается
                  pass
              elif result[car_index + 1] == "G":  # Если перед машиной зеленый свет, машина движется вперед
                  result[car_index], result[car_index + 1] = result[car_index + 1], result[car_index]
                  result[car_index] = "."
                  pred = "G"
                  car_index += 1

          print(f"{''.join(result)} - {count}")  # Вывод текущего состояния дороги и времени

road = "C...R...R.R..G....G"  # Дорога с машиной и светофорами
n = 20  # Время движения
traffic = traffic(road, n)
traffic.begin()