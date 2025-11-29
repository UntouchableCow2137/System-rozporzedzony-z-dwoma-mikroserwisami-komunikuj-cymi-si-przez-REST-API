# System-rozporzedzony-z-dwoma-mikroserwisami-komunikuj-cymi-si-przez-REST-API
# Distributed REST API System - Microservices

## Opis projektu
System rozporzedzony składający się z dwóch niezależnych mikroserwisów komunikujących się przez REST API:
- **Serwis Produktów** - zarządzanie informacjami o produktach
- **Serwis Magazynowy** - zarządzanie stanami magazynowymi

## Wymagania
- Python 3.7+
- Flask
- requests

## Instalacja
1. Zainstaluj zależności:
2. Pobierz pliki z repozytorium:

## Uruchomienie

### Terminal 1 - Serwis Produktów (port 8001)

### Terminal 2 - Serwis Magazynowy (port 8002)

## Testowanie API

### Scenariusz sukcesu - Produkt istnieje (ID: 1)

**Serwis Produktów:**
curl http://localhost:8001/products/1
**Odpowiedź:**
{"id": 1, "name": "Laptop", "price": 4500.0}

**Serwis Magazynowy:**
curl http://localhost:8002/stock/1
**Odpowiedź:**
{"productId": 1, "quantity": 15}


### Scenariusz błędu - Produkt nie istnieje (ID: 10)

**Serwis Produktów:**
curl http://localhost:8001/products/10
**Odpowiedź:**
{"description": "Product not found", "status": 404}

**Serwis Magazynowy:**
curl http://localhost:8002/stock/10
**Odpowiedź:**
{"description": "Product not found in product service", "status": 404}


## Architektura
Client
|
└─→ Stock Service (port 8002)
└─→ HTTP Request
└─→ Product Service (port 8001)
└─→ Response

## Autor
Maciej Wydrowski 79875
