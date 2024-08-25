docker build --pull --rm -f "Dockerfile" -t techchallengep2:latest "."
docker rm -f techchallengep2
docker run -dit --name techchallengep2 \
           -v ./downloads:/app/downloads \
           -e URL_B3='https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br' \
           -e DOWNLOAD_FOLDER='/app/downloads' \
           -e FILTER_SELECTION='Setor de Atuação' \
           -p 8000:8000 \
           techchallengep2:latest