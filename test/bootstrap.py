#https://pyscript.net/examples/repl.html
#
# Al ejecutar este codigo en el REPL de PyScript, Python descarga el contenido de un URL, e inmediatamente ejecuta su codigo
#

import asyncio
from pyodide.http import pyfetch
async def main():
    exec(await (await pyfetch("https://raw.githubusercontent.com/jesusjorge/pyscript/main/test/target.py")).string(),globals())
asyncio.ensure_future(main())
