sudo docker build -t oreilly-library ./app/.

sudo  kubectl apply -f ./kubernetes/mysql/mysql-pv.yaml
sudo  kubectl apply -f ./kubernetes/mysql/mysql-deployment.yaml
sleep 5
sudo  kubectl apply -f ./kubernetes/deployment.yaml


