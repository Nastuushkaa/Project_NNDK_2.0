from pprint import pprint
class Traffic:
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
      # Функция для смены цвета светофора   
      for key in self.lights:
        if key == self.car_index:
          continue
        color, n = self.lights[key]  # Получение текущего цвета и оставшегося времени 

        n -= 1  # Уменьшение времени на один шаг  
        self.result[key] = color  # Обновление цвета на дороге            
        if n < 1:
          if color == "G":
            color = "O"               
          elif color == "O":
            color = "R"               
          else:
              color = "G"             

          self.lights[key] = color, self.light_time[color] 
              # Обновление времени и цвета   
        else:
          self.lights[key] = color, n  
            # Обновление оставшегося времени    

  def begin(self):
    count = 0  # Счетчик времени
    traffic_road = [road]
    #print(f"{''.join(result)} - {count}")
    # Начало движения
    while count < self.n:

        count += 1
        self.change_light()
        self.__move_car()
        traffic_road.append("".join(self.result))
    return traffic_road
    
  def __move_car(self):
    # Движение машины
    if self.car_index + 1 < len(self.road) - 1:
        if self.result[self.car_index + 1] == ".":  
          # Если следующая ячейка свободна,машина движется вперед
            self.result[self.car_index], self.result[self.car_index + 1] = self.result[self.car_index + 1], self.result[self.car_index] 
          #Машина движется вперед если перед ней точка, а прошлое место машины заменяется на "."
            if self.pred == "G":
                self.result[self.car_index] = self.pred
                self.pred = "."

            self.car_index += 1
        elif self.result[self.car_index + 1] == "R":  
          # Если перед машиной красный свет, машина останавливается
            pass
        elif self.result[self.car_index + 1] == "G":  
          # Если перед машиной зеленый свет, машина движется вперед
            self.result[self.car_index], self.result[self.car_index + 1] = self.result[self.car_index + 1], self.result[self.car_index]
            self.result[self.car_index] = "."
            self.pred = "G"
            self.car_index += 1



t = Traffic("C...R...R.R..G....G", 15)
road = "C...R...R.R..G....G"  # Дорога с машиной и светофорами
n = 20  # Время движения
traffic = Traffic(road, n)
pprint(traffic.begin())

