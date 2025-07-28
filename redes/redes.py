"""ID é quando os octetos do host estão zerados
broadcast é quando os octetos do host então maximizados (255)

tipo C:
excemplos 192.168.0.0 ID
192.168.0.255 Broadcast

sempre menos 2(ID e Broadcast que são reservados) para fazer o calculo de quantas maquinas podem receber os IPs = 2^8 = 256-2 = 254

Mascara default maximiza a rede e zera os hosts EX: R  R  R  H  ||R R H H|| R  H  H  H
                                                  |255|255|255|0||255|255|0|0||255|0|0|0|

quantidades max de IPs em uma maquina, do 1 ao 254.

"""