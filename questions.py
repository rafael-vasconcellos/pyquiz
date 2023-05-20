

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

questions.append(questions[0].copy()) # isto é um teste

class Question:
    def __init__(self, index):
        self.index = questions.index(index)
        self.text = index['text']
        self.altA = index['altA']
        self.altB = index['altB']
        self.altC = index['altC']
        self.altD = index['altD']
        self.answered = index['answered']

