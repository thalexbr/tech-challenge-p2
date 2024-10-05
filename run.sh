echo 
echo '###################################################################'
echo '## FIAP MLET PHASE 2 - SETUP APP                                 ##'
echo '## Make sure to add your credentials to AWS on <roo>\credentials ##'
echo '###################################################################'
echo
read -p "Enter the S3 bucket to store data: " BUCKET_NAME


docker build --pull --rm -f "Dockerfile" -t techchallengep2:latest "."
docker rm -f techchallengep2
docker run -dit --name techchallengep2 \
           -v ./downloads:/app/downloads \
           -v ./credentials:/root/.aws \
           -e URL_B3='https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br' \
           -e DOWNLOAD_FOLDER='/app/downloads' \
           -e FILTER_SELECTION='Setor de Atuação' \
           -e BUCKET_NAME=$BUCKET_NAME \
           -p 8000:8000 \
           techchallengep2:latest