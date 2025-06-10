from fastapi import FastAPI, HTTPException
import schemas
app = FastAPI()


books = {}

# crud.py
@app.post("/books")
def create(book: schemas.Book):
    id = book.id
    title = book.title
    author = book.author
    year = book.year
    if id in books:
        raise HTTPException(status_code=409, detail="Item exists")
    books[id] = book
    return {"message": f"Added {id} to items."}

@app.get("/books")
def get_books():
    return books
@app.get("/books/{id}")
def get(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[id]

@app.put("/books/{id}")
def update(book: schemas.Book):
    if book.id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book.id] = book

@app.delete("/books/{id}")
def delete(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[id]