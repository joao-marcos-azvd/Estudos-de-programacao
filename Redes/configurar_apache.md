# Configuração e instalação do apache2
## Quais devem ser as condições da V.M.? 
Bem meu caro gafanhoto, sua V.M. tem que seguir os seguintes requisito: 
- O ip da sua V.M. deve ser o mesmo da sua máquina física;
    - Deixe a máquina em placa de rede modo bridge.

## Instalar o apache2
     $ sudo apt install apache2

### E agora patrão?
Bicho, se tudo tiver dado certo é só tu colocar o seu IP no navegado que vai aparecer uma página padrão do apache.

# Resumão do que eu entendi!
Bem, pelo que eu vi tudo vai girar entorno dos diretórios **sites-available** e **sites-enabled** e dos arquivos de configuração **.conf**, além de indicar a(s) porta(s) que o site vai usar, tudo isso sendo indicado no **documentroot**.

## Beleza, e agora? Agora vamos ver os principais comandos de hoje!
- **nano, cd, mkdir, rm -r** -> Sei pra que esses danados servem.

- **git pull** -> Atualiza o repositório da V.M.

- **sudo systemctl restart** -> Reinicia o site.

- **a2ensite (nome_do_site.conf)**  -> Serve para habilitar o arquivo de configuração do site.

- **a2dissite (nome_do_site.conf)** -> Serve para desabilitar o arquivo de configuração do site.

- **ip address** -> Serve para pegar o IP da V.M.
