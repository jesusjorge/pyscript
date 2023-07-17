#https://pyscript.net/examples/repl.html
#
# Al ejecutar este codigo en el REPL de PyScript, Python descarga el contenido de un URL, e inmediatamente ejecuta su codigo
# En el caso de GitHub, no necesita ninguna consideración especial con CORS
# No es el mismo caso con otros sitios (http://checkip.dyndns.org).
#   Para tales propositos, se podria utilizar un proxy de CORS (https://corsproxy.io/)
#   ej. https://corsproxy.io/?http%3A%2F%2Fcheckip.dyndns.org
#EOHC END OF HEADER COMMENTS

import asyncio
from pyodide.http import pyfetch
async def main():
    exec(await (await pyfetch("https://raw.githubusercontent.com/jesusjorge/pyscript/main/test/target.py")).string(),globals())
asyncio.ensure_future(main())
