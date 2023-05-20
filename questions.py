

questions = [
    {
        "text": "Pergunta",
        "altA": { "text": "Alternativa A", "label": False, "exp": "Explicação" },
        "altB": { "text": "Alternativa B", "label": False, "exp": "Explicação" },
        "altC": { "text": "Alternativa C", "label": True, "exp": "Explicação" },
        "altD": { "text": "Alternativa D", "label": False, "exp": "Explicação" },
        "answered": None
    },
]

#questions.append(questions[0].copy()) # isto é um teste

class Question:
    def __init__(self, item):
        self.index = questions.index(item)
        self.text = item['text']
        self.altA = item['altA']
        self.altB = item['altB']
        self.altC = item['altC']
        self.altD = item['altD']
        self.answered = item['answered']

