def main():
  try:
    with open("data/prog285b.dat", 'r') as f:
      for line in f:
        ldata = line.split(" ")

except Exception as e:
  print("Error:", e)


if __name == "__main__":
  main()
