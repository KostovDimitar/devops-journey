# Visit Counter

A simple containerized Flask app that counts page visits.
Built to practice Docker images, port mapping and persistent volumes.

## Run

```bash
docker run -d --name app -p 8080:5000 -v visits:/data kostoff/app:1.0
```

## Test

- `http://localhost:8080` – shows the visit count
- `http://localhost:8080/health` – returns `{"status": "ok"}`

## Volume test

1. Open the page a few times. The counter goes up.
2. Remove the container: `docker rm -f app`
3. Run it again with the same `-v visits:/data`. The counter continues from where it stopped.

## Build from source

```bash
docker build -t kostoff/app:1.0 ./app
```
