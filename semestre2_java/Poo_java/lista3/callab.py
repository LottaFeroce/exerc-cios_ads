from datetime import date
class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.nome = nome
        self.matricula = matricula

    def set_nome(self, novo_nome: str):
        self.nome = novo_nome
    def get_nome(self) -> str:
        return self.nome
    def visualizar_matricula(self):
        print(f"Matrícula do aluno {self.nome}: {self.matricula}")


class Disciplina:
    def __init__(self, nome: str, codigo: int, horario: date):
        self.nome = nome
        self.codigo = codigo
        self.horario = horario

    def horarios(self) -> date:
        return self.horario


class Nota:
    def __init__(self, valor: int, aluno: Aluno, disciplina: Disciplina):
        self.valor = valor
        self.aluno = aluno
        self.disciplina = disciplina



if __name__ == "__main__":
    aluno1 = Aluno("Lazaro", 123)
    disciplina1 = Disciplina("Ferragem", 101, date(2025, 10, 13))
    nota1 = Nota(95, aluno1, disciplina1)
    aluno1.visualizar_matricula()
    print(f"Disciplina: {nota1.disciplina.nome}, Nota: {nota1.valor}")
