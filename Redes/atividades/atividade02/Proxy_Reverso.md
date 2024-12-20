# Proxy Reverso

## O que é o proxy reverso?
O proxy reverso é um intermediário entre cliente e um ou mais servidores web, que recebe as solicitações do cliente e envia para o servidor. Ele também pode retornar uma resposta do servidor para a solicitação do cliente. Ele é chamado de "reverso" por fazer o trabalho contrário do proxy, onde a solicitação sai do cliente para a internet.

## Quais as suas funcionalidades?
- Proteger o servidor
- Balanceamento de Carga
- Compressão de Dados
- Controle de Acesso
- Monitoramento e Logs  

Em resumo, o proxy reverso oferece uma série de benefícios essenciais para melhorar a escalabilidade, segurança e desempenho de sistemas distribuídos.

## Como implementar?  
Para a nossa implementação vamos utilizar o proxy reverso **Nginx**.
### Passo 1 - Instalação do Nginx:
1. Garanta que sua máquina esteja atualizada.

        sudo apt update
        sudo apt upgrade

2. Use o gerenciador de arquivos da sua máquina para instala o Nginx.

        sudo apt install nginx  

### Passo 2 - Configuração do Proxy Reverso:
1. Crie ou edite o arquivo de configuração para o seu proxy reverso.  

        sudo nano /etc/nginx/sites-available/nome_arquivo.conf

2. Adicione o seguinte conteúdo dentro do arquivo.conf.

        server {
                listen 80;
                server_name seu_dominio.com;

                location / {
                        proxy_pass http://IP_DO_SERVIDOR_DESTINO;
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
                }
        }
   Substitua **IP_DO_SERVIDOR_DESTINO** pelo endereço IP do servidor ou pelo hostname para onde deseja encaminhar as requisições.

### Passo 3 - Ativar configurações:
1. Crie um link simbólico para ativar o site.

        sudo ln -s /etc/nginx/sites-available/proxy_reverso /etc/nginx/sites-enabled/

### Passo 4 - Teste de configuração:
1. Garanta que não há erro de sintaxe nas configurações do nginx.

        sudo nginx -t

### Passo 5 - Salvar as alterações:
1. Recarregue o arquivo de configuração para que as alterações sejam efetuadas.

        sudo systemctl reload nginx

# Autores
João Marcos de Azevedo Dantas  
Ruan Allyson de Araújo Felix

# Referencias
KingHost, R. (2024, dezembro 7). Proxy Reverso — O Que É, Como Funciona E Quais São Suas Vantagens? KingHost. https://king.host/blog/tutoriais/proxy-reverso-o-que-e-e-como-usar/  

Configuração de Proxy Reverso com Nginx no Debian 12. ([s.d.]). RosneRTech. Recuperado 19 de dezembro de 2024, de https://blog.rosnertech.com.br/arquivos/1329