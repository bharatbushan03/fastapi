from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

events = [ { "id": 1, "title": "Python Backend Workshop", "category": "Workshop", "location": "Hyderabad", "date": "2026-07-20", "organizer": "Code Club", "capacity": 100, "is_open": True }, { "id": 2, "title": "Tech Career Fair", "category": "Career", "location": "Bengaluru", "date": "2026-07-25", "organizer": "Career Connect", "capacity": 300, "is_open": True }, { "id": 3, "title": "Cultural Evening", "category": "Cultural", "location": "Hyderabad", "date": "2026-08-02", "organizer": "Arts Forum", "capacity": 500, "is_open": False} ]

@app.get('/')
def home():
    return {"message": "welcome to Event API"}

# @app.get('/events')
# def get_events():
#     return events

@app.get('/events/{event_id}')
def get_event_by_id(event_id: int):
    for event in events:
        if event['id'] == event_id:
            return event
        
    raise HTTPException(status_code = 404, detail = 'event not found')

@app.get("/events")
def event_filtered_by_query(
    title: str | None = None,
    category: str | None = None,
    location: str | None = None,
    date: str | None = None,
    organizer: str | None = None,
    capacity: int | None = None,
    is_open: bool | None = None,
):
    filtered_events = events

    if title is not None:
        filtered_events = [
            event for event in filtered_events
            if event["title"] == title
        ]

    if category is not None:
        filtered_events = [
            event for event in filtered_events
            if event["category"] == category
        ]

    if location is not None:
        filtered_events = [
            event for event in filtered_events
            if event["location"] == location
        ]

    if date is not None:
        filtered_events = [
            event for event in filtered_events
            if event["date"] == date
        ]

    if organizer is not None:
        filtered_events = [
            event for event in filtered_events
            if event["organizer"] == organizer
        ]

    if capacity is not None:
        filtered_events = [
            event for event in filtered_events
            if event["capacity"] == capacity
        ]

    if is_open is not None:
        filtered_events = [
            event for event in filtered_events
            if event["is_open"] == is_open
        ]

    return filtered_events

class EventCreate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool

@app.post('/events', status_code = 201)
def create_event(event: EventCreate):
    new_id = max((event['id'] for event in events), default = 0) + 1
    new_event = {
        "id": new_id,
        "title": event.title,
        "category": event.category,
        "location": event.location,
        "date": event.date,
        "organizer": event.organizer,
        "capacity": event.capacity,
        "is_open": event.is_open
    }
    events.append(new_event)
    return {
        "message": "event created successfully",
        "event": new_event
    }

@app.delete('/events/{event_id}')
def delete_event(event_id: int):
    for event in events:
        if event['id'] == event_id:
            events.remove(event)
            return {
                "message": "event removed successfully"
            }
    raise HTTPException(status_code = 404, detail = "event not found")

class PutUpdate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool

@app.put('/events/{event_id}')
def put_update(event_id: int, event: PutUpdate):
    for existing_event in events:
        if existing_event['id'] == event_id:
            existing_event.update(event.model_dump())
            return {
                "message": "event updated successfully"
            }
        
    raise HTTPException(status_code = 404, detail = 'Event not found')

class PatchUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    organizer: Optional[str] = None
    capacity: Optional[int] = None
    is_open: Optional[bool] = None

@app.patch('/events/{event_id}')
def patch_update(event_id: int, event: PatchUpdate):
    for existing_event in events:
        if existing_event['id'] == event_id:
            if event.title:
                existing_event['title'] = event.title
            if event.category:
                existing_event['category'] = event.category
            if event.location:
                existing_event['location'] = event.location
            if event.date:
                existing_event['date'] = event.date
            if event.organizer:
                existing_event['organizer'] = event.organizer
            if event.capacity:
                existing_event['capacity'] = event.capacity
            if event.is_open:
                existing_event['is_open'] = event.is_open
            return {
                "message": "patch event updated"
            }
            

    raise HTTPException(status_code = 404, detail = 'event not found')