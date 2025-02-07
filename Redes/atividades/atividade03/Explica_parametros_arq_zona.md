# Explicação dos parametros de um arquivo de zona DNS
## Serial
* É um número de série que permite ao servidor identificar se há ou não alterações nos arquivos;
* Sempre que alguma alteração for feita deve-se mudar o número de série para indicar ao servidor que há alterações.

  
## Refresh
* É um parametro passado para indicar o "envelhecimento" do site;
* Verifica se há atualizações para serem feitas na tela;
* O adiministrador do sistema que define o tempo que o sistema deve durar antes de ser atualizado. 


## Retry  
* É um tempo extra que o servidor espera para tentar fazer uma atualização caso ele não tenha recebido uma resposta na primeira solicitação.


##  Expire
* É o tempo que um servidor primário deve responder ao servidor secundário;
* Caso ele ultrapasse esse tempo, o servidor secundário deve considerar inválidos os dados que estavam nele.


## Negative Cache TTL
* É o tempo mínimo de vida de um servidor (Em segundos);
* Por quanto tempo um servidor de nome ou resolvedor deve armazenar no cache uma resposta negativa.

## REFERÊNCIAS:
* Labs, F. (2014, outubro 15). Finalidade do número de série em arquivos de zona DNS. SuperUser. https://superuser-com.translate.goog/questions/826658/purpose-of-serial-number-in-dns-zone-files?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc

* Intervalo de atualizações. ([s.d.]). sciencedirect. Recuperado 7 de fevereiro de 2025, de https://www-sciencedirect-com.translate.goog/topics/computer-science/refresh-interval?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc#definition

* O que é um registro de DNS SOA? ([s.d.]). cloudflare. Recuperado 7 de fevereiro de 2025, de https://www.cloudflare.com/pt-br/learning/dns/dns-records/dns-soa-record/

* Formatando um Arquivo de Zona de DNS. (2025, janeiro 10). Oracle. https://docs.oracle.com/pt-br/iaas/Content/DNS/Reference/formattingzonefile.htm#format-zone-file

## Autores
* João Marcos de Azevedo Dantas
* Ruan Allyson de Araújo Felix
