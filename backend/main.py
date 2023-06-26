"""Run fastapi server
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Simple hello world

    Returns:
        json: hello world
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query: str = None):
    """Get an item

    Args:
        item_id (int): id number of an item
        query (str, optional): url query value. Defaults to None.

    Returns:
        json: item id and query values
    """
    return {"item_id": item_id, "query": query}
