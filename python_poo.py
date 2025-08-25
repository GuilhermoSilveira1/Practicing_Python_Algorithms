# 🎓 Projeto: Sistema de Cadastro Escolar
# 📘 Classe: Aluno
# Atributos:
# nome: str
# ra: str (Registro Acadêmico)
# ano: int
# turma: Turma (associação com a classe Turma)
# Métodos:
# apresentar(): retorna uma string com os dados do aluno
# alterar_turma(nova_turma): muda a turma do aluno
class Aluno:
    def __init__(self, nome, ra, ano, turma):
        self._nome = nome
        self._ra = ra
        self._ano = ano
        self._turma = turma

    def apresentar(self):
        print(f'Nome: {self._nome}, RA: {self._ra}, Ano: {self._ano}, Turma: {self._turma}')

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, nova_turma):
        self._turma = nova_turma

# 🏫 Classe: Turma
# Atributos:
# codigo: str (ex: "1A", "2B")
# ano: int
# alunos: list[Aluno]
# disciplinas: list[Disciplina]
# Métodos:
# adicionar_aluno(aluno: Aluno)
# listar_alunos()
# adicionar_disciplina(disciplina: Disciplina)
# listar_disciplinas()
class Turma:
    def __init__(self, codigo, ano):
        self._codigo = codigo
        self._ano = ano
        self._alunos = []
        self._disciplinas = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def ano(self):
        return self._ano

    @property
    def alunos(self):
        return self._alunos

    @property
    def disciplinas(self):
        return self._disciplinas

    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self._alunos:
            aluno.apresentar()

    def adicionar_disciplina(self, disciplina):
        self._disciplinas.append(disciplina)

    def listar_disciplinas(self):
        for d in self._disciplinas:
            print(f'Disciplina: {d.nome}, Código: {d.codigo}, Professor: {d.professor}')

# 📚 Classe: Disciplina
# Atributos:
# nome: str
# codigo: str (ex: "MAT101")
# professor: str
# Métodos:
# detalhes(): retorna uma string com os dados da disciplina
class Disciplina:
    def __init__(self, nome, codigo, professor):
        self._nome = nome
        self._codigo = codigo
        self._professor = professor
    
    @property
    def nome(self):
        return self._nome
    
    def detalhes(self):
        print(f'Nome: {self._nome}, Código: {self._codigo}, Professor: {self._professor}')



# Implementação
matematica = Disciplina("Matemática", "MAT101", "Prof. Marcia")
guilhermo = Aluno("Guilhermo", "5469", "3°", "A1")
A1 = Turma("A1", "7°")
A1.adicionar_disciplina(matematica)
A1.adicionar_aluno(guilhermo)