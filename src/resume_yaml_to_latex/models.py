"""Data models for resume structure."""

from typing import List, Optional
from pydantic import BaseModel, Field


class BasicInfo(BaseModel):
    """Basic information about the person."""
    name: str
    address: str
    email: str
    phone: str
    websites: Optional[List[str]] = Field(default_factory=list)


class Degree(BaseModel):
    """Educational degree information."""
    names: List[str]


class Education(BaseModel):
    """Education entry."""
    school: str
    degrees: List[Degree]


class Title(BaseModel):
    """Job title with dates."""
    name: str
    startdate: str
    enddate: str


class Experience(BaseModel):
    """Work experience entry."""
    company: str
    location: str
    titles: List[Title]
    highlights: List[str]


class SkillCategory(BaseModel):
    """Category of skills."""
    category: str
    skills: List[str]


class Resume(BaseModel):
    """Complete resume data structure."""
    basic: BasicInfo
    objective: str
    education: List[Education]
    experiences: List[Experience]
    skills: List[SkillCategory] 