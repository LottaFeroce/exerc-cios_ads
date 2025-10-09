class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"APROVADO (média = {media:.2f})"
        elif media >= 5:
            return f"EXAME (média = {media:.2f})"
        else:
            return f"REPROVADO (média = {media:.2f})"

aluno1 = Aluno("Karlmarcos", "Matricula", [8.0, 7.0, 9.0, 6.0])

print(aluno1.nome)
print(aluno1.calcular_media())
print(aluno1.mostrar_situacao())