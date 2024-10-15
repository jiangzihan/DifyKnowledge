from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


class RetrivalSetting(BaseModel):
    top_k: int
    score_threshold: float

class RetrievalRequest(BaseModel):
    knowledge_id: str
    query: str
    retrival_setting: RetrivalSetting

class Record(BaseModel):
    content:str
    score:float
    title:str
    metadata:str

class RespRecords(BaseModel):
    records: Record

@app.post("/retrieval", response_model=RespRecords)
async def retrieval(
    data:RetrievalRequest,
    authorization:str = Header(None),
):
    print("获取token: %s"%authorization)
    print("获取data: %s"%data)
    return RespRecords(
        records=Record(
            content="Title: Go Pet Club 32' Soft Collapsible Dog Crate, Portable Pet Carrier, Thick Padded Pet Travel Crate for Indoor & Outdoor, Foldable Kennel Cage with Durable Mesh Windows, Brown ",
            score=0.2,
            title="product info",
            metadata="product: ABC"
        )
    )
