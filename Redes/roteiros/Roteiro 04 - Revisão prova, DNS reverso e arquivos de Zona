--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Instalação e configuração de servidores
Prof: Iuri Souza
IFRN Campus Caicó

Considerações sobre as configurações da etapa 04

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					Instalação do Flask
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Para consulta de erros, acesso o diretório /var/log
Verifique se existe um arquivo chamado flask_error.log (o nome antes de _error pode ser o nome do seu projeto).
Se existir, é nele que estará a indicação do problema que está acontecendo.

	Erros comuns: 

		Falta de permissão ao diretório do projeto
			Solução: conceder permissão, inclusive ao diretório pai, e atribuir o usuário www-data como dono e grupo da aplicação.

		Modulo não encontrado

			Solução: deve-se verificar se o flask está de fato instalado. Use o comando python3 -m flask --version
					Se o módulo não estiver instalado, proceda a instalação com: sudo apt install python3-flask


	Teste final: você deve ser capaz de acessar a sua aplicação flask diretamente pelo navegador através do IP da sua máquina e pela porta especificada no arquivo .conf do apache2.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			Exemplo de configuração de arquivo .conf do apache2 para uma aplicação em Flask rodando na porta 8000
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<VirtualHost *:8000>

        ServerName labredes.com

        WSGIDaemonProcess flaskapp user=www-data group=www-data threads=5 python-home=/var/www/flaskapp/venv
        WSGIScriptAlias / /var/www/flaskapp/flaskapp.wsgi


        <Directory /var/www/flaskapp>
                Require all granted
        </Directory>

        Alias /static /var/www/flaskapp/static

        <Directory /var/www/flaskapp/static/>
                Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/flaskapp_error.log
        CustomLog ${APACHE_LOG_DIR}/flaskapp_access.log combined

</VirtualHost>

OBS: a porta 8000 deve ser liberada no arquivo ports.conf
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			Exemplo de arquivo wsgi
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
import os

sys.path.insert(0, "/var/www/flaskapp")

from app import app as application


OBS: o arquivo deve apontar para onde está a aplicação.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			EXEMPLO DE CONFIGURAÇÃO DE DOMÍNIO. ARQUIVO db.labredes.com
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     labredes.com. root.labredes.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      labredes.com.
@       IN      A       10.0.3.15
flask   IN      A       10.0.3.15
laravel IN      A       10.0.3.15

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 			EXEMPLO DE CONFIGURAÇÃO DE DOMÍNIO REVERSO. ARQUIVO db.10.0.3    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OBS: Deve-se analisar qual o IP utilizado e realizar as devidas alterações. No exemplo, o IP utilizado é 10.0.3.15
                    
;
; BIND reverse data file for local loopback interface
;
$TTL    604800
@       IN      SOA     labredes.com. root.labredes.com. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      labredes.com.
15  IN      PTR     labredes.com.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 			EXEMPLO DE CONFIGURAÇÃO DO ARQUIVO DE ZONAS (named.conf.local)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


zone "labredes.com"{
        type master;
        file "/etc/bind/db.labredes.com";
};

zone "3.0.10.in-addr.arpa" {
        type master;
        file "/etc/bind/db.10.0.3";
};


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			QUESTÕES PARA ORIENTAÇÃO DOS ESTUDOS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1 - Para que serve o arquivo named.conf.local e named.conf.default-zones ??

2 - Nos arquivos db (onde definimos o domínio a ser utilizado) qual(is) parâmetros definem a resolução domínio-IP ?

3 - Qual a função do arquivo /etc/resolv.conf ? A ordem dos servidores tem importância?

4 - Explique o comando nslookup e o que significa a sua saída.

5 - Situação problema: Você configurou um servidor DNS na mesma máquina em que está rodando o seu servidor WEB. Uma vez que você configurou um domínio para o seu serviço WEB
quais os procedimentos devem ser adotados para que uma outra máquina na mesma rede que os seus servidores, possam acessar o seu servidor WEB através do domínio que você cadastrou?
Agora, imagine que você quer acessar o servidor WEB do seu colega ao lado através do domínio que ele cadastrou. Quais os procedimento devem ser adotados?

6 - No contexto do nosso laboratório, considerando a rede wLabredes5, é possível um mesmo servidor WEB ser acessado por domínios diferentes? Analisem todos os casos possíveis e justifique sua resposta.

7 - Se desejarmos um único servidor DNS para atender a todos os serviços WEB que rodam em nosso laboratório, quais procedimentos devem ser tomados?

8 - Considerando as configurações de IP estático e IP dinâmico utilizados ao longo da nossa disciplina, como poderíamos habilitar o servidor DNS da questões 7 nestes dois contextos?
