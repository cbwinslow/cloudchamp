# Sports Data IDE & Real-Time Pipeline Integration

This project provides a real-time sports data IDE with:

- **Live event streaming** from your Redis-backed sports data pipeline
- **Script/query editor** (integrates with your backend)
- **Chatbot** (powered by OpenAI or your logic)
- **Workspace save/load**
- **React + Chakra UI frontend**
- **FastAPI + Redis backend**
- **Docker Compose for full stack (backend, Postgres, Redis)**

---

## Quick Start

1. **Clone and configure**
    - Fill in your `.env` in `backend` for OpenAI, etc.

2. **Build and run (from project root)**
    ```sh
    docker compose up --build
    ```

3. **Publish test events (in a separate shell):**
    ```sh
    docker compose exec app python backend/publish_test_event.py
    ```

4. **Open the web IDE:**  
    Visit [http://localhost:8080](http://localhost:8080)

---

## Integrating with your real pipeline

- In your sports data pipeline, publish events to Redis channel `sports_events`:
    ```python
    import redis, json
    r = redis.Redis(host="redis", port=6379, decode_responses=True)
    r.publish("sports_events", json.dumps({...}))
    ```
- The IDE will show events live!

---

## Extending

- Connect `/api/script` to your real script/query logic.
- Enhance the chatbot with more pipeline-aware support.
- Support multiple files/workspaces.
- Add authentication or user accounts if needed.

---

## License

MIT