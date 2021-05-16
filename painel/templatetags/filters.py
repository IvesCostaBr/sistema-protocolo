from django import template

#crio uma variavel template que vai ser um objeto do tipo template
# e em seguida vamos registrar nosso templates nela 
# através do metodo register

register = template.Library()

