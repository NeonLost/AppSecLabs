docker ps -aq | xargs docker rm -f
docker images -aq | xargs docker rmi -f
docker build --rm -t "appsec:rce" .
docker run -it -p 5000:5000 appsec:rce
