from produto import cadastrar_produto

def test_cadastro_valido():
  produto = cadastrar_produto('123', 'Notebook', 2500, 12)
  assert isinstance(produto, dict)
  
  nome = produto['Nome']
  assert isinstance(produto["Código"], str)
  assert nome.replace(' ', ' ').isalpha()
  assert isinstance(produto["Preço"], (int, float))
  assert isinstance(produto["Estoque"], int)

def test_cadastro_invalido():
  produto = cadastrar_produto('aaaa', '123', 'Acer', 'i5 14400f')
  
  codigo = produto['Código']
  nome = produto['Nome']
  assert isinstance(produto, dict)

  # Verifica se os tipos estão incorretos
  assert not codigo.isalpha()
  assert not nome.isdigit()
  assert not isinstance(produto["Preço"], (int, float))
  assert not isinstance(produto["Estoque"], int)