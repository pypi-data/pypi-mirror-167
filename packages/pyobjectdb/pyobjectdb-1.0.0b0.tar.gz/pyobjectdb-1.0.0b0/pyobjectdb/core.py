import pickle


class TypeChangeOrientedObject:
    """
        Objeto base de Key, é uma forma mais simplificada de acessar ou definir
    keys em um banco de dados.
    """

    def __init__(self, **kwargs):
        self.__dict__ = kwargs.get('keys', {})

    def add(self, name: str | int, value):
        """   Adiciona uma nova key no banco de dados   """
        self.__dict__[name] = value

    def remove(self, name: str):
        """   Remove uma chave no banco de dados  """
        self.__dict__.pop(name)

    def convert(self):
        """  Converte essa chave em um <python dict>  """
        return self.__dict__


class StandardStorageBase(TypeChangeOrientedObject):
    """   Objeto base de armazenamento de dados   """
    def __init__(self, **kwargs):
        super().__init__(keys=kwargs.get('dictionary', {}))


class DatabaseCore:
    _storage = StandardStorageBase()

    def __init__(self, fp):
        """
            Esse é o núcleo do banco de dados.

        :param fp: nome do arquivo a ser conectado.
        """
        self.file = fp

    def connect(self):
        """  Responsável por se conectar ao arquive de banco de dados  """
        with open(self.file, 'rb') as file:
            self._storage = pickle.load(file)

    def query(self):
        """   Retorna o objeto de armazenamento para consultas   """

        return self._storage

    def submit(self, key, value):
        """   Adiciona uma key no banco de dados e após isso salva as alterações   """
        self._storage.add(key, value)
        self.commit()

    def remove(self, key):
        """
            Remove uma chave do banco de dados e salva a modificação automaticamente.

        :param key: chave a ser deletada.
        """
        self._storage.remove(key)
        self.commit()

    def commit(self):
        """   Salva modificações feitas no banco de dados   """

        with open(self.file, 'wb') as file:
            pickle.dump(self._storage, file)


def create(fp, keys: dict):
    """

        Função responsável por criar um banco de dados caso ele ainda não exista

    :param fp: nome do arquivo onde será armazenado todos os dados.
    :param keys: é um dict comum que será convertido em <KeyObjectType>
    """
    if not _file_exists(fp):

        # se o arquivo não existir ele será criado com o objeto de armazenamento base já integrado.
        with open(fp, 'wb') as file:
            pickle.dump(StandardStorageBase(dictionary=keys), file)
    else:

        # caso o arquivo exista, mas não há nada nele, será criado o objeto de armazenamento base nele.
        with open(fp, 'rb') as file:
            if file.read() == '':
                pickle.dump(StandardStorageBase(dictionary=keys), file)


def _file_exists(file):
    """
        Essa função verifica se um arquivo existe.

    :param file: qual arquivo que será verificado a existência.
    :return: True se existe, senão False
    """
    try:
        with open(file, 'r'):
            return True

    except FileNotFoundError:
        return False
