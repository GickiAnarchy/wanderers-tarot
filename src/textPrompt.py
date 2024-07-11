from src.geminiRequest import gemrequest,geminiWT

models = ["gemini-1.5-flash-latest", "gemini-1.5-pro-latest", "gemini-1.0-pro"]

def getGemReading(reading):
    txtmodel = models[0]
    cds = ""
    i = 0
    cds_list = reading.getCards()
    for d in cds_list:
        i += 1
        cds += f"{str(i)}:{d}\n"
    result = geminiWT(f"Read my tarot from the following question and cards:\n\tQuestion:{reading.question}\n\tCards:{cds}")
    if result[0]:
        return result[1]
    else:
        for t in range(3):
            print("********************************")
        print("The prompt was blocked! See below for reason:")
        print(result[1])