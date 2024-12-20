# DNS - Sistema de nome de domínio (Domain Name System)
## O que é DNS?
O DNS não é nada mais que um sistema de tradução de IP, que permite que os usuários acessem os sites, apenas digitando nomes como www.vendas.com em vez de decorar sequências de números.

## Estrutura do DNS / Tipos de servidores DNS:
- Servidores DNS Recursivos: Recebem consultas de clientes e buscam as informações necessárias em outros servidores DNS. Eles atuam como intermediários entre o cliente e os servidores autoritativos.

- Servidores DNS Autoritativos: Contêm registros DNS para um domínio específico e respondem a consultas diretamente. Eles são responsáveis por fornecer informações sobre os domínios que gerenciam.

- Servidores de Cache: Armazena temporariamente as respostas às consultas DNS para acelerar o processo de resolução de nomes, evitando consultas repetidas para o mesmo domínio.

## Funções do DNS:
- Tradução dos IPS, para nomes
- Gerenciamento de registros
- Distribuição do tráfego entre servidores  

# DNS local
O DNS local é uma forma de implementação do sistema DNS dentro de uma rede específica, onde é utilizado em uma rede interna. Ele permite que dispositivos na rede resolvam nomes de domínio locais, como um servidor local ou sem a necessidade de consultar servidores DNS externos. Sendo útil em ambientes corporativos ou confinados onde as máquinas precisam se comunicar entre si.

## Aplicação de um DNS local
Para a nossa aplicação vamos installar um software de DNS. O software que iremops utilizar é o **BIND**.  

### Passo 1 - Instalação do BIND:
1. Atualize o sistema.

        sudo apt update 
        sudo apt upgrade

2. Use o gerenciador de arquivos da sua máquina para instalar o BIND.

        sudo apt install bind9 bind9utils bind9-doc 

### Passo 2 - Configurar o BIND:
A resolução de nomes converte nomes de sistemas no seu endereço IP e vice-versa. Assim, a configuração consiste, basicamente na criação de 2 zonas, uma (zone “home.lan”) que converte nomes em endereços IP e outra (zone “1.168.192.in-addr.arpa”) que converte endereços IP no respectivo nome de sistema. (3.1.3 Servidor DNS Local, [s.d.])  

1. Edite o arquivo de configuração principal.   
_O arquivo principal de configuração do BIND é o /etc/bind/named.conf.options_

        sudo nano /etc/bind/named.conf.options   
    Adicione ou modifique as seguintes linhas:.

        options {
            directory "/var/cache/bind";

            recursion yes;                  // Permitir requisições recursivas
            allow-recursion { localhost; }; // Permitir apenas localhost

            dnssec-validation auto;
            auth-nxdomain no;    # Conformidade com RFCs
            listen-on-v6 { any; }; // Ou { none; } para desabilitar IPv6
        };

2. Configurar zonas no arquivo /etc/bind/named.conf.local.

        sudo nano /etc/bind/named.conf.local

    Adicione o seguinte conteúdo. 

        zone "meudominio.local" {
            type master;
            file "/etc/bind/db.meudominio.local";
        };

3. Criar o arquivo de zona.  
Copie o arquivo anterior para criar sua nova zona.

        sudo cp /etc/bind/db.local /etc/bind/db.meudominio.local
    
    Edite o arquivo.
        
        sudo nano /etc/bind/db.meudominio.local

    Modifique as entradas conforme necessário.

        ;
        ; BIND data file for meudominio.local
        ;
        $TTL    604800
        @       IN      SOA     ns.meudominio.local. admin.meudominio.local. (
                                2         ; Serial
                            604800         ; Refresh
                            86400         ; Retry
                            2419200         ; Expire
                            604800 )       ; Negative Cache TTL
        ;
        @       IN      NS      ns.meudominio.local.
        ns      IN      A       SEU_IP_PRIVADO   ; IP do servidor DNS
        @       IN      A       SEU_IP_PRIVADO   ; IP do domínio
        www     IN      A       SEU_IP_PRIVADO   ; IP do www

### Passo 3 - Testar e Reiniciar o BIND:
1. Verifique as configurações.

        sudo named-checkconf

    Para verificar as zonas:

        sudo named-checkzone meudominio.local /etc/bind/db.meudominio.local

2. Reinicie o BIND. 
        
        sudo systemctl restart bind9

### Passo 4 - Configurar o Cliente para Usar o DNS Local:
1. Edite o arquivo /etc/resolv.conf.   
Adicione a seguinte linha:

        nameserver SEU_IP_PRIVADO 

### Passo 5 - Testar a Configuração:
Use o comando dig ou nslookup para verificar se o DNS está funcionando corretamente.

        dig @SEU_IP_PRIVADO meudominio.local

### Precauções:
- Certifique-se de que as portas necessárias (normalmente a 53) estão abertas no firewall.

- Essa configuração é básica e pode ser expandida conforme suas necessidades, incluindo a configuração de registros adicionais e segurança.

# Autores 
João Marcos de Azevedo Dantas  
Ruan Allyson de Araújo Felix

# Referências
3.1.3 Servidor DNS Local. ([s.d.]). Servido Debian. Recuperado 20 de dezembro de 2024, de https://servidordebian.org/pt/squeeze/intranet/dns/server

Habbema, H. (24DC, maio 26). Sistema de Nomes de Domínio. Medium. https://medium.com/@habbema/domain-name-system-b35994260c03

O que é : Local DNS. (2024, agosto 13). Napoleon. https://napoleon.com.br/glossario/o-que-e-local-dns/