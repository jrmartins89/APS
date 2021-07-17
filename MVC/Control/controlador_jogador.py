from MVC.Model.jogador_humano import JogadorHumano
from MVC.View.tela_login_jogador import TelaLoginJogador
from MVC.View.tela_cadastro_jogador import TelaCadastroJogador


class ControladorJogador:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cadastro = TelaCadastroJogador(self)
        self.__tela_login = TelaLoginJogador(self)
        self.__usuarios = []

    def abre_tela_login(self):
        button, values = self.__tela_login.open_menu()

        if button == 'Adicionar usuário':
            self.incluir_usuario(values['nome'], values['email'], values['id_usuario'])
        elif button == 'Remover usuário':
            self.excluir_usuario(values['nome_exclusao'])
        elif button == 'Listar usuários':
            self.listar_usuarios()
        elif button == 'Voltar ao menu principal':
            self.__controlador_biblioteca.abre_tela()

    def incluir_usuario(self, nome: str, email: str, id_usuario: str):
        try:
            for usuario in self.__usuarios:
              if usuario.id_usuario == id_usuario:
                raise Exception()
        except Exception:
            self.__tela.show_message("Usuários", "Usuário já existente no sistema")
        else:
            self.__usuarios.append(Usuario(nome, email, id_usuario))
            self.__tela.show_message("CADASTRO DE USUÁRIOS", "Usuário cadastrado com sucesso!")

# essa funçao percorre toda a lista de usuário para localizar o registro com o id_usuario que foi
# passado como parametro. quando acha esse registro, o objeto é removido

    def excluir_usuario(self, nome: str):
        if isinstance(nome, str):
            for usuario in self.__usuarios:
                if usuario.nome == nome:
                    self.__usuarios.remove(usuario)
                    self.__tela.show_message("Usuários", "Usuário excluído com sucesso!")

    def listar_usuarios(self):
        lista_usuarios = ''
        for usuario in self.__usuarios:
            lista_usuarios += "Nome: " + usuario.nome + '\n' + "Email: " + usuario.email + '\n' + "ID Usuário: " +\
                                usuario.id_usuario + '\n'
            self.__tela.show_message('Usuários', lista_usuarios)

# ção do método próprio da tela para exibição da lista ao invés do print. O método recebe uma lista de strings.
# Ela incia vazia e a cada iteração é adicionado o usuario.nome
# percorrer a lista e retornar o objeto do usuario cujo parametro id_usuario seja igual ao parametro
# id_usuario da funcao de listagem
