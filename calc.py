from tkinter import *
from math import sqrt

def setWindow(root):
  root.title("Калькулятор")
  root.resizable(False, False)

  w = 414
  h = 673
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  x = int(ws / 2 - w / 2)
  y = int(hs / 2 - h / 2)

  root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

  #root.iconbitmap('ПИВ-PAV.ico')

root = Tk()
setWindow(root)

# Работа с кнопкой C
def clickC(event):
  global lst
  global a
  global b
  global c
  plus.config(bg=colours[index])
  minus.config(bg=colours[index])
  multiplication.config(bg=colours[index])
  division.config(bg=colours[index])
  equally.config(bg=colours[index])
  r = display.get()
  lst.clear()
  display.set(lst)
  a = ""
  b = ""
  c = ""

# Работа с кнопкой 0
def clickZero(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    one["state"] == DISABLED
  elif len(display.get()) >= 14:
    one["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "0"
        display.set(r)
      else:
        r = display.get()
        r += "0"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "0"
      result.config(display.set(r))

# Работа с кнопкой 1
def clickOne(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    one["state"] == DISABLED
  elif len(display.get()) >= 14:
    one["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "1"
        display.set(r)
      else:
        r = display.get()
        r += "1"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "1"
      result.config(display.set(r))

# Работа кнопки 2
def clickTwo(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    two["state"] == DISABLED
  elif len(display.get()) >= 14:
    two["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "2"
        display.set(r)
      else:
        r = display.get()
        r += "2"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "2"
      result.config(display.set(r))

# Работа кнопки 3
def clickThree(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    three["state"] == DISABLED
  elif len(display.get()) >= 14:
    three["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "3"
        display.set(r)
      else:
        r = display.get()
        r += "3"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "3"
      result.config(display.set(r))

# Работа кнопки 4
def clickFour(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    four["state"] == DISABLED
  elif len(display.get()) >= 14:
    four["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "4"
        display.set(r)
      else:
        r = display.get()
        r += "4"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "4"
      result.config(display.set(r))

# Работа кнопки 5
def clickFive(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    five["state"] == DISABLED
  elif len(display.get()) >= 14:
    five["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "5"
        display.set(r)
      else:
        r = display.get()
        r += "5"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "5"
      result.config(display.set(r))

# Работа кнопки 6
def clickSix(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    six["state"] == DISABLED
  elif len(display.get()) >= 14:
    six["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "6"
        display.set(r)
      else:
        r = display.get()
        r += "6"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "6"
      result.config(display.set(r))

# Работа кнопки 7
def clickSeven(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    seven["state"] == DISABLED
  elif len(display.get()) >= 14:
    seven["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "7"
        display.set(r)
      else:
        r = display.get()
        r += "7"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "7"
      result.config(display.set(r))

# Работа кнопки 8
def clickEight(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    eight["state"] == DISABLED
  elif len(display.get()) >= 14:
    eight["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "8"
        display.set(r)
      else:
        r = display.get()
        r += "8"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "8"
      result.config(display.set(r))

# Работа кнопки 9
def clickNine(event):
  global lst
  global a
  global b
  lst = []
  if display.get() == "Ошибка":
    nine["state"] == DISABLED
  elif len(display.get()) >= 14:
    nine["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or equally.cget("bg") == "#05FF04":
        plus.config(bg=colours[index])
        minus.config(bg=colours[index])
        multiplication.config(bg=colours[index])
        division.config(bg=colours[index])
        equally.config(bg=colours[index])
        r = "9"
        display.set(r)
      else:
        r = display.get()
        r += "9"
        result.config(display.set(r))
      b = display.get()
    else:
      r = display.get()
      r += "9"
      result.config(display.set(r))

# Работа кнопки %
def clickPercent(event):
  try:
    r = display.get()
    r = float(r) / 100
  except ValueError:
    result.config(text=display.set("Ошибка"))
  else:
    if len(str(r)) > 14:
      r = round(r, 5)
    result.config(text=display.set(r))

# Работа кнопки +/-
def clickNegative(event):
  global lst
  global b
  lst = []
  if a != "":
    if plus.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or multiplication.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF":
      plus.config(bg=colours[index])
      minus.config(bg=colours[index])
      multiplication.config(bg=colours[index])
      division.config(bg=colours[index])
      equally.config(bg=colours[index])
      r = "-"
      display.set(r)
    else:
      try:
        r = display.get()
        r = int(r) * -1
        display.set(r)
      except ValueError:
        r = display.get()
        r = float(r) * -1
        display.set(r)
    b = display.get()
  elif len(display.get()) == 0:
    r = "-"
    display.set(r)
  elif display.get() == "-":
    r = ""
    display.set(r)
  else:
    try:
      r = display.get()
      r = int(r) * -1
      display.set(r)
    except ValueError:
      r = display.get()
      r = float(r) * -1
      display.set(r)
    except ValueError:
      display.set("Ошибка")

# Работа кнопки √
def clickSquare(event):
  global lst
  try:
    r = display.get()
    r = sqrt(float(r))
    if len(str(r)) > 14:
      r = round(r, 5)
    display.set(r)
  except ValueError:
    result.config(text=display.set("Ошибка"))

# Работа кнопки +
def clickPlus(event):
  global c
  global lst
  global a
  global b
  plus.config(bg="#1CE8FF")
  multiplication.config(bg=colours[index])
  division.config(bg=colours[index])
  minus.config(bg=colours[index])
  # В исключениях такого типа проверяется тип числа и ответ выводится в int или float
  try:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = int(a) + int(b)
        display.set(a)
      elif c == "-":
        a = int(a) - int(b)
        display.set(a)
      elif c == "×":
        a = int(a) * int(b)
        display.set(a)
      else:
        # В этом исключении выводится "Ошибка", если переменная b равна нулю
        try:
          a = float(a) / float(b)
          a = round(a, 5)
          display.set(a)
        except ZeroDivisionError:
          display.set("Ошибка")
  except ValueError:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = float(a) + float(b)
        display.set(a)
      elif c == "-":
        a = float(a) - float(b)
        display.set(a)
      elif c == "×":
        a = float(a) * float(b)
        a = round(a, 5)
        display.set(a)
  b = ""
  c = "+"

# Работа кнопки -
def clickMinus(event):
  global c
  global lst
  global a
  global b
  minus.config(bg="#1CE8FF")
  division.config(bg=colours[index])
  multiplication.config(bg=colours[index])
  plus.config(bg=colours[index])
  try:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = int(a) + int(b)
        display.set(a)
      elif c == "-":
        a = int(a) - int(b)
        display.set(a)
      elif c == "×":
        a = int(a) * int(b)
        display.set(a)
      else:
        try:
          a = float(a) / float(b)
          a = round(a, 5)
          display.set(a)
        except ZeroDivisionError:
          display.set("Ошибка")
  except ValueError:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = float(a) + float(b)
        display.set(a)
      elif c == "-":
        a = float(a) - float(b)
        display.set(a)
      elif c == "×":
        a = float(a) * float(b)
        a = round(a, 5)
        display.set(a)
  b = ""
  c = "-"

# Работа кнопки ×
def clickMultiplication(event):
  global c
  global a
  global b
  multiplication.config(bg="#1CE8FF")
  division.config(bg=colours[index])
  plus.config(bg=colours[index])
  minus.config(bg=colours[index])
  try:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = int(a) + int(b)
        display.set(a)
      elif c == "-":
        a = int(a) - int(b)
        display.set(a)
      elif c == "×":
        a = int(a) * int(b)
        display.set(a)
      else:
        try:
          a = float(a) / float(b)
          a = round(a, 5)
          display.set(a)
        except ZeroDivisionError:
          display.set("Ошибка")
  except ValueError:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = float(a) + float(b)
        display.set(a)
      elif c == "-":
        a = float(a) - float(b)
        display.set(a)
      elif c == "×":
        a = float(a) * float(b)
        a = round(a, 5)
        display.set(a)
  b = ""
  c = "×"

# Работа кнопки ÷
def clickDivision(event):
  global c
  global lst
  global a
  global b
  division.config(bg="#1CE8FF")
  multiplication.config(bg=colours[index])
  plus.config(bg=colours[index])
  minus.config(bg=colours[index])
  try:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = int(a) + int(b)
        display.set(a)
      elif c == "-":
        a = int(a) - int(b)
        display.set(a)
      elif c == "×":
        a = int(a) * int(b)
        display.set(a)
      else:
        try:
          a = float(a) / float(b)
          a = round(a, 5)
          display.set(a)
        except ZeroDivisionError:
          display.set("Ошибка")
  except ValueError:
    if b == "":
      a = display.get()
    elif b != "":
      if c == "+":
        a = float(a) + float(b)
        display.set(a)
      elif c == "-":
        a = float(a) - float(b)
        display.set(a)
      elif c == "×":
        a = float(a) * float(b)
        a = round(a, 5)
        display.set(a)
  b = ""
  c = "÷"

# Работа кнопки =
def clickEqually(event):
  global a
  global b
  global c
  global lst
  equally.config(bg=colours[index])
  try:
    if c == "+":
      try:
        r = int(a) + int(b)
        result.config(text=display.set(r))
      except ValueError:
        r = float(a) + float(b)
        r = round(r, 5)
        result.config(text=display.set(r))
    elif c == "×":
      try:
        r = int(a) * int(b)
        result.config(text=display.set(r))
      except ValueError:
        r = float(a) * float(b)
        r = round(r, 5)
        result.config(text=display.set(r))
    elif c == "÷":
      try:
        r = float(a) / float(b)
        if len(str(r)) > 14:
          r = round(r, 5)
        result.config(text=display.set(r))
      except ZeroDivisionError:
        display.set("Ошибка")
    else:
      try:
        r = int(a) - int(b)
        result.config(text=display.set(r))
      except ValueError:
        r = float(a) - float(b)
        r = round(r, 5)
        result.config(text=display.set(r))
  except ValueError:
    r = display.get()
    display.set(r)

# Работа кнопки .
def clickPoint(event):
  global lst
  global a
  global b
  lst = []
  for i in str(display.get()):
    lst.append(i)
  if display.get() == "Ошибка":
    point["state"] == DISABLED
  elif len(lst) >= 14:
    point["state"] == DISABLED
  elif display.get() == "" or display.get() == "-":
    point["state"] == DISABLED
  else:
    replay = lst.count(".")
    if replay == 0:
      r = display.get()
      r += "."
      result.config(display.set(r))
      if multiplication.cget("bg") == "#1CE8FF" or minus.cget("bg") == "#1CE8FF" or division.cget("bg") == "#1CE8FF" or plus.cget("bg") == "#1CE8FF":
        b = display.get()
        plus.config(bg=colours[col])
        minus.config(bg=colours[col])
        multiplication.config(bg=colours[col])
        division.config(bg=colours[col])
      else:
        point["state"] == DISABLED

# Работа кнопки backspace
def backspace(event):
  global b
  global a
  r = display.get()
  if r == "Ошибка":
    back["state"] == DISABLED
  elif r == "":
    back["state"] == DISABLED
  else:
    if c == "+" or c == "-" or c == "×" or c == "÷":
      b = r[:-1] # С помощью этой строки происходит удаление последнего элемента
      display.set(b)
    else:
      a = r[:-1] # С помощью этой строки происходит удаление последнего элемента
      display.set(a)

# С помощью сочетания клавиш можно будет менять цветовую гамму
def colour(event):
  global col
  global colours
  global index
  index += 1
  col = open("index.txt", "w") # Открытие файла для изменения в нём индекса, для сохранения цвета
  if event.keycode == 1099 or event.keycode == 115 or event.keycode == 1067 or event.keycode == 83: # Проверка на клавишу(заглавные или строчные буквы в двух раскладках)

    try:
      # Изменение фона и активного фона на следующий цвет в списке
      division.config(bg=colours[index], activebackground=colours[index])
      multiplication.config(bg=colours[index], activebackground=colours[index])
      minus.config(bg=colours[index], activebackground=colours[index])
      plus.config(bg=colours[index], activebackground=colours[index])
      equally.config(bg=colours[index], activebackground=colours[index])
    except IndexError: # Если индекс стал больше, чем цветов, индекс становится нулём
      index = 0
      division.config(bg=colours[index], activebackground=colours[index])
      multiplication.config(bg=colours[index], activebackground=colours[index])
      minus.config(bg=colours[index], activebackground=colours[index])
      plus.config(bg=colours[index], activebackground=colours[index])
      equally.config(bg=colours[index], activebackground=colours[index])
  col.write(str(index)) # Изменение индекса цвета в файле
  col.close() # Закрытие файла


lst = []
a = "" # В эту переменную записывается первое значение
b = "" # В эту переменную записывается второе значение
c = "" # В эту переменную записывается знак действия
col = open("index.txt", "r") # В этой переменной открывается файл с индексом цвета из списка
index = int(col.read()) # В эту переменную записывается индекс цвета для кнопок
colours = ["#05FF05", "#FFFB23", "#FF2DEA", "#FF0217", "#FF9D00", "#A435FF", "#FFB08E", "#09EFA2"] # В этом списке размещены цвета кнопок
#FFB5F7

root.config(bg="Black") # Меняю цвет фона на чёрный
display = StringVar() # Для получения значений с метки
txt = Frame(root) # В этом фрейме будет выводиться результат

result = Label(txt, bg="Black", fg="White", font="Arial 40", textvariable=display) # В этой метке будут выводиться числа и результат

buttons = Frame(root, width=414, height=560, bg="black") # В этом фрейме находятся кнопки
clear = Button(buttons, text="C", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Сброс
negative = Button(buttons, text="+/-", font="Arial 40", bg="#FFFFFF", fg="Black", activebackground="#FFFFFF") # Отрицательное число
percent = Button(buttons, text="%", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Процент
division = Button(buttons, text="÷", font="Arial 40", bg=colours[index], activebackground=colours[index], fg="Black") # Деление
seven = Button(buttons, text="7", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Семь
eight= Button(buttons, text="8", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Восемь
nine = Button(buttons, text="9", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Девять
multiplication = Button(buttons, text="×", font="Arial 40", bg=colours[index], activebackground=colours[index], fg="Black") # Умножение
four = Button(buttons, text="4", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Четыре
five = Button(buttons, text="5", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Пять
six = Button(buttons, text="6", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Шесть
minus = Button(buttons, text="-", font="Arial 40", bg=colours[index], activebackground=colours[index], fg="Black") # Минус
one = Button(buttons, text="1", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Один
two = Button(buttons, text="2", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Два
three = Button(buttons, text="3", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Три
plus = Button(buttons, text="+", font="Arial 40", bg=colours[index], activebackground=colours[index], fg="Black") # Плюс
zero = Button(buttons, text="0", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Ноль
point = Button(buttons, text=".", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Точка
square = Button(buttons, text="√", font="Arial 40", bg="#FFFFFF", activebackground="#FFFFFF", fg="Black") # Квадратный корень
equally = Button(buttons, text="=", font="Arial 40", bg=colours[index], activebackground=colours[index], fg="Black") # Равно
back = Button(root, bg="Black", bd=0, activebackground="Black", text="BACKSPACE", fg="Black", font="Arial 40") # Backspace
button = Button(root) # Невидимая кнопка изменения цвета

col.close() # Здесь закрытие файла для дальнейших изменений

result.pack() # Вывод метки для результата
back.place(relx=0, rely=0, width=414, height=100) # Кнопка backspace будет невидимой
txt.place(relx=1, rely=0.23, anchor="se") # Вывод фрейма для метки

buttons.place(relx=0.5, rely=0.23, anchor="n") # Вывод фрейма для кнопок

# Первая стока
clear.place(relx=0, rely=0, width=103.5, height=103.5)
negative.place(relx=0.25, rely=0, width=103.5, height=103.5)
percent.place(relx=0.503, rely=0, width=103.5, height=103.5)
division.place(relx=0.753, rely=0, width=103.5, height=103.5)

# Вторая строка
seven.place(relx=0, rely=0.186, width=103.5, height=103.5)
eight.place(relx=0.250, rely=0.186, width=103.5, height=103.5)
nine.place(relx=0.503, rely=0.186, width=103.5, height=103.5)
multiplication.place(relx=0.753, rely=0.186, width=103.5, height=103.5)

# Третья строка
four.place(relx=0, rely=0.372, width=103.5, height=103.5)
five.place(relx=0.250, rely=0.372, width=103.5, height=103.5)
six.place(relx=0.503, rely=0.372, width=103.5, height=103.5)
minus.place(relx=0.753, rely=0.372, width=103.5, height=103.5)

# Четвёртая строка
one.place(relx=0, rely=0.558, width=103.5, height=103.5)
two.place(relx=0.250, rely=0.558, width=103.5, height=103.5)
three.place(relx=0.503, rely=0.558, width=103.5, height=103.5)
plus.place(relx=0.753, rely=0.558, width=103.5, height=103.5)

# Пятая строка
zero.place(relx=0, rely=0.743, width=103.5, height=103.5)
point.place(relx=0.250, rely=0.743, width=103.5, height=103.5)
square.place(relx=0.503, rely=0.743, width=103.5, height=103.5)
equally.place(relx=0.753, rely=0.743, width=103.5, height=103.5)


clear.bind("<Button-1>", clickC) # Кнопка сброса
clear.bind_all("<space>", clickC) # Сброс при испольтзовании пробела
zero.bind("<Button-1>", clickZero) # Кнопка 0
zero.bind_all("0", clickZero) # Клавиша 0
one.bind("<Button-1>", clickOne) # Кнопка 1
one.bind_all("1", clickOne) # Клавиша 1
two.bind("<Button-1>", clickTwo) # Кнопка 2
two.bind_all("2", clickTwo) # Клавиша 2
three.bind("<Button-1>", clickThree) # Кнопка 3
three.bind_all("3", clickThree) # Клавиша 3
four.bind("<Button-1>", clickFour) # Кнопка 4
four.bind_all("4", clickFour) # Клавиша 4
five.bind("<Button-1>", clickFive) # Кнопка 5
five.bind_all("5", clickFive) # Клавиша 5
six.bind("<Button-1>", clickSix) # Кнопка 6
six.bind_all("6", clickSix) # Клавиша 6
seven.bind("<Button-1>", clickSeven) # Кнопка 7
seven.bind_all("7", clickSeven) # Клавиша 7
eight.bind("<Button-1>", clickEight) # Кнопка 8
eight.bind_all("8", clickEight) # Клавиша 8
nine.bind("<Button-1>", clickNine) # Кнопка 9
nine.bind_all("9", clickNine) # Клавиша 9
percent.bind("<Button-1>", clickPercent) # Кнопка %
percent.bind_all("<Shift-%>", clickPercent) # Клавиша %
negative.bind("<Button-1>", clickNegative) # Кнопка +/-
square.bind("<Button-1>", clickSquare) # Кнопка √
plus.bind("<Button-1>", clickPlus) # Кнопка +
plus.bind_all("<Shift-+>", clickPlus) # Клавиша +
minus.bind("<Button-1>", clickMinus) # Кнопка -
minus.bind_all("-", clickMinus) # Клавиша -
multiplication.bind("<Button-1>", clickMultiplication) # Кнопка ×
multiplication.bind_all("<Shift-*>", clickMultiplication) # Клавиша ×
division.bind("<Button-1>", clickDivision) # Кнопка ÷
division.bind_all("</>", clickDivision) # Клавиша ÷
division.bind_all("<Shift-,>", clickDivision) # Клавиша ÷
equally.bind("<Button-1>", clickEqually) # Кнопка =
equally.bind_all("<Return>", clickEqually) # Клавиша =
equally.bind_all("<=>", clickEqually) # Кнопка = на цифровой клавиатуре
point.bind("<Button-1>", clickPoint) # Кнопка .
point.bind_all(".", clickPoint) # Клавиша .
back.bind_all("<BackSpace>", backspace) # Клавиша backspace
back.bind("<Button-1>", backspace) # Кнопка backspace
button.bind_all("<Control-KeyPress>", colour) # Изменение цвета

root.mainloop()
