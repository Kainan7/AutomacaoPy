# AutomacaoPy
Este código Python utiliza a biblioteca PyAutoGUI para automatizar a simulação de interações em um sistema web, em um navegador Chrome, a fim de realizar algumas ações específicas, como entrar no sistema da 
empresa, fazer login, importar uma base de dados de produtos, cadastrar produtos e repetir o cadastro para todos os produtos da base de dados.

Aqui está uma breve descrição das etapas do código:

Importa as bibliotecas necessárias, como pyautogui para controle de mouse e teclado, e time para controle de tempo.
Define uma pausa padrão de 0.3 segundos entre os comandos do pyautogui para garantir que o sistema tenha tempo de responder adequadamente.

Passo 1: Abre o navegador Chrome usando atalhos do teclado e navega para o link fornecido.
Passo 2: Realiza o login no sistema da empresa fornecendo o email e a senha.
Passo 3: Importa uma base de dados de produtos a partir de um arquivo CSV chamado "produtos.csv" usando a biblioteca pandas.
Passo 4: Para cada linha na tabela de produtos, o código simula o preenchimento de campos, como código, marca, tipo, categoria, preço unitário, custo e observações, para cadastrar um produto. Ele também verifica
se a coluna de observações não está vazia antes de preenchê-la.

Ao final de cada cadastro de produto, o código pressiona a tecla "Enter" para enviar os dados.
O código utiliza pyautogui.scroll para rolar a página até o topo, se necessário.
Este código é uma automação útil para a entrada de dados em um sistema web, economizando tempo e minimizando erros manuais. Certifique-se de personalizá-lo com as informações de login e o caminho para o arquivo
CSV apropriado. Além disso, é importante ter cuidado ao automatizar interações em sistemas, pois isso pode violar os termos de uso do site ou aplicativo, e você deve garantir que tem permissão para fazer essa 
automação.
