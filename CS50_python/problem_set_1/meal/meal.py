def main():
    Time = input("Enter:")
    if 7<=convert(Time)<=8:
        print("breakfast time")
    elif 12<=convert(Time)<=13:
        print("lunch time")
    elif 18<=convert(Time)<=19:
        print("dinner time")


def convert(Time):
  hours, minutes = Time.split(":")
  hours = float(hours)
  minutes = float(minutes)
  sum = hours + (minutes/60)

  return sum



if __name__ == "__main__":
    main()