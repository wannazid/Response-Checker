![alt text](https://github.com/wannazid/Response-Checker/blob/main/img.jpg)
# Response Checker
Response Checker merupakan tool berbasis CLI yang berfungsi untuk mendapatkan beberapa informasi header, sni, open port suatu website.
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
```
python3 Hostresp.py -s [domain] -r [filesresult]
```
- Example
```
python3 Hostresp.py -s axis.co.id -r hasil.txt
```
## Multi Target
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
[*] axis.co.id |http_status_code|server_name|open_port|protocol_version|
```
# Support 
Dengan star dan memakai tool ini sudah sangat mensupport saya:)
