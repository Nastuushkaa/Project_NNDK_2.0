# class Traffic:
#   def __init__(self, road, n):
#       self.road = road
#       self.n = n

#   def __change_light(self, light):
#       if light == "G":
#         return "O"
#       elif light == "O":
#         return "R"
#       else:
#         return "G"

  def begin(self):
      result = list(self.road)  # Преобразование дороги в список символов

      # light_time = {"G": 5, "O": 1, "R": 5}  # Время для каждого цвета светофора
      # lights = {}  # Словарь для хранения светофоров
      # car_index = result.index("C")  # Индекс машины на дороге
      # pred = ""  # Предыдущее состояние светофора

      # # Поиск светофоров и их времени
      # for i in range(len(result)):
      #     x = self.road[i]
      #     if x in light_time:
      #         lights[i] = (x, light_time[x])  # Запись светофора в словарь

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
                  result[car_index], result[car_index + 1] = result[car_index + 1], result[car_index] #Машина движется вперед если перед ней точка, а прошлое место машины заменяется на "."
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
traffic = Traffic(road, n)
traffic.begin()