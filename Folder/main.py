from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# FastAPI instance
app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///Image_Record_SQLDB.db"  # SQLite database file
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base
Base = declarative_base()

# Database Model
class ImageSummary(Base):
    __tablename__ = 'Image_Record_SQLDB_TABLE'
    id = Column("image_id", Integer, primary_key=True, index=True)
    filename = Column("image_filename", String, unique=True, index=True)
    summary = Column("image_summary", Text)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoint to fetch image summary by filename
@app.get("/image-summary/{filename}", response_model=dict)
async def read_image_summary(filename: str, db: Session = Depends(get_db)):
    image_summary = db.query(ImageSummary).filter(ImageSummary.filename == filename).first()
    if image_summary is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"filename": filename, "summary": image_summary.summary}
