import fastapi
import uvicorn

print("Hello")

#create microservices instance
api = fastapi.FastAPI()

@api.get("/")
def index():
    return {"msg":"This is landing page"}


@api.get("/api/endpoint")
def endpoint():
    return {"msg": "Hello Fast Api"}




uvicorn.run(api) #run the instance
