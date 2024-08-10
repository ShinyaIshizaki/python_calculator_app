import arrr
from pyscript import document

# 
def calculate():
  
  # 入力値を取得する
  number_1 = document.querySelector("#number_1")
  number_2 = document.querySelector("#number_2")

  # 選択された値を取得する
  select = document.getElementedById("selected-compute")
  how_to_compute = select.options[select.selectedIndex].value
  
  # 計算結果の変数を定義する
  answer = document.querySelector("#answer")

  # 選択された項目により、計算方法を条件分岐する
  print("how_to_compute: " + how_to_compute)
  match how_to_compute:
    case "+":
      add(number_1, number_2, answer)
    case "-":
      minus(number_1, number_2, answer)
    case "*":
      multiple(number_1, number_2, answer)
    case "/":
      devide(number_1, number_2, answer)
    case _:
      print("ERORR : Out of range")


# add
def add(num_1, num_2, ans):
  ans.innerText = int(num_1) + int(num_2)


# minus
def minus(num_1, num_2, ans):
  ans.innerText = int(num_1) - int(num_2)


# multiple
def multiple(num_1, num_2, ans):
  ans.innerText = int(num_1) * int(num_2)


# devide
def devide(num_1, num_2, ans):
  ans.innerText = int(num_1) / int(num_2)