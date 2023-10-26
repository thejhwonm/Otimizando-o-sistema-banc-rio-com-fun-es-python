# Otimizando-o-sistema-banc-rio-com-fun-es-python
Uma otimização do "sistema-de-banco-simples-em-python" onde foram adicionadas novas funções:

foi adicionado uma função para limpar a tela

foi adicionado funções para todas as operações do sistema antigo:
		sacar
		depositar
		extrato

foi adicionado novas funções:
	criar_usuario
	filtrar_usuario
	criar_conta
	listar_contas

Detalhes do que foi pedido:

objetivo geral
	Criar funções para todas as operações do sistema.
	Separar as funções existentes de saque, depósito e extrato em funções.
	Criar duas novas funções: 
		cadastrar usuário(cliente) e cadastrar conta bancária.
	
  Criar funções para as operações existentes:
		sacar, depositar, visualizar histórico(extrato).
		
  Criar duas novas funções:
		usuário(cliente do banco), conta corrente(vincular com o usuário).
		obs: fique a vontade para adicionar mais funções.
		exemplo: listar contas.
	
  Função saque:
		a função saque deve receber os argumentos apenas por nome (keyword only). 
		Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
		Sugestão de retorno: saldo e extrato.
		
  Função depósito:
		A função depósito deve receber os argumentos apenas por posição(positional only).
		Sugestão de argumentos: saldo, valor, extrato.
		Sugestão de retorno: saldo e extrato.
		
  Função extrato:
		A função extrato deve receber os argumentos por posição e nome (positional only e 
		keyword only).
		Argumentos posicionais: saldo.
		Argumentos nomeados: extrato.
    		
  Função usuário:
    		O programa deve armazenar os usuários em uma lista, um usuário é composto por:
    		nome, data de nascimento, cpf, endereço.
    		O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
    		Deve ser armazenado somente os números do CPF. 
    		Não podemos cadastrar 2 usuários com o mesmo CPF.
    		
  Função conta corrente:
    		O programa deve armazenar contas em uma lista, uma conta é composta por:
    		agência, número da conta e usuário.
    		O número da conta é sequencial, iniciando em 1.
    		O número da agência é fixo: "0001".
    		O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    		
  Dica:
    		Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do
    		CPF informado para cada usuário da lista.
