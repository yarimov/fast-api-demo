from fastapi import FastAPI
# import uvicorn

app = FastAPI(
    title="FastApi"
)


@app.get("/")
# Параметры пути
def get_hello():
    return "Hello world!"

#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
