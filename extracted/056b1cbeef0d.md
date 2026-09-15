# Sistema de Gestão de Empréstimos (Securities Lending Service)

Source: https://www.euronext.com/sites/default/files/2023-07/manualsge.pdf

Retrieved: 2026-09-11

Extraction: text only; reading order and graphics not verified.


## PDF page 1

SGE – Sistema de Gestão de Empréstimos


              Descrição funcional



                          Versão do Documento – 2.5

                                    2018-01-02





   INTERBOLSA – Sociedade Gestora de Sistemas de Liquidação e de Sistemas Centralizados de Valores Mobiliários, S.A.
                               Avenida da Boavista, 3433 – 4100-138 PORTO - Portugal
                            Tel. 351.22.615 84 00  • Fax 351.22.610 30 29  • Fax CVM 351.22.618 98 26
                                     http://www.interbolsa.pt  • e-mail: interbolsa@interbolsa.pt
                                                  Contribuinte N.º 502 962 275

## PDF page 2

Atualizações



    Data       Versão            Utilizador                         Comentário
  2005/05/06       0.2    Interbolsa                     Definição do Modelo funcional/técnico do SGE

  2005/06/28       1.0    Interbolsa                     Alterações gerais ao Modelo Funcional do SGE
  2006/01/05       2.0    Interbolsa                    Modificações ao Modelo Funcional do SGE
  2006/04/03       2.1    Interbolsa                     Introdução de Layouts (msg’s + ficheiros)
                                                        Alterações ponto 2.8.2 – Outros Eventos
                                                        Alterações descritivos de instruções (2.5.1 e 2.5.2)
                                                         Inclusão da fórmula de cálculo da remuneração da
                                                           garantia em 2.6.2
  2006/04/20       2.2    Interbolsa                     Alterações diversas
  2006/05/15       2.3    Interbolsa                     Alterações pontos 2.4, 2.5. – e 2.5.2 - inclusão de
                                                          difusão bilateral e tratamentos diferenciados de
                                                        quantidade.
                                                        Alterações tabela de motivos – criação do motivo
                                                007 e anulação do motivo 118.
  2006/07/21       2.4    Interbolsa                     Alteração ponto 2.8.2 – “Outros exercícios de
                                                                  direitos de conteúdo patrimonial”, tratamento do
                                                     evento split.
  2018/01/02       2.5    Interbolsa                     Alteração do documento – após entrada no T2S





SGE - Descrição Funcional                                                        2 de Janeiro de 2018

## PDF page 3

Índice


   1- Introdução ...................................................................................................................... 3

            1.1 - Sistema de Gestão de Empréstimos .......................................................................................... 3


  2 - Descrição do Modelo ................................................................................................... 4

            2.1 - Valores Mobiliários ...................................................................................................................... 4

            2.2 - Participantes ............................................................................................................................... 4

            2.3 - Horário de funcionamento (WET) ............................................................................................... 4

            2.4 - Empréstimo de Valores ............................................................................................................... 4

            2.5 - Registo de instruções ................................................................................................................. 5
                2.5.1 - Procura de Valores para empréstimo ................................................................................. 5
                    2.5.1.1 - Procura de valores ..................................................................................................... 5
                    2.5.1.2 - Cedência de valores ................................................................................................... 6
                    2.5.1.3 - Confirmação ............................................................................................................... 7
                2.5.2 - Oferta de Valores para empréstimo ................................................................................... 9
                    2.5.2.1 - Oferta de valores ........................................................................................................ 9
                    2.5.2.2 - Tomada de valores ................................................................................................... 10
                    2.5.2.3 – Confirmação............................................................................................................. 11
                2.5.3 - Registo de operações de empréstimo in-house ............................................................... 12
                2.5.4 - Cancelamento de instruções ............................................................................................ 13

            2.6 - Operação de Empréstimo ......................................................................................................... 14
                   2.6.1 - Abertura do empréstimo .............................................................................................. 14
                   2.6.2 - Fecho do empréstimo .................................................................................................. 15
                   2.6.3 - Cálculo diário de margens ........................................................................................... 16

            2.7 - Gestão das Operações em aberto ............................................................................................ 17
                   2.7.1 - Alteração da data de fecho do empréstimo ................................................................. 17
                   2.7.2 - Alteração da taxa de remuneração do colateral.......................................................... 17

            2.8 - Tratamento de exercícios de direitos de conteúdo patrimonial ................................................ 17
                   2.8.1 - Dividendos ................................................................................................................... 18
                   2.8.2 - Outros exercícios de direitos de conteúdo patrimonial ............................................... 18

            2.10 - Informação aos Participantes ................................................................................................. 19

            2.11 - Fluxo de informação ............................................................................................................... 19



SGE - Descrição Funcional                                                        2 de Janeiro de 2018              Índice I

## PDF page 4

  3 – Layouts ....................................................................................................................... 24

             3.1- Ficheiros/mensagens de envio .................................................................................................. 24
                3.1.1 – SGEmsg/SGEfile ............................................................................................................. 24

             3.2- Ficheiros/mensagens de receção .............................................................................................. 26
                3.2.1 – SGE .................................................................................................................................. 26
                3.2.2 – SGE-PND ......................................................................................................................... 29
                3.2.3 – SGE-RES ......................................................................................................................... 31
                3.2.4 – SGE-SEC ......................................................................................................................... 33
                3.2.5 – SGE-RC ........................................................................................................................... 34

             4.1- Janelas STD – SGE (Exemplos) ............................................................................................... 38
                4.1.1 – SGEmsg ........................................................................................................................... 38
                4.1.2 – SGE .................................................................................................................................. 38
                4.1.3 – Ficheiro SGE-PND ........................................................................................................... 38
                4.1.4 – Ficheiro SGE-RES ........................................................................................................... 38





SGE - Descrição Funcional                                                        2 de Janeiro de 2018             Índice II

## PDF page 5

1- Introdução



1.1 - Sistema de Gestão de Empréstimos


    O Sistema de Gestão de Empréstimos (SGE) é uma plataforma informática que se destina a servir de
suporte a um serviço que a Interbolsa disponibiliza, o Empréstimo de Valores Mobiliários.

      Este serviço possibilita aos seus Participantes difundir informação sobre procura e oferta de valores a
todos os Participantes, confirmar, entre as contrapartes, as caraterísticas da operação de empréstimo e efetuar
as liquidações inerentes à abertura e fecho de operações de empréstimo.

    O Sistema de Gestão de Empréstimos está disponível apenas no STD – Sistema de Transferência de
Dados, sendo a liquidação das respetivas instruções efetuada na plataforma TARGET2-Securities (T2S). A
informação  relativa às instruções de liquidações também é enviada através de mensagens ISO 15022
(MT545/547/548), caso estas tenham sido subscritas pelos Participantes.

    O presente documento descreve as funcionalidades do SGE, as quais pretendem responder às
necessidades dos Participantes e dos investidores do mercado de capitais português.





SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 3

## PDF page 6

2 - Descrição do Modelo



2.1 - Valores Mobiliários


    Os valores mobiliários suscetíveis de serem alvo de operações de empréstimo são as ações que fazem
parte do índice PSI-20.

     Sempre que determinados valores mobiliários deixem de fazer parte do índice PSI-20, o SGE deixa de
aceitar o registo de novas operações sobre esses mesmos valores, mas mantém no sistema as operações já
confirmadas ou abertas processando-as normalmente.



2.2 - Participantes


     Todos os intermediários financeiros filiados na Interbolsa têm acesso ao serviço de empréstimo de
valores mobiliários disponibilizado através do SGE.




2.3 - Horário de funcionamento (WET)


    O horário de funcionamento do SGE é o seguinte:

        a)  07h45 – Aplicação de Corporate Actions em empréstimos abertos (compensação de dividendos ou
            cancelamento);
        b)  08h30 – Início de registo de empréstimos;
        c)  10h30 – Abertura de empréstimos forward e atualização de garantias;
        d)  13h00 – Ciclo de fecho de empréstimos;
        e)  14h50 – Limite para abertura de empréstimos em Real-time (10 min antes do DVP cut-off no T2S);
           f)   17h00 – Fim do registo de empréstimos.



2.4 - Empréstimo de Valores


    Uma operação de empréstimo de valores é composta por duas operações de liquidação interligadas, a
abertura e o fecho, que são executadas no sistema nas condições acordadas entre as contrapartes da operação,

SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 4

## PDF page 7

ou através de um registo direto, no caso do Participante ser, simultaneamente, o mutuante e o mutuário (registo
de operações in-house).

     As condições do empréstimo são acordadas entre as partes através do registo de instruções no SGE. As
instruções, de procura ou de oferta de valores, são registadas e divulgadas, através do SGE, a todos os
Participantes, sendo que, se algum dos Participantes estiver interessado em ser contraparte na operação, pode
propor as suas condições, que serão transmitidas, unicamente, ao intermediário que introduziu a primeira
instrução. Este pode, então, aceitar as condições propostas, através de uma operação de confirmação, ou ignorar
a proposta.

     Se na instrução de procura ou oferta de valores, for indicado o código do Participante contraparte, esta
instrução é registada e divulgada, através do SGE, unicamente ao Participante indicado, podendo este, propor
as suas condições, que serão transmitidas única e exclusivamente ao Participante que introduziu a instrução
inicial. Este pode, então, aceitar as condições propostas, através de uma operação de confirmação, ou ignorar a
proposta.

     As operações de empréstimo são garantidas mediante a entrega de uma quantia em dinheiro como
colateral, cujo montante inicial será calculado com base na margem acordada entre as contrapartes da operação
e cujo valor será mantido atualizado através de cálculo diário, havendo lugar, se necessário, a pagamentos de
reforço ou de devolução de garantia a serem processados no T2S.



2.5 - Registo de instruções


    Os intermediários financeiros podem proceder ao registo de instruções (oferta e procura de valores), bem
como, à gestão corrente das operações de empréstimo e instruções em curso. Para o efeito, procederão ao envio
de instruções utilizando mensagens ou ficheiros através do STD, Sistema de Transferência de Dados, que serão
processados em tempo real.

     As instruções validadas e registadas no sistema são identificadas através de um número atribuído pelo
sistema. As instruções válidas e não satisfeitas, que ainda se encontrem no sistema no final do dia, são,
automaticamente canceladas, num processamento específico a realizar após o fecho do SGE (após as 17h00).

    O prazo máximo admitido para data de fecho de operações de empréstimo é de 2 anos, sendo, no entanto,
permitido o registo de operações sem data de fecho (operações “open-end”).


2.5.1 - Procura de Valores para empréstimo


2.5.1.1 - Procura de valores


    O Participante procede ao registo no sistema da instrução de procura de valores para empréstimo, a qual

SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 5

## PDF page 8

deverá conter todas as menções estabelecidas, no âmbito do SGE, como obrigatórias. O Participante pode,
ainda, indicar outras condições contratuais que entenda conveniente divulgar. Por cada instrução de procura de
valores, validada e registada no sistema, será disponibilizada informação a todos os Participantes, através de
mensagens em tempo real (difusão pública).


    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                             Obrigatório   Difusão Pública
 Tipo de pedido                                                      Sim           Sim
 Número da instrução do pedido                                                    n.a           Sim
 Código do Participante/BIC que procura valores (Mutuário)                    Sim           Sim
 Código do Participante/BIC contraparte (Mutuante)                         Não           Não1
 Código do valor mobiliário (ISIN ou CVM)                                  Sim           Sim
 Tipo de Quantidade (UNIT)                                             Sim           Sim
 Quantidade pretendida                                                Sim           Sim
 Conta de liquidação (Mutuário)                                          Sim          Não
 Conta de liquidação (Mutuante) da contraparte2                                    n.a              n.a
 Data de abertura do empréstimo                                         Sim           Sim
 Data de fecho do empréstimo (não preenchido para empréstimos ”open-end”)     Não           Sim
 Margem para cálculo diário do valor da garantia (haircut)                    Não           Sim
 Valor mínimo da remuneração do empréstimo                            Não           Sim
 Código da Moeda (EUR)                                               Sim           Sim
 Taxa anual de remuneração do empréstimo                              Não           Sim
 Taxa anual de remuneração do colateral                                Não           Sim


    A instrução de procura pode ser cancelada, em qualquer momento, pelo Participante que a instruiu, sendo
disponibilizada informação, para os restantes Participantes do SGE, de que a instrução cancelada já não se
encontra ativa. Se, no momento do cancelamento, existirem instruções de resposta à procura em causa, estas
serão também canceladas.





2.5.1.2 - Cedência de valores


    O Participante interessado em responder a uma instrução de procura, disponibilizando valores para
empréstimo, deverá proceder ao registo das condições contratuais que está disposto a oferecer para o efeito.


1 Se o campo código do Participante de cedência de valores for indicado na instrução de procura, a difusão será efetuada em modo privado
(bilateral).
2 A utilizar unicamente nas operações in-house.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 6

## PDF page 9

Após a validação da instrução de cedência de valores, o sistema envia para a contraparte a informação das
condições da cedência registadas (difusão privada). A validação da instrução consiste, para além da verificação
sintática dos dados, na verificação da correspondência da informação dos campos indicados como sendo de
“matching” entre a instrução de cedência e a instrução de procura de valores.

    A quantidade de valores a ceder tem que ser sempre igual à quantidade indicada na instrução de procura.

    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                  Obrigatório       Difusão     Match
                                                                              Privada
 Tipo de pedido                                             Sim           Sim        Sim
 Número da instrução do pedido                                Sim           Sim        Sim
 Número da instrução de resposta                                          n.a.           Sim        Não
 Código do Participante/BIC contraparte de valores (Mutuário)         Sim           Sim        Sim
 Código do Participante/BIC de oferta (Mutuante)                   Sim           Sim        Não
 Código do valor mobiliário (ISIN ou CVM)                        Sim           Sim        Sim
 Tipo de Quantidade (UNIT)                                   Sim           Sim        Sim
 Quantidade oferecida                                        Sim           Sim        Não3
 Conta de liquidação (Mutuário)                                Sim           Não       Não
 Conta de liquidação (Mutuante) da contraparte4                        n.a               n.a        Não
 Data de abertura do empréstimo                               Sim           Sim        Sim
 Data de fecho do empréstimo (não preenchido para empréstimos      Não           Sim        Não
 ”open-end”)
 Margem para cálculo diário do valor da garantia (haircut)            Sim           Sim        Não
 Valor mínimo da remuneração do empréstimo                     Sim           Sim        Não
 Código da Moeda (EUR)                                     Sim           Sim        Sim
 Taxa anual de remuneração do empréstimo                      Sim           Sim        Não
 Taxa anual de remuneração do colateral                         Sim           Sim        Não


    A instrução de cedência proposta pode ser cancelada, em qualquer momento, pelo Participante que a
instruiu, sendo disponibilizada informação para a contraparte de que a instrução já não se encontra ativa.



2.5.1.3 - Confirmação


    O Participante que registar no SGE a instrução de procura de valores pode escolher entre as possíveis
instruções de cedência, aquela que mais lhe interessar, manifestando o seu acordo com as condições da
operação através do envio de uma instrução de confirmação. Após a validação da instrução de confirmação, é


3 No momento da resposta pode haver divergências entre a quantidade da procura e a da cedência de valores.
4 A utilizar unicamente nas operações in-house.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 7

## PDF page 10

efetuada uma difusão da informação para as contrapartes e a operação de empréstimo é aberta de imediato
(após liquidação no T2S), se a data de abertura do empréstimo for a data da confirmação da operação, caso
contrário, será aberta em data futura, acordada pelas partes. Uma vez que a quantidade registada na instrução
de cedência e na de procura de valores é, obrigatoriamente, igual, a operação de empréstimo é gerada por esta
quantidade, havendo lugar a uma difusão pública, informando que aquela instrução deixou de estar disponível
para o mercado. As restantes propostas de cedência registadas para aquela procura de valores serão
canceladas, automaticamente, pelo sistema, havendo lugar à difusão dessa informação para as partes
correspondentes.

    A validação da instrução consiste, para além da verificação sintática dos dados, na verificação da
correspondência da informação dos campos indicados como sendo de “matching” entre a instrução de
confirmação e a instrução de oferta de valores.

    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                  Obrigatório     Difusão      Match5
                                                                           Privada
 Tipo de pedido                                            Sim          Sim         Sim
 Número de instrução do pedido                                Sim          Sim         Sim
 Número de instrução da resposta                              Sim          Sim         Sim
 Código do Participante/BIC que procura valores (Mutuário)          Sim          Sim         Sim
 Código do Participante/BIC contraparte (Mutuante)                 Sim          Sim         Sim
 Código do valor mobiliário (ISIN ou CVM)                        Sim          Sim         Sim
 Tipo de Quantidade (UNIT)                                   Sim          Sim         Sim
 Quantidade oferecida                                       Sim          Sim         Sim6
 Conta de liquidação da contraparte (Mutuário)                         n.a             n.a         Sim
 Conta de liquidação (Mutuante) da contraparte7                   Sim          Sim8         Sim
 Data de abertura do empréstimo                               Sim          Sim         Sim
 Data de fecho do empréstimo (não preenchido para empréstimos     Sim          Sim         Sim
 ”open-end”)
 Margem para cálculo diário do valor da garantia (haircut)            Sim          Sim         Sim
 Valor mínimo da remuneração do empréstimo                    Sim          Sim         Sim
 Código da Moeda (EUR)                                     Sim          Sim         Sim
 Taxa anual de remuneração do empréstimo                      Sim          Sim         Sim
 Taxa anual de remuneração do colateral                         Sim          Sim         Sim


     Após confirmação, se a data de abertura do empréstimo for o próprio dia, dentro do horário de
funcionamento do SGE, será criada e enviada de imediato para o T2S uma instrução de liquidação contra
pagamento (DVP),  “already matched”. A  instrução de  liquidação  permite a  transferência dos  valores


5 Os campos indicados nesta coluna como “Sim” são critérios de matching obrigatório.
6 O campo quantidade só é critério de matching entre a instrução de cedência de valores e a respetiva confirmação.
7 A utilizar unicamente nas operações in-house.
8 Só será visualizada a própria conta do IF.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 8

## PDF page 11

correspondentes ao empréstimo da situação de disponível da conta do mutuante (Oferta de Valores) para a conta
do mutuário (Procura de Valores) por contrapartida do pagamento da garantia inicial (Gi) do mutuário para o
mutuante.

    No caso da data de abertura do empréstimo ser no futuro (operações forward), a instrução de liquidação
contra pagamento (DVP) será enviada para o T2S, no horário definido para o efeito (10h30), na respetiva data
de abertura.




2.5.2 - Oferta de Valores para empréstimo


2.5.2.1 - Oferta de valores


    O Participante procede ao registo da instrução de oferta de valores para empréstimo no sistema, a qual
deverá conter todas as menções estabelecidas, no âmbito do SGE, como obrigatórias. O Participante pode,
ainda, indicar outras condições contratuais que entenda conveniente divulgar.

     Após validação da instrução e registo da mesma no sistema, será disponibilizada informação para todos
os Participantes, através de mensagens em tempo real (difusão pública).


    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                             Obrigatório   Difusão Pública
 Tipo de pedido                                                      Sim           Sim
 Número da instrução do pedido de oferta                                               n.a.           Sim
 Código do Participante/BIC de oferta de valores (Mutuário)                   Não           Não9
 Código do Participante/BIC contraparte (Mutuante)                          Sim           Sim
 Código do valor mobiliário (ISIN ou CVM)                                  Sim           Sim
 Tipo de Quantidade (UNIT)                                             Sim           Sim
 Quantidade oferecida                                                 Sim           Sim
 Conta de liquidação da contraparte10 (Mutuário)                                    n.a              n.a
 Conta de liquidação (Mutuante)                                         Sim          Não
 Data de abertura do empréstimo                                         Sim           Sim
 Data de fecho do empréstimo (não preenchido para empréstimos ”open-end”)     Não           Sim
 Margem para cálculo diário do valor da garantia (haircut)                    Não           Sim
 Valor mínimo da remuneração do empréstimo                            Não           Sim


9 Se o campo código do Participante de procura de valores for indicado na instrução de oferta, a difusão será efetuada em modo privado
(bilateral).
10 A utilizar unicamente nas operações in-house.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018           Página 9

## PDF page 12

 Informação                                                             Obrigatório   Difusão Pública
 Código da Moeda (EUR)                                               Sim           Sim
 Taxa anual de remuneração do empréstimo                              Não           Sim
 Taxa anual de remuneração do colateral                                Não           Sim


    A instrução de oferta pode ser cancelada, em qualquer momento, pelo Participante que a instruiu, sendo
disponibilizada informação para os restantes Participantes do SGE de que aquela instrução cancelada já não se
encontra ativa. Se, no momento do cancelamento, existirem instruções de resposta à oferta em causa, estas
serão também canceladas.



2.5.2.2 - Tomada de valores


    O Participante interessado em receber valores através de empréstimo, pode introduzir a sua instrução de
tomada de valores no sistema propondo as suas condições. Após a validação da instrução o sistema informa a
contraparte das condições propostas (difusão privada). A validação da instrução consiste, para além da
verificação sintática dos dados, na verificação da correspondência da informação dos campos indicados como
sendo de “matching” entre a instrução de tomada e a instrução de oferta de valores.

    A quantidade de valores a receber tem que ser sempre igual à quantidade indicada na instrução de oferta.

    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                             Obrigatório      Difusão         Match11
                                                                       Privada
 Tipo de pedido                                        Sim          Sim           Sim
 Número da instrução do pedido (oferta)                     Sim          Sim           Sim
 Número da instrução da resposta (procura)                         n.a.          Sim           Não
 Código do Participante/BIC contraparte valores (Mutuário)       Sim          Sim           Não
 Código do Participante/BIC de oferta de valores (Mutuante)      Sim          Sim           Sim
 Código do valor mobiliário (ISIN ou CVM)                    Sim          Sim           Sim
 Tipo de Quantidade (UNIT)                               Sim          Sim           Sim
 Quantidade pretendida                                  Sim          Sim             Não12
 Conta de liquidação (Mutuário)                            Sim         Não          Não
 Conta de liquidação (Mutuante) da contraparte13                  n.a             n.a           Não
 Data de abertura do empréstimo                           Sim          Sim           Sim
 Data de  fecho do  empréstimo  (não  preenchido  para     Não          Sim           Não
 empréstimos ”open-end”)


11 Os campos indicados nesta coluna como "Sim" são critérios de matching obrigatório.
12 No momento da resposta pode haver divergências entre a quantidade da oferta e a da tomada de valores.
13 A utilizar unicamente nas operações in-house.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 10

## PDF page 13

 Informação                                             Obrigatório      Difusão         Match11
                                                                       Privada
 Margem para cálculo diário do valor da garantia (haircut)        Sim          Sim           Não
 Valor mínimo da remuneração do empréstimo                Sim          Sim           Não
 Código da Moeda (EUR)                                 Sim          Sim           Sim
 Taxa anual de remuneração do empréstimo                  Sim          Sim           Não
 Taxa anual de remuneração do colateral                    Sim          Sim           Não


    A instrução de tomada de valores pode ser cancelada, em qualquer momento, pelo Participante que a
instruiu, sendo disponibilizada informação para a contraparte de que a instrução já não se encontra ativa.



2.5.2.3 – Confirmação


    O Participante ofertante pode escolher entre as possíveis instruções de tomada de valores, aquela que
mais lhe interessar, manifestando o seu acordo com as condições da operação através do envio de uma instrução
de confirmação. Após a validação da instrução de confirmação, é efetuada uma difusão da informação para as
contrapartes da operação e a operação de empréstimo é aberta de imediato (após liquidação no T2S), se a data
de abertura do empréstimo for a data da confirmação da operação, caso contrário, será aberta em data futura,
acordada pelas partes. Uma vez que a quantidade registada na instrução de oferta e na de tomada de valores é,
obrigatoriamente, igual, a operação de empréstimo é gerada por esta quantidade, havendo lugar a uma difusão
pública, informando que aquela instrução deixou de estar disponível para o mercado. As restantes propostas de
tomada de valores registadas para aquela oferta de valores serão canceladas, automaticamente, pelo sistema.
Dos cancelamentos efetuados será efetuada difusão de informação para as partes correspondentes.

    A validação da instrução consiste, para além da verificação sintática dos dados, na verificação da
correspondência da informação dos campos indicados como sendo de “matching” entre a instrução de
confirmação e a instrução de tomada de valores.

    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que
facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                  Obrigatório    Difusão      Match14
                                                                          Privada
 Tipo de pedido                                            Sim        Sim         Sim
 Número da instrução do pedido (oferta)                         Sim        Sim         Sim
 Número da instrução da resposta (procura)                      Sim        Sim         Sim
 Código do Participante/BIC contraparte (Mutuário)                 Sim        Sim         Sim
 Código do  Participante/BIC  ofertante de  valores  contraparte     Sim        Sim         Sim
 (Mutuante)
 Código do valor mobiliário (ISIN ou CVM)                        Sim        Sim         Sim

14 Os campos indicados nesta coluna como “Sim” são critérios de matching obrigatório.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 11

## PDF page 14

 Informação                                                  Obrigatório    Difusão      Match14
                                                                          Privada
 Tipo de Quantidade (UNIT)                                   Sim        Sim         Sim
 Quantidade oferecida                                       Sim         Sim          Sim15
 Conta de liquidação da contraparte (Mutuário)                         n.a           n.a         Sim
 Conta de liquidação (Mutuante) 16                              Sim          Sim17        Sim
 BIC Mutuário/Mutuante                                   Não        Sim         Sim
 Margem para cálculo diário do valor da garantia (haircut)            Sim        Sim         Sim
 Valor mínimo da remuneração do empréstimo                    Sim        Sim         Sim
 Código da Moeda (EUR)                                     Sim        Sim         Sim
 Taxa anual de remuneração do empréstimo                      Sim        Sim         Sim
 Taxa anual de remuneração do colateral                         Sim        Sim         Sim


     Após confirmação, se a data de abertura do empréstimo for o próprio dia, dentro do horário de
funcionamento do SGE, será criada e enviada de imediato para o T2S uma instrução de liquidação contra
pagamento (DVP),  “already matched”. A  instrução de  liquidação  permite a  transferência dos  valores
correspondentes ao empréstimo da situação de disponível da conta do mutuante (Oferta de Valores) para a conta
do mutuário (Procura de Valores) por contrapartida do pagamento da garantia inicial (Gi) do mutuário para o
mutuante.

    No caso de a data de abertura do empréstimo ser no futuro (operações foward), a instrução de liquidação
contra pagamento (DVP) será enviada para o T2S, no horário definido para o efeito (10h30), na respetiva data
de abertura.



2.5.3 - Registo de operações de empréstimo in-house


    O registo das operações de empréstimo em que o mesmo Participante no SGE tem funções de ambas as
contrapartes (mutuário e mutuante), pode ser efetuado registando-se, no sistema, apenas uma instrução com
toda a informação necessária. Destas operações não será efetuada difusão pública aos restantes Participantes
do sistema.

     Após o registo é gerada a operação de empréstimo e procede-se à sua abertura:

             a) Imediatamente, após liquidação no T2S, se a data de abertura do empréstimo for a do registo;

             b) Em data futura, caso a operação seja forward.


    A informação que deve obrigatoriamente constar da instrução de procura de valores, bem como a que


15 O campo quantidade só é critério de matching entre a instrução de tomada de valores e a respetiva confirmação.
16 A utilizar unicamente nas operações in-house.
17 Só será visualizada a própria conta do IF.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 12

## PDF page 15

facultativamente pode ser aditada, encontra-se referida no quadro infra:

 Informação                                                             Obrigatório   Difusão Privada
 Tipo de pedido                                                      Sim            Sim
 Número da instrução                                                                    n.a.            Sim
 Código do Participante/BIC que procura valores (Mutuário)                    Sim            Sim
 Código do Participante/BIC que oferece valores (Mutuante)                    Sim            Sim
 Código do valor mobiliário (ISIN ou CVM)                                  Sim            Sim
 Tipo de Quantidade (UNIT)                                             Sim            Sim
 Quantidade do empréstimo                                             Sim            Sim
 Conta de liquidação (Mutuário)                                          Sim            Sim
 Conta de liquidação (Mutuante)                                         Sim            Sim
 Data de abertura do empréstimo                                         Sim            Sim
 Data de fecho do empréstimo (não preenchido para empréstimos ”open-end”)     Não            Sim
 Margem para cálculo diário do valor da garantia (haircut)                      Sim            Sim
 Valor mínimo da remuneração do empréstimo                              Sim            Sim
 Código da Moeda (EUR)                                               Sim            Sim
 Taxa anual de remuneração do empréstimo                                Sim            Sim
 Taxa anual de remuneração do colateral                                  Sim            Sim


     Após registo e validação pelo sistema, se a data de abertura do empréstimo for o próprio dia, dentro do
horário de funcionamento do SGE, será criada e enviada de imediato para o T2S uma instrução de liquidação
contra pagamento (DVP), “already matched”. A instrução de liquidação permite a transferência dos valores
correspondentes ao empréstimo da situação de disponível da conta do mutuante (Oferta de Valores) para a conta
do mutuário (Procura de Valores) por contrapartida do pagamento da garantia inicial (Gi) do mutuário para o
mutuante, de acordo com a informação enviada pelo Participante.

    No caso de a data de abertura do empréstimo ser no futuro (operações foward), a instrução de liquidação
contra pagamento (DVP) será enviada para o T2S, no horário definido para o efeito (10h30), na respetiva data
de abertura.





2.5.4 - Cancelamento de instruções


    O cancelamento das instruções de procura e cedência de valores pode ser automático ou manual.

     As instruções de procura e cedência de valores não confirmadas são canceladas automaticamente, no
final do dia, em processamento específico a correr após o encerramento do registo de instruções no sistema
(após as 17h00). Será efetuada difusão de mensagens de cancelamento automático aos Participantes.

     As instruções de procura e cedência de valores podem ser canceladas em qualquer momento pelo

SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 13

## PDF page 16

Participante que as introduziu no sistema. Se o cancelamento for efetuado sobre uma instrução original (oferta
ou procura), será efetuada a difusão pública do cancelamento. Se a instrução já foi alvo de resposta (aguardando
confirmação), o sistema procede ao cancelamento automático da(s) resposta(s) associada(s) e à difusão de
informação às partes envolvidas.

     Após a confirmação da operação de empréstimo, os Participantes não poderão proceder ao cancelamento
da mesma, havendo apenas, possibilidade de antecipação do respetivo fecho.



2.6 - Operação de Empréstimo


      2.6.1 - Abertura do empréstimo


     As operações de empréstimo são identificadas através de um número atribuído pelo sistema no momento
da confirmação. No momento da abertura do empréstimo, de acordo com o horário estabelecido, é criada e
enviada para o T2S uma instrução de liquidação DVP com uma referência atribuída pela Interbolsa, para ser
liquidada em tempo real. Após validação da instrução pelo T2S, será atribuída uma referência T2S. As
liquidações relacionadas com as operações de empréstimo poderão então ser identificadas através de uma
referência atribuída pela Interbolsa e uma referência atribuída pelo T2S.

     São aceites operações de empréstimo com abertura em data futura (operações forward), sendo o período
máximo admissível de 20 dias úteis. Estas operações serão abertas num ciclo de processamento, a ocorrer pelas
10h30m da respetiva data de abertura.

    A operação de abertura do empréstimo ocorre com o envio de uma instrução de liquidação contra
pagamento (DVP) para o T2S. A liquidação processa-se no T2S através da transferência dos valores
correspondentes ao empréstimo da situação de disponível da conta do mutuante (Oferta de Valores) para a conta
do mutuário (Procura de Valores) por contrapartida do pagamento da garantia inicial (Gi) do mutuário para o
mutuante. Após validação, a instrução é imediatamente submetida a liquidação na plataforma, sendo liquidada
caso existam, simultaneamente, valores disponíveis na conta do IF mutuante e dinheiro na conta do IF mutuário.

    No caso da falha física (IF mutuante não tem títulos na conta para empréstimo) ou falha da liquidação
financeira (falta de dinheiro na conta de cash do IF mutuário) a operação de empréstimo não é aberta, sendo
cancelada pela Interbolsa (e as instruções de liquidação serão canceladas no T2S).

    No caso de operações “in-house”, o SGE efetua os cálculos relativos à componente financeira divulgando-
os ao Participante em causa, e envia a respetiva instrução financeira para o T2S.


    O valor da garantia inicial (Gi) é calculado de acordo com a fórmula seguinte:

                                    Gi = Q × C × (1 + M)

SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 14

## PDF page 17

               Onde:
                         Gi –  Garantia inicial;
               Q –  Quantidade de valores mobiliários emprestados;
                C –  Última cotação de fecho divulgada à Interbolsa pela Euronext Lisbon;
              M –  Margem acordada.





2.6.2 - Fecho do empréstimo


    A operação de empréstimo é encerrada, automaticamente, na data indicada de fecho, no ciclo de
processamento do fecho às 13h00, através da criação e envio para o T2S de uma instrução de liquidação DVP
(“already matched”), sendo a componente financeira igual ao resultado da compensação da devolução ao
mutuário da garantia acrescida da remuneração do colateral, e do pagamento ao mutuante da remuneração do
empréstimo. A quantidade de valores da operação de empréstimo será debitada na conta do IF mutuário por
contrapartida do pagamento na conta do IF mutuante. Após validação a liquidação da instrução será efetuada
imediatamente no T2S caso existam, simultaneamente, valores disponíveis na conta do IF mutuário e dinheiro
na conta do IF mutuante.

    No caso de operações “in-house”, o SGE efetua os cálculos relativos à componente financeira divulgando-
os ao Participante em causa, e envia a instrução financeira para o T2S.


    No caso de falha física (IF mutuário não tem títulos na conta para devolver) ou falha na liquidação
financeira a operação de empréstimo é cancelada pela Interbolsa (e as instruções de liquidação correspondentes
serão canceladas no T2S) e as contrapartes do empréstimo deverão proceder ao fecho ou execução da garantia
fora do sistema SGE.

    A remuneração do empréstimo é calculada segundo a fórmula seguinte:

                  R = max { K ; ((Q × C × T) / 360 × P) }

               Onde:
                R –  Remuneração do empréstimo;
                  K –  Remuneração mínima exigida;
               Q –  Quantidade de valores mobiliários emprestados;
                C –  Última cotação de fecho divulgada à Interbolsa pela Euronext Lisbon;
                   T –  Taxa de remuneração anual;
                  P –  Prazo do empréstimo em dias.


    A remuneração do empréstimo calculada será o valor mais alto das duas componentes da fórmula, isto é,
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 15

## PDF page 18

se K for maior que (QxCxT)/360xP será utilizado o valor K, caso contrário será utilizado o valor dado pela segunda
componente da fórmula.


    A remuneração da garantia é calculada segundo a fórmula seguinte:

                            Rg = Σin (Gi × Tgi / 360 × Pi)

               Onde:
                      Rg – Remuneração da Garantia;
                         Gi –  Garantia exigida no período;
                           Tgi – Taxa anual de remuneração da Garantia, em vigor durante o período;
                             Pi –  Período (dias) correspondente à aplicabilidade da taxa e/ou garantia exigida;
                     n –  Nº total de períodos alvo de cálculo – (resultante do nº de alterações da garantia
                                exigida e/ou da taxa de remuneração da garantia).



2.6.3 - Cálculo diário de margens


      Diariamente é reavaliado de modo automático o valor da garantia exigida (GE), de acordo com a seguinte
expressão:

                            GE = Q × C × (1 + M)

               Onde:
                   GE – Garantia exigida;
               Q –  Quantidade de valores mobiliários emprestados;
                C –  Última cotação de fecho divulgada à Interbolsa pela Euronext Lisbon;
              M –  Margem acordada.




     Sempre que a garantia exigida18 ultrapasse o valor da garantia constituída e o valor do reforço da garantia
a exigir (margin call) for maior ou igual ao montante mínimo exigível19, será exigido ao Participante mutuário um
reforço de garantia. Este reforço será efetuado através do envio para o T2S de uma instrução PFD (Payment
free of Delivery):débito da conta de dinheiro (DCA) do Participante mutuário, por contrapartida de crédito da conta
de dinheiro (DCA) do Participante mutuante. Nos casos em que a garantia exigida, calculada, é inferior ao da
garantia constituída e o valor da diferença é maior ou igual ao montante mínimo exigível, será enviada para o



18 Na primeira fase do projeto as garantias são efetuados em dinheiro. Numa segunda fase poderá ser equacionado a prestação das
garantias em valores mobiliários.
19 O valor previsto para o montante mínimo exigível é de 25,00€.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 16

## PDF page 19

T2S uma instrução PFD (Payment free of Delivery):crédito na conta de dinheiro (DCA) do Participante mutuário
no montante da diferença, por contrapartida de um débito na conta de dinheiro (DCA) do Participante mutuante.


    No caso de operações “in-house”, o SGE efetua os cálculos relativos à componente financeira do mesmo
modo, divulgando-os ao Participante em causa, e envia para o T2S a respetiva instrução PFD.



2.7 - Gestão das Operações em aberto


2.7.1 - Alteração da data de fecho do empréstimo


      Qualquer um dos intermediários financeiros, envolvidos numa operação de empréstimo em curso, pode
propor a alteração da data de fecho da mesma. Após introdução da instrução de alteração no sistema, o
Participante contraparte será avisado, pelo sistema, através do envio de uma mensagem em tempo real. Se o
Participante contraparte aceitar a proposta, será enviada uma mensagem de confirmação da alteração para o
Participante proponente. As propostas não confirmadas até às 17h00 serão anuladas, automaticamente, após o
fecho do sistema. Se a nova data for coincidente com a data do próprio dia, o sistema procederá ao fecho
antecipado do empréstimo submetendo a operação de fecho a liquidação, de acordo com o horário definido, no
ciclo de processamento das 13h00.



2.7.2 - Alteração da taxa de remuneração do colateral


      Qualquer um dos intermediários financeiros, envolvidos numa operação de empréstimo em curso, pode
propor a alteração da taxa de remuneração do colateral. Após introdução da instrução de alteração no sistema,
o Participante contraparte será avisado através de envio de uma mensagem de confirmação da alteração em
tempo real. Se o Participante contraparte aceitar a proposta de alteração, será enviada uma mensagem para o
Participante proponente. As propostas não confirmadas serão anuladas, automaticamente, após o fecho do
sistema, mantendo-se inalterável a taxa até então em vigor.



2.8 - Tratamento de exercícios de direitos de conteúdo patrimonial


     Sempre que ocorra um exercício de direitos de conteúdo patrimonial sobre um determinado valor mobiliário
elegível no âmbito do SGE, o sistema fornece, antecipadamente, aos Participantes, informação sobre o referido


SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 17

## PDF page 20

facto. O sistema fornece, unicamente, informação sobre a data e o tipo de evento a ocorrer.



2.8.1 - Dividendos


    Na data de pagamento, o sistema envia para o T2S uma instrução PFD, relativa à compensação do
dividendo: débito na conta de dinheiro (DCA) do mutuário (borrower), por um montante igual ao do dividendo
(bruto), por contrapartida do crédito na conta de dinheiro (DCA) do intermediário mutuante (lender).



2.8.2 - Outros exercícios de direitos de conteúdo patrimonial


      Salvo o disposto no número anterior, e uma vez que, nesta fase, a Interbolsa não efetua a compensação
automática de outros exercícios de direitos, as operações de empréstimo, no âmbito do SGE, deverão ser
fechadas, antecipadamente, pelos intervenientes, sempre que, durante o período do empréstimo, ocorram, sobre
os valores mobiliários objeto do mesmo, outros exercícios de direitos de conteúdo patrimonial, que não
dividendos.

    No entanto, se os intervenientes não procederem, na situação prevista no parágrafo anterior, ao fecho
antecipado das operações de empréstimo antes da data de processamento do evento (Record Date/Market
Deadline), a Interbolsa efetuará o tratamento, de acordo com o tipo de evento envolvido, conforme especificado
na tabela a seguir.



              Evento                                Tratamento a efetuar 20

 Redução                                                 Cancelamento

 Fusão                                                   Cancelamento

 Cisão                                                   Cancelamento

 Alteração de Código de V.M.                                Cancelamento

 Conversão Titulado em Escritural                            Cancelamento

 Incorporação                                 Nenhum tratamento adicional

 Subscrição                                   Nenhum tratamento adicional



20 As contrapartes deverão proceder ao fecho ou à execução da Garantia fora do Sistema, sempre que ocorram cancelamentos sobre
empréstimos em aberto.
SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 18

## PDF page 21

              Evento                                Tratamento a efetuar 20

 Split                                                    Cancelamento



2.10 - Informação aos Participantes


    A Interbolsa disponibiliza aos Participantes (Mutuantes e Mutuários) um conjunto de informações em
tempo real.

      Diariamente,  para  além  das  informações  usualmente  fornecidas  aos  Participantes  (ficheiros e
mensagens), é ainda divulgada informação relativa ao valor das garantias constituídas e às responsabilidades
de liquidação para cada uma das operações realizadas.

     Toda a informação relativa ao registo, confirmação, liquidação e cancelamento ou rejeição das operações
de empréstimo pode ser consultada através da aplicação STD, menu SGE (mnemónicas SGE, SGE-PND e SGE-
RES), bem como, através das mensagens ISO 15022 (MT545, MT547 e MT548).





2.11 - Fluxo de informação


    Os diagramas seguintes esquematizam a sequência de mensagens/operações recebidas e enviadas
durante o processo de tratamento de qualquer uma das instruções/operações associadas ao SGE. O feedback
do sistema é efetuado através do envio de mensagens “SGE”, cujos estados e motivos (nnn) estão especificados
nos diagramas referidos. As mensagens de rejeição podem conter de um até oito motivos, conforme quadro-
resumo, abaixo apresentado, de operações passíveis de realização no âmbito do SGE:

            Designação da operação

              Registo de Instrução de Oferta de valores para Empréstimo

              Registo de Instrução de Procura de valores para Empréstimo

              Abertura da Operação de Empréstimo

            Fecho da Operação de Empréstimo

            Cancelamento de Instrução de Oferta

            Cancelamento de Instrução de Procura


SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 19

## PDF page 22

              Alteração da data de fecho do Empréstimo

              Alteração da Taxa de Remuneração do Colateral.

             Consultas de operações/instruções (Síntese + Detalhes) - SLRTqry


    A segmentação de operações apresentada nos diagramas abaixo, foi efetuada em concordância com a
divisão indicada na tabela anterior.





SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 20

## PDF page 23

    1. – Operação de Empréstimo de valores - iniciada pela Procura (Mutuários).


                   Mutuário               SGE                        Mutuante

                              Instrução de procura


                                  REJT nnn
                                                                                   Validação
                                                                        Erros
                                       PEND’ nnn                    Registo e Difusão              PEND  nnn



                                       (CANC)
                                                                                                                                   Instrução de Cedência


                                                                                     REJT nnn
                                                                              Validação
                                                                                                 Erros
                               PEND  nnn                 Registo e Difusão  .            PEND  nnn


                                       (CANC)                     (CANC)



                           Confirmação da operação


                                  REJT nnn
                                                                                   Validação
                                                                        Erros
                                   'CONF nnn                                   CONF nnn




                                SETT                                                SETT
                                                                                     Liq. DVP T2S  Abertura
                             OPEN                    OK                   OPEN





                      SETT                                             SETT
                                                                       Liq. DVP T2S Fecho

                     CLOS                                          CLOS
                                            OK





SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 21

## PDF page 24

    2. – Operação de Empréstimo de valores - iniciada pela Oferta (Mutuantes).

       Mutuário                SGE                        Mutuante

                                                                                                                      Instrução de Oferta


                                                                           REJT nnn
                                                               Validação


                                                               Registo e Difusão                    PEND  nnn                                        PEND  nnn



                                            (CANC)                                                       Erros

               Instrução de tomada


                                                               Validação
                                                     Erros
                    PEND  nnn                     Registo e Difusão            PEND   nnn


                          (CANC)                         (CANC)



                                                                                                  Confirmação da operação


                                                                           REJT nnn
                                                            Validação
                                                                               Erros                   CONF nnn                                    CONF nnn


                                          OK


                    SETT                                                   SETT
                                                              Liq. DVP T2S Abertura
                  OPEN                      OK                   OPEN




                 SETT                               Liq. DVP T2S Fecho                SETT
                CLOS                                              CLOS                                        OK





SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 22

## PDF page 25

    Os diagramas seguintes contêm o fluxo de mensagens das situações de falha, falha da liquidação física e
financeira, respetivamente:



         Mutuário               SGE                        Mutuante





                    NSET nnn                                     NSET nnn
                                                          Liquidação
                                                              Física/Financeira
                   CANC nnn                           Falha               CANC nnn





                                                          Liquidação
                                                              Física/Financeira
                                        O


                 MONY/AWMO nnn                             AWMO/MONY nnn


                     SETT nnn                                       SETT nnn

                  OPEN/CLOS                   Liquidação DVP – T2S         OPEN/CLOS
                                          OK

                    NSET nnn                                     NSET nnn

                   CANC nnn                 Liquidação DVP – T2S        CANC nnn
                                                             Falha





SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 23

## PDF page 26

                                                   of                                                                        “A”)          1-6                                                                      the                                                                            7-9                                                                        “E”,              pos.for      the                                                                                                 "I")        "I")                                                                                                      pos.for    or   or                                                                                          (“I”,          (or
                                                                            (or                                                                                                                                            spaces                                                                   SGE                                                                                                                                                                                                                         (function       spaces(function        digits)            digits)                                                                            SGE                                                                   the            (3   (3                                                                                                                                                              (Demand)                                             bycontain   the                                                                                                                                                                  Amendment                                                                                                                                                 (Offer)                                                                                                                                                                                                                                                                Borrower:                                                                                                                                                                                                                          Lender:                                                                                                                     Code                                                                                                                                Code                                                                                                                                                                         request bycontainrequest                                                                                                                                                                              Description                                                                                             must            the     digits)the                                                                                                            House                                                                        new     mustnew of   of                                                                                           (11                                                                                                                                                                                  BorrowingLendingInassignedID);a  a                                                                                                                                                                                    Exclusion, --–                                                                                               Type:     ID of   assignedID);of                    POH                                                                    InterbolsaBIC        Interbolsa                                                                                             Loan  ID
                     •••               Loan  •• •                                                                      the                                                                                                                                                           Function:Inclusion,Request                  Requestofinclusion  Replytheinclusion    Identification                       Identification
                                                                                                 novo
                                                                           (ou       ou   ou 24                                                                        “A”)          (ou                                                                                                                                                                                                                      resposta                                                                        “E”,                          deverápedidoSGEdeverá                                                                   SGE                                                                                                                                                                                                                                           dígitos)             dígitos)    Página                                                                                uma                                                                                          (“I”,          umpelo                                                           (3   (3                                                                                          pelo
                                                                                                                                                                                                                                                                                        empréstimo);deatribuídoempréstimo);de                             2018                                                                                                                                                                                    Alteração,                                    incluir           incluir                                                                                                                                                                                                          atribuído                                                                                                                                                                                                                                                                Mutuário:Interbolsa       Mutuante:Interbolsa                                                                                                                                              Descrição                                               de   de                                                                                   de                                                         IFdadígitos)IFda                                                                                                              House nºcaso nºcaso
                                                no                                                     no do  (11do                                                                                                                            OfertaInpedidodo                                                                                                                                                                                                        respostado                                                                                                                                                                                                                                                                                                   Janeiro                                                                                                                                           Procura
                     –                      –                    -                                                                                                       empréstimo;                                                                     Exclusão,                                                                                   de                                                                                                                                    Pedido:                    P                     O                      Hde1-6 de7-9               CódigoBIC     Código                                                                                                                         zeros        zeros                          de:de                             2                                      de
                     •••       •• •                                                                                                                        Função:Inclusão,Tipo               NúmeroposiçãoconterNúmeroposiçãoconternovaIdentificação                      Identificação                                                                                      instruçõesoperações                                                               (EN)
                 dede                                               ID
                                                     ID                                                               Name                                           envio                                                                                                                 empréstimo;
         o                    de              STD   Func             Req.Type              Request          Reply                Borrower       Lender                                                                                                                          empréstimo.
                      de                                                            permite
                                                               (PT)                                                                                            operações
          envio             de                  Name                                                                                                    operações    de                               Empréstimo      de                                               STD                                                                                                                                                                                                                                                                                 (pedido/resposta/confirmação)              de                                       Func             Ped.Tipo                     Num-Pedido                Num-Resp                Mutuário          Mutuante                                                                                                                                                 mensagem/ficheiro

                  A  A  A  A  A A                                                                  RegistoCancelamentoAlteração                                                        SGEmsg/SGEfileRegistoSGEEsta---               Type



       =                                                                                                                              mensagem:     01   01    06    03    11  11          Funcional      =         =         da     Length                                                              SGEmsg/SGEfile  =Layouts                 Ficheiros/mensagens –                                                                                                                                                                                                                                                                                                                         Descrição                                   01   02    03    09    12  23 -
–                                                                                                                              Position3    3.1-   3.1.1     MnemónicaDenominaçãoMenuDescrição                                    Conteúdo                                                                                                                             SGE

## PDF page 27

     orcode
                                                     places                                                         (Rate)             thiswith              format in                                                Borrower  Lender                     places     Fee          (Rate)                                                                                                       4217                code,                                                           Fee                                 the                                     the                                                                  Fee                                                              decimal         ISIN                        filled                                                                             ISO
  -                      of                         of                                                                                                                                                                                                                                                     seguintes         5          CVM                                                                                        decimal                to                left                                            os
                 6                                                                                                                                                                       Lending         Code                                                                                              YYYYMMDD)             withthe                                                                                          YYYYMMDD)                                                                  Number  Number              with                   Remuneration           theDescription      on                           maximum       -          digits)                                                          (14+5)                                                                        for       according                                                                                                                                                                                                                                                                        Remuneration                                                                                                 (format                   filled    right)Code:                                                                                                         (format                                                                                                                                                                                                                                                                                                           obrigatório    (11  (if                                                                                     Securities:                                            UNIT:                                                                             Account  Account                        placed               the                                                                                                     Margin                                                                                                                        value   Code                                                       Date                                                                                                                                                                                                  Collateral      Loan                       Type               of    BICIdentification                                                            Date                           UNIT                           for(format:        be          on                   format
  •     • •                   SecurityCVMshouldblanksQuantity        Quantity                       Securities   Securities   Opening  Closing        Collateral             (Annual)             (Annual)       Minimum      Currency                                                                                                                                                                                                                                                                                                                                                                  preenchimento
                   o
                                                      de
     ou o                                                                                  casas      sobre                       são              25             CVM,e                6                     casas         ISIN                                            decimais            6             4217                                       direita)                                                                                                                                                                                                                                                                   empréstimo,                                                                     Página     a                     mobiliário:                       com                                                                                                                                                           decimais                   código
                   a   o                                esquerda                   casas                                                             aplicar                formato à              valor 5                                  AAAAMMDD)                     com  do    ISOcom                                                                                                 casas                                                                                                                                       AAAAMMDD)                                  espaços    de                   6                                decimais                                                                                                                                  (anual)                                                                                        Mutuário   Mutuante                                                                                                                                                                                    (Garantia),                                                                                                                                                                                                                                                                                                                                                                                                                        “Taxa-Rem-Gar”,
                      IF                         IF                                                     máximo                                                                                                                                                          acordoDescrição                    utilizado                                                                                                                                                   2018                                                                                    de                                                          com             empréstimo,                                                                                                              (formato          for                                                          (14+5)                                                                                                             e/ou                                                                                                                                                                                                                                                                   remuneraçãocasas                      do                         do           dígitos)mobiliário-                                    encostado                                                   de                                                                                                                        (formato                                           do               com               unidades                        2          (se                 mobiliário:                                  de    (11     ser                                            UNIT:                                                           Colateral                                                                                                                                               Janeiro               de            valor                                                                             títulos  títulos                                                                                                                                                                                                                                                                                                   (percentagem)   com                                                                                    de                                                                                                              Abertura  Fecho do             remuneraçãoGarantia,                                                                                                                                moeda    BIC                             valorUNIT     para(formato:     doCVM       preenchido                      de de                         2                                     deda                   mínimo  de                        deverá de              de de  •     • •                                                          EUR,                                                                                                                                                                                                                                                                                                                                       “Data-Fecho”         MutuanteValMob/ISINQuantidade

                             ---              CódigoformatoestecampoTipo          Quantidade           Conta  Conta Data Data  Margemdecimais Taxavalor(percentagem)    Remuneraçãodecimais Valorem Tipo
                                                                                                                                                                                               alterar(EN)                          a
              Code                                     Date Date
Name                                                                                                                                   campo
                                                      doSTD                     Security                Quant-Type            Quantity                 Borrower-Acct    Lender-Acct   Opening  Closing    Margin                     Coll-Rem-Rate                     Loan-Rem-Rate             Min-Lend-Fee     Currency
                                                                                                             além
(PT)                                                                                                             para
                                                                                                                                        “A”),Name                                                                                                                                                                                                                                                                                                                        empréstimo)                                                                                                                                                                                                                                                                                                                                            empréstimo)
STD                                                         dede                                                           nº                                        Cod-Val-Mob                Tipo-Quant               Quantidade                  Conta-Mutuário     Conta-Mutuante      Data-Abertura   Data-Fecho    Margem                   Taxa-Rem-Gar                   Taxa-Rem-Emp          Valor-Min   Moeda    (função                                                            nº
                                                           do
                                                            do
Type   A  A  N A A D D N  N N N A        1-67-9                                                                                                                                                                                                                                                     alteração
                                                      de                                                                                                                                                                                                                                           (posição       12   04                      10 10 08 08  3+6     3+6    3+6   6+2  03                                                                                                                                                                                                                                                 (posição                              Funcional                                   14+5Length                                                                                                         caso
                                                      No

                           -                                                                                                                                                                                                                                                                                                                                                                                         Descrição

                                          -       34   46   50   69 79 89 97  105     114    123   132  140Position                                                                                                                                                                                                                                                                                            Num-PedidoNum-RespMutuário                                                                                                                                        Nota:campos: ---       SGE

## PDF page 28

               -
                                                           “A”)                                                                               digits)                                                      (3            digits)
                                                           “E”,                            (3
                                                                          (“I”,                                             Code                                                                                                                                                                                                       digits) Code                                                                                                                                                                                                                          digits)                                                            SGE                      (11                                                                                                                                                                               LendingBorrowing                                                                 SGE                         (11                                                            the                                                                                                                                             rejection      (Demand)                                                                                                                                      Amendment                                                                                                                 Interbolsa BIC                                                                                                                                (Offer)
                               of          by                                                                                                                                           Description             by  the                                                                       Interbolsa BIC                                                                                                                         Code:SecuritiesSecurities

                                   - -                                                               case             House                               in       BorrowingLendingInassigned                                                                                                                                                                                                                                                                                                  Reference                                                                                                                                                    Exclusion,                                                                                                                                                                                                                                                                                                                                                                                                                       identification:     identification:                                                                                   Type:                 --–ID    assigned Loan                 POH                                "SECL""SECB"                                          identification:     identification:
                                           ID the                                                                                                                                                                                                                                                                          Transaction                                                                              shown •••
                          • •                                              of                                                                                                                              Function:Inclusion,onlyRequest                  Request   Reply ID ISO                Borrower   Borrower  Lender  Lender Interbolsa

                              só

               -

                                                                                     26                                                           "A")                     SGE
                                                                SGE                                                           "E",             SGE       pelo                                                                              Página
              de                                  ("I",                       pelo                                                                                 pelo                           títulos                                                                                                                                                                                      títulos                                                                                                                                                                                                                                             dígitos)                                                                                                                                                                                                                       dígitos)                                                  de
                                                    de                                                           (3   dígitos)                                                              alteração,fecho                                                                                                                                     atribuído                                                      (3   dígitos)                                                                                                                                                                                                 atribuído       ISO:       e                                                                                                                                             rejeição.                                                                                                                                                                          2018                                                                                     (11     (11                                                                                                                                                                                     atribuído                                                                                                                  Descrição           Alteração
                               de                                            de                                                                                                                                                                               ProcuraOferta                                   – –                                                      Interbolsa                                                                                                  House                                                               caso                                                                                                                                Oferta,                                                                                                                                                                            resposta                                                                                                                                                                                                                                    empréstimo                                       Inpedido                                                                                                                                            Procura,                                                                 da         Janeiro                                                        abertura                                                                                                                                                                                                                         transação                                                      IF                                                           IF
                  -                   -                 -                                                                                                                                                                                                                                  Mutuário                                                                                                                                                                                                                                                        Mutuante                                                                                                                                      Exclusão,                                                                                     de                               no                                        de                                           de                                              de                                                                                                                    Pedido:                                          de:                 P                  O                   H                                                                                 cancelamento,                                                                                                                                                              Mutuário             Mutuante                                                      do                                                           do                                           2                                                         IF                                                              IF                                                de "SECL" "SECB"
                                 de
                  •••
                          • •                                                  registo,                                         FunçãoInclusão,indicada                                                                  Tipo                                                                                                                         Número  Número  Número  Código                                                                                                                                                                  Código doBIC  Código doBIC   Referência                                                                       dividendo,
            do
              de                                                   (EN)
                                         ID                                                                                               mobiliários.                                           ID                                                   Name                   ID                                      STD     Func                 Req.Type          Request  Reply Loan           ISO-Tx-Cod         Borrower    Borrower(BIC)  Lender    Lender(BIC)    IB-Reference                                                       valores                                                                              compensação                                    Empréstimo         acompanhamento                de
       de a                      (PT)
receção                                   permitegarantias,                  Name                      Gestão                                                                               empréstimo
              dede       de                de           STD     Func                 Ped.Tipo              Num-Pedido   Num-Resp   Empréstimo           ISO-Tx-Cod         Mutuário    Mutuário(BIC)   Mutuante    Mutuante(BIC)    Referencia-IB                                                  mensagem
               A  A A A A A A A A A A       SGESistemaSGEEstaatualizaçãooperações               Type



    =                                                                                                  ficheiro:      01    01   06 03 09  04  03 11 03 11 16          Funcional    =      =       do     Length
      SGE  =Ficheiros/mensagens –                                                                                                                                                                                                                                                                                                                                                               Descrição
                              01    02   03 09 12  21  25 28 39 42 53 -                                                                                                     Position3.2-   3.2.1     MnemónicaDenominação MenuDescrição                             Conteúdo                                                                                                                                SGE

## PDF page 29

                 or                                        will             or                     loan:
                         )                                                                                  settle                   reason“REJT”.        or                   =they                                 reply            to      or                                                                                                                                                                 maximum                                              places
                                                be                                                            request                                                                                                                       description )At                    for                                                                                                                                                                                  4*(7+1)         format

                         (                              request                                                                              successfully      failed                           may                                                                                                      codes                    CVM                   decimal                                                                                                          Code -   5                                                                                                                                               messagestransactionpresented,           8*(3+1)                                           rejected pendingconfirmation                 Close     Close                      (      ‘;’.                                                           are                                                                                                          ISIN                       or  or                                                                                               Opened Closed                      for                   confirmed                           - Code                                                 by                                                                                         alert                                                                         cash)                                                                                                                     UNIT                                                                                                                status     (Reason    “nnn;”Identifications.               “ABCDnnn;”Description                           or       the                                     Request Request                 Lending/borrowing    Loan Open    Open    Loan Loan        codes“;”.                                    Identifications                                                maximum     - - - - - - - -of                                                                                  (14+5)                        Reference                                                            when             Rule                          Code:                                                                        lending/borrowing               pending         cancelled                    by   times            times
                      8                                                                                               Ruleseparated4                                                                                                                                                               UNIT:
                      -                         -             the                                                                                                                     reason        separately).                                                                                              error
                      0                         0  Identification     Identification Type    Securities:of                                "REJT" "PEND"reply "CANC"Loan "CONF" "SETT"settled "NSET"(securities "OPEN" "CLOS"Codes
        of                                     of            Reference   Matching                                                                                                                                                          Business                       for(format:
      • • • • • • • •                                                                                                                                                                                        separated           •                                                                                                                                         several                          Business    T2S T2S   Status                                                                            ReasoncodesIfbeavailableFormat:T2S4presented,Format: Security   Security   Quantity   Quantity

                                    de                T2S.                 ou                                                                                                                                                                                                                                                              decimais   27                       ou         (Abertura                                                    resposta                   =             pelopodem       à                 cancelada                                                    códigos     códigos,                       ISIN CVM                                    ou                                                            (4*(7+1))                                             mobiliário: casas        Página                                                                                  confirmação                                                                                                                                                                        rejeitada                                                                                               aberto fechado                                                             ";"(7+1))         5       à cancelado,          confirmado  (Abertura                                                                                                                     vários                                                                                                                                                                                                               instrução                 formato                                                                                                                                                                                                  formato                                                                (8*                                                                                                                                                         valor de                                                                                                                                         Liquidaçãofinanceira)             aviso,ser  por                          -                            -                                          instrução:          pendente                             ou               daidentificação                           na      de                       de        ou                                                de                                                                                                          “nnn”                                                                                                                                                                                                                                                               “ABCDnnn;”                                                                                                                                    Procura/Oferta                                                                                                     sucesso.                                                                                                                                                                        2018                                                                                                                                                            enviados                             :                                                                                                                                                                                              máximoDescrição                                                                                                                     Liquidação                                                                     Falha                                                                                                      (física Empréstimo                                                                                                                                                                         Empréstimo                                                                                                                                                                        instrução                                                                                    de                   de Empréstimo                                                rejeitada                                                           pendente Empréstimo                                                                                                                                                                                                   (14+5)                                                           Instrução           -            -              -                -                 -                                                                                                                                                                                                                                                                        mobiliário   mobiliário UNIT     -                   a                      Matching         -                                                           serseparados                                      com       -                                                                                                          vezes                                                                                                                                                                                                                                                     unidades                                                                                                                               vezes                                                                                                                                                                       códigos                                     de  8                         4                          UNIT:                                                             de                    Janeiro    T2S T2S                                                                                                                                                                 mensagens     são–          Identificação4 –valor  valor                                          empréstimo                 resposta                                     Fecho)
                                                                                    de                                    de                     0 de  0                                “REJT" "PEND"ou "CANC"Instrução "CONF"  "SETT"Fecho)  "NSET"ou  "OPEN"  "CLOS"                                                                           casoPodem        de                                          2                                                     do do   quantidade       Para(formato:                                                                                  caso                                                          de      • • • • • • • •  no                         máximoapresentados                                 •             Referência   Referência   Estado                                                                                        Códigoserro“REJT”.nesteFormato:     CódigosNoserFormatoCódigo  Código Tipo      Quantidade
(EN)
                                                                                                                Code
NameSTD       T2S-Reference    T2S-Match-Ref                                        Status                                                   Reason                             Rsn-Descr           ISIN-Cod   Security   Quant-Type          Quantity

(PT)
Name
STD                      Referencia-T2S    Ref-T2S-Match                                        Estado                                                   Motivo                             Mot-Descr           Cod-ISIN  Cod-CVM   Tipo-Quant             Quantidade



  A A       A        A   A A A A NType
   16 16             04                 32       32   12 09 04                                        Funcional                                                                                                                              14+5Length
                                                                                                                                                                                                                                                                                                                                                                                         Descrição

                                          -   69 85                    101                         105          137    169 181 190    194Position                                                                                                                              SGE

## PDF page 30

                                                              places                                                                                      places                                                                         (Rate)                                        places            Borrower  Lender                            days     places     decimal  Fee                    (Rate)                4217                                                      Fee     the the      of   2                    decimal              2   Fee                decimal  ISO   of of                2                                                             decimal   with                    to          -            with         6     -                   Lending   with                                       YYYYMMDD)         number                                                  YYYYMMDD)             -
              in         Number  Number                   with                              Remuneration               theDescription
         -                                                      for                       according                            loan               Amount                                                                                      Amount              Remuneration                              (format                                       (format                                                                               Amount                     the                                                                                                         remarks           Account  Account                                                    Margin   Cash
              of                 Date                                                                                                                          Collateral                                           Fee     Loan   value  Fee   Code                      Date
                Securities   Securities   Opening  Closing   Duration        Collateral        Collateral      (Annual)            Collateral         (Annual)    Minimum     Lending      Currency   Processing



              2                                                          com
                                         casas              com                                               28
        6                                                                                      4217                                                                                  (anual)                                                                                                                                                                                    empréstimo                                                                                                              Página                         com                                            (percentagem)                                                                                   decimais                                                                                                                             garantia,      do    empréstimo,   ISO
                            da         do                                      AAAAMMDD)                                                  AAAAMMDD) dias             casas2   colateralGarantia                         empréstimo             com                       do       do            Mutuário   Mutuante      em    (Garantia),                         da                                                                                                    2018Descrição IF IF                    com                                                             acordo                                  (formato                                                                       de   do do                                                                                                                                                            remuneração                                             (formato                              valor                de             o    remuneração      de    remuneração                                                                          Colateral                                                                                                                                                                                                                      Janeiro                            da         da           títulos                    títulos                                                                     empréstimo                                                                                    de                do           Garantia,                                                                                                                                                                                 remuneração                                                                                                                                 remuneração                                  Abertura                            Fecho                                                                                                                                                                  decimais  moeda                                          2                                                               sobre   de      de              do                     da                                                                      finaldecimais                                da      mínimo  final                       da        de           de                                           de
                                                                                                     casas        Conta  Conta Data Data  Prazo  Margemdecimais  Valor Taxaaplicar  Valorcasas Taxa(percentagem) Valor  Valor2 Tipo    Observações
(EN)                                           Fee                 Date                                                            Fee                       DateNameSTD       Borrower-Acct    Lender-Acct   Opening  Closing   Duration    Margin        Collateral          Coll-Rem-Rate            Collateral               Loan-Rem-Rate        Min-Lend-Fee     Lending     Currency  Remarks

(PT)
Name
STD                      Conta-Mutuário     Conta-Mutuante      Data-Abertura   Data-Fecho  Prazo    Margem      Garantia         Taxa-Rem-Gar           Remun-Gar              Taxa-Rem-Emp      Valor-Min       Remun-Emp   Moeda    Observações



  A A D D N N N N N N N N A AType
                                           03 20                                                                                                               Funcional   10 10 08 08 05  3+6   12+2  3+6     12+2   3+6  6+2   12+2Length
                                                                                                                                                                                                                                                                                                                                                                                         Descrição

                                          -     213 223 233 241 249  254  263  277    286   300  309  317  331 334Position                                                                                                                              SGE

## PDF page 31

                                                                                                                                                                                digits)
                      (3                                                  (3              digits)
                                                        (3                                             Code                                                                                                                         format                                                                                                     Code                                                                                                                                                                                           digits)  Code                                                                                                                                             LendingBorrowing                                                      digits)     CVM                                                                               Record                                     (11      (11 Code -                                                                                                                Interbolsa                                                                                                                                                                                                                                                           Interbolsa  BIC              ISIN                                        the        (Demand)                                                                                                                                                                                                              confirmedOpened                                  Interbolsa  BIC - Code                          of             (Offer)                                                                                                             Description                                                                                                                                                                                                                   Securities                                                                                                Code:Securities                                                                                               Loan                             -   Loan
                    -                                                                                     House                       -                        -                                                                                                              loan:
                                  In                                                                                                                                                                         identification:      Number         BorrowingLending
                -                 –               -                                                                                                                                                                                                                                                                                                                                                                                         identification:        identification:                                                                  the
               P                O                 H                                                                                                                                                                                                                                                                                                                                                                                                                                       identification:        identification:     Identification     Identification                                                                        Loan         "SECL" "SECB"                                            of"CONF""OPEN"                                                                        Type:        the                                                                                                                                                                                                                   Transaction
                     • •                •••of                                                                                                                            Participantdigits.) Sequential Loan     ID ISO           Status                 Borrower    Borrower   Lender   Lender   Security   Security

                                                 (3    (3


                                                                                     29                                                                                                                Interbolsa                                                                                                                           ISIN CVM                                                                                                                                                                                                                                                       Interbolsa                     Interbolsa                                                                              pedido                                                                                                                                                       Página                                                        da      dígitos)                                                 da      dígitos)                                                                   Código de                                                                                                                                                                                                                                     confirmadoaberto           :                                                       títulos                                                                                                                                                                                                                        formato                                                                                                                                                                                                                                 formato                                                                               (11      (11                                                                                                                                                    títulos                               -
                                        de           -                                          de                Código            Código                                       encontram                                                      registo                                                                             ISO:                          do                                                                                                     2018         se                                         Descrição                                                                                                                                                                                                                    Mutuário                 Mutuante         de                                                                                                                                       Participante                                                        empréstimo         ProcuraOferta        EmpréstimoEmpréstimo                                                             mobiliário   mobiliário             que                                                           House   – – ––   IF    IF                      do           do                                                     Mutuário:                   Mutuante:                                                                                                          ProcuraOfertaIn                 do    do                                 Janeiro                                                 IF    IF          valor  valor               --–           transação                    empréstimo:
                                                 do  BIC do  BIC do do   de2                                                                                                                                  sequencial    empréstimo:POH  de "SECL" "SECB"do"CONF""OPEN"
                             de
                •••  • •                                                                                                 dígitos)                                               empréstimos                                                                                                                                                  Identificação(3Número Tipo                                 Identificação  Código           Estado          Códigodígitos)Código  Códigodígitos)Código  Código  Código
         os
                                        (EN)
                      todos                                                                                                            Code
         de                  Name              ID                  Pendentes                              STD        Participant    Seq-Num      Type      Loan           ISO-Tx-Cod           Status          Borrower       Borrower(BIC)   Lender      Lender(BIC)   ISIN-Cod   Security
                                           informação                  (PT)
    a                  Name                      Empréstimos    contém                                                              confirmados.           STD  IF    Num-Seq      Tipo              Empréstimo           ISO-Tx-Cod           Estado          Mutuário       Mutuário(BIC)    Mutuante       Mutuante(BIC)   Cod-ISIN  Cod-CVM    de
          ou                                  ficheiro
            N N A A A  A A A A A A A                                        Type      SGE-PNDOrdensSGEEsteabertos



  =                                                                         ficheiro:     03 06   01   09  04    04  03 11 03 11 12 09          Funcional  =    =      do     LengthSGE-PND  =–                                                                                                                                                                                                                                                                                                                                                                                    Descrição
                       01 04   10   11  20    24  28 31 42 45 56 68 -                                                                               Position3.2.2     MnemónicaDenominação MenuDescrição                       Conteúdo                                                                                                                                SGE

## PDF page 32

                                                                                                  places         decimals                    (Rate)
                   2                                       (format:          Borrower  Lender                                                                     Fee       (Rate)                                                                                                                4217                                                  days     places        decimal     with        Update)                                                                                Fee                     the the      of   2 -                                                                           Fee                                                                                    ISO                             places  of of                                                                                                                                                                                                                                                                       YYYYMMDD)                                                                                                   decimal     with                     to              6 -        settled                                                                                                                                                                                          Lending                                                                           number                                                                                         YYYYMMDD)                                                                                                                                                                                                                                    (Collateral                                                                                                    YYYYMMDD)      UNIT
                         in                                  decimal       Number  Number                                                         with       be                                        Remuneration        the            (formatDescription    5        -       to          -                                                                                for   according                                                  loan                  Amount                                                                                            Remuneration        Code:                                                   (format                                                                              (format                                                                             Indicator                                Securities:                          the                                                                                                                        remarks                    UNIT:               Account  Account                                                                                     Margin     Cash       Update                                                                                                                                     value Code  updated                                        Date   of                                                                                                                                                                                                                                     Collateral     Loan      Type of            formaximum(14+5)                 Date
                                                                                                                     last

    ••            Quantity   Quantity                                Securities   Securities   Opening  Closing   Duration        Collateral            Collateral            Collateral              Debit/Credit         (Annual)         (Annual)    Minimum   Currency Date   Processing



                  2
                                                      com  do                               30                                                                     casas      casas
              6 2                                                                                                                4217                                                                                                                                                                                                                                                                          empréstimo                                            (formato:                                         com    com                                                                                                                                                                                                                                          decimais                                                                                                                                                                                                          colateral            empréstimo                                                                                                                                                                   garantia,               do ISO                                     Página
                                             do  do                                                                                                                                                                                                                                                    (atualização                                                                                        AAAAMMDD)                                                  dias         da                                                                                    com  casas                                       decimais                                               AAAAMMDD)                 2                                   mobiliários:                                                         Mutuário                                                                    Mutuante                         em    (Garantia),           montante,     UNIT                                                                                                                                                                        2018
 :              IF                 IFDescrição                                em                                                                  acordo com                                                                                    de                         casas                                                                              (formato                                                                                                                                                                                                                                                                                                     remuneração
                                                        de     5  do do             (formato                                                                                                                  remuneração             remuneração                    valores                                                     de                                                                                                                                                                                                       remuneração                débito/crédito                    UNIT:                                                                               Colateral                                             de  de                                                                                                                                                                                                                                                                                                      Janeiro      de                                    da                                         de                                                  títulos  títulos                                                                                                                            empréstimo                                                                                                                                                                                                                                                                       Garantia,         de                            do         Garantia                                                                              Abertura  Fecho                                                                                                                                            moeda                                          2             quantidade       paramáximo(14+5))              de de                                                           da                    de de   de                         do     da      finaldecimais             anual      anual      mínimo de

    ••                                    Conta  Conta Data Data  Prazo  Margemdecimais  Valordecimais  Valorcasas   Indicadorcolateral) Taxa(percentagem) Taxa(percentagem) Valor Tipo  Valor    Observações     Tipo      Quantidade
(EN)
                                        Date                                             DateNameSTD      Quant-Type              Quantity                       Borrower-Acct    Lender-Acct   Opening  Closing   Duration    Margin            Collateral            Collat-Upd    D/C               Coll-Rem-Rate               Loan-Rem-Rate        Min-Lend-Fee  Currency   Date-Upd  Remarks

(PT)
Name
STD                Tipo-Quant                  Quantidade                         Conta-Mutuário     Conta-Mutuante      Data-Abertura   Data-Fecho  Prazo    Margem         Garantia            Atu-Garant    D/C              Taxa-Rem-Gar              Taxa-Rem-Emp      Valor-Min Moeda   Data-Alt    Observações



  A  N  A A D D N N N N A N N N A D AType



   04                                         01    3+6   3+6  6+2 03 08 20                         Funcional                 14+5              10 10 08 08 05  3+6     12+2     12+2Length
                                                                                                                                                                                                                                                                                                                                                                                         Descrição

                                          -   77    81     100 110 120 128 136  141    150    164    178    179   188  197 205 208 216Position                                                                                                                              SGE

## PDF page 33

                                                          dig.)                                                                                                          digits)
                       (3                                                        (3              digits)
                                                              (3                                               Code                                                                                                               Code                                                                                                                                                                                                                                YYYYMMDD)  hhmmss)              digits)  Code                                                                                                                                                                                                                                   digits)
                                                                                        (11                                                                                                                                             LendingBorrowing                                                                               Record                                                       (11                                                                                                                     Interbolsa                                                                                                                                                                               (format  (format     Interbolsa  BIC                                        the        (Demand)                                        closedcancelled - -                                                                                                                                                                                                                                                                                                                     Interbolsa  BIC                          of             (Offer)                                                                                                             Description                                                                                                Code:SecuritiesSecurities   LoanLoan                                                                                     House   - - -- update  update                                                                                                              loan:
                                  In                                                                                                                                                                               identification:   Number         BorrowingLending
               --–                                                                        Loan         the                                                                        identification:        identification:               POH               "SECL" "SECB"of"CLOS""CANC" Status  Status                                                      identification:        identification:                                                                        Type:        the            of of                                                                                                                                                                                                                   Transaction
                     • •                •••of                                                                                                                                Participant     Sequential Loan     ID ISO           Status        Date Time    Borrower    Borrower   Lender   Lender

                                                       (3    (3


                                                                                     31                                                                                                                Interbolsa                                                                                                                                                                                                                                                                                  Interbolsa                     Interbolsa                                                                              pedido                                                                                                                                                       Página                                                                                                                                                                                                                                AAAAMMDD) hhmmss)                                                             da      dígitos)                                                       da      dígitos)         ou                                    Código de           :                                                       títulos                                                                                                                                                                fechadocancelado                                                                                       (11      (11                                                                                                                                                    títulos
                                        de                                                                                           registo              de                       (formato (formato  Código            Código                                                                             ISO:     – –                                                                                                                                                                          2018                          do                                  fechados                                         Descrição                                                                                                                                                                                                                                         Mutuário                 Mutuante   de                                                                                                                                       Participante                                                        empréstimo         ProcuraOferta                                                                                                                                                                                                                                     Empréstimo                                                                                                                                                                                                                                              Empréstimo                                                          IF                                                                IF                                                                                      House                      foram
                       –                        – estado estado   Mutuário:                                                                                                                                                                                                                                                                                  Mutuante:                      do                                    do  – –                                                                                                 Oferta                                  In                                                          do                                                                do          Janeiro                                                                                                          Procura                                                                                                                                                                             transação                                                             IF                                                  do do IF                ––               -                                                                                                                                                                                                                                                  empréstimo:             que
                                                       do  BIC do  BIC   de2                                                                                                                                  sequencial    empréstimo:POH  de "SECL" "SECB"do                                                                                                                                        "CLOS""OPEN" atual atual                             de
                •••  • •                                                                                                 dígitos)      dia                                                                                                                                                  Identificação(3Número Tipo                                 Identificação  Código           Estado        Data Hora  Códigodígitos)Código  Códigodígitos)Código    do       empréstimos
         os                  (EN)
                      todos                  Name              ID            Resumo
         de
  –                              STD        Participant    Seq-Num      Type      Loan           ISO-Tx-Cod           Status         Stat-Date   Stat-Time    Borrower       Borrower(BIC)   Lender      Lender(BIC)

                                        (PT)                                           informação                                              anterior.                                        Name
               dia                      Empréstimos                          contém          no           STD    de                IF    Num-Seq      Tipo              Empréstimo           ISO-Tx-Cod           Estado        Data-Est   Hora-Est    Mutuário       Mutuário(BIC)    Mutuante       Mutuante(BIC)
                                  ficheiro
            N N A A A  A A A A A A A                                        Type      SGE-RESOrdensSGEEstecancelados



  =                                                                         ficheiro:     03 06   01   09  04    04  08 06 03 11 03 11          Funcional  =    =      do     LengthSGE-RES  =–                                                                                                                                                                                                                                                                                                                                                                                    Descrição
                       01 04   10   11  20    24  28 36 42 45 56 59 -                                                                               Position3.2.3     MnemónicaDenominação MenuDescrição                       Conteúdo                                                                                                                                SGE

## PDF page 34

                                                                                                                 places                                                                                                                                        places                                                                                                                           (Rate)                                        places                 format                              (format:          Borrower  Lender                                                             days     places     decimal  Fee                    (Rate)                4217                                                                               Fee                              the the      of   2                    decimal                       2   Fee                decimal                                                                                          ISO      Code CVM-                       places   of of                            2                                                                                                                       decimal   with                    to      ISIN                -            with                 6     -                   Lending   with                                                                                            number                                                                                                                   YYYYMMDD)  - Code
                            -                                                                                                                              YYYYMMDD)                 UNIT
                               in                                                      decimal        Number  Number                                                                    with                              Remuneration               theDescription       5        -                                                                               for                       according                                                             loan               Amount                                                                                                                                        Amount              Remuneration                     Code:                                                    (format                                                                                                  (format                                                                               Amount                                  UNIT:                                                                      Account  Account                                                                                                      Margin   Cash
                               of                                                   Date                                                                                                                                                                                                              Collateral                      Identification     Identification Type     Securities:of                          the                                                                                                         remarks                                                                    Fee     Loan   value  Fee   Code                                                        Date                    formaximum(14+5)



       ••            Security   Security   Quantity    Quantity                                 Securities   Securities   Opening  Closing   Duration        Collateral        Collateral      (Annual)            Collateral         (Annual)    Minimum     Lending      Currency   Processing



                                        do                                                                                   casas         do                          32                                                                                                                                           casas
                 6
                            2     ISIN CVM                                                                                                         4217                                                                      (formato:                                                                                                                                                                                                                                                                        empréstimo                                                Página                                                  com                                                                                                                                                      decimais   colateral                                 empréstimo       com                                                                                          ISO                                                     do –
                                        do       do         formato  formato                                                                                                                                                                                                                                                                            (atualização - -                                                                                 AAAAMMDD)                                                                                          com                                                             dias             casas                                                              decimais                                               AAAAMMDD)    2                                                                   mobiliários:                           Mutuário                                                                                          Mutuante                               em    (Garantia),                UNIT                                                                                                                                                                        2018
    :                    IF                       IFDescrição                                                        com                                                             acordo                                                                                    de                                       casas                                                                                                     (formato                                                                                                                                                                                                                                                                                                   remuneração   empréstimo             mobiliário   mobiliário        5  do do                                                            de                                                                                                                (formato                                                         remuneração                                     remuneração                                                        do                                       valores                                                     de                                 UNIT:                                                                                 Colateral     de(percentagem)     débito/crédito  de                                                                         Janeiro           de       valor  valor                                             de                                                                      títulos  títulos                                                                                                                                                         empréstimo                                                                                    de                                 do           Garantia,                                                                                                     Abertura  Fecho                                                                                                                                                      moeda                                          2   do do   quantidade       para máximo(14+5))                    de de                         de de        de                               do     da  anual                 anual      mínimo     de

       • •        Código  Código Tipo      Quantidade                 Conta  Conta Data Data  Prazo  Margemdecimais  Valor Taxaempréstimo   Indicadorcolateral) Taxa(percentagem) Valor    Remuneraçãodecimais Tipo    Observações
(EN)
            Code                                   Date Date                       Fee              FeeNameSTD    ISIN-Cod   Security   Quant-Type               Quantity                        Borrower-Acct    Lender-Acct   Opening  Closing   Duration    Margin        Collateral          Coll-Rem-Rate            Collateral               Loan-Rem-Rate        Min-Lend-Fee     Lending     Currency  Remarks

(PT)
Name
STD            Cod-ISIN  Cod-CVM   Tipo-Quant                   Quantidade                          Conta-Mutuário     Conta-Mutuante      Data-Abertura   Data-Fecho  Prazo    Margem      Garantia         Taxa-Rem-Gar           Remun-Gar              Taxa-Rem-Emp      Valor-Min       Remun-Emp   Moeda    Observações



  A A A  N  A A D D N N N N N N N N A AType



   12 09 04                                                            03 20                  Funcional                            14+5                    10 10 08 08 05  3+6   12+2  3+6     12+2   3+6  6+2   12+2Length
                                                                                                                                                                                                                                                                                                                                                                                         Descrição

                                          -   70 82 91    95      114 124 134 142 150  155  164  178    187   201  210  218  232 235Position                                                                                                                              SGE

## PDF page 35

                                                                                            places
                                                                                  format                                                                                     Date   Date                                                                                                                                                                           (YYYYMMDD)                                                                                                            decimal                                                 Code CVM- 4                    from    until
                                                                                                       Action                                                 ISIN                                                                                                   (Y/N)  SGE  SGE            - Code   with-
                                                                for  for                                                                                      Corp.                                                                                                                      Description           EUR
                               in                                                                     next               indicator                                                                                                               (CAEV)                                                                                                                                                                            Identification     Identification                                                                   authorized       authorized                                                                     Date                                                                          Code                                                                                                                                           quotation                                                                                                  Security   Security   Last     Record  Event    Authorization    Security      Security



                       à
                                                                                                         desde  até                          33
                                                ISIN CVM
                                                                           casas               SGE  SGE                                                                               Página
                     o o
               4                                                                                                                                                                         (AAAAMMDD)                                                                                     formato  formato                                                                                    para   para                      assimevento      – –  com               –                  (S/N)
          do                 SGE,                                                                                             direitos                                                                                 2018                                             EUR                                                                                                 Descrição          de  (CAEV)                                     de         no                                                                                                                         mobiliário   mobiliário                               código                              em                                                  autorizado       autorizado     o                                                                                                                                                    autorização     e                              valor  valor                       evento                                                                                                                                   Janeiro                                       de                                                                                                                                                        Exercício                                         de                        do do                                     do                                           2                                                                                                         cotação                                            de                                                                                                                                                                                                                 mobiliário                                                                                                                                                                                                                                   mobiliário                                  do                                               de                                               autorizados                                              anterior)                                                              data                                                                         Código  Código   Últimadecimais Data  Código   Indicador  ValoraValordata
               dia
          do                                               mobiliários                      (EN)                                                       Code                          fecho                                            Date                                           Name                                  Quotation                      Autorizados     valoresde                                    date).                                STD    ISIN-Cod   Security   Last    Record CAEV Auth     From-Date     To-Date             dos
                                          (record                      lista(cotação                                           (PT)
    a                        data                      Mobiliários                                           Name                      Date                                    cotação                          contém                                STD                                                      respetiva                                           Cod-ISIN  Cod-CVM          Ult-Cotação    Record CAEV Aut   Desde  Até              Valores         últimae
  –  a                                  ficheiro
            A A N A A A A A                                           Type      SGE-SECSGESGEEstecomo,previsto



  =

  =                                                                                 ficheiro:     12 09  6+4  08 04 01 08 08                                                                                                                  Funcional    =       do     LengthSGE-SEC  =–                                                                                                                                                                                                                                                                                                                                                                                    Descrição
                         01 13  22  32 40 44 45 53             -                                                                                      Position                                                                                                                                SGE3.2.4     MnemónicaDenominação MenuDescrição                             Conteúdo

## PDF page 36

                                                                                                                                             Portuguese            English
                            in   in
                                                                             shown)          shown)                                                         code       code
                                                   (not       (not
                                      ';'     ';'                                                                                     reason          reason                                                                                                             Description
                                          the     the
                            of   of                                                                                                                   character               character                                              Code
                                                                     Reason   Separator    Description   Separator    Description

                                                                                                     visível)             visível)                                             34             é  é                                                                                                                                      Página
                                                  (não       (não                                      “;”   Português “;”  Inglês                                  mensagem                            em   em                                                                                   2018
         na                                                                                         Descrição                                                          de      SGE                                                                                 separador  código   separador  código                                                                   motivo do do do do                                                                                                                                                 Janeiro
                                                                                     de                                           informados
                      do   caracter             caracter                      2                mensagem    codes)                                    Código O   Descrição O   Descrição

                            PT   EN    na     (reason                  (EN)
                                        Name                    utilizados     motivos              STD   Reason                  Description                  Description

                                        (PT)          codes delista
    a                  PT   EN
                                        Name            reason    contém                              STD                                                                     Motivo               Descrição               Descrição
    de     ficheiro
           N A A  A                                        Type     SGE-RCTabelaSGEEsteSGE



  =                                                                         ficheiro:     03 01 96 01 96                                                                                                                                                                                        Funcional  =    =      do     LengthSGE-RC  =–                                                                                                                                                                                                                                                                                                                                                                                    Descrição
                       01 04 05 101 102                                                                               Position3.2.5     MnemónicaDenominação MenuDescrição                       Conteúdo                               -                                                                                                                                SGE

## PDF page 37

Tabela de motivos utilizados na mnemónica SGE

 Estado  Motivo                 Descrição                                 Description
MACH     003    Instrução matched, aguarda liquidação          Instruction matched, waiting for settlement
 LACK,
 CLAC,
NSET      004    Falha de liquidação física                         Fail on securities settlement
MONY,
AWMO,
NSET      006    Falha de liquidação financeira                    Fail on cash settlement
CANC      011    Cancelado pela Interbolsa                    Cancelled by Interbolsa
PEND      071    Instrução de pedido registada               Request instruction registered
                     Instrução de pedido registada pela           Request instruction registered by the
PEND      072    contraparte                                   counterparty
PEND      073    Instrução de resposta registada              Reply instruction registered

                     Instrução de resposta registada pela          Reply instruction registered by the
PEND      074    contraparte                                   counterparty
CONF      075    Empréstimo confirmado, aguarda liquidação   Loan confirmed, awaiting settlement
CONF      076    Empréstimo in-house confirmado             In-House Loan confirmed
CONF      077    Registo bilateral                                   Bilateral registry
CANC      080    Instrução de resposta cancelada              Reply instruction cancelled
                     Instrução de resposta cancelada pela         Reply instruction cancelled by the
CANC      081    contraparte                                   counterparty
CANC      082    Instrução de pedido cancelada               Request instruction cancelled
                     Instrução de pedido cancelada pela           Request instruction cancelled by the
CANC      083    contraparte                                   counterparty
                  Cancelamento do pedido de alteração não
CANC      084    confirmado                                Unconfirmed modification request cancelled
CONF,
OPEN      085    Valor da Garantia alterado                       Collateral value modified
CANC      086    Cancelado por evento                        Cancelled due to Corporate Action
CONF,            Pedido de alteração da data de fecho
OPEN      089    registado                                    Closing date modification request registered
CONF,            Pedido de alteração da data de fecho          Closing date modification request registered
OPEN      090    registado pela contraparte                  by the counterparty
CONF,            Pedido de alteração da taxa de remuneração   Collateral remuneration fee modification
OPEN      091   da garantia registado                         request registered
CONF,            Pedido de alteração da taxa de remuneração   Collateral remuneration fee modification
OPEN      092   da garantia registado pela contraparte         request registered by the counterparty
CONF,
OPEN      093    Data de fecho alterada                        Closing date modified
CONF,
OPEN      094   Taxa de remuneração da garantia alterada      Collateral remuneration fee (rate) modified
                Compensação de dividendo, do mutuário      Dividend payment compensated from the
OPEN      095    para o mutuante                             borrower to the lender
                     IF a registar diferente do IF STD (IF não        Registering FI different from STD (FI not
REJT      100    autorizado para registar esta operação)        authorized to register this operation)
REJT      119    Quantidade inválida                              Invalid quantity
REJT      120    Tipo de quantidade inválido                    Quantity type indicator invalid
                  Quantidade deve ser múltiplo do Multiple       Quantity not multiple of Multiple Settlement
REJT      122    Settlement Unit                                 Unit
                Número de casas decimais na Quantidade    Number of decimal digits in Quantity invalid
REJT      127    inválido para este valor mobiliário                 for this security
REJT      149   Moeda inválida                                    Invalid currency
                  Quantidade deve ser maior que o Minimum     Quantity less than Minimum Settlement
REJT      166    Settlement Quantity                           Quantity

  SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 35

## PDF page 38

Estado  Motivo                 Descrição                                 Description
REJT      302   Função inválida (I, E, A)                          Invalid function (I, E, A)
REJT      303    Tipo de pedido inválido (P, O, H)                 Invalid request type (P, O, H)
               Não pode ser preenchida num. resposta sem
REJT      304   num. pedido                               Reply ID specified without Request Id
REJT      305   Num. pedido não numérico/inválido              Invalid Request Id
REJT      306   Num. resposta não numérico/inválido            Invalid Reply Id
               Num. pedido/num. resposta obrigatório para   Request ID and/or Reply ID mandatory for
REJT      307    esta função                                          this function
               Num. empréstimo obrigatório para esta
REJT      308    função                                 Loan ID mandatory for this function
                                                                    Security code (ISIN or CVM format)
REJT      309    Valor Mobiliário ou Código ISIN obrigatório     mandatory
                                                                    Security not authorized for Lending &
REJT      310    Valor Mobiliário não autorizado para SGE      Borrowing
                    Valor Mobiliário/Código ISIN não autorizado
REJT      312    para novos empréstimos                       Security not allowed for new loans
REJT      314    IF Mutuário obrigatório                      Borrower participant must be specified
                     IF Mutuário só pode ser igual ao IF Mutuante   Borrower and Lender may only be the same
REJT      315    para operações in-house                         participant for In House L&B instructions
                     IF Mutuário não autorizado para operações    Borrower not authorized for Lending &
REJT      316   SGE                                       Borrowing
REJT      317    IF Mutuante obrigatório                     Lender participant must be specified
                     IF Mutuante não autorizado para operações
REJT      319   SGE                                     Lender not authorized for Lender & Borrowing
REJT      321    Conta-Mutuário inválida                          Invalid Borrower account
REJT      322    Conta-Mutuário não existe                   Borrower account does not exist
REJT      324    Conta-Mutuante inválida                          Invalid lender account
REJT      325    Conta-Mutuante não existe                  Lender account does not exist
                     IF Mutuante inválido para empréstimo in-
REJT      326   house                                             Invalid Lender for In House L&B instruction
REJT      328    Data Abertura não é dia útil                 Opening date is not a settlement day
                 Data Abertura inválida/não pode estar no
REJT      329   passado                                 Opening date invalid, may not be in the past
                 Data Abertura pode estar no máximo 20 dias   Opening date may be at most 20 business
REJT      330    úteis no futuro                             days in the future
                 Data Fecho não pode ser antes da data de     Closing date may not be before the Opening
REJT      333    Abertura                                    date
                 Data Fecho pode estar no máximo 2 anos no   Closing date may be at most 2 years in the
REJT      334    futuro                                            future
                 Data de Fecho inválida: ciclo de fecho já       Closing date invalid: closing cycle already
REJT      335    executado                                 executed
                 Data de Abertura inválida. Já não pode       Opening date invalid: settlement today not
REJT      336     liquidar hoje                                   possible anymore (after DVP cut-off)
                Taxa anual de remuneração do empréstimo
REJT      343    inválida                                            Invalid (Annual) Loan remuneration fee (rate)
                    Valor mínimo de remuneração do
REJT      344    empréstimo inválido                              Invalid Mininum lending Fee
REJT      345   Margem da garantia (colateral) inválida          Invalid Collateral margin
REJT      346   Taxa de remuneração da garantia inválida      Invalid Collateral remuneration fee (rate)
                 Poderão ser alteradas: Data Fecho ou Taxa     Attributes that can be modified: Closing date
REJT      347   de Remuneração da Garantia                   or Collateral remuneration fee
REJT      348    IF não pode responder ao pedido do próprio    Participant may not reply to own request
REJT      349   Não preencher conta contraparte           Do not specify counterpart account
REJT      400   Num. pedido não existe                    Request ID does not exist
REJT      401   Num. resposta não existe                    Reply does not exist
REJT      402   Num. empréstimo não existe                Loan ID does not exist
REJT      403    Pedido não está pendente                  Request not pending
 SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 36

## PDF page 39

Estado  Motivo                 Descrição                                 Description
REJT      404    Tipo registado diferente                    Request type is different
REJT      405    IF Contraparte inválido                           Invalid Counterpart participant
                    Valor Mobiliário/Código ISIN registado
REJT      406    diferente                                    Registered Security code is different
REJT      407    Quantidade registada diferente                Registered Quantity is different
REJT      408    Data Abertura registada diferente              Registered Opening date is different
REJT      409    Resposta não está pendente                 Reply not pending
REJT      410    IF Mutuário registado diferente                Registered Borrower is different
REJT      411    IF Mutuante registado diferente                Registered Lender is different
REJT      412    Conta do IF Mutuário registada diferente        Different Borrower account registered
REJT      413    Conta do IF Mutuante registada diferente       Different Lender account registered
REJT      414    Data Fecho registada diferente                  Different Closing date registered
                Taxa anual de remuneração do empréstimo     Different (Annual) Loan remuneration fee
REJT      415    registada diferente                              registered
                    Valor mínimo de remuneração do
REJT      416    empréstimo registado diferente                  Different Mininum lending Fee registered
               Margem da garantia (colateral) registada
REJT      417    diferente                                          Different Collateral margin registered
                Taxa de remuneração da garantia registada     Different Collateral remuneration fee
REJT      418    diferente                                       registered
                                                                 Status of the loan does not permit
REJT      419    Estado do empréstimo não permite alteração  amendment
                  Pedido de alteração está aguardar              Modification request is awaiting confirmation
REJT      420    confirmação pela contraparte                 from the counterparty
                   Diferença com o pedido de alteração da data   Different Closing date in pending modification
REJT      421   de fecho pendente                            request
                   Diferença com o pedido de alteração da taxa    Different Collateral remuneration fee in
REJT      422   de remuneração garantia pendente           pending modification request





 SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 37

## PDF page 40

4 – ANEXOS

4.1- Janelas STD – SGE (Exemplos)

4.1.1 – SGEmsg





4.1.2 – SGE





4.1.3 – Ficheiro SGE-PND





4.1.4 – Ficheiro SGE-RES





SGE - Descrição Funcional                                                        2 de Janeiro de 2018          Página 38