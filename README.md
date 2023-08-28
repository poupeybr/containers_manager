# Containers Manager
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/poupey/container-manager?label=DockerHub%20Tag)

This repository contains a Docker-based Python API designed to accept a JSON POST request and create a new container on the host machine. This can be useful in scenarios where you need to dynamically provision new containers based on provided data.

⚠️ **Please note that this project is currently under development and may not be production-ready. Use caution when testing and deploying.**

## Prerequisites

- Docker installed on the host machine.

## Pull the Docker Image

You can pull the Docker image for the API from Docker Hub using the following command:

```bash
docker pull poupey/container-manager
```
## How to use

### Run container:
Replace 'YourKeyToAuthYourPost' with your chosen authentication key in the following command:
```bash
docker run -d \
  -p 7500:7500 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name container-manager \
  --env AUTH_KEY=YourKeyToAuthYourPost \
  poupey/container-manager
```
### Make a POST request:
If you've set an AUTH_KEY, pass it as a bearer token in the request header:
```bash
curl -X POST -H "Authorization: Bearer YourKeyToAuthYourPost" -H "Content-Type: application/json" -d '{
  ...
}' http://localhost:7500/runcontainer
```
If you haven't set an AUTH_KEY, you can make a request without the Authorization header.

### Check the new container:

After a successful POST request, check the host machine to confirm that a new container has been created according to the provided data.

## Example JSON
Here's an example JSON that you can use for deploying a MariaDB database
```json
{
	"containerName": "mariadb",
	"image": "mariadb:latest",
	"ports": [
		{
			"containerPort": 3306,
			"protocolPort": "tcp",
			"externalPort": 3307
		}
	],
	"volumes": [
		{
			"containerVolume": "/var/lib/mysql",
			"externalVolume": "/home/mariadb/"
		}
	],
	"environmentVariables": [
		{
		"name": "MARIADB_ROOT_PASSWORD",
		"value": "IqvRt7JPFBfM3y2e"
		},
		{
		"name": "MARIADB_DATABASE",
		"value": "db_api"
		}
	],
	"network": "reverse-proxy",
	"ip": "172.28.0.2",
	"restartPolicy": "always"
}
```
Feel free to modify the JSON to suit your needs.

## Additional Notes
- You can modify the JSON payload to customize various aspects of container creation. Add more ports, alter volumes, adjust environment variables, include or omit network settings, IP addresses, or change restart policies to fit your requirements.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
