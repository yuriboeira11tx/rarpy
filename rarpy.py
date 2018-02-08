#coding: utf-8
# Developer: Derxs
# Version: 1.0
import rarfile, sys, time

arquivo = sys.argv[1]
wordlist = open(sys.argv[2])

def descompacta():
	with rarfile.RarFile(arquivo) as desc:
		for senha in wordlist:
			try:
				desc.extractall(path='.', members=desc.namelist(), pwd=senha.strip())
				print('\n\033[01;32m[*] SENHA ENCONTRADA:\033[0m \033[01;35m{}\033[0m'.format(senha), end='')
				
				for informacao in desc.infolist():
					print('\033[01;34m[*]\033[0m Arquivo descompactado!\n\033[01;34m[*]\033[0m Nome: \033[01;35m{}\033[0m\n\033[01;34m[*]\033[0m Tamanho: \033[01;35m{} bytes\033[0m\n'.format(informacao.filename, informacao.file_size))
				
				exit(0)
			except rarfile.RarCRCError:
				print('\033[01;31m[!]\033[0m Testando senha: {}'.format(senha), end='')
				
def verifica():
	if rarfile.is_rarfile(arquivo):
		descompacta()
	else:
		print('\033[01;31m[!]\033[0m Arquivo não é .rar')

def main():
	print('''\033[01;35m
__________    _____ ____________________        
\______   \  /  _  \\______   \______   \___.__.
 |       _/ /  /_\  \|       _/|     ___<   |  |
 |    |   \/    |    \    |   \|    |    \___  |
 |____|_  /\____|__  /____|_  /|____|    / ____|
        \/         \/       \/           \/       by \033[01;31mDerxs\033[0m v1.0
	''')
	time.sleep(2)
	verifica()
	descompacta()

try:
	main()
except KeyboardInterrupt:
	print('\n\033[01;31m[!]\033[0m Você escolheu sair!')
