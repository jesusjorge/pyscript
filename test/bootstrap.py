import asyncio
from pyodide.http import pyfetch
async def main():
    exec(await (await pyfetch("https://raw.githubusercontent.com/jesusjorge/pyscript/main/test/target.py")).string(),globals())
asyncio.ensure_future(main())
