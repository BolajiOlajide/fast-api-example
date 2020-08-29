start:
	uvicorn main:app

dev:
	uvicorn main:app --reload --port 5000
