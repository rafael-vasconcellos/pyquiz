

questions = [
    {
        "text": "Qual é o maior animal terrestre?",
        "altA": { "text": "Elefante", "label": True, "exp": "Explicação" },
        "altB": { "text": "Girafa", "label": False, "exp": "Explicação" },
        "altC": { "text": "Rinoceronte", "label": False, "exp": "Explicação" },
        "altD": { "text": "Hipopótamo", "label": False, "exp": "Explicação" },
        "answered": None
    },

    {
        "text": "Qual é o maior animal marinho?",
        "altA": { "text": "Tubarão-baleia", "label": False, "exp": "Explicação" },
        "altB": { "text": "Baleia-azul", "label": True, "exp": "Explicação" },
        "altC": { "text": "Polvo-gigante", "label": False, "exp": "Explicação" },
        "altD": { "text": "Golfinho", "label": False, "exp": "Explicação" },
        "answered": None
    },

    {
        "text": "Quantas pernas um inseto possui?",
        "altA": { "text": "2", "label": False, "exp": "Explicação" },
        "altB": { "text": "4", "label": False, "exp": "Explicação" },
        "altC": { "text": "6", "label": True, "exp": "Explicação" },
        "altD": { "text": "8", "label": False, "exp": "Explicação" },
        "answered": None
    },

    {
        "text": "Qual é o maior felino do mundo?",
        "altA": { "text": "Leão", "label": False, "exp": "Explicação" },
        "altB": { "text": "Tigre", "label": True, "exp": "Explicação" },
        "altC": { "text": "Onça-pintada", "label": False, "exp": "Explicação" },
        "altD": { "text": "Leopardo", "label": False, "exp": "Explicação" },
        "answered": None
    },
]

class Question:
    def __init__(self, item):
        self.index = questions.index(item)
        self.text = item['text']
        self.altA = item['altA']
        self.altB = item['altB']
        self.altC = item['altC']
        self.altD = item['altD']
        self.answered = item['answered']





"""
    {
        "text": "Pergunta",
        "altA": { "text": "Alternativa A", "label": False, "exp": "Explicação" },
        "altB": { "text": "Alternativa B", "label": False, "exp": "Explicação" },
        "altC": { "text": "Alternativa C", "label": True, "exp": "Explicação" },
        "altD": { "text": "Alternativa D", "label": False, "exp": "Explicação" },
        "answered": None
    },

questions.append(questions[0].copy()) # isto é um teste

"""


"""{
        "text": """""",

        "altA": { 
            "text": "Elefante", "label": False, 
            "exp": "Explicação" 
        },

        "altB": { 
            "text": "Girafa", "label": False, 
            "exp": "Explicação"
        },

        "altC": { 
            "text": "Rinoceronte", "label": False, 
            "exp": "Explicação"
        },
    
        "altD": { 
            "text": "Hipopótamo", "label": False, 
            "exp": "Explicação"
        },

        "answered": None
    },"""