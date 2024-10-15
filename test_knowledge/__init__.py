from fastapi import FastAPI, Header, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


class RetrivalSetting(BaseModel):
    top_k: int
    score_threshold: float

class RetrievalRequest(BaseModel):
    knowledge_id: str
    query: str
    retrieval_setting: RetrivalSetting

class Record(BaseModel):
    content:str
    score:float
    title:str
    metadata:str

class RespRecords(BaseModel):
    records: List[Record]


@app.post("/retrieval", response_model=RespRecords)
async def retrieval(
    request:Request,
    data:RetrievalRequest,
    authorization:str = Header(None),
):
    print("原始请求头: %s"%request.headers)
    print("原始消息: %s"%await request.body())
    print("获取data: %s"%data)
    return RespRecords(
        records=[
            Record(
                content="Title: Go Pet Club 32' Soft Collapsible Dog Crate, Portable Pet Carrier, Thick Padded Pet Travel Crate for Indoor & Outdoor, Foldable Kennel Cage with Durable Mesh Windows, Brown ",
                score=0.2,
                title="product info",
                metadata="product: ABC"
            ),
            Record(
                content="Title: 324234wn ",
                score=0.8,
                title="product info22",
                metadata="product: ABC222"
            )
        ]
    )
