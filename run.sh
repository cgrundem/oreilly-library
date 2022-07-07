sudo  kubectl apply -f ./kubernetes/mysql/mysql-pv.yaml
sudo  kubectl apply -f ./kubernetes/mysql/mysql-deployment.yaml

sudo  kubectl apply -f ./kubernetes/deployment.yaml

sudo  kubectl describe deployment mysql
sudo  kubectl describe deployment oreilly-library


