with open ("C:/Users/student/Desktop/kr/Extinct_languages.tsv", encoding="utf-8") as f:
    for line in f:
        if len(line) > 35:
            print(line)
