dev-frontend:
	cd frontend && npm run dev
	
dev-backend:
	cd backend && poetry run uvicorn pli5.main:app --reload