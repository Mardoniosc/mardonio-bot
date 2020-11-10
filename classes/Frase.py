class Frase:
  def __init__(self, frase, livro, autor):
      self.frase = frase
      self.livro = livro
      self.autor = autor

  def mensagemCompleta(self):
      return self.frase + "\nLivro: " + self.livro + "\nAuthor: " + self.autor
