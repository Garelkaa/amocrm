import json
import aiohttp

from config import access_token, url_contacts, url_leads


async def create_contact(name, client_phone):
    url = url_contacts

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = [
        {
            "name": name,
            "custom_fields_values": [
                {
                    "field_id": 728181,
                    "values": [{"value": client_phone}]
                }
            ]
        }
    ]

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                response_json = await response.json()
                contact_id = response_json['_embedded']['contacts'][0]['id']
                print("Контакт успешно создан", contact_id)
                return contact_id
            else:
                print("Произошла ошибка при создании контакта", await response.text())
                return None


async def add_lead(cnt_id, name_client, client_phone, comment, city, name):
    url = url_leads
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = [
        {
            "pipeline_id": 8220682,
            "status_id": 67139718,
            "custom_fields_values": [
                {
                    "field_id": 1769685,
                    "values": [{"value": client_phone}]
                },

                {
                    "field_id": 1769687,
                    "values": [{"value": city}]
                },

                {
                    "field_id": 1769689,
                    "values": [{"value": name_client}]
                },

                {
                    "field_id": 1769691,
                    "values": [{"value": comment}]
                },

                {
                    "field_id": 1769731,
                    "values": [{"value": name}]
                }
            ],

             "_embedded": {
                "contacts": [
                    {
                        "id": cnt_id
                    }
                ]
            }
        }
    ]
            
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                response_json = await response.json()
                lead_id = response_json["_embedded"]["leads"][0]["id"]
                print("Сделка успешно создана", lead_id)
                return True
            else:
                print("Произошла ошибка при добавлении сделки")
                return False
