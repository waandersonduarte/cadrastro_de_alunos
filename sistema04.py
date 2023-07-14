import sqlite3

# Função para criar a tabela de alunos no banco de dados


def criar_tabela_alunos():
    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alunos
                 (nome TEXT, idade INTEGER, genero TEXT, curso TEXT)''')
    conn.commit()
    conn.close()

# Função para cadastrar um novo aluno


def cadastrar_aluno():
    nome = input('Nome do aluno: ')
    while nome == "":
        print('O nome é obrigatório.')
        nome = input('Nome do aluno: ')

    idade = None

    while idade is None or idade <= 0:
        idade_str = input('Idade: ')
        if idade_str:
            try:
                idade = int(idade_str)
                if idade <= 0:
                    print('A idade não pode ser negativa.')
            except ValueError:
                print('A idade deve ser um valor inteiro.')
        else:
            print('A idade é obrigatória.')
            continue

    genero = input('Gênero: ')
    curso = input('Curso: ')

    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('INSERT INTO alunos VALUES (?, ?, ?, ?)',
              (nome, idade, genero, curso))
    conn.commit()
    conn.close()

    print('Aluno cadastrado com sucesso!')

# Função para exibir a lista de alunos cadastrados


def exibir_alunos():
    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM alunos')
    alunos = c.fetchall()
    conn.close()

    if alunos:
        for aluno in alunos:
            print('Nome:', aluno[0])
            print('Idade:', aluno[1])
            print('Gênero:', aluno[2])
            print('Curso:', aluno[3])
            print('-----------------------')
    else:
        print('Não há alunos cadastrados.')

# Função para editar os dados de um aluno


def editar_aluno():
    nome_busca = input('Digite o nome do aluno que deseja editar: ')

    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM alunos WHERE nome=?', (nome_busca,))
    aluno = c.fetchone()

    if aluno:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        genero = input('Gênero: ')
        curso = input('Curso: ')

        c.execute('UPDATE alunos SET nome=?, idade=?, genero=?, curso=? WHERE nome=?',
                  (nome, idade, genero, curso, nome_busca))
        conn.commit()
        conn.close()

        print('Dados do aluno atualizados com sucesso!')
    else:
        print('Aluno não encontrado.')

# Função para remover um aluno da lista


def remover_aluno():
    nome_busca = input('Digite o nome do aluno que deseja remover: ')

    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM alunos WHERE nome=?', (nome_busca,))
    aluno = c.fetchone()

    if aluno:
        c.execute('DELETE FROM alunos WHERE nome=?', (nome_busca,))
        conn.commit()
        conn.close()

        print('Aluno removido com sucesso!')
    else:
        print('Aluno não encontrado.')

# Função para buscar um aluno pelo nome


def buscar_aluno():
    nome_busca = input('Digite o nome do aluno que deseja buscar: ')

    conn = sqlite3.connect('alunos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM alunos WHERE nome=?', (nome_busca,))
    aluno = c.fetchone()
    conn.close()

    if aluno:
        print('Nome:', aluno[0])
        print('Idade:', aluno[1])
        print('Gênero:', aluno[2])
        print('Curso:', aluno[3])
    else:
        print('Aluno não encontrado.')

# Função para exibir o menu e interagir com as funcionalidades


def exibir_menu():
    while True:
        print('---- Sistema de Cadastro de Alunos ----')
        print('1. Cadastrar novo aluno')
        print('2. Exibir lista de alunos')
        print('3. Editar dados de um aluno')
        print('4. Remover aluno')
        print('5. Buscar aluno')
        print('0. Sair do sistema')

        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            editar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            buscar_aluno()
        elif opcao == "0":
            break
        else:
            print('Opção inválida. Tente novamente.')

# Função principal para executar o programa


def main():
    criar_tabela_alunos()
    exibir_menu()


# Executar o programa
if __name__ == "__main__":
    main()
