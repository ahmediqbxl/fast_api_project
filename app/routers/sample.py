from fastapi import APIRouter, HTTPException
from typing import List
from app.models.sample import SampleModel

router = APIRouter(
    prefix="/samples",
    tags=["samples"],
    responses={404: {"description": "Not found"}},
)

# In-memory storage for demonstration
samples = []

@router.post("/", response_model=SampleModel)
async def create_sample(sample: SampleModel):
    samples.append(sample)
    return sample

@router.get("/", response_model=List[SampleModel])
async def get_samples():
    return samples

@router.get("/{sample_id}", response_model=SampleModel)
async def get_sample(sample_id: int):
    for sample in samples:
        if sample.id == sample_id:
            return sample
    raise HTTPException(status_code=404, detail="Sample not found")

@router.put("/{sample_id}", response_model=SampleModel)
async def update_sample(sample_id: int, updated_sample: SampleModel):
    for i, sample in enumerate(samples):
        if sample.id == sample_id:
            samples[i] = updated_sample
            return updated_sample
    raise HTTPException(status_code=404, detail="Sample not found")

@router.delete("/{sample_id}")
async def delete_sample(sample_id: int):
    for i, sample in enumerate(samples):
        if sample.id == sample_id:
            samples.pop(i)
            return {"message": "Sample deleted successfully"}
    raise HTTPException(status_code=404, detail="Sample not found") 