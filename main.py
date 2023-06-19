from fastapi import FastAPI
import httpx
from pydantic import BaseModel
import psycopg2
from psycopg2 import Error
from config import (
    HUBSPOT_API_KEY,
    CLICKUP_API_KEY,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)

app = FastAPI()


class Contact(BaseModel):
    email: str
    firstname: str
    lastname: str
    website: str
    phone: int
    


def create_hubspot_contact(contact: Contact):
    url = f"https://developers.hubspot.com/docs/api/crm/contacts?hapikey={HUBSPOT_API_KEY}"
    data = {
        "properties": [
            {"property": "email", "value": contact.email},
            {"property": "firstname", "value": contact.firstname},
            {"property": "lastname", "value": contact.lastname},
            {"property": "website", "value": contact.website},
            {"property": "phone", "value": contact.phone}
            
        ]
    }

    response = httpx.post(url, json=data)
    response.raise_for_status()
    return response.json()


def create_clickup_task(contact: Contact):
    url = "https://clickup.com/api/"
    headers = {
        "Authorization": CLICKUP_API_KEY
    }
    data = {
        "name": f"Contacto: {contact.firstname}, lastname: {contact.lastname}",
        "description": f"Email: {contact.email}, website: {contact.website} Teléfono: {contact.phone}"
    }

    response = httpx.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def create_call_log(contact: Contact):
    try:
        connection = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )

        cursor = connection.cursor()

        insert_query = """
        INSERT INTO call_logs (firstname, lastname, email, website, phone)
        VALUES (%s, %s, %s)
        """
        record_to_insert = (contact.firstname, contact.lastname, contact.email, contact.website, contact.phone)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        cursor.close()

    except (Exception, Error) as error:
        print("Error al insertar el registro:", error)

    finally:
        if connection:
            connection.close()


@app.post("/contacts")
async def create_contact(contact: Contact):
    hubspot_contact = create_hubspot_contact(contact)
    clickup_task = create_clickup_task(contact)
    create_call_log(contact)
    return {"hubspot_contact": hubspot_contact, "clickup_task": clickup_task}
