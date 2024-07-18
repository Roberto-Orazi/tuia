# Movie App

Como hacemos para correr el cliente y el servidor?
Cliente:
```bash
python front.py
```

Servidor:
```bash
uvicorn back:app --reload --host 0.0.0.0 --port 8000
```



Creamos un entorno virtual:
```bash
python3 -m venv myenv
source myenv/bin/activate # lo activamos
pip install requests fastapi httpx pydantic # instalamos las librerias que vamos a usar
sudo apt-get install python3-tk # Tkinter lo instalamos asi porque no se puede instalar mediante pip
```

Para verificar las versiones usamos vamos a usar:
```bash
pip list
# Y nos va a devolver esto:
Package            Version
------------------ -----------
annotated-types    0.7.0
anyio              4.4.0
asttokens          2.4.1
certifi            2024.7.4
charset-normalizer 3.3.2
click              8.1.7
comm               0.2.2
debugpy            1.8.1
decorator          5.1.1
dnspython          2.6.1
email_validator    2.2.0
executing          2.0.1
fastapi            0.111.1
fastapi-cli        0.0.4
h11                0.14.0
httpcore           1.0.5
httptools          0.6.1
httpx              0.27.0
idna               3.7
ipykernel          6.29.4
ipython            8.25.0
jedi               0.19.1
Jinja2             3.1.4
jupyter_client     8.6.2
jupyter_core       5.7.2
markdown-it-py     3.0.0
MarkupSafe         2.1.5
matplotlib-inline  0.1.7
mdurl              0.1.2
nest-asyncio       1.6.0
packaging          24.1
parso              0.8.4
pexpect            4.9.0
pip                24.0
platformdirs       4.2.2
prompt_toolkit     3.0.47
psutil             5.9.8
ptyprocess         0.7.0
pure-eval          0.2.2
pydantic           2.8.2
pydantic_core      2.20.1
Pygments           2.18.0
python-dateutil    2.9.0.post0
python-dotenv      1.0.1
python-multipart   0.0.9
PyYAML             6.0.1
pyzmq              26.0.3
requests           2.32.3
rich               13.7.1
shellingham        1.5.4
six                1.16.0
sniffio            1.3.1
stack-data         0.6.3
starlette          0.37.2
tornado            6.4.1
traitlets          5.14.3
typer              0.12.3
typing_extensions  4.12.2
urllib3            2.2.2
uvicorn            0.30.1
uvloop             0.19.0
watchfiles         0.22.0
wcwidth            0.2.13
websockets         12.0
```