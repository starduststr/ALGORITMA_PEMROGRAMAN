def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def main():
    n = eval(input("Masukan angka : "))
    for x in range(1, n + 1):
        if is_prima(x):
            print(x)

main()