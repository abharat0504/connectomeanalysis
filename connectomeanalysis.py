with open("connectomeanalysis/HighRes.obj") as connectomeanalysis:
    file_open = False
    for line in connectomeanalysis:
        if line[0] == "g":
            if file_open == True:
                file.close()
            file = open(f"connectomeanalysis/{line[1:].strip()}.obj", "w")
            file.write(line)
        else:
            file.write(line)
                