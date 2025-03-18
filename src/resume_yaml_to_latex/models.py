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


class Education(BaseModel):
    """Education entry."""
    name: str
    school: str
    startdate: str
    enddate: str
    highlights: Optional[List[str]] = Field(default_factory=list)


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


class Publication(BaseModel):
    """Publication entry."""
    authors: str
    title: str
    conference: str
    location: str
    date: str


class Resume(BaseModel):
    """Complete resume data structure."""
    basic: BasicInfo
    objective: str
    education: List[Education]
    experiences: List[Experience]
    skills: List[SkillCategory]
    publications: Optional[List[Publication]] = Field(default_factory=list) 