# security-lab
Iniciando estudo de lab em cybersecurity

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

**Primeira tentativa via FTP:** O FTP (File Transfer Protocol ou Protocolo de Transferência de Arquivos) é um protocolo de rede padrão usado para enviar e receber arquivos entre um computador (cliente) e um servidor pela internet ou em redes locais.
Iremos verificar se existe alguma porta aberta típica FTP: 21,22,80,445,139

**1. Varredura de rede e enumeração
Utilizaremos NMAP, já instalado no KALI. O Nmap é uma ferramenta de cibersegurança usada para escanear redes, identificar dispositivos conectados e verificar portas abertas em sistemas remotos.

```bash
nmap -v -sV -p 21,22,80,445,139 192.168.56.101
```
Ao identificar alguma porta FTP aberta, podemos verificar via FTP, mas não temos o id, nem o password

```bash
ftp 192.168.56.101
```













