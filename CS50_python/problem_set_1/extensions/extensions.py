extention = input("user input: ").lower().strip()
if extention.endswith("gif"):
    print("image/gif")
elif extention.endswith("jpg"):
    print("image/jpeg")
elif extention.endswith("jpeg"):
    print("image/jpeg")
elif extention.endswith("png"):
    print("image/png")
elif extention.endswith("pdf"):
    print("application/pdf")
elif extention.endswith("txt"):
    print("text/"+extention.split(".")[0])
elif extention.endswith("zip"):
    print("application/zip")
elif extention.endswith("bin"):
    print("application/octet-stream")
elif extention.endswith(""):
    print("application/octet-stream")
else:
    print("unknown")




