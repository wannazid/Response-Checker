![alt text](https://github.com/wannazid/Response-Checker/blob/main/img-tool.jpg)
![](https://img.shields.io/badge/HostResponse-Version%202.0-orange)
# Response Checker
Response Checker merupakan tool berbasis CLI yang berfungsi untuk mendapatkan beberapa informasi header, sni, open port suatu website.
# Apa yang baru?
- Support input ip address in single/multi
- Add result ip address domain
- Code adjustments
# Cara Install
- Gunakan terminal contohnya jika di android : Termux.
- Masuk Termux masukan command.
```
pkg update && pkg upgrade
```
- Install Python,Git,PIP (Termux)
```
pkg install python && pkg install git && pkg install python-pip
```
- Clone Repository
```
git clone https://github.com/wannazid/Response-Checker
```
- Masuk Repository
```
cd Response-Checker
```
- Install Requirement
```
pip install -r requirements.txt
```
- Berhasil, tinggal mau pake mode single/multi
# Mode
## Single Target
Single target untuk 1 yang di scan ip maupun domain.
```
python3 Hostresp.py -s [domain] -r [filesresult]
```
- Example
```
python3 Hostresp.py -s axis.co.id -r hasil.txt
```
## Multi Target
Multi target sangat cocok untuk scan banyak domain/ip dengan memasukannya dalam list txt files.
```
python3 Hostresp.py -m [filestarget] -r [filesresult]
```
- Example
```
python3 Hostresp.py -m domain.txt -r hasil.txt
```
## Proxy Mode (Opsional)
Gunakan -proxy [ip:port] jika ingin get menggunakan proxy
- Example
```
python3 -s axis.co.id -r hasil.txt -proxy 123.123.123:8080
```
# Fitur
- [-s] Single target
- [-m] Multi target
- [-r] Saving result
- [-proxy] Use proxy get (opsional)
- Fast checking (use thread)
# Format Result
```python
[*] axis.co.id|ip_web|http_status_code|server_name|open_port|protocol_version|
```
# Support 
Traktir buat semangat buat tool menarik lainya, terimakasih.
- https://sociabuzz.com/wannazid
