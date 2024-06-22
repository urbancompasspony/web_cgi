# web_cgi
Examples and More

https://thobias.org/doc/cgi_shell.html

Existem diversas maneiras de configurá-lo:

ScriptAlias
esta diretiva define um diretório para o Apache onde serão armazenados os scripts CGI. Todos os arquivos que estiverem neste diretório serão interpretados pelo Apache como programas CGI, assim ele tentará executá-los. Adicione ou descomente a seguinte linha no seu arquivo httpd.conf

  ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/ 
O exemplo acima instrui o Apache para que qualquer requisição começando por /cgi-bin/ deva ser acessada no diretório /usr/lib/cgi-bin/ e deva ser tratada como um programa CGI, i.e., ele irá executar o arquivo requisitado.

se você acessar por exemplo http://localhost/cgi-bin/meu_script.cgi, o Apache irá procurar este arquivo em /usr/lib/cgi-bin/meu_script.cgi e tentará executá-lo.

fora do ScriptAlias
você pode especificar um diretório particular e dar permissão para a execução de CGIs.

  <Directory /home/user/public_html/cgi-bin/>
                  Options +ExecCGI
  </Directory>
esta diretiva acima permite a execução de CGIs, mas você ainda precisa avisar o Apache que tipo de arquivos são estes CGIs. Procure por uma linha igual ou semelhante a esta no seu httpd.conf e descomente.

  AddHandler cgi-script .cgi .sh .pl
OBS: se você colocar um index.cgi em algum diretório e quiser que por default o Apache execute-o, não se esqueça de adicionar esta extensão no seu DirectoryIndex.
  <IfModule mod_dir.c>
      DirectoryIndex index.html index.htm index.shtml index.cgi
  </IfModule>
O Apache irá procurar pelo index.cgi seguindo a ordem dos argumentos, ou seja, o index.cgi será a última opção que ele irá procurar no diretório.


2.0.1. Algumas considerações importantes:
você não deve colocar seus scripts no document root do Apache, porque alguém pode pegar seus scripts, analisá-los procurando furos de segurança, etc. Além do mais, o código do script não é o que você quer mostrar :) Então mantenha-os em /usr/lib/cgi-bin ou algum outro diretório fora do document root.
o script precisa ser um executável, não se esqueça de dar um chmod nele. Ah, certifique que o script tem permissão de execução para o usuário que o Apache está rodando.
